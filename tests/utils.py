from typing import Callable, Dict, Union, List
from unittest import TestCase


class Util:

    def __init__(self, obj: TestCase,
                 to_test: Callable[[str], Union[int, float]]) -> None:
        self.obj = obj
        self.to_test = to_test

    def testall(self, dictionary: Dict[int, Union[str, List[str]]]):
        for num, word in dictionary.items():
            with self.obj.subTest(f"{word}", num=num):
                if type(word) == list:
                    for w in word:
                        self.obj.assertEqual(num, self.to_test(w),
                                             f"failed at: {num} | {w}")
                else:
                    self.obj.assertEqual(
                        num,
                        self.to_test(word),  # type: ignore
                        f"failed at: {num} | {word}")  # type: ignore
