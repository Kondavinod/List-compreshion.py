

# 20. Print "Even" or "Odd" for numbers 1–10

s=["Even"  if i%2==0  else  "odd" for i in range(1,11)]
print(s)


# 21	Find the length of each word in ["vinod","Python","Django"]

n="vinod","Python","Django"
s=[len(i) for i in n ]
print(s)


# 22.Extract file extensions from ["data.csv","report.pdf","image.png"].

n="data.csv","report.pdf","image.png"

s=[i.split(".")[-1] for i in n]
print(s)


# 23.	Create a dictionary where keys are numbers 1–5 and values are their squares.

s={i:i**2 for i in range(1,6)}
print(s)

 
# 24.	Map characters of "ABC" to their ASCII values using dictionary comprehension.

n="ABC"
s={i : ord(i) for i in n}
print(s)


# 25.	Combine ['a','b','c'] and [1,2,3] into a dictionary using comprehension.

keys = ['a','b','c']
values = [1, 2, 3]
s={ keys:values for keys,values in zip (keys,values)}
print(s)

# 26.	Generate all prime numbers between 1 and 100 using list comprehension.

s=[ i for i in range(1,100) if i>1 and all (i%j!=0 for j in range(2,i))]
print(s)


# 27.	Create all possible pairs (x, y) from [1,2,3] and [3,1,4] where x ≠ y.

a=[1,2,3]
b=[3,1,4]

s=[(x+y) for x in a  for y in b  if x!=y]
print(s)

# 28.	Generate palindrome numbers between 1 and 100.

s=[ i for i in range(1,101)  if str(i)==str(i) [::-1]  ]
print(s)



# 29.	Add elements from two lists [1,2,3] and [10,20,30] using list comprehension.

a=[1,2,3]
b=[10,11,12]
s=[ (i+j) for i,j in zip(a,b)]
print(s)


# 30.	Extract all student names from [{'name':'Ajay','marks':80},{'name':'Riya','marks':90}].

names=[{'name':'Ajay','marks':80},{'name':'Riya','marks':90}]

s=[ i["name"]  for i in names]
print(s)



# 31.	Generate all palindromic numbers between 1 and 1000.

s=[ i for i in range(1,1001) if str(i)==str(i)[::-1]]
print(s)


# 32.	Get all words starting with 'a' from ['apple','ant','banana','ball']

w='apple','ant','banana','ball'
s=[ i for i in w  if i.startswith("a")]
print(s)


# 33.	Generate numbers between 1 and 20 that are divisible by 2 or 3.

s=[ i for i in range(1,21)  if i%2==0 and i%3==0]
print(s)


# 34.	Generate all coordinate pairs [x, y] where x and y range from 0 to 2.

s=[(i,j)for i in range(3)  for j in range(3)]
print(s)