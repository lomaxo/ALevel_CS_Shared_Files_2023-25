def tables():
    num = getNumber('Which table would you like to view?', 1, 12)
    for x in range(1, 13):
        print(f'{x:2} x {num:2} = {x*num:3}')

def getNumber(disp: str, min: int, max: int):
    while True:
        num_str = input(disp)
        if not num_str.isdecimal():
            print("Not a valid number")
            continue
        num = int(num_str)
        if num < min or num > max:
            print("Not in the correct range")
            continue
        return num

while True:
    tables()


