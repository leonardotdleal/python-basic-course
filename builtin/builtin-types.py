guest_list = ['Leonardo', 'Eduardo', 'Fabio']

print(guest_list)

guest_list.append('Tiago')

print(guest_list)

guest_list.remove('Leonardo')

print(guest_list)

print(guest_list[0])

# get last element
print(guest_list[2])
print(guest_list[-1])

guest_list.append(50)

print(guest_list)

# tuple
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2

print(tupla3)

# key -> value

personal_data = {'name': 'Batman', 'city': 'Gothan'}

print(personal_data)

personal_data['vehicle'] = 'Batmobile'

print(personal_data)

del personal_data['city']

print(personal_data)
