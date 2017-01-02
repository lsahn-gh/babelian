"""
Copyright (c) Babelian 2015-2016, Yi Soo, (Jeff) An

Babelian is a dictionary of a Terminal.
You can search some words/phrases/examples without Browser.
This program will help Developers/Students/Teachers,
or who is learning 2nd languages.
glosbe provides the API of dictionary.
Thanks **glosbe**!
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals, with_statement

try:
    from urllib import urlopen, quote_plus
except ImportError:
    from urllib.request import urlopen
    from urllib.parse import quote_plus
import json
from textwrap import wrap
from .color import COLOR


class Babelian():
    DASH = 52
    WIDTH_OF_TERM = 60

    def __init__(self, args):
        self.words = args.word
        self.src_lang = args.src_lang
        self.dest_lang = args.dest_lang
        self.print_limit = args.print_limit
        self.with_example = args.ws
        self.only_example = args.os

    @classmethod
    def search_word(cls, args):
        babel = cls(args)
        try:
            if babel.are_ws_os_used_at_the_same():
                raise Exception('Dont use -ws, -os at the same time')
        except Exception as err:
            babel.print_err_msg(err)
        else:
            babel.print_result()

    @classmethod
    def test_for_charset(cls, args):
        babel = cls(args)
        try:
            if python_version() is not 3:
                raise Exception('This routine only allows on Python 3!.')
        except Exception as err:
            babel.print_err_msg(err)
        else:
            f = urlopen(babel.make_url())
            charset = f.info().get_param('charset', 'utf-8')
            print(charset)

    def print_result(self):
        data = self.get_data()
        try:
            if 'tuc' not in data:
                raise Exception(' * Make sure the Options!')
        except Exception as err:
            self.print_err_msg(err)
        else:
            if self.is_os_on() is False:
                self.print_phrases(data['tuc'])
            if self.is_ws_on() or self.is_os_on():
                self.print_with_examples(data['examples'])

    def print_phrases(self, res):
        if len(res) > 0:
            for item in res[:self.print_limit]:
                blank_line()
                if 'phrase' in item:
                    self.wrap_for_phrase(item['phrase']['text'])
                if 'meanings' in item:
                    for mean in item['meanings'][:self.print_limit]:
                        self.wrap_for_meaning(mean['text'])
        else:
            blank_line()
            self.print_err_msg(' * Not found phrases.')
        blank_line()

    def print_with_examples(self, res):
        if len(res) > 0:
            print(colored_msg(COLOR.YELLOW, ' * Examples'))
            for items in res[:self.print_limit]:
                blank_line()
                self.wrap_for_examples(items)
        else:
            blank_line()
            self.print_err_msg(' * Not found examples.')
        blank_line()

    def get_data(self):
        try:
            response = urlopen(self.make_url())
        except Exception(' Can\'t load datas, try it again later.') as err:
            self.print_err_msg(err)
        else:
            return json.loads(response.read().decode('utf-8'))

    def make_url(self):
        return ''.join([
            'https://glosbe.com/gapi/translate?',
            'from={}&'.format(self.src_lang),
            'dest={}&'.format(self.dest_lang),
            'format=json&',
            'tm={}&'.format(self.is_ws_on() or self.is_os_on()),
            'phrase={}'.format(self.to_unicode_url(self.words))
        ])

    def to_unicode_url(self, words):
        if python_version() is 2:
            return quote_plus(b' '.join(words))
        elif python_version() is 3:
            return quote_plus(' '.join(words))
        else:
            raise Exception('Unknown python version!')

    def wrap_for_phrase(self, item):
        print(self.routine_for_align('  - Phrase  : ', item))

    def wrap_for_meaning(self, item):
        try:
            # Python 2
            from HTMLParser import HTMLParser
            html = HTMLParser()
        except:
            # Python 3
            import html
        print(self.routine_for_align('  - Meaning : ', html.unescape(item)))

    def wrap_for_examples(self, item):
        phrs_of_native = item['first']
        phrs_of_second = item['second']
        if phrs_of_native is not None:
            self.print_examples('  - Native  : ', 
                                phrs_of_native, 
                                # colors for replacing tags.
                                COLOR.CYAN, COLOR.ENDC)
        if phrs_of_second is not None:
            self.print_examples('  - Second  : ', 
                                phrs_of_second, 
                                COLOR.GREEN, COLOR.ENDC)

    def print_examples(self, str, phrs, *colors):
        tags = ['<strong class="keyword">', '</strong>']
        lang = phrs \
                .replace(tags[0], colors[0]) \
                .replace(tags[1], colors[1])
        print(self.routine_for_align(str, lang))

    def routine_for_align(self, prefix_txt, item):
        ws = ''.join(['\n', ' ' * len(prefix_txt)])
        return ''.join([prefix_txt, ws.join(wrap(item, self.WIDTH_OF_TERM))])

    def are_ws_os_used_at_the_same(self):
        return (self.is_ws_on() and self.is_os_on())

    def is_ws_on(self):
        """ return type : bool """
        return self.with_example

    def is_os_on(self):
        """ return type : bool """
        return self.only_example

    def print_err_msg(self, err):
        print(colored_msg(COLOR.RED, str(err)))


def python_version():
    import sys
    return sys.version_info[0]

def blank_line():
    print('')

def colored_msg(color, str):
    return ''.join([color, str, COLOR.ENDC])
