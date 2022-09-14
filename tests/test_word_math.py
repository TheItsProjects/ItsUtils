import unittest
from its_utils.word_math import WordMath
from tests.utils import Util


class Tests(unittest.TestCase):

    def setUp(self) -> None:
        self.util = Util(self, WordMath.full)

    def tearDown(self) -> None:
        pass

    def test_one_digit_numbers(self):
        # zero (upper- and lowercase)
        zero = {0: ["null", "Null"]}

        # other numbers
        ones = {
            1: "eins",
            2: "zwei",
            3: "drei",
            4: "vier",
            5: "fünf",
            6: "sechs",
            7: "sieben",
            8: "acht",
            9: "neun"
        }

        self.util.testall(zero)  # type: ignore
        self.util.testall(ones)  # type: ignore

    def test_two_digit_numbers(self):
        # tenth numbers
        tenth = {
            10: "zehn",
            11: "elf",
            12: "zwölf",
            13: "dreizehn",
            14: "vierzehn",
            15: "fünfzehn",
            16: "sechzehn",
            17: "siebzehn",
            18: "achtzehn",
            19: "neunzehn"
        }

        # ten-like numbers
        tens = {
            20: "zwanzig",
            21: "einundzwanzig",
            30: "dreißig",
            31: "einunddreißig",
            40: "vierzig",
            50: "fünfzig",
            60: "sechzig",
            70: "siebzig",
            80: "achtzig",
            90: "neunzig"
        }

        self.util.testall(tenth)  # type: ignore
        self.util.testall(tens)  # type: ignore

    def test_three_digit_numbers(self):
        threes = {
            100: ["einhundert", "hundert"],
            101: ["einhunderteins", "einhundertundeins", "hundertundeins"],
            112: "einhundertzwölf",
            162: "einhundertzweiundsechzig",
            200: "zweihundert",
            300: "dreihundert",
            400: "vierhundert",
            500: "fünfhundert",
            600: "sechshundert",
            700: "siebenhundert",
            800: "achthundert",
            900: "neunhundert"
        }

        self.util.testall(threes)

    def test_four_digit_numbers(self):
        fours = {
            # 1000: ["eintausend", "tausend"],
            1001: ["eintausendeins", "eintausendeins", "eintausendundeins"],
            1043: "eintausenddreiundvierzig",
            1521: "eintausendundfünfhunderteinundzwanzig",
            2000: "zweitausend",
            3000: "dreitausend",
            4000: "viertausend",
            5000: "fünftausend",
            6000: "sechstausend",
            7000: "siebentausend",
            8000: "achttausend",
            9000: "neuntausend"
        }

        self.util.testall(fours)

    def test_five_six_seven_nine_digit_numbers(self):
        fives = {10000: "zehntausend", 50000: "fünfzigtausend"}
        sixes = {
            100000: ["hunderttausend", "einhunderttausend"],
            500000: "fünfhunderttausend",
            703010: "siebenhundertdreitausendundzehn"
        }

        sevens = {
            # 1000000: ["millionen", "eine millionen"],
            # 5000000: "fünf millionen",
            6041345:
            "sechs millionen einundvierzigtausenddreihundertundfünfundvierzig"
        }

        nines = {
            999999999:
            "neunhundertneunundneunzig millionen neunhundertneunundneunzigtausendneunhundertundneunundneunzig"
        }

        self.util.testall(fives)  # type: ignore
        self.util.testall(sixes)
        self.util.testall(sevens)  # type: ignore
        self.util.testall(nines)  # type: ignore

    def test_error(self):
        self.assertRaises(ValueError, WordMath.full, "")
