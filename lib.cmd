chcp 65001
@echo off
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
echo Скрипт завершил работу.
pause