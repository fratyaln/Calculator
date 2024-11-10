 
def calculator(process ,num1,num2):
    
    num1 = float(num1)
    num2 = float(num2)
    if process == '+' :
      return num1+num2
    elif process == '-' :
      return num1-num2
    elif process == '/' :
      return num1/num2
    elif process == '*' :
      return num1*num2


process = ''
while process not in [ '+','-','/','*']:
    process = input ("Which Process you want to do(+,-,/,*) : ")
    if process not in [ '-','+','/','*']:{
       print (" Invalid Process !!! ")
    }
    
  

 
num1 = input("Enter first number : ")
num2 = input("Enter second number : ")
result= calculator(process,num1,num2)
print(num1 +" "+process+" "+num2+" = " + str(result))


