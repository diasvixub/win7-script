chcp 65001
@echo off
title Скрипт для настройки Windows
cls

echo Будут установлены следующие компоненты:
echo ═════════════════════════════════════════
echo • Обновление Windows
echo • Обновление корневых сертификатов
echo • Установка необходимых библиотек
echo • Установка программ
echo • Оптимизация Windows
echo ═════════════════════════════════════════
timeout 5
cls

title Обновление Windows
cd C:\INST\Updates

echo Включение Центра обновления Windows...
sc start wuauserv
cls

echo Обновление Агента центра обновления Windows (1 из 1)...
windowsupdateagent-7.6-x64.exe
cls

echo Установка обновления  (1 из 61)...
wusa.exe Windows6.1-kb2533552-x64.msu /quiet /norestart
cls

echo Установка KB2545698 (2 из 61)...
wusa.exe Windows6.1-kb2545698-x64.msu /quiet /norestart
cls

echo Установка KB2547666 (3 из 61)...
wusa.exe Windows6.1-kb2547666-x64.msu /quiet /norestart
cls

echo Установка KB2574819 (4 из 61)...
wusa.exe Windows6.1-kb2574819-v2-x64.msu /quiet /norestart
cls

echo Установка KB2603229 (5 из 61)...
wusa.exe Windows6.1-kb2603229-x64.msu /quiet /norestart
cls

echo Установка KB2667402 (6 из 61)...
wusa.exe Windows6.1-kb2667402-v2-x64.msu /quiet /norestart
cls

echo Установка KB2670838 (7 из 61)...
wusa.exe Windows6.1-kb2670838-x64.msu /quiet /norestart
cls

echo Установка KB2676561 (8 из 61)...
wusa.exe Windows6.1-kb2676561-x64.msu /quiet /norestart
cls

echo Установка KB2685811 (9 из 61)...
wusa.exe Windows6.1-kb2685811-x64.msu /quiet /norestart
cls

echo Установка KB2685813 (10 из 61)...
wusa.exe Windows6.1-kb2685813-x64.msu /quiet /norestart
cls

echo Установка KB2698365 (11 из 61)...
wusa.exe Windows6.1-kb2698365-x64.msu /quiet /norestart
cls

echo Установка KB2706045 (12 из 61)...
wusa.exe Windows6.1-kb2706045-x64.msu /quiet /norestart
cls

echo Установка KB2729094 (13 из 61)...
wusa.exe Windows6.1-kb2729094-v2-x64.msu /quiet /norestart
cls

echo Установка KB2732061 (14 из 61)...
wusa.exe Windows6.1-kb2732061-v5-x64.msu /quiet /norestart
cls

echo Установка KB2750841 (15 из 61)...
wusa.exe Windows6.1-kb2750841-x64.msu /quiet /norestart
cls

echo Установка KB2761217 (16 из 61)...
wusa.exe Windows6.1-kb2761217-x64.msu /quiet /norestart
cls

echo Установка KB2773072 (17 из 61)...
wusa.exe Windows6.1-kb2773072-x64.msu /quiet /norestart
cls

echo Установка KB2813347 (18 из 61)...
wusa.exe Windows6.1-kb2813347-x64.msu /quiet /norestart
cls

echo Установка KB2830477 (19 из 61)...
wusa.exe Windows6.1-kb2830477-x64.msu /quiet /norestart
cls

echo Установка KB2834140 (20 из 61)...
wusa.exe Windows6.1-kb2834140-v2-x64.msu /quiet /norestart
cls

echo Установка KB2861330 (21 из 61)...
wusa.exe Windows6.1-kb2861330-v2-x64.msu /quiet /norestart
cls

echo Установка KB2894844 (22 из 61)...
wusa.exe Windows6.1-kb2894844-x64.msu /quiet /norestart
cls

echo Установка KB2900986 (23 из 61)...
wusa.exe Windows6.1-kb2900986-x64.msu /quiet /norestart
cls

echo Установка KB2919469 (24 из 61)...
wusa.exe Windows6.1-kb2919469-x64.msu /quiet /norestart
cls

echo Установка KB2952664 (25 из 61)...
wusa.exe Windows6.1-kb2952664-v25-x64.msu /quiet /norestart
cls

echo Установка KB2970228 (26 из 61)...
wusa.exe Windows6.1-kb2970228-x64.msu /quiet /norestart
cls

echo Установка KB2984972 (27 из 61)...
wusa.exe Windows6.1-kb2984972-x64.msu /quiet /norestart
cls

echo Установка KB3004375 (28 из 61)...
wusa.exe Windows6.1-kb3004375-v3-x64.msu /quiet /norestart
cls

