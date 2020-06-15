""" range(start, end, steps)"""

my_range= range(1, 5)
type(my_range) 
""" range """

for i in my_range:
    print(i)
    """ 1 2 3 4 --> non inclusive 5"""

my_range= range(0, 7, 2) 
""" goes two by two""" """0246"""
other_range= range(0, 8, 2) 
"""0246"""

"""value equality"""
my_range == other_range 
"""Result is true """

id(my_range)
"""one position id"""
id(other_range) 
"""ither position id """

"""object equality"""
my_range is other_range 
""" returns false not the same object !!!! """

for i in range(1, 102, 2):
    print(i)