my_tuple= ()
my_tuple= (1, "dos", true)
type(my_tuple)
my_tuple[0] """ 1"""

my_tuple[0]= 2 """it's not possibe todo"""

my_tuple(1)
type(my_tuple)""" int """

my_tuple(1,)
type(my_tuple) """ tuple type"""

tuple_two= (2, 3, 4)
my_tuple += tuple_two """(1, 2, 3, 4)"""

x, y, z =  tuple_two

x """ 2 """
y """ 3 """
z """ 4 """

def coords():
    return (5, 4)

coordinate= coords()
x, y = coords()  """ x =5 , y= 4 """
