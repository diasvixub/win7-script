chcp 65001
@echo off
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

cls
echo Скрипт завершил работу.
pause