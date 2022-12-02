chcp 65001
@echo off
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
echo Скрипт завершил работу.
pause