import datetime

print('Welcome to Personal Data Collector')

print('Please enter your information')

name = input('Enter your name: ')
age = int(input('Enter your age: '))
height = float(input('Enter your height in meters: '))
fav_num = int(input('Enter your favourite number: '))

current_year = datetime.date.today().year
birth_year = current_year - age

print()
print('Your Information')

print('Name:', name)
print('Type:', type(name))
print('Memory Address:', id(name))

print()
print('Age:', age)
print('Type:', type(age))
print('Memory Address:', id(age))

print()
print('Height:', height)
print('Type:', type(height))
print('Memory Address:', id(height))

print()
print('Favourite Number:', fav_num)
print('Type:', type(fav_num))
print('Memory Address:', id(fav_num))

print()
print('Your approximate birth year is:', birth_year)

height_int = int(height)

print('Height as float:', height)
print('Height as integer:', height_int)

print()
print('Type Conversion:')
print('Height was converted from float to int')
print('New type:', type(height_int))

print()
print('Thank you for using my program!')
print('Keep learning Python!')