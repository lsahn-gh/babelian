"""
Copyright (c) Babelian 2015, Hyun Jun (Cryptos) An

The Babelian is a dictionary of a Terminal.
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


class Babelian():

    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    ENDC = '\033[0m'
    DASH = 52
    WIDTH_OF_TERM = 60

    def __init__(self, args):
        self.words = args.word
        self.from_lang = args.from_lang
        self.dest_lang = args.dest_lang
        self.num_for_out = args.num_for_out
        self.with_example = args.we
        self.only_example = args.op
        self.get_python_version()

    @classmethod
    def search_word(cls, args):
        babel = cls(args)
        babel.print_result()

    @classmethod
    def search_only_examples(cls, args):
        babel = cls(args)
        babel.print_only_examples()

    @classmethod
    def test_for_charset(cls, args):
        babel = cls(args)
        try:
            if babel.get_python_version() is not 3:
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
            self.print_phrases(data['tuc'])
            if 'examples' in data:
                self.print_with_examples(data['examples'])

    def print_phrases(self, res):
        if not len(res) > 0:
            self.print_err_msg(' * Not found phrases.')
        else:
            print('')
            for items in res[:self.num_for_out]:
                if 'phrase' in items:
                    self.wrap_for_phrase(items['phrase']['text'])
                if 'meanings' in items:
                    for item in items['meanings'][:self.num_for_out]:
                        self.wrap_for_meaning(item['text'])
                print('')

    def print_only_examples(self):
        data = self.get_data()
        if 'examples' in data:
            self.print_with_examples(data['examples'])

    def print_with_examples(self, res):
        if not len(res) > 0:
            self.print_err_msg(' * Not found examples.')
        else:
            print(''.join([self.YELLOW, ' * Examples', self.ENDC]))
            for items in res[:self.num_for_out]:
                self.wrap_for_examples(items)
                print('')

    def get_data(self):
        return self.get_json()

    def get_json(self):
        try:
            response = urlopen(self.make_url())
        except Exception(' Can\'t load datas, try it again later.') as err:
            self.print_err_msg(err)
        else:
            return json.loads(response.read().decode('utf-8'))

    def make_url(self):
        url = None
        if self.only_example:
            url = 'https://glosbe.com/gapi/tm?'
        else:
            url = 'https://glosbe.com/gapi/translate?'
        return ''.join([url,
                        'from={}&'.format(self.from_lang),
                        'dest={}&'.format(self.dest_lang),
                        'format=json&',
                        'tm={}&'.format(self.with_example),
                        'phrase={}'.format(self.to_unicode_url(self.words))
                        ])

    def to_unicode_url(self, words):
        if self.get_python_version() is 2:
            return quote_plus(b' '.join(words))
        elif self.get_python_version() is 3:
            return quote_plus(' '.join(words))
        else:
            raise Exception('Unknown python version!')

    def wrap_for_phrase(self, item):
        text = '  - Phrase  : '
        print(self.routine_for_align(text, item))

    def wrap_for_meaning(self, item):
        try:
            # Python 2
            from HTMLParser import HTMLParser
            html = HTMLParser()
        except:
            # Python 3
            import html
        # Decode HTML escape characters.
        meanings = html.unescape(item)
        print(self.routine_for_align('  - Meaning : ', meanings))

    def wrap_for_examples(self, item):
        tags = [
            '<strong class="keyword">',
            '</strong>'
        ]
        phrs_of_native = item['first']
        phrs_of_second = item['second']
        if phrs_of_native is not None:
            self.print_examples_of_native(phrs_of_native, tags)
        if phrs_of_second is not None:
            self.print_examples_of_second(phrs_of_second, tags)

    def print_examples_of_native(self, phrs, tags):
        native = phrs \
            .replace(tags[0], self.CYAN) \
            .replace(tags[1], self.ENDC)
        print(self.routine_for_align('  - Native  : ', native))

    def print_examples_of_second(self, phrs, tags):
        second = phrs \
            .replace(tags[0], self.GREEN) \
            .replace(tags[1], self.ENDC)
        print(self.routine_for_align('  - Second  : ', second))

    def routine_for_align(self, prefix_txt, item):
        ws = ''.join(['\n', ' ' * len(prefix_txt)])
        return ''.join([prefix_txt, ws.join(wrap(item, self.WIDTH_OF_TERM))])

    def print_err_msg(self, err):
        print(''.join([self.RED, str(err), self.ENDC]))

    def get_python_version(self):
        import sys
        return sys.version_info[0]
