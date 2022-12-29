# simple student managemnet system through which we can add student, display all the students information, update student infomation, and delete studnt information 
# witout using any database only basic data types of python and OOPs concept are used

class student:

    def __init__(self, roll_number, name, dob, admission_year, eng_marks,math_marks):
        #roll_number/rn: Roll Number of the student
        #name: Name of the student
        #dob: Date of birth of the student
        #admission_year: year in which student was admitted
        #eng_marks: marks in subject english
        #math_marks: marks in subject mathematics
        self.rn = roll_number
        self.name = name
        self.dob = dob
        self.admission_year = admission_year
        self.eng_marks = eng_marks
        self.math_marks = math_marks 
        

    def accept(self,roll_number, name, dob, admission_year, eng_marks,math_marks):
        stu_obj = student(roll_number, name, dob, admission_year, eng_marks,math_marks)
        students_list.append(stu_obj)

    
    def display(self,obj):
        print("Roll Number: ",obj.rn)
        print("Name: ",obj.name)
        print("Date Of Birth: ",obj.dob)
        print("Enrolment Year: ",obj.admission_year)
        print("Marks in English: ",obj.eng_marks)
        print("Marks in Mathematics: ",obj.math_marks)
        print("\n")

    def search(self,current_rn):
        for i in range(len(students_list)):
            if students_list[i].rn == current_rn:
                return i


    def edit_roll_no(self, current_roll_num, value):
        i=self.search(current_roll_num)
        students_list[i].rn=value

    def edit_name(self, current_roll_num, value):
        i=self.search(current_roll_num)
        students_list[i].name=value

    def edit_dob(self, current_roll_num, value):
        i=self.search(current_roll_num)
        students_list[i].dob=value
        
    def edit_admission_year(self, current_roll_num, value):
        i=self.search(current_roll_num)
        students_list[i].admission_year=value

    def edit_eng_marks(self, current_roll_num, value):
        i=self.search(current_roll_num)
        students_list[i].eng_marks=value

    def edit_math_marks(self, current_roll_num, value):
        i=self.search(current_roll_num)
        students_list[i].math_marks=value

    

students_list = []
obj = student(0,"","",0,0,0)
obj.accept(1,"raj","12/12/2000",2018,90,90)
obj.accept(2,"sam","12/09/2000",2018,80,90)
flag=True
while(flag):
    print("Choose one of the option by entering the number in front of the option: ")
    print("\n1 add a student \n2 display all students \n3 edit student information \n4 Break")
    inp = input()
    if inp=="1":
        print("Enter Roll Number: ")
        roll_no = int(input())
        print("Enter Name: ")
        name = input()
        print("Enter Date of Birth: ")
        dob = input()
        print("Enter Enrolment Year: ")
        admi_year = int(input())
        print("Enter English marks: ")
        eng_mark = int(input())
        print("Enter math marks: ")
        math_marks = int(input())
        
        obj.accept(roll_no,name,dob,admi_year,eng_mark,math_marks)
    elif inp=="2":
        for i in students_list:
            obj.display(i)
    elif inp=="3":
        print("Enter roll number of the student: ")
        rol_no = int(input())
        print("current details \n")
        stu_ind = obj.search(rol_no)
        obj.display(students_list[stu_ind])
        print("What to update \n")
        print("\n1 roll number \n2 name \n3 Date of Birth \n4 Enrolment year \n5 English marks \n6 Mathematics marks \n7 Go back")
        what_to_update = input()
        print("Enter the new value: ")
        if what_to_update=="1":
            new_val = int(input())
            obj.edit_roll_no(rol_no,new_val)
        elif what_to_update =="2":
            new_val = input()
            obj.edit_name(rol_no,new_val)
        elif what_to_update =="3":
            new_val = input()
            obj.edit_dob(rol_no,new_val)
        elif what_to_update =="4":
            new_val = int(input())
            obj.edit_admission_year(rol_no,new_val)
        elif what_to_update =="5":
            new_val = int(input())
            obj.edit_eng_marks(rol_no,new_val)
        elif what_to_update =="6":
            new_val = int(input())
            obj.edit_math_marks(rol_no,new_val)
        elif what_to_update == "7":
            continue
        
        print("\nInformation updated\n")

    elif inp=="4":
        break
    else:
        print("wrong input") 