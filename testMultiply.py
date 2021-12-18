import unittest

import main

class MyTestCase(unittest.TestCase):
    def test_multiply(self):
        main.readNums("simpleTest.txt")
        self.assertEqual(main.getMult(), -20397256704000)


if __name__ == '__main__':
    unittest.main()
