age = 25

if age < 18:
    print('Age less than 18')
else:
    print('Age more than 18')

vehicle = {'type': 'motorcycle', 'brand': 'Honda', 'potency': 140}

if vehicle['type'] == 'motorcycle' and vehicle['brand'] == 'Honda':
    print('Vehicle is a motorcycle')
else:
    print('Vehicle isn\'t a motorcycle')

result = vehicle['type'] == 'motorcycle'

print(result)

if vehicle['type'] == 'car' or vehicle['potency'] < 120:
    print('You have a very fast vehicle')
else:
    print('You haven\'t a very fast vehicle')

if (vehicle['type'] == 'car' or vehicle['potency'] < 120) or vehicle['brand'] == 'Honda':
    print('You have a very fast vehicle')

if vehicle['type'] == 'car':
    print('You have a car')
elif vehicle['type'] == 'truck':
    print('You have a truck')
elif vehicle['type'] == 'motorcycle':
    print('You have a motorcycle')

name = 'Leonardo'

if name:
    print('True')
else:
    print('False')

positive = 1
zero = 0
negative = -1

if positive:
    print('Positive "1" is valid')

if zero:
    print('Zero "0" is valid')
else:
    print('Zero "0" is not valid')

if negative:
    print('Negative "-1" is valid')