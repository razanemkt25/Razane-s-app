#lists_exercise
Math=["Charlie","Kevin","Alise","Bob","Leo"]
Physics=["Jack","Paolo","Alex","Bob","Charlie"]
newM=input("add a new student name in math: ")
Math.append(newM)
newF=input("add a new student name in physics : ")
Physics.insert(2,newF)
print("math:")
for studentM in Math:
    print(studentM) 
print() #for separation 
print("physics:")     
for studentF in  Physics:
    print(studentF)
Math.sort()
Physics.sort()
print()
print("alphabetically ordered math:")
for studentM in Math:
    print(studentM) 
print() 
print("alphabitically ordered physics:")     
for studentF in  Physics:
    print(studentF)
    
newnew=input("add a new student name ")
Math.append(newnew)
if newnew in Physics:
    print("true")
    Physics.remove(newnew)
else :
    print("false")
  
print("math:")  
for studentM in Math:
    print(studentM) 
print()
print("physics:")
for studentF in Physics:
    print(studentF)


