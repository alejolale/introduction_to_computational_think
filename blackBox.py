import unittest

def somme(num_1, num_2):
    """ if we change the function we can see the errors """
    return abs(num_1) + num_2

class BlackBoxTest(unittest.TestCase):

    def test_somme(self):
        num_1= 10
        num_2= 5

        result= somme(num_1, num_2)

        self.assertEqual(result, 15)

    def test_somme_negatifs(self):
        num_1= -10
        num_2= -7

        result= somme(num_1, num_2)

        self.assertEqual(result, -17)

if __name__ == '__main__':
    unittest.main()

