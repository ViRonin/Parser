# Parser
Простые парсеры для сбора статичной информации с сайтов методом requests и уже сохраненных html ссылок в XLS (EXCEL) и TXT
==============================

[![Downloads](https://pepy.tech/badge/requests/month)](https://pepy.tech/project/requests)
[![Supported Versions](https://img.shields.io/pypi/pyversions/requests.svg)](https://pypi.org/project/requests)
[![Contributors](https://img.shields.io/github/contributors/psf/requests.svg)](https://github.com/psf/requests/graphs/contributors)

------------------------------

Парсер работает из командной строки и раздельно на 4 блока. Есть возможность выполнять по запросам методом использования библиотеки [requests](https://pypi.org/project/requests/) а так же извлекать информацию уже из сохранённой *html* страницы.


## [1. Блок сохранения](https://github.com/ViRonin/Parser/blob/main/Parser%20py/Sawer%20html%20file%20.py) 


Sawer html file .py следующие библиотеки в этом блоке :	  

	import pyautogui
	from time import sleep
	from selenium import webdriver
	from selenium.webdriver.chrome.options import Options
	from random import choice
	import requests

Данные сохраняються в формате `.html`


## [2. Блок разбора сохраненной страницы](https://github.com/ViRonin/Parser/blob/main/Parser%20py/Data%20collection%20through.py) 

Data collection through.py:

Используеться одна библиотека [beautifulsoup4](https://pypi.org/project/beautifulsoup4/), код выполнен для разбора *html* в виде ранжирования `for i in range(2, 800):` 

В этом блоке данные вызываться в терминале ссылки поэтом для своих нужд изменяйте `class_` и `item`.

## [3. Блок разбора сохраненной страницы для `.xlsx` и `.txt`](https://github.com/ViRonin/Parser/blob/main/Parser%20py/Pars%20in%20Exel%20and%20text.py)
Sawer html file .py следующие библиотеки в этом блоке :	  

	from bs4 import BeautifulSoup
	import os, openpyxl
	from datetime import datetime

Данные сохраняться в формате `.xlsx` и `.txt`, в разбивке `одна ячейка информации = одна строка`. 

`datetime` необходимо для записи `.xlsx` документа во избежание конфликта называя сам документ датой записи и формированием документа


[4. Парс методом requests](https://github.com/ViRonin/Parser/blob/main/Parser%20py/With%20requests%20.py)

[requests](https://pypi.org/project/requests/) или запросами непосредственно на указанный сайт но может не работать если:

- указано неправильно `div` или `class`
- сработала капча сайта
- необходимо юзер агент прописывать или прокси


Преимущество: 
- скорость выполнения задач
- отпадает необходимость сохранять страницы на жёсткий диск ПК
-   


## Технические параметры

Код парсера написан на Python 3.9.
