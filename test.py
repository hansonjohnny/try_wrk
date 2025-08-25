"""
# Variables in Python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Asabeneh',
   'lastname':'Yetayeh',
   'country':'Finland',
   'city':'Helsinki'
   }

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)


firstname = input('What is your name? ')
age = input('Your age? ')

print(firstname)
print(age)

firstname = 'James '
lastname = 'Cook'
fullname = firstname + lastname
country = 'Ghana'
city = 'Accra'
age = 26
year = 1998
is_married = True
is_true = 'yes'
is_light_on = True
father, mother, brother, sister, = 'Michael', 'Comfort', 'Bright','Tiff'

print(type(firstname))

num_one = 5
num_two = 4

total = num_two + num_one
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

radius = 30
area_of_circle = 3.143 * radius ** 2
print(area_of_circle)
circum_of_circle = 2 * 3.143 * radius
print('The Circumference is: ', circum_of_circle)

#taking radius as input from the user
radius = float(input('Enter the radius: '))
area = 3.143 * (radius ** 2)
print('The area of the circle is: ', area)

firstname = input('Your first name: ')
lastname = input('Your last name: ')
fullname = firstname + " " + lastname
print('full name is: ', fullname)

from selectors import SelectSelector

length_of_python = len('python')
length_of_dragon = len('dragon')
print('length of python: ', length_of_python)
print('length of dragon: ', length_of_dragon)
print('are the length equal? ', length_of_python == length_of_dragon)
print('is on in both words? ', 'on' in 'python' and 'on' in 'dragon')
sentence = 'I hope this course is not full of jargon. '
print('jargon' in sentence)

num = int(input('Enter number: '))
if num % 2 == 0:
    print(f'{num} is even')
else:
    print(f'{num} is odd')

for i in range(1, 6):
    print(i, 1, i, i**2, i**3)

age = int(input('Enter age: '))
difference = 18 - age
if age >= 18:
    print('You are old enough to drive')
else:
    print(f'Wait for {difference} years')


my_age = int(input('Enter my age; '))
your_age = int(input('Enter your age; '))
if my_age > your_age:
    difference = my_age - your_age
    if difference == 1:
        print(f'I am {difference} year older than you')
    else:
        print(f'I am {difference} years older than you')
elif my_age < your_age:
    dif = your_age - my_age
    if dif == 1:
        print(f'You are {dif} year older than me')
    else:
        print(f'You are {dif} years older than me')
else:
        print('We are the same age')


scores = int(input('Enter Your scores: '))
if 80 <= scores <= 100:
    print('A')
elif 70 <= scores <=79:
    print('B')
elif 60 <= scores <= 69:
    print('C')
elif 50 <= scores <= 59:
    print('D')
elif 0 <= scores <= 49:
    print('F')
else:
    print('Enter score between 0 and 100')


month = str(input('Enter Month: ')).strip().capitalize() # strip removes extra spaces
if month in ['September', 'October', 'November']:
    print('Autumn')
elif month in ['December', 'January', 'February']:
    print('Winter')
elif month in ['March', 'April', 'May']:
    print('Spring')
elif month in ['June', 'July', 'August']:
    print('Summer')
else:
    print('Enter the correct month!')


fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input('Enter a fruit: ').strip().lower()
if new_fruit in fruits:
    print('This fruit already exits in the list')
else:
    fruits.append(new_fruit)
    print('updated list: ', fruits)


person = {
    'firstname': 'James',
    'lastname': 'Akpa',
    'age': '27',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoBD', 'Python'],
    'address': {
        'street': 'Space Street',
        'zipcode': '02210'
    }
}
if 'skills' in person:
    skills_list = person['skills']
    middle_skill = len(skills_list) // 2
    print('The middle skill is', skills_list[middle_skill])

language = 'python'
for i in range(len(language)):
    print(language[i])


numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be', number + 1) if number !=5 else print("Loop's end")
print('outside the loop')


for i in range(11):
    print(i)

count = 10
while count >= 0:
    print(count)
    count = count - 1


for i in range(1,7):
    print("#" * i)



for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()


for i in range(11):
    print(f"{i} x {i} = {i * i}")


items = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in items:
    print(item)


total = 0
for i in range(101):
    total += i
print('The sum of all numbers is: ', total)
"""
even = 0
odd = 0
for i in range(101):
    if i % 2 == 0:
        even += i
    else:
        odd +=i
print('even is ', even,  "and odd is ", odd)

sum_even = sum(range(0,101,2))
sum_odd = sum(range(1,101,2))
print('even is ', sum_even,  "and odd is ", sum_odd)