'''
# WordMath Utility

created by ItsNameless

:copyright: (c) 2022-present ItsNameless
:license: MIT, see LICENSE for more details.
'''

from typing import List
from .string_math import StringMath


class WordMath:
    '''
    # Utility for converting numerals to integers

    This utility converts numerals to their integer counterparts and returns their value.

    To use it, simply use the command:
    ```
    WordMath.full("siebenhundertdrei")
    ```
    '''
    # simple numbers
    # prefixable numbers and suffixes
    tenths = {
        "null": ["+", "0"],
        "ein": ["+", "1"],
        "zwei": ["+", "2"],
        "drei": ["+", "3"],
        "vier": ["+", "4"],
        "fünf": ["+", "5"],
        "sechs": ["+", "6"],
        "sieben": ["+", "7"],
        "acht": ["+", "8"],
        "neun": ["+", "9"],
        "zehn": ["+", "10"],
        "zig": ["*", "10"]
    }

    # big multiplicators
    bigs = {
        "hundert": ["*", "100"],
        "tausend": ["*", "1000"],
        "million": ["*", "1000000"]
    }

    # conjunctions without any use
    conjunctions = {" ": ["", ""], "": ["", ""], "und": ["", ""]}

    # all matchable substrings
    all_matches = tenths.copy()
    all_matches.update(bigs)
    all_matches.update(conjunctions)

    # substrings which need to be replaced in order to be processed more easily
    replaces = {
        "elf": "einszehn",
        "zwölf": "zweizehn",
        "sechzehn": "sechszehn",
        "siebzehn": "siebenzehn",
        "zwanzig": "zweizig",
        "sechzig": "sechszig",
        "siebzig": "siebenzig",
        "eine": "ein",
        "eins": "ein",
        "dreißig": "dreizig",
        "millionen": "million"
    }

    @classmethod
    def preprocess(cls, numword: str) -> List[str]:
        '''
        Preprocesses the input string for usage with the converter.

        Whitespaces are allowed.

        :param numword: Numeral to be preprocessed.
        :type numword: str
        :raises ValueError: Raises when the string contains invalid characters. (Substrings not defined in cls.all_matches)
        :return: A list of substrings that represent the tokens in the numword.
        :rtype: List[str]
        '''

        # check if string is empty
        if not numword:
            raise ValueError("Object can not be preprocessed. It is empty.")

        # make all chars lowercase
        numword = numword.lower()

        # replace substrings with recognizable counterparts
        for old, new in cls.replaces.items():
            numword = numword.replace(old, new)

        # seperate numword into its substrings
        out: List[str] = []
        stack = ""

        for char in numword:

            # append char to stack
            stack += char

            # iterate over each matchable substring
            for match in cls.all_matches.keys():

                if stack == match:
                    # check if match is a conjunction
                    if match in cls.conjunctions.keys():
                        # do not append them, as they are not needed
                        stack = ""
                        continue

                    # check if there is a single before bigs
                    elif match in cls.bigs.keys():
                        # if there is no element before a big, add a 1

                        if len(out) == 0:
                            out.append("ein")

                    # append substring to out and clear stack
                    out.append(stack)
                    stack = ""

        # check if stack is not empty
        # raise Exception if there are still elements
        if stack != "":
            raise ValueError(
                'Object can not be preprocessed. It contains invalid characters.'
            )

        return out

    @classmethod
    def converter(cls, inp: List[str]) -> List[str]:
        '''
        Converts the input string into an mathmatical expression to be used with string_math.

        :param inp: The input string to be converted into a mathmatical expression.
        :type inp: List[str]
        :return: The input string converted into a mathmatical expression.
        :rtype: List[str]
        '''

        # convert substrings to numbers and mathmatical symbols
        out: List[str] = []
        stack: List[str] = []

        partial_bigs = cls.bigs.copy()
        partial_bigs.pop("hundert")

        # iterate over each substring in inp
        for sub in inp:

            # check if word is a big (without "hundert")
            # If it is, its prefix numbers (Ein-, Zehn-, ...)
            # will be surrounded by brackets so they will be
            # calculated correctly.
            if sub in partial_bigs.keys():
                # check if "(" is not the first element
                # add "+"
                if len(out) > 0:
                    out.append("+")
                # add "(" before stack
                out.append("(")
                # push stack without its first operator
                out += stack[1:]
                # add ")" after stack
                out.append(")")
                # append sub
                out += cls.all_matches[sub]
                # clear stack
                stack = []

            # otherwise add sub to stack
            else:
                stack += cls.all_matches[sub]

        # append last numbers to out
        out += stack

        # remove first element if it is a "+" or "*", as this would not be
        # calculated correctly
        if out[0] in ("+", "*"):
            out.pop(0)

        return out

    @classmethod
    def _calculate(cls, inp: List[str]) -> int:

        # send to StringMath to calculate the result
        return StringMath.calculate(
            StringMath.shunting_yard(inp))  # type: ignore

    @classmethod
    def full(cls, numword: str) -> int:
        '''
        Calculates the integer of a given numeral (numword).

        Uses a conversion algorithm and string_math to convert the the input into an integer.

        :param numword: The string to be converted.
        :type numword: str
        :return: The string converted into an integer.
        :rtype: int
        '''

        return cls._calculate(cls.converter(cls.preprocess(numword)))
