﻿chcp 65001
@echo off
title Скрипт для настройки Windows
cls

echo Будут установлены следующие компоненты:
echo ═════════════════════════════════════════
echo • Обновление корневых сертификатов
echo • Установка необходимых библиотек
echo • Установка программ
echo • Оптимизация Windows
echo ═════════════════════════════════════════
timeout 5
cls

title Обновление корневых сертификатов
cd C:\INST\Certs

rootsupd.exe /c /t:C:\INST\Certs\
updroots.exe C:\INST\Certs\roots.sst
cls

echo Обновление сертификатов выполнено успешно
timeout 3
cls

title Установка библиотек
cd C:\INST\Lib

echo Установка DirectX (1 из 3)...
dxwebsetup.exe 
cls

echo Установка .NET Framework 3.5 (2 из 3)...
dotNetFx35setup.exe
cls

echo Установка Visual C++ Redistributable (3 из 3)...
VisualCppRedist_AIO_x86_x64.exe
cls

echo Установка библиотек выполнена успешно
timeout 3
cls

title Установка программ
cd C:\INST\Program

echo Установка 7-Zip (1 из 11)...
7z2201-x64.exe /S
cls

echo Установка Google Chrome (2 из 11)...
ChromeStandaloneSetup64.exe
Taskkill /IM chrome.exe /F
cls

echo Установка Firefox (3 из 11)...
Firefox-Installer.exe
Taskkill /IM firefox.exe /F
cls

echo Установка Microsoft Office 2010 (4 из 11)...
Office-2010-Word-Excel-Powerpoint-x64.exe
cls

echo Установка Notepad++ (5 из 11)...
npp.8.4.7.Installer.x64.exe /S
cls

echo Установка GDevelop (6 из 11)...
GDevelop-5-Setup-5.1.149.exe
cls

echo Установка GIMP (7 из 11)...
gimp-2.10.32-setup-1.exe
cls

echo Установка PyCharm Community (8 из 11)...
pycharm-community-2019.3.5.exe
cls

echo Установка Visual Studio Code (9 из 11)...
VSCodeUserSetup-x64-1.70.2.exe
cls

echo Установка VLC (10 из 11)...
vlc-3.0.17.4-win64.exe /S
cls

echo Установка Python 3.7 (11 из 11)...
python-3.7.0-amd64.exe
cls

echo Установка программ выполнена успешно
timeout 3
cls

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

echo Очистка временных файлов...
timeout 2
cls

del C:\Windows\SoftwareDistribution\Download\*.* /f /s /q
del C:\Windows\Prefetch\*.* /f /s /q
del %temp%\*.* /f /s /q

echo Перезагрузка компьютера через 5 сек...
shutdown /r /t 5
rmdir /s /q C:\INST