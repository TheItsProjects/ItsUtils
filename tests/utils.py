from typing import Any, Callable, Dict, Union, List
from unittest import TestCase

FirstTest = Any
SecondTest = Any

class Util:

    def __init__(self, obj: TestCase, to_test: Callable[[SecondTest],
                                                        FirstTest]) -> None:
        self.obj = obj
        self.to_test = to_test

    def testall(self, dictionary: Dict[FirstTest, Union[SecondTest,
                                                        List[SecondTest]]]):
        for first, second in dictionary.items():
            with self.obj.subTest(f"{second}", num=first):
                if type(second) == list:
                    for s in second:
                        self.obj.assertEqual(first, self.to_test(s),
                                             f"failed at: {first} | {s}")
                else:
                    self.obj.assertEqual(
                        first,
                        self.to_test(second),  # type: ignore
                        f"failed at: {first} | {second}")  # type: ignore
