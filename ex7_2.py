# imports

import beaupy

# functions
# def initialStudentValues():
#     # nome genero idade localidade curso
#     temp = []
#     temp.append({'id' : 1, 'name' : 'Ana', 'gender' : 'f', 'age' : 26, 'city' : 'Matosinhos'})
#     temp.append({'id' : 2, 'name' : 'Paula', 'gender' : 'f', 'age' : 36, 'city' : 'Lisboa'})
#     temp.append({'id' : 3, 'name' : 'Manel', 'gender' : 'm', 'age' : 55, 'city' : 'Faro'})
#     temp.append({'id' : 4, 'name' : 'Clarice', 'gender' : 'f', 'age' : 31, 'city' : 'Viana do Castelo'})
#     temp.append({'id' : 5, 'name' : 'João', 'gender' : 'm', 'age' : 18, 'city' : 'Braga'})
#     return temp

# def initialCourseValues():
#     temp = []
#     temp.append({'id' : 1, 'course' : 'Python'})
#     temp.append({'id' : 2, 'course' : 'Java'})
#     temp.append({'id' : 3, 'course' : 'Base de dados relacionais'})
#     return temp

# def enrollStudentCourse():
#     temp = []
#     temp.append({'id' : 1, 'student_id' : 1, 'course_id': 1})
#     temp.append({'id' : 2, 'student_id' : 1, 'course_id': 3})
#     temp.append({'id' : 3, 'student_id' : 2, 'course_id': 1})
#     temp.append({'id' : 4, 'student_id' : 3, 'course_id': 2})
#     temp.append({'id' : 5, 'student_id' : 4, 'course_id': 3})
#     temp.append({'id' : 6, 'student_id' : 5, 'course_id': 1})
#     return temp

# #
# studentsList = initialStudentValues()
# courseList = initialCourseValues()
# enrollList = enrollStudentCourse()

# # menu list
# # courseMenuList = []
# # for course in courseList:
# #     courseMenuList.append(course['course'])
# # courseMenuList = [course['course'] for course in courseList]

# # print(courseList)
# # print(courseMenuList)
# # courseIndex = beaupy.select(courseList, cursor="->", cursor_style='green', return_index = True)
# # print(courseList[courseIndex]['course'])

# # listagem de alunos que frequentam o curso x ######################################################


# def listStudent(courseIndex):
#     course_id = courseList[courseIndex]['id']
#     course_students = [studentsList[enroll['student_id'] - 1]['name'] for enroll in enrollList if enroll['course_id'] == course_id]
#     for student in course_students:
#         print(student)
            
# courseIndex = beaupy.select(courseList, cursor="->", cursor_style='green', return_index=True)
# listStudent(courseIndex)


# # todos os cursos frequantados pelo aluno y #############################################

# def courseByStudent(studentIndex):
#     student_id = studentsList[studentIndex]['id']
#     student_courses = [course['course'] for enroll in enrollList if enroll['student_id'] == student_id for course in courseList if course['id'] == enroll['course_id']]
#     for course in student_courses:
#         print(course)


# studentIndex = beaupy.select(studentsList, cursor="->", cursor_style='green' , return_index=True )           
# courseByStudent(studentIndex)
# realizem o preenchimento dos alunos ( comentar o initialValues) - fazer menu em beaupy ################################


import beaupy
 
def initialStudentValues():
    # nome genero idade localidade curso
    temp = []
    temp.append({'id' : 1, 'name' : 'Ana', 'gender' : 'f', 'age' : 26, 'city' : 'Matosinhos'})
    temp.append({'id' : 2, 'name' : 'Paula', 'gender' : 'f', 'age' : 36, 'city' : 'Lisboa'})
    temp.append({'id' : 3, 'name' : 'Manel', 'gender' : 'm', 'age' : 55, 'city' : 'Faro'})
    temp.append({'id' : 4, 'name' : 'Clarice', 'gender' : 'f', 'age' : 31, 'city' : 'Viana do Castelo'})
    temp.append({'id' : 5, 'name' : 'João', 'gender' : 'm', 'age' : 18, 'city' : 'Braga'})
    return temp
 
def initialCourseValues():
    temp = []
    temp.append({'id' : 1, 'course' : 'Python'})
    temp.append({'id' : 2, 'course' : 'Java'})
    temp.append({'id' : 3, 'course' : 'Base de dados relacionais'})
    return temp
 
