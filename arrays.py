myList= [1, 2, 3]

myList[0]
""" 1 """

myList[1:]
""" [2, 3] """

myList.append(4)
print(myList)
""" [1, 2, 3, 4] """

myList[0]= 'a'
print(myList)
""" ['a', 2, 3 ,4] """

myList.pop()
"""quit last element """


for elem in myList:
    print(element)

a= [1, 2, 3]
b= a

id(a)
id(b)
""" same point """


c= list(a)

id(c)
""" different object in memory-- no side effects """

d= a[::]
""" another form to clonate an array :) """

""" List comprehension """
""" apply operations to an array """

myList= list(range(100))

double= [i * 2 for i in myList]

""" get array list multiplied by 2 """

pairs= [i for i in myList if i % 2 == 0]
""" get pais values """
