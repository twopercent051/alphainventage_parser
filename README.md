<h2>Скрипт для получения сводной информации по ценным бумагам (P/S, Total Revenue 5TTM)</h2>

Скрипт использует подключение по API к ресурсу https://www.alphavantage.co/


<h4>Подготовка к работе</h4>
1. Получить токен доступа к API на https://www.alphavantage.co/
2. Вставить в <code>self.token = "demo"</code> файла api.py полученный токен
3. Заполнить список tickers.json тикерами компаний (соблюдение регистра необязательно)
4. Развернуть виртуальное окружение (при необходимости) и запустить его\
    <code>python3 -m venv venv</code>\
    <code>source venv/bin/activate</code>
5. Установка пакетов и библиотек\
    <code>pip install -r requirements.txt</code>
6. Запуск\
    <code>python3 main.py</code>


<h4>Технологический стек:</h4>\
python 3.10

