def gen_func():
    yield 1
    yield 2
    yield 5
gen = gen_func()
print(next(gen))
print(next(gen))
print(next(gen))
#print(next(gen)) StopIteration 


#normal function - small data
def normal():
    return[2,4,6]
print(normal())