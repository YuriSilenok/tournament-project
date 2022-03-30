@echo off
mode con:cols=66 lines=20
chcp 65001
cls
if exist "%cd%\venv\" (
	if exist "%cd%\test_data.yaml" (
		.\venv\Scripts\activate
		py manage.py loaddata test_data.yaml
		echo Данные для тестирования успешо загружены.
	) else echo Не найден файл "test_data.yaml"
) ELSE (
	echo Для загрузки тестировочных данных необходимо установить проект.
)
echo Автоматическое завершение через 5 секунд
timeout /t 5 /nobreak > nul
exit