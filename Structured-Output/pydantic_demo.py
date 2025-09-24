from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    # default value
    # name: str = 'Nensi'
    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, description='A decimal value representing the cgpa of the student')

# for default value
# new_student = {}
new_student = {'name': 'Nensi', 'age': 20, 'email': 'abc@gmail.com', 'cgpa':5}

student = Student(**new_student)

print("In Pydantic Format:")
print(type(student))
print(student)
print(student.name)

# Dictionary
print("In Dictionary Format:")
student_dict = dict(student)
print(student_dict['age'])

# Json
print("In Json Format:")
student_json = student.model_dump_json()
print(student_json)