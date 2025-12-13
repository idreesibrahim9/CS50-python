from fractions import Fraction
def output(fuel):
    if fuel==1 or fuel==0:
        print("E")
    elif fuel==99 or fuel ==100:
        print("F")
    else:
        print(f"{fuel}%")

def main():
    while True:
        try:
            frac=input("Fraction: ")
            x,y=frac.split("/")
            x,y=int(x),int(y)
            if x>y or x<0:
                raise ValueError
            per=(x/y)*100
            break
        except ZeroDivisionError:
            pass
        except ValueError:
            pass
    per=round(per)
    output(per)
main()
