from collections import Counter
import re
from os import path
# defining a function
def function_example(str):
    # This function will print the given number inside the function
    x = 3
    y = 7
    print("x = ", x)
    print("str = ", str)

def function_ret(str):
    print("str = ", str)
    ii = str + 5
    return ii




# calling a function
x = 7
print("x outside \'\"the function = ", x)
function_example("ijio")
print("x outside the function = ", x)
#print("x outside the function = ", y)
tt="ir.ia"
print(tt.upper())
print(tt.replace('i','kkkkkkkk'))
print(tt.split('.'))
"""ghgjf 
gj"""
num= 2.55
intnum= int(num)
print(intnum)

mylist = ['a', 'b', 'c', 'a', 'a', 'a', 'b', 'c']
count = Counter(mylist)
print(count)
print(count['a'])

print(mylist[0])

print("uiohuiojnmpklj ",function_ret(77))

L = ['workearly', 'python', 'e-learning']
print(len(L))
print(range(len(L)))
for i in range(0,len(L)):
       print(i)
       print(L[i])


for k in range(20, 40):
         if k == 0: break
         if k % 2: continue
         print(k)



patterns = ['Learning Python', 'workearly']
text = 'Learning Python now'
for pattern in patterns:
     #print(%(pattern, text))
     print('Looking for "%s" in "%s" --> ' %(pattern, text) , end = '')
     print('Looking for ', pattern , ' mesa ', text , end = '')
     if re.search(pattern, text):
          print('Found a match')
     else:
          print('No match found!')

fruits = ['apple', 'banana', 'cherry', 'date']
fruits.insert(1, 'fig')
print("The updated list after insert:", fruits)
last_fruit = fruits.pop()
print("The updated list after insert:", fruits," gsdfgrtgw ",last_fruit)

fruits.remove('banana')
print("The updated list after insert:", fruits," gsdfgrtgw ",last_fruit)


fruits = ['apple', 'banana', 'cherry', 'date', 'date']
fruits_set = set(fruits)
print("The updated set after insert:", fruits_set)

fruits1 = {'apple', 'banana', 'cherry'}
fruits2 = {'date', 'fig', 'grape'}
fruits_union = fruits1.union(fruits2)
print("Tunion:", fruits_union)

fruits1 = {'apple', 'banana', 'cherry'}
fruits2 = {'banana', 'cherry', 'date'}
fruits_intersection = fruits1.intersection(fruits2)

print("The intersection of two sets:", fruits_intersection)

tt=55

def irias_func(str):
    tt=3
    print("Iria:",str," ",tt)

irias_func("Godess111")
print(tt)

string = "Hello World!"
print(string.replace('ll', 'a'))
print(string.split(' '))

text = "Type \"cooking tips\" in Google search!"
print(text)

mylist = ['a', 'b', 'c', 'a', 'a', 'a', 'b', 'c']
count = Counter(mylist)
print(Counter(mylist))

count.update(['a', 'b', 'b', 'c'])
print("Updated", count)

print("Count of \'b\':", count['b'])


def add_numbers(a, b):
    return a + b


# Calling the Function
c = add_numbers(2, 3)
print("Sum: ", c)  # Output: Sum: 5

c = add_numbers("Iria", "3")
print("Sum: ", c)  # Output: Sum: 5


# Example of a Custom Function to Multiply a String
def multiply_string(string, times):
    return string * times


# Calling the Function
result = multiply_string("Na", 4)
print("result: ", result)


# Example of a Custom Function to Check if a String is a Palindrome
def is_palindrome(string):
    return string == string[::-1]



str="irias"
print("test:",str[::-1])
# Calling the Function
result = is_palindrome("level")
print("Result: ", result)  # Output: Result: True

# Example of a Custom Function to Count the Occurrence of a Character in a String
def count_char_occurrence(string, char):
  return string.count(char)

result = count_char_occurrence("mississippi", "s")
print("Result: ", result) # Output: Result: 4

# Example of Using Counter on a List
my_list = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]

result = Counter(my_list)
print("Result: ", result)


# Example of Using most_common
my_list = [1, 1, 2, 3, 4, 5, 3, 2, 3, 4, 2, 1, 2, 3]
counter = Counter(my_list)

result = counter.most_common(3)
print("Result: ", result)

x = 18
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

for x in range(20, 50, 4):
      print(x)
print("-----------")
for x in range(20, 0, -5):
      print(x)

lista=['a','b']

for x in lista:
    print(x)

print("-----------")

for x in range(0,len(lista)):
    print(x)

word = 'workearly'
for letter in word:
       print(letter)
print("-----------")

