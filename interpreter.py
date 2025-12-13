expression=input("Expression:")
x,y,z=expression.split()
x=float(x)
z=float(z)
match y:
    case "+" :
        print("sum=",x+z)
    case "-" :
        print("difference=",x-z)
    case "*" :
        print("multiple=",x*z)
    case "/" :
        if z==0:
            print("not possible")
        else:
            print("quotient",x/z)
    case "%" :
        print("remainder=",x%z)
    case _:
        print("invalid operation")
