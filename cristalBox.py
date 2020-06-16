import unittest

def isAdult(age):
    if age >= 18:
        return True
    else:
        return False

class CristalTest(unittest.TestCase):
    
    def test_isAdult(self):
        age= 20

        result= isAdult(age)

        self.assertEqual(result, True)

    def test_isYounger(self):

        age= 5

        result= isAdult(age)

        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()