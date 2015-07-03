# Babelian
바벨리안은 브라우저 없이 단어/구/예제를 검색할 수 있는 터미널 사전입니다.  
이 프로그램은 개발자/학생/선생님, 또는 외국어를 공부하는 사람을 도와줍니다.  
사전 API는 [*glosbe.com*](https://glosbe.com)에서 지원하고 있습니다.  
**glosbe**에게 고마움을 전합니다.  

## Index
 - [번역판](#번역판)
 - [기능](#기능)
 - [설치하기](#설치하기)
 - [퀵 가이드](#퀵-가이드)
   - 옵션
     - [-f LANG](#-f-lang)
     - [-d LANG](#-d-lang)
     - [-n NUM](#-n-num)
     - [-we](#-we)
     - [-op](#-op)
 - [응용하기](#응용하기)
 - [라이센스](#라이센스)
 - [API](#api)

## 번역판
- [한국어](./README-ko.md)

## 기능
- ISO-639-3(또는 2)에 있는 언어 코드를 모두 지원합니다.
  - [ISO-639-3 codes.](https://en.wikipedia.org/wiki/List_of_ISO_639-3_codes)
- 유니코드를 지원합니다.
- 예제를 지원합니다.
  - 외국어를 공부할 때 예제와 같이 학습하는 방법은 굉장히 중요합니다.
- 지원하는 시스템
  - 리눅스 (테스트 완료)
  - 맥 OS X
- 지원하는 파이썬 버전
  - >= Python 2.7 (테스트 완료)
  - >= Python 3.4 (테스트 완료)

## 설치하기
- [English](./docs/INSTALL.md)
- [한국어](./docs/INSTALL-ko.md)

## 퀵 가이드
Usage: td [-h] [-f LANG] [-d LANG] [-n NUM] [-we] [-op] wrd [wrd ...]  

| args | default | description |
|------|---------|-------------|
| -h, --help | None | help 메세지 보기. |
| wrd | None | 최소 하나 이상의 단어가 필요합니다. |
| -f LANG | eng | 검색에 사용할 단어의 ISO-639-3 code. |
| -d LANG | eng | 검색할 단어의 ISO-639-3 code. |
| -n NUM | 3 | 출력할 개수 |
| -we | False | 예제와 같이 검색하기. |
| -op | False | 예제만 검색하기. |

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

## 응용하기
여러 단어를 이용해서 검색하기.
```shell
$ td please to meet you -d tur -we -n 1
 * Not found phrases.
 * Examples
  - Native  : Pleased to meet you
  - Second  : Çok memnun oldum

$
```
핀란드어로 러시아어 검색하기.
```shell
$ td kirjasto -f fin -d rus -n 1

  - Phrase  : библиотека
  - Meaning : Место, где хранятся книги и другие написанные материалы.

$
```
터키어로 아랍어 검색하기.
```shell
$ td kütüphane -f tur -d ara -n 1

  - Phrase  : مكتبة

$
```
아랍어로 독일어 검색하기.
```shell
$ td مكتبة -f ara -d deu -n 1

  - Phrase  : Bibliothek

$
```

# 라이센스
The MIT License (MIT)

# API
[Glosbe](https://glosbe.com) provides.