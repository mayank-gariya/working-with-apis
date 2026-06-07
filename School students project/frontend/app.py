import streamlit as st
import requests

API_URI = 'http://127.0.0.1:8000'

st.set_page_config(page_title="School Records", layout="wide")
st.title("🏫 School Student Database Management")

tab1, tab2 = st.tabs(["📋 View & Manage Students", "➕ Add New Student"])

#helper function 
def get_active_students():
    try:
        response = requests.get(f'{API_URI}/')
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        st.error(f"Cannot connect to API backend: {e}")
    return []

current_students = get_active_students()

with tab1:
    st.subheader("Active Student Roster")
    if not current_students:
        st.info("No active students found in your cluster.")
    else:
        # Render a clean UI table presentation
        st.table(current_students)
        st.divider()
        
        col1, col2 = st.columns(2)
        
        # UPDATE SECTION
        with col1:
            st.markdown("### 📝 Edit Student Profile")
            selected_update = st.selectbox(
                "Select student to edit:",
                options=current_students,
                format_func=lambda s: f"{s['name']} (Class: {s.get('class_studed', 'N/A')})"
            )
            
            if selected_update:
                with st.form("update_student_form"):
                    # Maps your 'get_student' schema names to form fields
                    u_name = st.text_input("Name", value=selected_update['name'])
                    u_class = st.text_input("Class Room", value=selected_update.get('class_studed', ''))
                    u_age = st.number_input("Age", value=int(selected_update['age']))
                    u_contact = st.number_input("Contact", value=int(selected_update.get('contact', 90909090)))
                    u_marks = st.number_input("Marks", value=int(selected_update['marks']))
                    u_tags = st.text_input("Tags", value=selected_update['tags'])
                    
                    if st.form_submit_button("Push Updates"):
                        # Maps directly back to your School Pydantic fields
                        payload = {
                            "name": u_name,
                            "class_studed": u_class,
                            "age": u_age,
                            "contact": u_contact,
                            "marks": u_marks,
                            "tags": u_tags,
                            "leaved": False
                        }
                        res = requests.put(f"{API_URI}/student/{selected_update['id']}", json=payload)
                        if res.status_code == 200:
                            st.success("Student updated successfully!")
                            st.rerun()
                        else:
                            st.error(f"Failed to update: {res.text}")

# DELETE SECTION
        with col2:
            st.markdown("### 🗑️ Remove Student")
            selected_delete = st.selectbox(
                "Select student to drop:",
                options=current_students,
                format_func=lambda s: f"{s['name']} (ID: ...{s['id'][-6:]})"
            )
            
            if selected_delete:
                st.warning(f"Are you sure you want to mark {selected_delete['name']} as leaved?")
                if st.button("Confirm Soft-Deletion", type="primary"):
                    res = requests.delete(f"{API_URI}/student/remove/{selected_delete['id']}")
                    if res.status_code == 200:
                        st.success("Student marked as leaved!")
                        st.rerun()
                    else:
                        st.error(f"Failed to remove: {res.text}")

# ==========================================
# TAB 2: CREATE
# ==========================================
with tab2:
    st.subheader("Enroll a Student")
    with st.form("create_form", clear_on_submit=True):
        name = st.text_input("Name", value="nonu500")
        class_studed = st.text_input("Class Studied")
        age = st.number_input("Age", min_value=1, value=15)
        contact = st.number_input("Contact No.", value=90909090)
        marks = st.number_input("Marks", min_value=0, value=75)
        tags = st.text_input("Tags", value="sudhra hai")
        
        if st.form_submit_button("Save to Database"):
            if not class_studed:
                st.error("Class field is required!")
            else:
                new_payload = {
                    "name": name,
                    "class_studed": class_studed,
                    "age": age,
                    "contact": contact,
                    "marks": marks,
                    "tags": tags,
                    "leaved": False
                }
                res = requests.post(f"{API_URI}/student", json=new_payload)
                if res.status_code == 200:
                    st.success("Student enrolled successfully!")
                    st.rerun()
                else:
                    st.error(f"Server rejection payload: {res.text}")