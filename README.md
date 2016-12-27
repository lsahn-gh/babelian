# Babelian
Babelian is a dictionary of a Terminal.  
You can search some words/phrases/examples without Browser.  
This program will help Developers/Students/Teachers, or who is learning 2nd languages.  
[*glosbe.com*](https://glosbe.com) provides the API of dictionary.  
Thanks **glosbe**!

## Index
 - [Translations](#translations)
 - [Features](#features)
 - [Install Guide](#install-guide)
 - [Quick Guide](#quick-guide)
   - Options
     - [-f LANG](#-f-lang)
     - [-d LANG](#-d-lang)
     - [-n NUM](#-n-num)
     - [-we](#-we)
     - [-op](#-op)
 - [Advanced](#advanced)
 - [License](#license)
 - [API](#api)

## Translations
- [한국어](./README-ko.md)

## Features
- Supports all languages of ISO-639-3(also 2) list.
  - [ISO-639-3 codes.](https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes)
- Supports Unicode.
- Supports Examples.
  - Examples are very important when you are learning 2nd languages.
- Supports systems.
  - Linux (tested)
  - Mac OS X
- Supports version of Python.
  - >= Python 2.7 (tested)
  - >= Python 3.4 (tested)

## Install Guide
- [English](./docs/INSTALL.md)
- [한국어](./docs/INSTALL-ko.md)

## Quick-Guide
Usage: td [-h] [-f LANG] [-d LANG] [-n NUM] [-we] [-op] wrd [wrd ...]  

| args | default | description |
|------|---------|-------------|
| -h, --help | None | Show help message and exit. |
| wrd | None | It must have a word at least. |
| -f LANG | eng | ISO-639-3 code to search in `LANG` from. |
| -d LANG | eng | ISO-639-3 code to search in `LANG` to. |
| -n NUM | 3 | A number of print out, three results will print without -n |
| -we | False | Search with examples. |
| -op | False | Search only examples. |

##### -f LANG
```shell
$ td 도서관 -f kor -n 1

  - Phrase  : library
  - Meaning : institution which holds books etc.

$
```

##### -d LANG
```shell
$ td library -d fra

  - Phrase  : bibliothèque
  - Meaning : collection of books
  - Meaning : institution which holds books etc.

  ...

$
```

##### -n NUM
```shell
$ td library -d kor -n 2

  - Phrase  : 도서관
  - Meaning : institution which holds books etc.
  - Meaning : Place where books and other literary materials are kept.

  - Phrase  : 라이브러리
  - Meaning : collection of subprograms
  - Meaning : A location on a SharePoint site where a collection of files
              and their associated metadata are stored.

$
```

##### -we
```shell
$ td library -d ara -n 1 -we

  - Phrase  : مكتبة
  - Meaning : institution which holds books etc.

 * Examples
  - Native  : The Satya N. Nandan Library manages the Authority's
              specialized collection of reference and research materials
              focusing on matters relating to the law of the sea, ocean
              affairs and deep seabed mining
  - Second  : تدير مكتبة ساتيا ن. ناندان مجموعة مراجع ومواد بحثية
              متخصصة تملكها السلطة وتركز على المسائل المتعلقة بقانون
              البحار وشؤون المحيطات والتعدين في قاع البحار العميقة

$
```

##### -op
```shell
$ td 도서관 -f kor -d tur -n 1 -op

 * Examples
  - Native  : 나는 도서관에서만 공부해요.
  - Second  : Yalnızca kütüphanede çalışırım.

$
```

## Advanced
Using multi-words.
```shell
$ td "please to meet you" -d tur -we -n 1
 * Not found phrases.
 * Examples
  - Native  : Pleased to meet you
  - Second  : Çok memnun oldum

$
```
From Finnish to Russian.
```shell
$ td kirjasto -f fin -d rus -n 1

  - Phrase  : библиотека
  - Meaning : Место, где хранятся книги и другие написанные материалы.

$
```
From Turkish to Arabic.
```shell
$ td kütüphane -f tur -d ara -n 1

  - Phrase  : مكتبة

$
```
From Arabic to Deutsch.
```shell
$ td مكتبة -f ara -d deu -n 1

  - Phrase  : Bibliothek

$
```

# License
The MIT License (MIT)

# API
[Glosbe](https://glosbe.com) provides.
