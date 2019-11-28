ds = int(input("enter marks of data structure sabject:"))
acc = int(input("enter marks of financial accounting sabject:"))
alg = int(input("enter marks of algorithm sabject:"))
ass = int(input("enter marks of assembly language sabject:"))
java = int(input("enter marks of java sabject:"))
total = (ds+acc+alg+ass+java)/5
percent = float((ds+acc+alg+ass+java)*100)/500
if(total>=80):
    grade = "Grade A"
elif(total>=60):
    grade = "Grade B"
elif(total>=50):
    grade = "Grade C"
elif(total>=40):
    grade = "Grade D"
else:
    grade = "FAIL"

    
print("-------------------------------------")
print("-   Subject                 marks   -")
print("-data structure               ",ds,"  -")
print("-financial accounting         ",acc,"  -")
print("-algorithm                    ",alg,"  -")
print("-assembly language            ",ass,"  -")
print("-Java Language                ",java,"  -")
print("-percentage  ",percent,"        ",grade,"-")
print("-------------------------------------")
