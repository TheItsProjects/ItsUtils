'''
# DebugPrompt Utility

created by ItsNameless

:copyright: (c) 2022-present ItsNameless
:license: MIT, see LICENSE for more details.
'''

from threading import Thread
from typing import Union


class Input():
    '''
    # Utility to ask the user for input for a specific time

    This utility can ask the user for input and wait a few seconds. If the user does not give an input, the input timeouts and you can decide what to do now.
    
    Usage:
    ```
    Input.input("Type your name: ", 5)
    '''
    _output = None

    @classmethod
    def input(cls, message: str, timeout: int) -> Union[str, None]:
        '''
        Ask the user for input and return the input and whether the user
        activated the input or not.

        The 'message' will be displayed to the user and the user will have
        'timeout' seconds to answer.
        
        If the user does not answer within 'timeout' seconds, the input will be returned as None.
        
        If the user answers, the input will be returned.

        :param message: The message to be displayed to the user.
        :type message: str
        :param timeout: The number of seconds to wait for the user to answer.
        :type timeout: int
        :return: The given input or None if no input was given.
        :rtype: Union[str, None]
        '''
        cls._output = None

        # create a thread to handle the input
        t = Thread(target=cls.get_input, args=(message, ))
        t.daemon = True
        t.start()
        t.join(timeout=timeout)

        return cls._output

    @classmethod
    def get_input(cls, message: str):
        cls._output = input(message)
