import unittest
from myparser import parser_check


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.good = 'Accepted'
        self.bad = 'Not Accepted'

    def test_1(self):
        self.assertEqual(parser_check('abb'), self.good)

    def test_2(self):
        self.assertEqual(parser_check('bababbaabababbabaababbaababba'), self.good)

    def test_3(self):
        self.assertEqual(parser_check('babbabaabbababaabbaababababbaabbababa'), self.good)

    def test_4(self):
        self.assertEqual(parser_check('bababababababababbaababab'), self.good)

    def test_5(self):
        self.assertEqual(parser_check('abbbabaababbabaabbabababaabbaabbaababab'), self.good)

    def test_6(self):
        self.assertEqual(parser_check('abaabbaabbababaababbaabbabababaabbabaabbaabbaababbaababab'), self.bad)

    def test_7(self):
        self.assertEqual(parser_check('abaabbaababababbabaab'), self.bad)

    def test_8(self):
        self.assertEqual(parser_check('abaabababbaabbabaabbaab'), self.bad)

    def test_9(self):
        self.assertEqual(parser_check('aabbaabbaababababbabaabbabaab'), self.bad)

    def test_10(self):
        self.assertEqual(parser_check('abaababbaabbaabbaababbaabbababaabbababababababababa'), self.bad)


if __name__ == '__main__':
    unittest.main()
