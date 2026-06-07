def get_student(student):
    return {
        'id':str(student['_id']),
        'name': str(student['name']),
        'age' : int(student['age']),
        'marks':int(student['marks']),
        'tags':str(student['tags']),
        'status': student.get('leaved',False)
    }

def get_school_students(students):
    return [get_student(student) for student in students]
