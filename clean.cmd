chcp 65001
@echo off
title Очистка временных файлов

del C:\Windows\SoftwareDistribution\Download\*.* /f /s /q
del C:\Windows\Prefetch\*.* /f /s /q
del %temp%\*.* /f /s /q

cls
echo Скрипт завершил работу.
pause
rmdir /s /q C:\INST