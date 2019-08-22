import unittest
from listutil import unique

class ListUtilTest(unittest.TestCase):
 
    def test_single_item_list(self):
        self.assertListEqual(['hi'],unique(['hi']))
        self.assertListEqual(['x'],unique(['x','x','x','x']))

    def test_average_empty_list(self):
        self.assertListEqual([], unique([]))

    def test_typical_extreme_list(self):
        self.assertListEqual([1,2,3,4,5], unique([1,2,1,1,1,2,3,4,5,5]))
        self.assertListEqual([1,2], unique([1,2,1,1,1,2,1]))
        self.assertListEqual(['z','x','c','v'], unique(['z','x','x','z','c','c','v','c','z']))
       
    


    

 
if __name__ == '__main__':
    unittest.main()