def enrollStudentCourse():
    temp = []
    temp.append({'id' : 1, 'student_id' : 1, 'course_id': 1})
    temp.append({'id' : 2, 'student_id' : 1, 'course_id': 3})
    temp.append({'id' : 3, 'student_id' : 2, 'course_id': 1})
    temp.append({'id' : 4, 'student_id' : 3, 'course_id': 2})
    temp.append({'id' : 5, 'student_id' : 4, 'course_id': 3})
    temp.append({'id' : 6, 'student_id' : 5, 'course_id': 1})
    return temp
 
def getStudentsFromCourse(course_id, enrollList):
    "This function returns the students that are enroll in specific course"
    temp = []
    for student in enrollList:
        if student['course_id'] == course_id:
            temp.append(student)
    return temp
 
def getStudentInfo(student_id, studentsList):
    for student in studentsList:
        if student['id'] == student_id:
            return student['name']
 
def printStudent(student_id, studentsList):
    print(f"Nome: {getStudentInfo(student_id, studentsList)}")
 
def printStudents(studentsFromCourse, studentsList):
    print("\nListagem de estudantes: \n")
    for student in studentsFromCourse:
        #print(student)
        printStudent(student['student_id'], studentsList)
 
def getStudentsCourse(studentsList, courseList, enrollList):
    # todos os alunos que frequentam um curso X
    print("\nPor favor indique o curso desejado: \n")
    courseMenuList = [course['course'] for course in courseList] # create a list with name of the courses
    courseIndex = beaupy.select(courseMenuList, cursor="->", cursor_style='green', return_index=True)
    course_id = courseList[courseIndex]['id']
    studentsFromCourse = getStudentsFromCourse(course_id, enrollList)
    printStudents(studentsFromCourse, studentsList)
 
def addFormando(nextID):
    print("Adicionar formando: ")
    name = input("Nome: ")
    gender = input("Género: ")
    age = int(input("Idade: "))
    city = input("Localidade: ")
    return {'id' : nextID, 'name' : name, 'gender' : gender, 'age' : age, 'city' : city}
 
def addCourse(nextID):
    print("Adicionar curso: ")
    course = input("Curso: ")
    return {'id' : nextID, 'course' : course}
 
def getNextID(list):
    if not list:
        return 1
    else:
        return list[-1]['id']+1
 
def getItemID(list):
    op = int(beaupy.select(list, cursor="->", cursor_style='green', return_index=True))
    return list[op]['id']
 
def addMatricula(nextID, studentsList, courseList):
    student_id = getItemID(studentsList)
    course_id = getItemID(courseList)
    return {'id' : nextID, 'student_id' : student_id, 'course_id': course_id}
 
def menu(studentsList, courseList, enrollList):
    menuList = [
        "Adicionar Formando",
        "Ver Formandos",
        "Adicionar Cursos",
        "Ver Cursos",
        "Matricular Aluno",
        "Matriculas por Curso",
        "Sair"
    ]
    while True:
        op = beaupy.select(menuList, cursor="->", cursor_style='green', return_index=True)+1
        match op:
            case 1:
                nextID = getNextID(studentsList)
                studentsList.append(addFormando(nextID))
            case 2:
                print(studentsList)
            case 3:
                nextID = getNextID(courseList)
                courseList.append(addCourse(nextID))
            case 4:
                print(courseList)
            case 5:
                nextID = getNextID(enrollList)
                enrollList.append(addMatricula(nextID, studentsList, courseList))
                print(enrollList)
            case 6:
                getStudentsCourse(studentsList, courseList, enrollList)
            case 7:
                break
            case _:
                print("\nErro: opção inválida\n")
   
 
 
studentsList = initialStudentValues()
#studentsList = []
courseList = initialCourseValues()
enrollList = enrollStudentCourse()
 
menu(studentsList, courseList, enrollList)[3:55 PM] Pedro Mendonça - FORMADOR PRT
import beaupy
 
def initialStudentValues():
    # nome genero idade localidade curso
    temp = []
    temp.append({'id' : 1, 'name' : 'Ana', 'gender' : 'f', 'age' : 26, 'city' : 'Matosinhos'})
    temp.append({'id' : 2, 'name' : 'Paula', 'gender' : 'f', 'age' : 36, 'city' : 'Lisboa'})
    temp.append({'id' : 3, 'name' : 'Manel', 'gender' : 'm', 'age' : 55, 'city' : 'Faro'})
    temp.append({'id' : 4, 'name' : 'Clarice', 'gender' : 'f', 'age' : 31, 'city' : 'Viana do Castelo'})
    temp.append({'id' : 5, 'name' : 'João', 'gender' : 'm', 'age' : 18, 'city' : 'Braga'})
    return temp
 
