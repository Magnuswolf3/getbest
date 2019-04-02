import unittest

import program

class TestExclude(unittest.TestCase):

def test_column(self)
self.testData = getbest.f(os.path.join(this_dir,"../test/bestdat0.csv"))
c1 = getbest.getCols(self.testData)
self.assertEqual(c1, [1,2])

def test_top(self)
c2 = findTop(self.testData, c1[0], c1[1])
self.assertEqual(c2,["167381",90])

if __name__ == '__main__':
unittest.main()
