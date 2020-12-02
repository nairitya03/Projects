import time

record = int(input("Enter the no of students record need to added :"))

student={}

for i in range(0,record):
    Name = input("Enter the New Student Name :").split()
    Maths= input("Maths grade :".format(Name)).split()
    Physics = input("Physics grade :".format(Name)).split()
    Chemistry = input("Chemistry grade :".format(Name)).split()
    Name_key =  Name[0]
    Maths_value = Maths[0]
    Phy_value = Physics[0]
    Chem_value = Chemistry[0]
    student[Name_key] = { Maths_value , Phy_value , Chem_value}

print(student)
time.sleep(30)
