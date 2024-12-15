 
print("hello !! welcome to our calculator program")

a = float(input("Please enter the first number: "))
b =float(input("Please enter the second number: ")) 
c = input("please enter the operand ")
   

if c == '+':
    print(a + b)

elif c == '*':
    print(a*b)
    
elif c == '/':
    print(a/b)

elif c == '-':
    print(a-b)    
else :
    print("sorry this operand is not supported by our calculator")
    
    