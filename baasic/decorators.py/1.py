#@decorator name

def decor(func):
    def warpper(name):
        if name == "pranitha":
            print(f"{name}, Likes Kfc")
        else:
            return func(name)
    return warpper

@decor
def process(name):
    print(f"{name} , Likes Biriyani")

process("Ramya")
process("Mahi")
process("kavya")
process("reshu")
process("pranitha")#pranitha likes kfc

print("--exam2--")
#decorator function
def smartdiv(function):
    def inner(a, b):
        if b == 0:
            print("division by 0 is not possible")
        else:
            return function(a, b)
    return inner
#original function
@smartdiv
def div(a, b):
    print(a/b)
div(10, 2)
div(10, 5)
div(10, 0)