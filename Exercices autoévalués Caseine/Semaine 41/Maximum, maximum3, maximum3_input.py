
def maximum(a,b):
    res = a
    if b>a:
        res = b
    return res
    
def maximum3(a,b,c):
    res = a
    if b>a or c>a:
        if c>b:
            res = c
        else: # si b>=c
            res = b
    return res

def maximum3_input():
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))
    return maximum3(a,b,c)
        