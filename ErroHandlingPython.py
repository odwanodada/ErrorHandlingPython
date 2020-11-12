#Try catch
#y:
    #Everything is done in the try
    #number1 = 9
    #number2 = 0
    #answer = number1 / number2
    #print(answer)

#except:
    #print("Something Went Wrong!")

def division(x,y):
    try:
        answer = x/y

    except ZeroDivisionError:
        print("Can not be divide by 0")
    except TypeError:
        print("Can not use  strings")
    else:
        print("This answer is: ", answer)
    finally:
        print("Go Exit")

number1 = int(input("Enter number1: "))
number2 = input("Enter number2: ")
division(number1,number2)