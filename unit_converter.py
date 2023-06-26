print()
print("*** UNIT CONVERTER ***")
print()

conversions_available = {1: ( 'km', 'mi', 0.621),
                         2:( 'mi', 'km', 1.609),
                         3:( 'kg', 'lbs', 2.205),
                         4:( 'lbs', 'kg', 0.454),
                         5:( '°C', '°F',None),
                         6:( '°F', '°C', None),
}

print('Conversion Available:')
print()

for no, (from_unit, to_unit, _) in conversions_available.items():
    print(f'{no}: {from_unit} -> {to_unit}')

print()

try:
    conversion = int(input('Enter the number of the conversion to use: '))
except:
    print('Please enter an integer')
    exit()

from_unit, to_unit, factor = conversions_available.get(conversion,(None,None,None))

try:
    from_value = float(input(f'Enter {from_unit}:'))
except:
    print('Please enter an integer')
    exit()

print()

if conversion in range(1,5) :
    to_value = from_value * factor
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

elif conversion == 5:
    to_value = (from_value * 9/5) + 32
    to_value = round(to_value, 2)
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')

else:
    to_value = (from_value - 32) * 5/9
    to_value = round(to_value, 2)
    print(f'{from_value} {from_unit} -> {to_value} {to_unit}')