echo Установка KB3006137 (29 из 61)...
wusa.exe Windows6.1-kb3006137-x64.msu /quiet /norestart
cls

echo Установка KB3020369 (30 из 61)...
wusa.exe Windows6.1-kb3020369-x64.msu /quiet /norestart
cls

echo Установка KB3021917 (31 из 61)...
wusa.exe Windows6.1-kb3021917-x64.msu /quiet /norestart
cls

echo Установка KB3046169 (32 из 61)...
wusa.exe Windows6.1-kb3046169-x64.msu /quiet /norestart
cls

echo Установка KB3061317 (33 из 61)...
wusa.exe Windows6.1-kb3061317-x64.msu /quiet /norestart
cls

echo Установка KB3068708 (34 из 61)...
wusa.exe Windows6.1-kb3068708-x64.msu /quiet /norestart
cls

echo Установка KB3080149 (35 из 61)...
wusa.exe Windows6.1-kb3080149-x64.msu /quiet /norestart
cls

echo Установка KB3102429 (36 из 61)...
wusa.exe Windows6.1-kb3102429-v2-x64.msu /quiet /norestart
cls

echo Установка KB3118401 (37 из 61)...
wusa.exe Windows6.1-kb3118401-x64.msu /quiet /norestart
cls

echo Установка KB3123479 (38 из 61)...
wusa.exe Windows6.1-kb3123479-x64.msu /quiet /norestart
cls

echo Установка KB3125574 (39 из 61)...
wusa.exe Windows6.1-kb3125574-v4-x64.msu /quiet /norestart
cls

echo Установка KB3138612 (40 из 61)...
wusa.exe Windows6.1-kb3138612-x64.msu /quiet /norestart
cls

echo Установка KB3140245 (41 из 61)...
wusa.exe Windows6.1-kb3140245-x64.msu /quiet /norestart
cls

echo Установка KB3150513 (42 из 61)...
wusa.exe Windows6.1-kb3150513-x64.msu /quiet /norestart
cls

echo Установка KB3156016 (43 из 61)...
wusa.exe Windows6.1-kb3156016-x64.msu /quiet /norestart
cls

echo Установка KB3161398 (44 из 61)...
wusa.exe Windows6.1-kb3161398-x64.msu /quiet /norestart
cls

echo Установка KB3161102 (45 из 61)...
wusa.exe Windows6.1-kb3161102-x64.msu /quiet /norestart
cls

echo Установка KB3161949 (46 из 61)...
wusa.exe Windows6.1-kb3161949-x64.msu /quiet /norestart
cls

echo Установка KB3172605 (47 из 61)...
wusa.exe Windows6.1-kb3172605-x64.msu /quiet /norestart
cls

echo Установка KB3179573 (48 из 61)...
wusa.exe Windows6.1-kb3179573-x64.msu /quiet /norestart
cls

echo Установка KB3184143 (49 из 61)...
wusa.exe Windows6.1-kb3184143-x64.msu /quiet /norestart
cls

echo Установка KB4019990 (50 из 61)...
wusa.exe Windows6.1-KB4019990-x64.msu /quiet /norestart
cls

echo Установка KB4040980 (51 из 61)...
wusa.exe Windows6.1-kb4040980-x64.msu /quiet /norestart
cls

echo Установка KB4088878 (52 из 61)...
wusa.exe Windows6.1-kb4088878-x64.msu /quiet /norestart
cls

echo Установка KB4099950 (53 из 61)...
wusa.exe Windows6.1-kb4099950-x64.msu /quiet /norestart
cls

echo Установка KB4474419 (54 из 61)...
wusa.exe Windows6.1-kb4474419-v3-x64.msu /quiet /norestart
cls

echo Установка KB4490618 (55 из 61)...
wusa.exe Windows6.1-kb4490618-x64.msu /quiet /norestart
cls

echo Установка KB4524752 (56 из 61)...
wusa.exe Windows6.1-kb4524752-x64.msu /quiet /norestart
cls

echo Установка KB5010798 (57 из 61)...
wusa.exe Windows6.1-kb5010798-x64.msu /quiet /norestart
cls

echo Установка KB5013637 (58 из 61)...
wusa.exe Windows6.1-kb5013637-x64.msu /quiet /norestart
cls

echo Установка KB5017397 (59 из 61)...
wusa.exe Windows6.1-kb5017397-x64.msu /quiet /norestart
cls

echo Установка KB5018454 (60 из 61)...
wusa.exe Windows6.1-kb5018454-x64.msu /quiet /norestart
cls

echo Установка KB5020000 (61 из 61)...
wusa.exe Windows6.1-kb5020000-x64.msu /quiet /norestart
cls

echo Установка обновлений выполнена успешно
timeout 3
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