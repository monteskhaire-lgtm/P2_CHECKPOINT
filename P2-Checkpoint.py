print("==========================`===================================")
print("Welcome User!")
print("Student Activity Score System.")
print("=============================================================")

def ave(score1, score2, score3):                                             #this function is about their average grade
    avg = (score1 + score2 + score3) / 3
    return avg

students = int(input("Enter how many students: "))
print("=============================================================")
n = 3                                                                         #n refers to the minimum of how many students.
stu = 0                                                                       #stu refers to the student number
exel = 0                                                                      #exel refers to the students who has 90+grades
very= 0                                                                       #very refers to the students whoi has 80+grades         #these variable can be used later
passed= 0                                                                     #passed refers to the students who has 75+ grades         for summary
fail= 0                                                                        #fail refers to the students who has below 75 grades
if students < n:
    print("Students must be Greater than 3!! Try again")
else:
    while stu < students:
        stu = stu + 1
        print("Student", stu)
        name = input("Enter name: ")
        score1 = float(input("Activity_1 score: "))
        score2 = float(input("Activity_2 score: "))
        score3 = float(input("Activity_3 score: "))

        avg = ave(score1, score2, score3)                                       # i called the function here

        if avg >= 90:
            status = ("Excellent!! HUWAWWW great job!!")
            exel= exel + 1
        elif avg >= 80:
            status = ("Very Good!")
            very= very + 1
        elif avg >= 75:
            status = ("Passed")
            passed = passed + 1
        else:
            status = ("Failed, Try harder next time!!")
            fail = fail + 1

        print(" ")
        print("Name: ", name)
        print("Average: ", avg)
        print("Status: ", status)
        print("=============================================================")
    
    summary = input("Do you want a summary?: ")
    if summary == "YES" or summary == "yes":
        print("Processing your request!!")
        print(" Done, sir, pogi!")
        print("=============================================================")
        print(" ")
        print("===========================SUMMARY===========================")
        print("Total Students: ", students)
        print("Excelent Students: ", exel)                                                              
        print("Very good Students: ", very)
        print("Passed Students: ", passed)
        print("Failed Students: ", fail)
        if exel +  very +  passed > fail:
            print("Comment: Your Students are Remarkable!!")
        else:                                                                                         #nested Statements
            print("Comment: Awww dang it!! They need to do their best!")
        print("=============================================================")
    else:
        print("Well then!")
    
    print("All done!! heheyy")
    print("Thank you for Using this Student Activity Score System, BOSS")
    print("=============================================================")

    #May explanation po ako naka separate. Please read, thank you pooo