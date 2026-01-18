                    # Connditional statement 

"""

light = "blue"

if(light == "red"):
    print("stop")   #indentation = proper spacing 
elif(light == "green" ):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")

    print ("end of code")

"""

marks = int (input("enter students marks : "))

if( marks>=90):
    grade =" A "
elif(marks>= 80 and marks < 90):
    grade ="B"
elif( marks >=70 and marks <80):
    grade = "C"
else:
    grade = "D"
    print("grade of the student -> " , grade)