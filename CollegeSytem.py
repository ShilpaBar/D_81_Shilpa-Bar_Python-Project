courses_db = []
batches_db = []
departments_db = []
students_db = []
exam_db=[]
performance_db=[]

def create_department(department_id, name):
  # Create a new department object
  department = {
    'department_id': department_id,
    'name': name,
    'batches': []
  }
  
  # Add the department to the database
  departments_db.append(department)

def view_department(department_id):
  # Find the department in the database
  for department in departments_db:
    if department['department_id'] == department_id:
      return department['batches']
  # Return null if the department was not found
  return None
#==============================================================
def create_batch(batch_id, batch_name, department_name, courses):
  # Create a new batch and add it to the database
  for department in departments_db:
    if department['department_id']==department_name:
        x=[]
        x.append(batch_id)
        department['batches']=x.copy()
        x.clear()
  new_batch = {
    'batch_id': batch_id,
    'batch_name': batch_name,
    'department_name': department_name,
    'courses': courses,
    'students': []
  }
  batches_db.append(new_batch)

def list_of_student_in_a_batch(batch_id):
  # Find the batch in the database and retrieve the list of students
  for batch in batches_db:
    if batch['batch_id'] == batch_id:
      print(f"List Of Student in {batch_id} are: {','.join(batch['students'])}")

def list_of_courses_in_a_batch(batch_id):
  # Find the batch in the database and retrieve the list of students
  for batch in batches_db:
    if batch['batch_id'] == batch_id:
      print(f"List Of courses in {batch_id} are: {','.join(batch['courses'])}")
#==============================================================================
def create_course(course_id, course_name):
  # Create a new course and add it to the database
  new_course = {
    'course_id': course_id,
    'course_name': course_name,
    'marks_obtained': []
  }
  courses_db.append(new_course.copy())
#===============================================================================
def create_student(student_id, name, class_roll_number, batch_id):
  # Create a new student and add them to the database
  for batch in batches_db:
    if batch['batch_id']==batch_id:
        x=[]
        x.append(student_id)
        batch['students']=x.copy()
        x.clear()
  new_student = {
    'student_id': student_id,
    'name': name,
    'class_roll_number': class_roll_number,
    'batch_id': batch_id
  }
  students_db.append(new_student)
  return True

def update_student(student_id, new_name, new_class_roll_number, new_batch_id):
  # Find the student in the database and update their information
  for student in students_db:
    if student['student_id'] == student_id:
      student['name'] = new_name
      student['class_roll_number'] = new_class_roll_number
      student['batch_id'] = new_batch_id
      break
  return True

def remove_student(student_id):
  # Find the student in the database and remove them
  for student in students_db:
    
    if student['student_id'] == student_id:
      value=student
      students_db.remove(student)
      break
  return value

#=================================================================
def add_student_in_exam(student_roll_num,course_id,marks):
    for student in students_db:
        if student['class_roll_number']==student_roll_num:
            student_id=student['student_id']
    for course in courses_db:
        if course['course_id']==course_id:
            x=[]
            x.append([student_id,marks])
            course['marks_obtained'].append(x.copy())
    new_student_marks = {
    'student_roll_num': student_roll_num,
    'course_id': course_id,
    'marks': marks
  }
    exam_db.append(new_student_marks.copy())

def performance_of_all_student():
  for exam in exam_db:
    student_roll_num=exam['student_roll_num']
    course_id=exam['course_id']
    marks=exam['marks']
    if marks >= 90:
      grade = 'A'
    elif marks >= 80:
      grade = 'B'
    elif marks >= 70:
      grade = 'C'
    elif marks >= 60:
      grade = 'D'
    elif marks >= 50:
      grade = 'E'
    else:
      grade = 'F'
    if grade in ['A', 'B', 'C', 'D', 'E']:
      result = 'PASS'
    else:
      result = 'FAIL'
    for student in students_db:
      if student['class_roll_number']==student_roll_num:
        name=student['name']
        break
    performance_of_a_student=[
      student_roll_num,name,course_id,marks,grade,result
    ]
    performance_db.append(performance_of_a_student.copy())
      
#===================================================================
def department_menu():
  while True:
    print('''\n====D E P A R T M E N T   M E N U====
1. Create Department
2. View all batches in a department
3. View average performance of all batches in the department
4. Show department statistics
5. back to main menu
6. exit
\n''')
    choice=int(input("Enter your choice:: "))
    if choice==1:
        department_id=input('Enter Department id: ')
        name=input("Enter department name: ")
        create_department(department_id, name)
        print("Department created...")
    elif choice==2:
        department_id=input("Enter Department id")
        batches=view_department(department_id)
        print("Batches are: ",batches)
    elif choice==5:
        main_menu()
    elif choice==6:
      exit()
    else:
        print("wrong option.....")