def initialCourseValues():
    temp = []
    temp.append({'id' : 1, 'course' : 'Python'})
    temp.append({'id' : 2, 'course' : 'Java'})
    temp.append({'id' : 3, 'course' : 'Base de dados relacionais'})
    return temp
 
def enrollStudentCourse():
    temp = []
    temp.append({'id' : 1, 'student_id' : 1, 'course_id': 1})
    temp.append({'id' : 2, 'student_id' : 1, 'course_id': 3})
    temp.append({'id' : 3, 'student_id' : 2, 'course_id': 1})
    temp.append({'id' : 4, 'student_id' : 3, 'course_id': 2})
    temp.append({'id' : 5, 'student_id' : 4, 'course_id': 3})
    temp.append({'id' : 6, 'student_id' : 5, 'course_id': 1})
    return temp
 
def getStudentsFromCourse(course_id, enrollList):
    "This function returns the students that are enroll in specific course"
    temp = []
    for student in enrollList:
        if student['course_id'] == course_id:
            temp.append(student)
    return temp
 
def getStudentInfo(student_id, studentsList):
    for student in studentsList:
        if student['id'] == student_id:
            return student['name']
 
def printStudent(student_id, studentsList):
    print(f"Nome: {getStudentInfo(student_id, studentsList)}")
 
def printStudents(studentsFromCourse, studentsList):
    print("\nListagem de estudantes: \n")
    for student in studentsFromCourse:
        #print(student)
        printStudent(student['student_id'], studentsList)
 
def getStudentsCourse(studentsList, courseList, enrollList):
    # todos os alunos que frequentam um curso X
    print("\nPor favor indique o curso desejado: \n")
    courseMenuList = [course['course'] for course in courseList] # create a list with name of the courses
    courseIndex = beaupy.select(courseMenuList, cursor="->", cursor_style='green', return_index=True)
    course_id = courseList[courseIndex]['id']
    studentsFromCourse = getStudentsFromCourse(course_id, enrollList)
    printStudents(studentsFromCourse, studentsList)
 
def addFormando(nextID):
    print("Adicionar formando: ")
    name = input("Nome: ")
    gender = input("Género: ")
    age = int(input("Idade: "))
    city = input("Localidade: ")
    return {'id' : nextID, 'name' : name, 'gender' : gender, 'age' : age, 'city' : city}
 
def addCourse(nextID):
    print("Adicionar curso: ")
    course = input("Curso: ")
    return {'id' : nextID, 'course' : course}
 
def getNextID(list):
    if not list:
        return 1
    else:
        return list[-1]['id']+1
 
def getItemID(list):
    op = int(beaupy.select(list, cursor="->", cursor_style='green', return_index=True))
    return list[op]['id']
 
def addMatricula(nextID, studentsList, courseList):
    student_id = getItemID(studentsList)
    course_id = getItemID(courseList)
    return {'id' : nextID, 'student_id' : student_id, 'course_id': course_id}
 
def menu(studentsList, courseList, enrollList):
    menuList = [
        "Adicionar Formando",
        "Ver Formandos",
        "Adicionar Cursos",
        "Ver Cursos",
        "Matricular Aluno",
        "Matriculas por Curso",
        "Sair"
    ]
    while True:
        op = beaupy.select(menuList, cursor="->", cursor_style='green', return_index=True)+1
        match op:
            case 1:
                nextID = getNextID(studentsList)
                studentsList.append(addFormando(nextID))
            case 2:
                print(studentsList)
            case 3:
                nextID = getNextID(courseList)
                courseList.append(addCourse(nextID))
            case 4:
                print(courseList)
            case 5:
                nextID = getNextID(enrollList)
                enrollList.append(addMatricula(nextID, studentsList, courseList))
                print(enrollList)
            case 6:
                getStudentsCourse(studentsList, courseList, enrollList)
            case 7:
                break
            case _:
                print("\nErro: opção inválida\n")
   
 
 
studentsList = initialStudentValues()
#studentsList = []
courseList = initialCourseValues()
enrollList = enrollStudentCourse()
 
menu(studentsList, courseList, enrollList)