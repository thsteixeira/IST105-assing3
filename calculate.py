import sys
import json


def calculate(x, y, z):
        values = {'x': x, 'y': y, 'z': z}
        x += y
        values['x1'] = x
        x -= z
        values['x2'] = x
        x *= y
        values['x3'] = x
        x %= z
        values['x4'] = x
        x /= z
        values['x5'] = x
        sum = x + y + z
        values['sum'] = sum
        return values

if len(sys.argv) > 3:
    if int(sys.argv[3]) > 0:
        print(json.dumps(calculate(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))))
    else print("z can't be 0") 
else:
    print("Error: Missing a number")