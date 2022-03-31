@echo off
mode con:cols=66 lines=20
chcp 65001
cls
echo Проверка наличия python.
if not exist "C:\Program Files\Python310\python.exe" (
	echo Требуется установка Python.
	echo Скачивние установочного файла python. Пожалуйста, подождите.
	bitsadmin.exe /transfer «DownloadingPython» https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe %cd%\python-3.10.4-amd64.exe > nul
	echo Установка python. Предоставьте программе права администратора.
	python-3.10.4-amd64.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
	timeout /t 3 /nobreak > nul
	del /q %cd%\python-3.10.4-amd64.exe
	echo Python успешно установлен.
	echo Автоматическое завершение через 5 секунд
	timeout /t 5 /nobreak > nul
) else (
	echo Установка Python не требуется.
	echo Автоматическое завершение через 5 секунд
	timeout /t 5 /nobreak > nul
)
exit