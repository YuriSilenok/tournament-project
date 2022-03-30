@echo off
mode con:cols=66 lines=20
chcp 65001
cls
if not exist "%cd%\venv\" (
	echo Для запуска веб-приложения необходимо сначала установить проект
) else if exist "%cd%\venv\" (
	.\venv\Scripts\activate
	start http://127.0.0.1:8000/   
	py manage.py runserver
)