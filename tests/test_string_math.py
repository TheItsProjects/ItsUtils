import unittest
from its_utils.string_math import StringMath
from tests.utils import Util


class CalculateTests(unittest.TestCase):

    def setUp(self) -> None:
        self.util = Util(self, StringMath.full)

    def tearDown(self) -> None:
        pass

    def test_addition(self):
        two_num = {40: "20+20", 134: "100+34", 500: "300+200"}

        three_num = {41: "20+6+15", 135: "50+41+44", 501: "200+211+90"}

        self.util.testall(two_num)  # type: ignore
        self.util.testall(three_num)  # type: ignore

    def test_substraction(self):
        two_num = {50: "60-10", 170: "200-30"}

        three_num = {60: "70-5-5", 180: "400-20-200"}

        self.util.testall(two_num)  # type: ignore
        self.util.testall(three_num)  # type: ignore

    def test_multiplication(self):
        num = {60: "20*3", 150: "25*2*3"}

        self.util.testall(num)  # type: ignore

    def test_division(self):
        num = {60: "120/2", 300: "1200/2/2"}

        self.util.testall(num)  # type: ignore

    def test_power(self):
        num = {25: "5^2", 81: "9^2", 125: "5^3"}

        self.util.testall(num)  # type: ignore

    def test_multi(self):
        num = {70: "(1+4)*(10+4)", 100: "(10^2)+5000-2500*2"}

        self.util.testall(num)  # type: ignore

    def test_error(self):
        self.assertRaises(ValueError, StringMath.full, "")


class CheckTests(unittest.TestCase):

    def setUp(self) -> None:
        self.util = Util(self, StringMath.check_valid_expression)

    def tearDown(self) -> None:
        pass

    def test_check_valid_expression(self):
        tests = {True: ["70*5", "10"], False: ["helloworld 70*5", "10x"]}

        self.util.testall(tests)  # type: ignore
