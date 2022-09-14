'''
# StringMath Utility

created by ItsNameless

:copyright: (c) 2022-present ItsNameless
:license: MIT, see LICENSE for more details.
'''


import re
from typing import Dict, List, Union


class StringMath:
    '''
    # Implementation of the shunting-yard algorithm

    This programm uses the shunting-yard algorithm to convert a stringified mathematical expression into a postfix notation.
    
    It then uses the postfix notation to calculate the result of the expression.

    To use it, simply use the command:
    ```
    StringMath.full("1+2+3")
    ```
    '''

    # define operands
    operands: Dict[str, int] = {
        '^': 2,
        '*': 1,
        '/': 1,
        '+': 0,
        '-': 0,
    }
       
    @classmethod
    def check_valid_expression(cls, expression: str) -> bool:
        '''
        Check whether the expression is valid.
        
        Whitespaces are allowed. \nOnly `numbers, +, -, *, /, ^, (, )`
        
            :param expression: String to be checked.
            :type expression: str
            :return: Whether the string only contains valid characters
            :rtype: bool
        '''
        expression = re.sub(r'\s+', '', expression)

        check = re.fullmatch(r'[\d\+\-\*/\^()]+', expression)

        return check is not None

    @classmethod
    def calculate_char(cls, char1: Union[str, int], char2: Union[str, int],
                       op: str) -> int:
        if op == '+':
            return int(char1) + int(char2)
        elif op == '-':
            return int(char1) - int(char2)
        elif op == '*':
            return int(char1) * int(char2)
        elif op == '/':
            return int(char1) / int(char2)  # type: ignore
        elif op == '^':
            return int(char1)**int(char2)
        else:
            raise ValueError

    @classmethod
    def preprocess(cls, inp: str) -> List[str]:
        '''
        Preprocesses the input string for usage with the shunting yard algorithm.

        Whitespaces are allowed.

            :param inp: String to be preprocessed.
            :type inp: str
            :raises ValueError: Raises when the string contains invalid characters. (Like letters, etc.)
            :return: A list of strings that represent the tokens in the input string.
            :rtype: List[str]
        '''
        # check if string only contains valid characters
        inp = re.sub(r'\s+', '', inp)

        check = re.fullmatch(r'[\d\+\-\*/\^()]+', inp)

        if check is None:
            raise ValueError(
                'Object can not be preprocessed. It contains invalid characters.'
            )

        # preprocess string
        return re.findall(r'([\d]+|[\+]|[-]|[\*]|[/]|[\^]|[(]|[)])', inp)

    @classmethod
    def shunting_yard(cls, inp: List[str]) -> List[Union[str, int]]:
        '''
        Sort the input string into a postfix notation

        Uses the shunting yard algorithm to sort the input string into a postfix notation.

        :param inp: The input string to be sorted into a postfix notation.
        :type inp: List[str]
        :raises ValueError: Raised when there are unmatched parentheses.
        :raises ValueError: Raises when the string contains invalid characters. (Like letters, etc.)
        :return: The input string sorted into a postfix notation.
        :rtype: List[Union[str, int]]
        '''

        # init vars
        parentheses: bool = False

        out: List[Union[str, int]] = []
        stack: list[str] = []

        # iterate over input
        for i in inp:

            # if i is digit, put in out
            if i.isdigit():
                out.append(int(i))

            # take operator from inp
            elif i in cls.operands:
                # iterate over stack to find operator with higher precedence
                # if higher precedence, put in out
                # if same precendence and left associative, put in out
                # else put i in stack
                for i2 in range(len(stack) - 1, -1, -1):
                    # stop at (
                    if stack[i2] == '(':
                        break
                    elif i in ['*', '/']:
                        if cls.operands[stack[i2]] >= 1:
                            out.append(stack.pop(i2))

                    elif i in ['+', '-']:
                        if cls.operands[stack[i2]] >= 0:
                            out.append(stack.pop(i2))

                    elif i == '^':
                        # same precendence and right associative
                        if stack[i2] == '^':
                            pass
                        elif cls.operands[stack[i2]] >= 2:
                            out.append(stack.pop(i2))

                # finally append operator to stack
                stack.append(i)

            elif i == '(':
                parentheses = True
                stack.append(i)

            elif i == ')':
                # if parentheses is True, put in out
                # else, raise error
                if not parentheses:
                    raise ValueError(
                        'Parentheses are not balanced. Too many closing parentheses.'
                    )
                parentheses = False
                for i2 in range(len(stack) - 1, -1, -1):
                    if stack[i2] != '(':
                        out.append(stack.pop(i2))
                    else:
                        stack.pop(i2)
                        break

        # if '(' is left in stack, raise error
        if '(' in stack:
            raise ValueError(
                'Parentheses are not balanced. Too many opening parentheses.')

        # finally empty stack in out
        out += stack[::-1]

        return out

    @classmethod
    def calculate(cls, inp: List[Union[int, str]]) -> Union[int, float]:
        '''
        Calculates the result of a postfix notated string.

        String has to be in postfix notation and has to be generated by the shunting yard algorithm.

        :param inp: The List of input symbols.
        :type inp: List[Union[int, str]]
        :return: The result of the calculation.
        :rtype: Union[int, float]
        '''
        # search for first operator in inp
        # get operator and two numbers before
        # calculate the result of those numbers
        # put result in inp at position of first char (i-2)
        # repeat until no operator is left

        while len(inp) > 1:
            for i in range(len(inp)):
                if inp[i] in cls.operands:
                    op: str = inp.pop(i)  # type: ignore
                    char2: int = inp.pop(i - 1)  # type: ignore
                    char1: int = inp.pop(i - 2)  # type: ignore

                    res = cls.calculate_char(char1, char2, op)

                    inp.insert(i - 2, res)
                    break

        return inp[0]  # type: ignore

    @classmethod
    def full(cls, inp: str) -> Union[int, float]:
        '''
        Calculates the result of a string.

        Uses the shunting yard algorithm to sort the input string into a postfix notation and then calculates its result.

        :param inp: The string to calculate.
        :type inp: str
        :return: The result of the calculation.
        :rtype: Union[int, float]
        '''

        return cls.calculate(cls.shunting_yard(cls.preprocess(inp)))
