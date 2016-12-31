#Exercise 1
from _datetime import date

name = input("Give me your name: ")
age = (int(input("Give me your age: ")))
loop = (int(input("How many time I must print that?: ")))
var = 1
year = date.today().year
tmp1 = 100 - age
then = year + tmp1

while var <= loop:
    print("Your name is %a\nand your age is %a, \nyou will be 100 in %s. " % (name, age, then))
    var = var + 1

#Exercise 2
numer = (int(input("Give me your numer: ")))
check = numer%2
check4 = numer%4

if check==0:
     print (str(numer) + " is even")
     if check4==0:
         print (str(numer) + " is a multiple of 4 ")
else:
     print ("This number is odd")

# Exercise 3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

b.append([x for x in a if x<5])
print (b)

#Exercise 4
number = (int(input("Give me your numer: ")))
a=[]
x = range(1, number)
for i in x:
   if number%i == 0:
       a.append(i)

print (a)
a.append([i for i in range(1, number) if number %i == 0])
print (a)

#Exercise 5
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
import random

a = [random.randrange(1,101) for i in range(random.randrange(3,20))]
b = [random.randrange(1,101) for i in range(random.randrange(3,20))]
c = list(set(a).intersection(b))
a.sort()
b.sort()
c.sort()
print (a)
print (b)
print (c)

#Exercise 5
word = input("Give me the word: ")
word = word.upper()
if word == word[::-1]:
    print ( word + " is a palindrome")
else:
    print ( word + " is not a palindrome")

#Exercise 6
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print ([x for x in a if x%2 == 0])


#Exercise 8
import random
guss_nubmer = str(random.randint(1, 100))
times = 0
score = 0

while score == 0:
    user_input = input("Give me number: ")
    times = times + 1
    if user_input < guss_nubmer:
        print ("Up please!")
    elif user_input > guss_nubmer:
        print ("Down please!")
    else:
        print ("Yeah you win")
        print ("It's take %s time" % (times))
        score = 1
    if times == 10:
        print ("10 miss shots - you LOSE !!! ")
        exit()

#Exercise 9
import random

a = [random.randrange(1,101) for i in range(random.randrange(3,20))]
b = [random.randrange(1,101) for i in range(random.randrange(3,20))]
c = [random.randrange(1,101) for i in range(random.randrange(3,20))]
d = list(set((set(a).intersection(b))).intersection(c))
a.sort()
b.sort()
c.sort()
d.sort()
print (a)
print (b)
print (c)
print (d)

#Exercise 11

def get_prime():
    a=[]
    number = (int(input("Give me your numer: ")))
    x = range(1, number)
    for i in x:
        if number%i == 0:
            a.append(i)
            print (i)
    if len(a) == 1 or number == 1:
        print ( str(number) + " is prime number")
        exit()
    else:
        print (str(number) +" is not a prime number")
        print(a)


print ("While number not be prime")
while True:
    get_prime()
#Exercise 12
a = [5, 10, 15, 20, 25]

def first_last():
    print (a[0])
    print (a[-1])
#one line combo
print (a[::len(a)-1])

first_last()

#Exercise 13
def gen_Fibonnaci():
    how_many_num = (int(input("How many Fibonnaci number do you want| '0' to quit : ")))
    if how_many_num == 0:
       print("Good Bye!")
       exit()
    else:
         if how_many_num == 1:
             a.append(1)
         elif how_many_num == 2:
             a.append(1)
             a.append(1)
         else:
             int(how_many_num)
             for n in range(1, how_many_num + 1):
                 if n == 1:
                     a.append(1)
                 elif n == 2:
                     a.append(1)
                 else:
                     a.append(a[-2] + a[-1])
         print(a)


while True:
     a=[]
     gen_Fibonnaci()

#Exercise 14

import random


def make_list_by_set():
    c=[]
    c = list(set(a).intersection(b))
    print(c)


def make_list_by_loop():
    d=[]
    for i in a:
        if i in b:
           d.append(i)
    print(d)


a = [random.randrange(1,101) for i in range(random.randrange(3,8))]
b = [random.randrange(1,101) for i in range(random.randrange(3,8))]
a.sort()
b.sort()
print(a)
print(b)
make_list_by_set()
make_list_by_loop()

#Exercise 15

word = input("Please give me samoe words:")
transform = word.split()
print(transform[::-1])


#Exercise 16

import random
import string


pwlist = []



def main():
    main_actiity = (int(input("\nWhat strong password do you need \n"
                    "\n  Weak - press 1 \n"
                    "  Stronh - press 2 \n"
                    "  Unix like pass - press 3 \n"
                    "  Press '0' for exit \n"
                    "What do you need? ")))
    if main_actiity == 1:
        weak_gen()
        print (pwstring)
    elif main_actiity == 2:
        strong_gen()
        print (pwstring)
    elif main_actiity == 3:
        unix_pass_gen()
    elif main_actiity == 0:
        print ("\nTo next time man")
        exit()
    else:
        main()


def weak_gen():
    global pwstring
    weak_req = input("Do you really need gen weak password(yes/no): ")
    if weak_req == "yes":
        gen_pass(5)
        random.shuffle(pwlist)
        pwstring = "".join(pwlist)
    elif weak_req == "no":
        main()
    else:
        weak_gen()
    print (pwstring)

def strong_gen():
    global pwstring
    gen_pass(8)
    random.shuffle(pwlist)
    pwstring = "".join(pwlist)
    print (pwstring)

def unix_pass_gen():
    global pwstring
    gen_pass(8)
    gen_random(string.digits)
    gen_random(string.punctuation)
    random.shuffle(pwlist)
    pwstring = "".join(pwlist)
    print (pwstring)


def gen_pass(sing):
    while len(pwlist) < sing:
        word = random.choice(string.ascii_letters)
        if word.lower() not in pwlist:
            if word.upper() not in pwlist:
                pwlist.append(word)


def gen_random(string_type):
        pwlist.append(random.choice(string_type))

main()

#Exercise 17
#HOMEWORD - requestsnei działa w pracy

#import requests
# from bs4 import BeautifulSoup
#
# url = 'http://www.nytimes.com'
# r = requests.get(url)
# r_html = r.text
# soup = BeautifulSoup(r_html, "lxml")
# title = soup.findAll(class_="story-heading")
#
# for item in title:
#     try:
#         print (item.text.strip())
#         except:
#         pass

#Exercise 18


import random


user_guess=(input("Proszę podaj liczbę: "))
random_number=str(random.randrange(1000,9999))
while user_guess != random_number:
     user_guess=(input("Proszę podaj liczbę: "))
     x=[]
     y=[]
     for a in user_guess:
         x.append(a)
     for b in random_number:
         y.append(b)
     cow = len(x)
     print (x)
     print (y)
     print(user_guess)
     print(random_number)

print ("yeah, wygrales")





