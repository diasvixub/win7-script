chcp 65001
@echo off
title Подготовка к установке
cls

echo Подготовка к установке
echo ═════════════════════════════════════════
rmdir /s /q C:\INST
mkdir C:\INST
xcopy * C:\INST /Y /S 
echo ═════════════════════════════════════════
echo Подготовка выполнена успешно
start %windir%\explorer.exe "C:\INST\"