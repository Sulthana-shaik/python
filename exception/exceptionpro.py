a = 10
b = 2
c = [1, 2, 3]
try:
    result = a / b
    print("Result: ", result)
    print("Element: ", c[5])
except ZeroDivisionError:
    
    print("Division by zero is not allowed")

except ValueError:

    print("Invalid Value")

except IndexError:

    print("Index error")

except NameError:

    print("Value not defined")

except Exception as e:

    print("Generic message: ", e)

finally:

    print("Closing resources")


#example 2
d = int(input("Enter value of a"))
f = int(input("Enter value of a"))
g = [1, 2, 3]

try:
    result = d / f
    print("Result: ", result)
except (ZeroDivisionError, ValueError, IndexError, NameError ) as e:
    print("Error occurred: ", e)
except:
    print("Error occurred")
finally:
    print("Execution completed !")

#example 3
#Example 5 - raise keyword
age = int(input("Enter the age : "))
if age < 0:
    raise ValueError("Age cannot be negative")

print("Your age is:", age)

def calculate_square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return number ** 0.5

try:
    result = calculate_square_root(-9)
    print(f"The result is: {result}")
except ValueError as e:
    print(f"Error: {e}")

# custom expection 
class InvalidMarksError(Exception):
    pass
try:
    marks = int(input("enter the marks"))
    if marks < 0 or marks > 100:
        raise InvalidMarksError("marks should be between 0 and 100")
    print("marks is: {marks}")
except InvalidMarksError as e:
    print("custom  error", e) 

#example5
print("program started")
try:
    username = input("enter username:")
    password = input("enter password")
    if username != "admin":
        raise Exception("invalid username")
    if password != "1234":
        raise Exception("Invalid pasword")
    
    print("Login successful")

except Exception as e:
    print("Login failed:",e)
finally:
    print("progrram ended")