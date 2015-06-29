#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from argparse import ArgumentParser, RawDescriptionHelpFormatter
import textwrap
from app import Babelian


def main():
    parser = ArgumentParser(
        formatter_class=RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            babelian is a terminal dictionary.
            https://github.com/cryptosan/babelian

                Support system list.
                - (O) Linux
                - (O) Mac OS X
                - (X) Windows
            '''))
    parser.add_argument('word', metavar='wrd', type=str, nargs='+',
                        help='A word to search.')
    parser.add_argument('-f', type=str, default='eng', dest='from_lang',
                        help='A language code to search from. (default: eng)')
    parser.add_argument('-d', type=str, default='eng', dest='dest_lang',
                        help='A language code to search to. (defualt: eng)')
    parser.add_argument('-wp', action='store_true', help='Search with phrase.')
    parser.add_argument('-op', action='store_true', help='Search only phrase.')
    args = parser.parse_args()

    if args.op:
        Babelian.search_phrase(args)
    else:
        Babelian.search_word(args)

if __name__ == '__main__':
    main()
