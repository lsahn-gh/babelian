[![Python](https://img.shields.io/badge/python-2.7%2C%203.4-red.svg)](#)
[![Platform](https://img.shields.io/badge/platform-osx%2C%20linux-lightgrey.svg)](#)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](#)

# Babelian
Language learners typically use a web-browser to look for the definition of words.  
But don't you think that the process of looking up is so pricky?!  
For example, the steps are,
- Open a web-browser.
- Click some links until you get a online dictionary  
- Type some words, then look for words.  

This is a solution for looking up words quickly and easily!  

Babelian is a dictionary on command-line.  
You can look up words/phrases/examples without web-browsers.  
This will help Developers/Students/Teachers, or 2nd languages learners.  

Youtube : [https://youtu.be/Za7eRZOowtw](https://youtu.be/Za7eRZOowtw)  
Github  : [https://github.com/memnoth/babelian](https://github.com/memnoth/babelian)

# Index
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

# Features
- Search words.
- Search examples.
  - Examples are very important when you learn 2nd languages.
- Support [ISO-639-3](https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes) codes. 
- Support unicode.
- Support systems.
  - Linux (tested)
  - Mac OS X


# Python
- Great than or equal Python 2.7 (tested)
- Great than or equal Python 3.4 (tested)

# Install 
```shell
$ git clone https://github.com/memnoth/babelian.git

$ cd babelian

$ [sudo] python setup.py install
```
Recommend to install it in Python Virtual Environment.

# Uninstall 
```shell
$ [sudo] pip uninstall babelian
```
All babelian modules will be removed from your system.

# Quick-Guide
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

#### -s LANG
```shell
$ wrds -s kor -n 1 도서관

  - Phrase  : library
  - Meaning : institution which holds books etc.

$
```

#### -d LANG
```shell
$ wrds -d fra library

  - Phrase  : bibliothèque
  - Meaning : collection of books
  - Meaning : institution which holds books etc.

  ...

$
```

#### -n NUM
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

#### -ws
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

#### -os
```shell
$ wrds -s kor -d tur -n 1 -os 도서관
 * Examples

  - Native  : 나는 도서관에서만 공부해요.
  - Second  : Yalnızca kütüphanede çalışırım.

$
```

# Advanced
Search sentences.
```shell
$ wrds -d tur -ws -n 1 please to meet you

 * Not found phrases.

 * Examples

  - Native  : Pleased to meet you.- Pleased to meet you
  - Second  : Tanıştığımıza sevindim- Tanıştığımıza
              sevindim

$
```
from Finnish to Russian.
```shell
$ wrds -s fin -d rus -n 1 kirjasto 

  - Phrase  : библиотека
  - Meaning : Место, где хранятся книги и другие написанные материалы.

$
```
from Turkish to Arabic.
```shell
$ wrds -s tur -d ara -n 1 kütüphane 

  - Phrase  : مكتبة

$
```
from Arabic to Deutsch.
```shell
$ wrds -s ara -d deu -n 1 مكتبة  

  - Phrase  : Bibliothek

$
```

# API
[Glosbe](https://glosbe.com) provides the API.  
Thanks to **Glosbe**!.    

# License
The MIT License (MIT)

# Author
Yi-Soo Thomas An
