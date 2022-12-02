chcp 65001
@echo off
title Обновление корневых сертификатов
cd C:\INST\Certs

rootsupd.exe /c /t:C:\INST\Certs\
updroots.exe C:\INST\Certs\roots.sst

cls
echo Скрипт завершил работу.
pause