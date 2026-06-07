from fastapi import FastAPI ,APIRouter,HTTPException
from fastapi.middleware.cors import CORSMiddleware 
from confugration import collections
from database.schemas import get_school_students
from database.models import School
from bson.objectid import ObjectId

app = FastAPI()

#connection between frontend and backend 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

@router.get('/')
async def get_school_student():
    data = collections.find({'leaved':False})
    return get_school_students(data)

@router.post('/student')
async def add_student(new_student:School):
    try :
        resp = collections.insert_one(dict(new_student))
        return {'statuscode':200,'id':str(resp.inserted_id)}
    except Exception as e :
        return HTTPException(status_code=500,detail=f'this is bad {e}')

@router.put('/student/{student_id}')
async def update_student(student_id:str,update_student:School):
    try:
        id = ObjectId(student_id)
        student_exists = collections.find_one({'_id':id ,'leaved':False})
        if not student_exists:
            return HTTPException(status_code=404,detail='student not found')
        resp = collections.update_one({'_id':id},{'$set':dict(update_student)})
        return HTTPException(status_code=200,detail='sucessfully updated the student')
    except Exception as e:
        return HTTPException(status_code=500,detail=f'error {e}')

@router.delete('/student/remove/{student_id}')
async def delete_student(student_id: str): 
    try:
        id = ObjectId(student_id)
        student_exists = collections.find_one({'_id': id, 'leaved': False})
        if not student_exists:
            raise HTTPException(status_code=404, detail='student not found')
            
        # Performed soft delete by setting 'leaved' to True
        collections.update_one({'_id': id}, {'$set': {'leaved': True}})
        return {'statuscode': 200, 'detail': 'sucessfully updated the student'}
    except HTTPException as http_ex:
        raise http_ex
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error {e}')



app.include_router(router)