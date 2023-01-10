# Парсер HTML социальной сети + интерфейс к нему ​и скрапинг & очередь задач


A brief description of what this project does and who it's for

## Технологии

* BeautifulSoup4
* Selenium
* eeL
* flask
* QR
* Redis

## Установка технологий

pip install BeautifulSoup4, Selenium, eel

## Установка технологий для скрапинг & очередь задач
pip install flask, rq, redis


## Необходимое условие

Установленный Python 3 или более поздней версии

Также необходимо установить на компьютер браузер Google Chrome и Chrome скачать драйвер для работы с Selenium. Драйвер можно скачать по ссылке https://github.com/Bisalia/vk-parser/blob/main/chromedrivier/chromedriver.exe После в самом коде необходимо будет указать полный путь до драйвера.

Пример для ОС Windows


    driver = webdriver.Chrome('D:\\parsing_1\\chomedriver\\chromedriver.exe', options=options)

и для скрапинг & очередь задач необходимо создать виртуальной среды

    python -m venv env
    source env/Scripts/activate 

затем создать среду разработки

    export FLASK_APP=run.py
    export FLASK_ENV=development
    flask run

чтобы запускать сервер redis 


    redis-server
    rq worker
