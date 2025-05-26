import sys

def calculate(x, y, z):
        values = []
        x += y
        values.append(x)
        x -= z
        values.append(x)
        x *= y
        values.append(x)
        x %= z
        values.append(x)
        x /= z
        values.append(x)
        sum = x + y + z
        values.append(sum)
        return values

if len(sys.argv) > 3:
    if int(sys.argv[3]) != 0:
        print(calculate(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])))
    else print("z can't be 0") 
else:
    print("Error: Missing a number")