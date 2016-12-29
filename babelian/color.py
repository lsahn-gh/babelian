"""
Copyright (c) Babelian 2015-2016, Yi Soo, (Jeff) An

A color class for terminal
"""
# -*- coding: utf-8 -*-

class COLOR(object):
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    ENDC = '\033[0m'    # The end of color

    def __setattr__(self, *_):
        pass

# Test for COLOR class
if __name__ == '__main__':
    COLOR = COLOR()

    print(''.join([COLOR.RED, "Hello", COLOR.ENDC]))
