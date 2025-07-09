import unittest
import hello


class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")
        self.assertNotEqual(hello.hello(), "bye, world!")
    
    def test_add(self):
        self.assertEqual(hello.add(6,7), 13)
        self.assertEqual(hello.add(4,5), 9)
        self.assertNotEqual(hello.add(6,7), 15)

    def test_subtract(self):
        self.assertEqual(hello.sub(7,5), 2)
        self.assertNotEqual(hello.sub(7,5), 6)
        self.assertEqual(hello.sub(7,3), 4)

    def test_muliply(self):
        self.assertEqual(hello.mul(2,3), 6)
        self.assertEqual(hello.mul(2,4), 8)
        self.assertNotEqual(hello.mul(2,3), 7)

    def test_sqrt(self):
        self.assertEqual(hello.sqrt(25), 5)
        self.assertEqual(hello.sqrt(16), 4)
        self.assertNotEqual(hello.sqrt(16), 5)
    
    def test_power(self):
        self.assertEqual(hello.power(2,2), 4)
        self.assertEqual(hello.power(3,3), 27)
        self.assertNotEqual(hello.power(4,2), 15)

    def test_log(self):
        self.assertEqual(hello.log(100), 4.605170185988092)

    def test_exp(self):
        self.assertEqual(hello.exp(1), 2.718281828459045)

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertEqual(hello.sin(1), 0.8414709848078965)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)

    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertEqual(hello.tan(1), 1.5574077246549023)

    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343306)


if __name__ == "__main__":
    unittest.main()
