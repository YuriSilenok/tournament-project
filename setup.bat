@echo off
mode con:cols=66 lines=20
chcp 65001
cls
echo Проверка наличия python.
if not exist "C:\Program Files\Python310\python.exe" (
	echo Скачивние установочного файла python. Пожалуйста, подождите.
	bitsadmin.exe /transfer «DownloadingPython» https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe %cd%\python-3.10.4-amd64.exe > nul
	echo Установка python. Предоставьте программе права администратора.
	python-3.10.4-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
	timeout /t 3 /nobreak > nul
	del /q %cd%\python-3.10.4-amd64.exe
)
if not exist "C:\Program Files\Python310\python.exe" (
	echo Ошибка во время выполнения программы. Завершение через 5 секунд.
	timeout /t 5 /nobreak > nul
	exit
)
if not exist "%cd%\venv\" (
	echo Установка дополнительных библиотек.
	py -m venv venv
	.\venv\Scripts\activate
	pip install -r requirements.txt >nul
	py manage.py makemigrations tournament >nul
	py manage.py migrate >nul
	echo Создание аккаунта администратора.
	py manage.py createsuperuser
	if exist "%cd%\initial_data.yaml" py manage.py loaddata initial_data.yaml
	if exist "%cd%\test_data.yaml" py manage.py loaddata test_data.yaml
	cls
	echo Запуск локального сервера.
	py manage.py runserver
) else if exist "%cd%\venv\" (
	cls
	.\venv\Scripts\activate
	echo Запуск локального сервера.       
	py manage.py runserver
)