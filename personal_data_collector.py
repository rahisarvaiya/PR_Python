import datetime
print('Welcome this program collects personal information')

name = input('Enter your name')
age = int(input('Enter your age'))
height = float(input('Enter your height'))
fav_num = int(input('Enter your fav num'))

print('Your name is', name)
print('Your age is', age)
print('Your height is', height)
print('Your favourite number is', fav_num)

c_year = datetime.date.today().year

birth_year = c_year - age
print('Your birth year is', birth_year)



