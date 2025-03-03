
# print("hello world")

# #take roll no , name ,  marks from student and store it , display it
# roll = input("Enter your roll no: ")
# name = input("Enter your name: ")
# marks =input("Enter marks: ")

# #display it
# print("Roll no = ",roll)
# print("Name = ",name)
# print("Marks = ",marks)

# #adding two numbers

# n1=int(input("Enter 1st no. : "))
# n2=float(input("Enter 2nd no. : "))
# add = n1+n2
# print("Addition is : ",add)

# #Operators
# #Arithemetic
# #

# #WAP to display area of square, triangle
# n1=int(input("Enter side 1 : "))
# n2=int(input("Enter side 2 : "))
# triangle=0.5*n1*n2
# square1=n1*n1
# square2=n2*n2
# print("Area of triangle : ",triangle)
# print("Area of square 1 : ",square1)
# print("Area of square 2 : ",square2)

# #Simple interest and compound interest
# #
# p=float(input("Enter principle amount : "))
# r=float(input("Enter rate of interest : "))
# n=float(input("Enter the tenure  : "))
# #Simple Interest
# SI=(p*r*n)/100
# CI=p*(1+r/100)**n
# print("Simple interest  ")
# print("Amount : ",SI)
# print("Compoound Interest ",round(CI,3)-p)

# WAP to implement SIP caculator
mi=float(input("Enter Monthly Investment : "))
err=float(input("Enter the  Expected return rate : "))
tp=float(input("Enter the time period : "))
i=err/12/100
M=tp*12

SIP=mi*((((1+i)**(M))-1)*(1+i))/i
print("SIP is : ",round(SIP))

