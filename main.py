import re

def simpleCalculator(option, x, y):
    answer = 0.0

    if option == 1:
        try:
            answer = x + y
        except Exception:
            print("no answers")
        else:
            print(str(x) + " + " + str(y) + " = " + str(answer) + "\n")
        
    if option == 2:
        try:
            answer = x - y
        except Exception:
            print("no answers")
        else:
            print(str(x) + " - " + str(y) + " = " + str(answer) + "\n")

    if option == 3:
        try:
            answer = x * y
        except Exception:
            print("no answers")
        else:
            print(str(x) + " * " + str(y) + " = " + str(answer) + "\n")

    if option == 4:
        try:
            answer = x / y
        except Exception:
            print("no answers\n")
        else:
            print(str(x) + " / " + str(y) + " = " + str(answer) + "\n")

    if option == 5:
        try:
            answer = x % y
        except Exception:
            print("no answers")
        else:
            print(str(x) + " % " + str(y) + " = " + str(answer) + "\n")


def isFloat(num):
    try:
        x = float(num)
    except Exception:
        return False
    else:
        return True


def isInt(num):
    try:
        x = float(num)
        y = int(x)
    except Exception:
        return False
    else:
        return x == y



def indexOf(arr, delimiter):

    for i in range(len(arr)):
        if arr[i] == delimiter:
            return i

    return -1



def lastIndexOf(arr, delimiter):

    for i in reversed(range(len(arr))):
        if arr[i] == delimiter:
            return i

    return -1



def complexCalculator(arr):

    answer = 0

    if isInt(arr[0].strip()):
        answer = int(arr[0].strip())
    elif isFloat(arr[0].strip()):
        answer = float(arr[0].strip())


    if arr[1].strip() == "+":
        try:
            if isInt(arr[2].strip()):
                answer += int(arr[2].strip())
            elif isFloat(arr[2].strip()):
                answer += float(arr[2].strip())
            else:
                return str(answer)

        except Exception:
            return str(answer)
    
    elif arr[1] == "-":
        try:
            if isInt(arr[2].strip()):
                answer -= int(arr[2].strip())
            elif isFloat(arr[2].strip()):
                answer -= float(arr[2].strip())
            else:
                return str(answer)

        except Exception:
            return str(answer)

    elif arr[1] == "*":
        try:
            if isInt(arr[2].strip()):
                answer *= int(arr[2].strip())
            elif isFloat(arr[2].strip()):
                answer *= float(arr[2].strip())
            else:
                return str(answer)

        except Exception:
            return str(answer)

    elif arr[1] == "/":
        try:
            if isInt(arr[2].strip()):
                answer /= int(arr[2].strip())
            elif isFloat(arr[2].strip()):
                answer /= float(arr[2].strip())
            else:
                return str(answer)

        except Exception:
            return str(answer)

    elif arr[1] == "%":
        try:
            if isInt(arr[2].strip()):
                answer %= int(arr[2].strip())
            elif isFloat(arr[2].strip()):
                answer %= float(arr[2].strip())
            else:
                return str(answer)

        except Exception:
            return str(answer)

    elif arr[1] == "^":
        try:
            if isInt(arr[2].strip()):
                answer = answer ** int(arr[2].strip())
            elif isFloat(arr[2].strip()):
                answer = answer ** float(arr[2].strip())
            else:
                return str(answer)

        except Exception:
            return str(answer)

    else:
        return str(answer)



    return str(answer)



def calculateBrackets(arr):

    operators = ["^", "/", "*", "%", "+", "-"]


    for operator in operators:
        index = 0
        while True:
            index = indexOf(arr, operator)

            if index == -1:
                break

            arr[index-1] = complexCalculator(arr[index-1:index+2])
            del arr[index], arr[index]

    

    return str(arr[0].strip())



