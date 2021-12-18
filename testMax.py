import unittest

import main


class MyTestCase(unittest.TestCase):
    def test_max(self):
        main.readNums("simpleTest.txt")
        self.assertEqual(main.getMax(), 324)


if __name__ == '__main__':
    unittest.main()
