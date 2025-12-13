def main():
    camelcase=input("camelcase: ")
    snake_case=convert(camelcase)
    print(snake_case)
def convert(camelcase):
    snake_case=""
    for char in camelcase:
        if char.isupper():
            char=char.lower()
            snake_case+=f"_{char}"
        else:
            snake_case+=char
    return snake_case

main()