L = ['workearly', 'python', 'e-learning']
for a in range(len(L)):
       print(L[a])

months = ('September', 'October', 'November', 'December')
for i, m in enumerate(months):
       print(i,m)
print("-----------")
for letter in 'Workearly':
    if letter == 'e':
        pass
        print('This is pass block')
    print( 'Current Letter :', letter)

print("-----------")
file1 = open('workearly.txt', 'w+')
for i in range(10):
      file1.write("The line is %d\r\n" % (i+1))

file1.close()


file1 = open('workearly.txt', 'r')
if file1.mode == 'r':
      contents = file1.read()
      print(contents)

print("-----------")
file1 = open('workearly.txt', 'r')
f2 = file1.readline()
f3 = file1.readline()
print(f2)
print(f3)

file1 = open('workearly.txt', 'a')
file1.write('This will add a new line in our file11122')
file1.close()

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(type(arr))

import numpy as np

arr = np.array(10)

print(arr)

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr[1, 1])

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr[0, -1])

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr[1:4])
print(arr[2:])
print(arr[:4])

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr[6: 8: 1])

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr[1, 0:3])

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
copy = arr.copy()

copy[0] = 24

print(arr)
print(copy)

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
view = arr.view()

view[0] = 24

print(arr)
print(view)

import numpy as np

arr = np.array([[1, 2, 3,4], [4, 5, 6,7], [9,8,6,4]])
copy = arr.copy()

print(arr)
print()
print(arr.shape)

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
view = arr.view()

print(arr)
print()
#print(arr.reshape(1, 3))

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

arrList = np.array_split(arr, 3 )

for arr in arrList:
    print(arr)
arr = np.array([1, 2, 3, 4, 5])

print("---------")
print(arr[1:4])
print(arr[0])
print(arr[2:])
print(arr[:4])

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

arrList = np.array_split(arr, 5)

for arr in arrList:
    print(arr)

    import pandas as pd

    x = [23, 48, 19]
    my_first_series = pd.Series(x)
    print(my_first_series)

    import pandas as pd

    data = {
        "students": ['Iria', 'Eric', 'Tsourapo'],
        "grades": [20, 18, 17]
    }
    my_first_dataframe = pd.DataFrame(data)
    print(my_first_dataframe)


import pandas as pd
data = {
    "students": ['Emma', 'John', 'Bob'],
    "grades": [12, 18, 17]
}
my_first_df=  pd.DataFrame(data)
print(my_first_df['grades'])

import pandas as pd
data = {
    "students": ['Iria', 'Eric', 'Tsourapo'],
    "grades": [20, 18, 17]
}
my_first_df=  pd.DataFrame(data, index=["a", "b", "c"])
first_row = my_first_df.loc["c"]
print(first_row)

import pandas as pd
data = {
    "students": ['Emma', 'John', 'Bob'],
    "grades": [12, 18, 17]
}
my_first_df=  pd.DataFrame(data, index=["a", "b", "c"])
second_row = my_first_df.iloc[0]
print(second_row)


import pandas as pd
df = pd.read_csv("finance_liquor_sales.csv")
print(df.head())


import pandas as pd
df = pd.read_csv("finance_liquor_sales.csv")
print(df.info())

import pandas as pd
df = pd.read_csv("finance_liquor_sales.csv")
print(df.shape)




import pandas as pd
d1 = {'Name': ['Mary', 'John', 'Alice', 'Bob'],
         'Age': [27, 24, 42, 32]}
d2 = {'Position': ['Data Analyst', 'Trainee', 'QA Tester', 'IT'],
          'Years_of_experience':[5, 1, 10, 3] }
df1 = pd.DataFrame(d1, index=[0, 1, 2, 3])
df2 = pd.DataFrame(d2, index=[0, 2, 3, 4])
result = df1.join(df2, how='inner')
print(result)

import matplotlib.pyplot as plt

plt.plot([0, 10], [0, 300])

plt.show()

import matplotlib.pyplot as plt

plt.plot([0, 10], [0, 300], 'o')

plt.show()

import matplotlib.pyplot as plt

plt.plot([0, 2, 4, 6, 8, 10], [3, 8, 1, 10, 5, 12])

plt.show()

import matplotlib.pyplot as plt

plt.plot([0, 2, 4], [3, 8, 1], ls='dotted')

plt.show()

import matplotlib.pyplot as plt

plt.plot([0, 10], [0, 300])

plt.title("Title")
plt.xlabel("X - Axis")
plt.ylabel("y - Axis")

plt.show()

import matplotlib.pyplot as plt

plt.plot([0, 10], [0, 300])

plt.grid()

plt.show()


print("Hello World")
