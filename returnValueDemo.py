# Returns nothing


def somefunction1():
    return

# return a value
def somefunction2():
    return 123

def somefunction3():
    return 456, 789

def main():
    print()
    print(somefunction1())
    print(somefunction2())
    x = somefunction2()
    print(x)
    x, y = somefunction3()
    print(x, y)
    print()
#done



main()