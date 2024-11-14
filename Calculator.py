 
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


if __name__ == "__main__":
    process = input("Which process you want to do (+, -, /, *): ")
    while process not in ['+', '-', '/', '*']:
        print("Invalid Process!")
        process = input("Which process you want to do (+, -, /, *): ")
    
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    result = calculator(process, num1, num2)
    print(f"{num1} {process} {num2} = {result}")

