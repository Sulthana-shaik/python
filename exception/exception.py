#code raise exception
#print("program started")
#a =10/b
#print(b)
#print("tq")

#handle exception
print("started")
try:
    a = 10/0
except (ZeroDivisionError) as e:
    print("AN error occured",e)
print("tq")
#example 2
print("started")
try:
    a = 10/0
except:
    print("AN error occured")
print("tq")
#example 3
try:
    num = int(input("enter a number: "))
    result = 10 / num  # exception zero,valueerror
    print(result)
except ZeroDivisionError:
    print("error, cannot be divided by zero")
except ValueError:
    print("only integer value should be given")

#generic block 
except:
    print("error , only int value should be given")

    #ex-4 try-except with else

try:
    num = int(input("enter a numbers:"))
    result = 10 / num #exception zero,valueerror
except ZeroDivisionError:
    print("error, cannot be divided ")
else:
    print("division succesful", result)

    #example 4 finally 
    # Example 4 - try - except with else, finally block always executes

try:
    num = int(input("Enter a number: "))
    result = 10 / num  # Exception ZeroDivisionError, ValueError

except ZeroDivisionError:
    print("Error, cannot be divided by zero")

except ValueError:
    print("Error, only integer value should be given")

# Generic Block
except:
    print("Error is occurred")

else:
    print("Division Successful", result)

finally:
    print("Program executed")