#======================================================================
def batch_menu():
  while True:
    print('''\n====B A T C H   M E N U====
1. Create Batch
2. View list of all students in a batch
3. View list of all courses taught in the batch
4. back to main menu
5. exit\n''')
    choice=int(input("Enter your choice::"))
    if choice==1:
        b_id=input("Enter Batch Id: ")
        b_name=input("Enter Batch Name: ")
        x=[y['department_id'] for y in departments_db]
        print("Departments are: ","/".join(x))
        dept_name=input("choose a department : ")
        course=input("Enter courses seperated by ',' : ").split(",")
        create_batch(b_id, b_name, dept_name, course)
        print("Batch created...")
    elif choice==2:
        batch_id=input("Enter Batch id: ")
        list_of_student_in_a_batch(batch_id)
    elif choice==3:
        batch_id=input("Enter Batch id: ")
        list_of_courses_in_a_batch(batch_id)
    elif choice==4:
        main_menu()
    elif choice==5:
        exit()
    else:
        print("wrong option.....")
        
#==============================================================================
def course_menu():
  while True:
    print('''\n====C O U R S E   M E N U====
1. Create Course
2. View list of all students in a batch
3. back to main menu
4. exit\n''')
    choice=int(input("Enter your choice:: "))
    if choice==1:
      course_id=(input("Enter Couse_ID :"))
      course_name=input("Enter Course_Name:")
      create_course(course_id, course_name)
      print("____Course  Created____")
    elif choice==3:
      main_menu()
    elif choice==4:
      exit()
    else:
        print("wrong option.....")

#==============================================================================
def student_menu():
  while True:
    print('''\n====S T U D E N T   M E N U====
1. Create Student
2. Update Student Details
3. Remove Student Details
4. back to main menu
5. exit\n''')
    choice=int(input("Enter your choice:: "))
    if choice==1:
      student_id=input("Enter Student ID:")
      name=input("Enter Name of The Student:")
      class_roll_number=input("Enter Class Roll No. of The Student:")
      x=[y['batch_id'] for y in batches_db]
      print("Batches are: ","/".join(x))
      batch_id=input("Choose Batch ID of The Student::")
      create_student(student_id, name, class_roll_number, batch_id)
      print("Student Entered Successfully.....")
    elif choice==2:
      student_id=input("Enter Student ID:")
      new_name=input("Enter Name of The Student:")
      new_class_roll_number=input("Enter Class Roll No. of The Student:")
      x=[y['batch_id'] for y in batches_db]
      print("Batches are: ","/".join(x))
      new_batch_id=input("Choose Batch ID of The Student::")
      update_student(student_id, new_name, new_class_roll_number, new_batch_id)
      print("Student Updated Successfully.....")
    elif choice==3:
      student_id=input("Enter Student ID:")
      name=remove_student(student_id)
      print(name,"Removed Successfully....")
    elif choice==4:
      main_menu()
    elif choice==5:
      exit()
    else:
        print("wrong option.....")
  
#==============================================================================
def exam_menu():
  while True:
    print('''\n====E X A M I N A T I O N   M E N U====
1. Enter marks of a Student
2. View performance of all students
3. back to main menu
4. exit\n''')
    choice=int(input("Enter your choice:: "))
    if choice==1:
      x=[y['class_roll_number'] for y in students_db]
      print("Roll Numbers are: ","/".join(x))
      student_roll_num=input("Choose Roll number of The Student::")
      x=[y['course_id'] for y in courses_db]
      print("Course Ids are: ","/".join(x))
      course_id=input("Choose ID of The Course::")
      marks=int(input("Enter mark:"))
      add_student_in_exam(student_roll_num,course_id,marks)
    elif choice==2:
      performance_of_all_student()
      for student in performance_db:
        print(student)
    elif choice==4:
      exit()

#==============================================================================
def main_menu():
  while True:
        print("\n****M A I N   M E N U****")
        print('''1. Department
2. Batch
3. Course
4. Student
5. Examination
6. exit\n''')
        choice=int(input("Enter your choice:: "))
        if choice==1:
            department_menu()
        elif choice==2:
            batch_menu()
        elif choice==3:
            course_menu()
        elif choice==4:
            student_menu()
        elif choice==5:
            exam_menu()
        elif choice==6:
          exit()

if __name__=='__main__':
    main_menu()