# -*- coding: utf-8 -*-

import urllib
import json


class Babelian():

    def __init__(self, words, fl, dl):
        self.words = words
        self.from_lang = fl
        self.dest_lang = dl

    @classmethod
    def search_word(cls, args):
        b2lian = cls(args.word, args.from_lang, args.dest_lang)
        b2lian.display_result()

    @classmethod
    def search_phrase(cls, args):
        b2lian = cls(args.word, args.from_lang, args.dest_lang)
        b2lian.display_result()

    def display_result(self):
        data = self.get_json()
        if "ok" not in data.get('result'):
            raise Exception("Couldn't get a result from dictionary.")
        if 'tuc' not in data:
            raise Exception("Check -f, or -d option!")
        res = data['tuc']
        print('The result of {0}'.format(' '.join(self.words)))
        for item in res:
            if 'phrase' in item:
                print('\t Phrase  : {0}'.format(
                    item["phrase"]["text"].encode('utf-8')))
            if "meanings" in item:
                print('\t Meaning : {0}'.format(
                    item["meanings"][0]["text"].encode('utf-8')))
            print('')

    def get_json(self):
        response = urllib.urlopen(self.make_url())
        data = json.loads(response.read())
        return data

    def make_url(self):
        return 'https://glosbe.com/gapi/translate?from={0}&dest={1}&format=json&phrase={2}'.format(self.from_lang, self.dest_lang, self.to_unicode_url(self.words))

    def to_unicode_url(self, words):
        return urllib.quote_plus(' '.join(words))
