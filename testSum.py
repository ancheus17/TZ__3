import unittest

import main


class MyTestCase(unittest.TestCase):
    def test_sum(self):
        main.readNums("simpleTest.txt")
        self.assertEqual(main.getSum(), 449)


if __name__ == '__main__':
    unittest.main()
