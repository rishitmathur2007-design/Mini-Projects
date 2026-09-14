num1=float(input("Enter a Number:"))
op=input("Enter Operator[+,-,*,/,%,**,//]:")
num2=float(input("Enter a Number:"))
match op:
    case '+':
        result=num1+num2
    case '-':
        result=num1-num2
    case '*':
        result=num1*num2
    case '/':
        result=num1/num2
    case '%':
        result=num1%num2
    case "**":
        result=num1**num2
    case "//":
        result=num1//num2
    case _:
        print("Enter Valid Operator!!")
print(num1,op,num2,"=",result)