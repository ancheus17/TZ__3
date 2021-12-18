import unittest

import main


class MyTestCase(unittest.TestCase):

    def test_min(self):
        main.readNums("./simpleTest.txt")
        self.assertEqual(main.getMin(), -6)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
