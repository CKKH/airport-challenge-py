''' Weather module '''

import random


class Weather:
    ''' Creates weather '''

    def __init__(self):
        pass

    @classmethod
    def check_stormy(cls):
        ''' Returns stormy as True '''

        return random.choice([True, False, False])
