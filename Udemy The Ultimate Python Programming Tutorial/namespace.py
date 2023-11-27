#when not using the "from" syntax and just importing, then we have to add the module name before calling the function
import newton

def square(number):
    print("not from the newton module: ")
    return number*number

print(newton.sqrt(9))
print(newton.square(9))
print(square(9))