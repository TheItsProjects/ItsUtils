from typing import Dict, List, Union
import unittest
from its_utils.word_math import WordMath

class Tests(unittest.TestCase):
    def setUp(self) -> None:
        pass
    
    def tearDown(self) -> None:
        pass
    
    def test_one_digit_numbers(self):
        # zero (upper- and lowercase)
        zero = {
            0: ["null", "Null"]
        }
        
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
        
        testall(zero, self) # type: ignore
        testall(ones, self) # type: ignore
        
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
            19: "neunzehn"}
        
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
        
        testall(tenth, self) # type: ignore
        testall(tens, self)  # type: ignore

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
        
        testall(threes, self)
        
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
        
        testall(fours, self)
        
    def test_five_six_seven_nine_digit_numbers(self):
        fives = {
            10000: "zehntausend",
            50000: "fünfzigtausend"
        }
        sixes = {
            100000: ["hunderttausend", "einhunderttausend"],
            500000: "fünfhunderttausend",
            703010: "siebenhundertdreitausendundzehn"
        }
        
        sevens = {
            # 1000000: ["millionen", "eine millionen"],
            # 5000000: "fünf millionen",
            6041345: "sechs millionen einundvierzigtausenddreihundertundfünfundvierzig"
        }
        
        nines = {
            999999999: "neunhundertneunundneunzig millionen neunhundertneunundneunzigtausendneunhundertundneunundneunzig"
        }
        
        testall(fives, self)  # type: ignore
        testall(sixes, self)
        testall(sevens, self)  # type: ignore
        testall(nines, self)  # type: ignore
        
def testall(dictionary: Dict[int, Union[str, List[str]]], self: Tests):
    for num, word in dictionary.items():
        with self.subTest("", num=num):
            if type(word) == list:
                for w in word:
                    self.assertEqual(num, WordMath.full(w), f"failed at: {num} | {w}")
            else:
                self.assertEqual(num, WordMath.full(word), f"failed at: {num} | {word}")  # type: ignore



