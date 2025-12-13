
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    check=[]

    check.append(first(s))
    check.append(second(s))
    check.append(third(s))
    check.append(fourth(s))
    if all(check):
        return True
    else:
        return False
def first(s):
    chars=s[:2]
    return chars.isalpha()
def second(s):
    if  1<len(s)<7:
        return True
    else:
        return False
def third(s):
    for index,char in enumerate(s):
        if char.isdigit():
            if char=="0":
                return False
            a=index
            s=s[a:]
            for b in s:
                if b.isalpha():
                     return False
            break
    return True
def fourth(s):
    check=[]
    for char in s:
        if char.isalpha() or char.isdigit():
            check.append(True)
        else:
            check.append(False)
    if all(check):
        return True
    else:
        return False

main()
