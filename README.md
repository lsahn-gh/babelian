[![Python](https://img.shields.io/badge/python-2.7%2C%203.4-red.svg)](#)
[![Platform](https://img.shields.io/badge/platform-osx%2C%20linux-lightgrey.svg)](#)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](#)

# Babelian
Babelian is a dictionary on command-line.  
You can search some words/phrases/examples without running WebBrowser.  
This program will help Developers/Students/Teachers, or who learns 2nd languages.  
[*glosbe.com*](https://glosbe.com) provides the API of dictionary.  
Thanks **glosbe**!

Youtube : [https://youtu.be/Za7eRZOowtw](https://youtu.be/Za7eRZOowtw)  

##### READMES
- [한국어](./README-ko.md)  

## Index
 - [Features](#features)
 - [Python](#python)
 - [Install](#install)
 - [Uninstall](#uninstall)
 - [Quick Guide](#quick-guide)
     - [-s LANG](#-s-lang)
     - [-d LANG](#-d-lang)
     - [-n NUM](#-n-num)
     - [-ws](#-ws)
     - [-os](#-os)
 - [Advanced](#advanced)
 - [API](#api)
 - [License](#license)

## Features
- Support all languages of [ISO-639-3](https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes) code.
- Support Unicode.
- Support Examples.
  - Examples are very important when you learn 2nd languages.
- Support Systems.
  - Linux (tested)
  - Mac OS X


## Python
- >= Python 2.7 (tested)
- >= Python 3.4 (tested)

## Install 
```shell
$ git clone https://github.com/memnoth/babelian.git

$ cd babelian

$ [sudo] python setup.py install
```
We recommend you install it on your Python Virtual Environment.

## Uninstall 
```shell
$ [sudo] pip uninstall babelian
```
All babelian modules will be removed from you system.

## Quick-Guide
Usage: wrds [-h] [-s LANG] [-d LANG] [-n NUM] [-ws] [-os] word [word ...]  

| args | default | description |
|------|---------|-------------|
| -h, --help | None | Show help message and exit. |
| word | None | It must be at least one **word**. |
| -s LANG | eng | ISO-639-3 code for source. |
| -d LANG | eng | ISO-639-3 code for destination. |
| -n NUM | 3 | A number for print limitation. |
| -ws | False | Search with examples. |
| -os | False | Search only examples. |

##### -s LANG
```shell
$ wrds -s kor -n 1 도서관

  - Phrase  : library
  - Meaning : institution which holds books etc.

$
```

##### -d LANG
```shell
$ wrds -d fra library

  - Phrase  : bibliothèque
  - Meaning : collection of books
  - Meaning : institution which holds books etc.

  ...

$
```

##### -n NUM
```shell
$ wrds -d kor -n 2 library

  - Phrase  : 도서관
  - Meaning : institution which holds books etc.
  - Meaning : Place where books and other literary materials are kept.

  - Phrase  : 라이브러리
  - Meaning : collection of subprograms
  - Meaning : A location on a SharePoint site where a collection of files
              and their associated metadata are stored.

$
```

##### -ws
```shell
$ wrds -d ara -n 1 -ws library

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

##### -os
```shell
$ wrds -s kor -d tur -n 1 -os 도서관
 * Examples

  - Native  : 나는 도서관에서만 공부해요.
  - Second  : Yalnızca kütüphanede çalışırım.

$
```

## Advanced
Searching sentences.
```shell
$ wrds -d tur -ws -n 1 please to meet you

 * Not found phrases.

 * Examples

  - Native  : Pleased to meet you.- Pleased to meet you
  - Second  : Tanıştığımıza sevindim- Tanıştığımıza
              sevindim

$
```
From Finnish to Russian.
```shell
$ wrds -s fin -d rus -n 1 kirjasto 

  - Phrase  : библиотека
  - Meaning : Место, где хранятся книги и другие написанные материалы.

$
```
From Turkish to Arabic.
```shell
$ wrds -s tur -d ara -n 1 kütüphane 

  - Phrase  : مكتبة

$
```
From Arabic to Deutsch.
```shell
$ wrds -s ara -d deu -n 1 مكتبة  

  - Phrase  : Bibliothek

$
```

# API
[Glosbe](https://glosbe.com)

# License
The MIT License (MIT)
