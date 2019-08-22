import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_init(self):
        x = Fraction(2,2)
        self.assertEqual(1, x.numerator)
        self.assertEqual(1, x.denominator)
        x = Fraction(3,42)
        self.assertEqual(1, x.numerator)
        self.assertEqual(14, x.denominator)
        x = Fraction(5,6)
        self.assertEqual(5, x.numerator)
        self.assertEqual(6, x.denominator)
        x = Fraction(4,-3)
        self.assertEqual(-4, x.numerator)
        self.assertEqual(3, x.denominator)
        x = Fraction(-2,-2)
        self.assertEqual(1, x.numerator)
        self.assertEqual(1, x.denominator)



    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        f = Fraction(99)
        self.assertEqual("99", f.__str__())

        f = Fraction(36, 0)
        self.assertEqual("0 can't be denominatory", f.__str__())

    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3,4), Fraction(1,12)+Fraction(2,3))
        self.assertEqual(Fraction(25,13), Fraction(2,2)+Fraction(12,13))
        self.assertEqual(Fraction(41,18), Fraction(12,8)+Fraction(7,9))
        self.assertEqual(Fraction(56,33), Fraction(4,3)+Fraction(4,11))
        self.assertEqual(Fraction(35,16), Fraction(6,32)+Fraction(6,3))

    def test_sub(self):
        self.assertEqual(Fraction(3,10), Fraction(2,4)-Fraction(1,5))
        self.assertEqual(Fraction(-2,3), Fraction(2,3)-Fraction(8,6))
        self.assertEqual(Fraction(1,4), Fraction(3,2)-Fraction(5,4))
        self.assertEqual(Fraction(-5,2), Fraction(7,6)-Fraction(11,3))
        self.assertEqual(Fraction(-7,20), Fraction(2,8)-Fraction(3,5))

    def test_mul(self):
        self.assertEqual(Fraction(1,2), Fraction(2,8)*Fraction(2,1))
        self.assertEqual(Fraction(9,16), Fraction(3,4)*Fraction(6,8))
        self.assertEqual(Fraction(5,8), Fraction(5,6)*Fraction(3,4))
        self.assertEqual(Fraction(1,1), Fraction(6,7)*Fraction(7,6))
        self.assertEqual(Fraction(1,1), Fraction(1,3)*Fraction(9,3))


    
    

    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        
        f = Fraction(2,2)
        g = Fraction(-1,-1)
        h = Fraction(5,4)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        
        f = Fraction(42,0)
        g = Fraction(5,0)
        h = Fraction(-5,0)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        


if __name__ == '__main__':
    unittest.main()
