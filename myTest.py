import unittest
from myMain import myMainClass

class myTest(unittest.TestCase):
    def setUp(self):
        self.mymain = myMainClass(3,8)
#assert(False)
#assert(True)

    def test_addition(self):
        self.assertEqual(self.mymain.myFunc(),10)



if __name__ == "__main__":
    unittest.main()