chcp 65001
@echo off
title Оптимизация Windows
echo Отключение ненужных компонентов Windows...
timeout 2
cls

Dism /online /Disable-Feature /FeatureName:WindowsGadgetPlatform /norestart
Dism /online /Disable-Feature /FeatureName:InboxGames /norestart
Dism /online /Disable-Feature /FeatureName:More Games /norestart
Dism /online /Disable-Feature /FeatureName:Solitaire /norestart
Dism /online /Disable-Feature /FeatureName:SpiderSolitaire /norestart
Dism /online /Disable-Feature /FeatureName:Hearts /norestart
Dism /online /Disable-Feature /FeatureName:FreeCell /norestart
Dism /online /Disable-Feature /FeatureName:Minesweeper /norestart
Dism /online /Disable-Feature /FeatureName:PurplePlace /norestart

echo Отключение неиспользуемых служб...
timeout 2
cls 

sc config WSearch start= disabled
sc config SDRSVC start= disabled
sc config TabletInputService start= disabled
sc config bthserv start= disabled
sc config BDESVC start= disabled
sc config wuauserv start= disabled
sc config VSS start= disabled
sc config SCardSvr start= disabled
sc config WinDefend start= disabled

echo Настройка файла подкачки...
timeout 2
cls

wmic computersystem set AutomaticManagedPagefile=False
wmic pagefileset where name="C:\\pagefile.sys" set InitialSize=4096,MaximumSize=4096

echo Включение показа расширения файлов
timeout 2
cls

reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v HideFileExt /t REG_DWORD /d 00000000 /f

cls
echo Скрипт завершил работу.
pause