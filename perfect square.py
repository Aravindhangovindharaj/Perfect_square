a=int(input("give a number"))
def square(a):
    n=a
    for i in  range(1,a):
        if i*i==n:
            return True
        else:
            return False
print(square(a))
