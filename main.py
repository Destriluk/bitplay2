print("**********************************")
print("------ARE THEY EQUAL OR NOT-------")
print("**********************************")
print(" ")
def Checkifsame(num1,num2):
    if(num1 ^ num2) !=0:
        print("++++++++++++++++++++++++")
        print("They are not equal")
    else:
        print("++++++++++++++++++++++++")
        print("They are equal")
num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the second number :"))
Checkifsame(num1,num2)