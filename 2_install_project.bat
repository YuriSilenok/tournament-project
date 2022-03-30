@echo off
mode con:cols=66 lines=20
chcp 65001
cls
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
	echo Проект успешно установлен.
	echo Автоматическое завершение через 5 секунд
	timeout /t 5 /nobreak > nul
) else echo Установка проекта не требуется.