def main(expression):

    while True:
        
        index = indexOf(expression, '')

        if(index == -1):
            break
            
        del expression[index]


    while True:
        
        index = indexOf(expression, ' ')

        if(index == -1):
            break
            
        del expression[index]


    while True:
        
        index = indexOf(expression, '\s')

        if(index == -1):
            break
            
        del expression[index]


    while True:
        index = indexOf(expression, '\t')

        if(index == -1):
            break
            
        del expression[index]

    

    # for brackets

    while True:
        if lastIndexOf(expression, '(') == -1:
            break

        open_bracket = lastIndexOf(expression, '(') + 1

        for i in range(open_bracket, len(expression)):
            if expression[i] == ')':
                close_bracket = i + 1
                break


        expression[lastIndexOf(expression, '(')] = str(calculateBrackets(expression[open_bracket:close_bracket-1]))
        del expression[open_bracket:close_bracket]


    #calculate


    # of

    index = 0
    while True:
        index = indexOf(expression, "^")

        if index == -1:
            break

        expression[index-1] = complexCalculator(expression[index-1:index+2])
        del expression[index], expression[index]



    # DM

    index = 0
    if indexOf(expression, "/") != -1 and indexOf(expression, "*") != -1:

        index = 0
        is_divide = False
        is_multiply = False
        
        while index != -1:

            if indexOf(expression, "/") > indexOf(expression, "*"):
                index = indexOf(expression, "*")

                if(index == -1):
                    is_multiply = True

                if(index != -1):
                    expression[index-1] = complexCalculator(expression[index-1:index+2])
                    del expression[index], expression[index]
            else:
                is_multiply = True


            if indexOf(expression, "*") > indexOf(expression, "/"):
                index = indexOf(expression, "/")

                if(index == -1):
                    is_divide = True


                if(index != -1):
                    expression[index-1] = complexCalculator(expression[index-1:index+2])
                    del expression[index], expression[index]
            else:
                is_divide = True

            if(is_multiply and is_divide):
                break

            is_multiply = False
            is_divide = False


    # Divide only
    index = 0
    if indexOf(expression, "/") != -1 and indexOf(expression, "*") == -1:
            
        while True:
            index = indexOf(expression, "/")

            if(index == -1):
                break

            expression[index-1] = complexCalculator(expression[index-1:index+2])
            del expression[index], expression[index]


    # Multiply only
    index = 0
    if indexOf(expression, "*") != -1 and indexOf(expression, "/") == -1:
            
        while True:    
            index = indexOf(expression, "*")

            if(index == -1):
                break

            expression[index-1] = complexCalculator(expression[index-1:index+2])
            del expression[index], expression[index]

    
        

    # MODULUS

    index = 0
    while True:
        index = indexOf(expression, "%")

        if index == -1:
            break

        expression[index-1] = complexCalculator(expression[index-1:index+2])
        del expression[index], expression[index]


    # AS


    index = 0
    if indexOf(expression, "+") != -1 and indexOf(expression, "-") != -1:

        index = 0
        is_add = False
        is_minus = False
        
        while True:

            if indexOf(expression, "-") > indexOf(expression, "+"):
                index = indexOf(expression, "+")

                if(index == -1):
                    is_add = True


                if(index != -1):
                    expression[index-1] = complexCalculator(expression[index-1:index+2])
                    del expression[index], expression[index]
            else:
                is_add = True



            if indexOf(expression, "+") > indexOf(expression, "-"):
                index = indexOf(expression, "-")

                if(index == -1):
                    is_minus = True


                if(index != -1):
                    expression[index-1] = complexCalculator(expression[index-1:index+2])
                    del expression[index], expression[index]
            else:
                is_minus = True

            if(is_add and is_minus):
                break

            is_add = False
            is_minus = False



    # ADD ONLY
    index = 0
    if indexOf(expression, "+") != -1 and indexOf(expression, "-") == -1:

        while True:
            index = indexOf(expression, "+")

            if(index == -1):
                break

            expression[index-1] = str(complexCalculator(expression[index-1:index+2]))
            del expression[index], expression[index]


    # SUBTRACT ONLY
    index = 0
    if indexOf(expression, "-") != -1 and indexOf(expression, "+") == -1:
            
        while True:    
            index = indexOf(expression, "-")

            if(index == -1):
                break

            expression[index-1] = complexCalculator(expression[index-1:index+2])
            del expression[index], expression[index]
    
        

    return expression[0]



option = 0

while True:
    print("Calculator\n")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Modulus (%)")
    print("6. Complex Calculator ")
    print("7. Exit\n")

    option = int(input("Choose your option: "))

    if option == 7:
        print("\nGoodbye!")
        break



    if(option in [1,2,3,4,5]):
        first_no = input("\nEnter the first number: ")
        second_no = input("Enter the second number: ")


        if isInt(first_no):
            first_no = int(first_no)
        elif isFloat(first_no):
            first_no = float(first_no)
        else:
            first_no = float(first_no)


        if isInt(second_no):
            second_no = int(second_no)
        elif isFloat(second_no):
            second_no = float(second_no)
        else:
            second_no = float(second_no)


        simpleCalculator(option, first_no, second_no)


    if(option == 6):
        while True:

            user_input = input("\nEnter your expression: ").strip()

            user_input = re.split('([^" ".0-9])', user_input)

            original = ' '.join(user_input).strip()
            answer = main(user_input)

            if(answer):
                print(original + " = " + answer)
            else:
                print('Incorrect sequence, try again.\n')
            
            user_input = input("\nDo you wish to quit this program? Yes/No: ").strip()
            if(user_input == 'yes' or user_input == 'YES' or user_input == 'Yes' or user_input == 'y' or user_input == 'Y'):
                print("\nGoodbye!")
                break



