def inner():
    coef = 1
    total = 0
    while True:
        try:
            input_val = yield total
            total = total + coef * input_val
        except:
            pass

def outer2():
    print("Before inner(), I do this.")
    yield from inner()
    print("After inner(), I do that.")

a = outer2()
b = a.__next__()
print (b)