import unittest

import main


class MyTestCase(unittest.TestCase):
    def test_valid(self):
        main.readNums("./validTest.txt")
        self.assertEqual(len(main.numbers), 6)


if __name__ == '__main__':
    unittest.main()
