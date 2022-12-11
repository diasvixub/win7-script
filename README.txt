!RU

# Программа по полуавтоматической настройке и установки обновлений, библиотек и программ для Windows 7

## Установка

Откройте файл "setup.exe" от имени Администратора.

Возможно для запуска программы понадобится "api-ms-win-core-path-l1-1-0-32.dll".
Её можно установить из папки "Api" в папке с программой, запустив "install.bat" имени Администратора.
После установки вновь откройте файл "setup.exe" от имени Администратора.

Будет начато копирование файлов в директорию "C:\INST", откуда будет произоводиться дальнейшая установка.
После завершения копирования, программа перезапустится с другим интерфейсом.

Вам будет предложено несколько вариантов операций:

1 Установка обновлений
2 Обновление корневых сертификатов
3 Установка библиотек
4 Установка программ
5 Оптимизация Windows
6 Очистка временных файлов
7 Получение справки
8 Перезагрузка компьютера
0 Выход из программы

## 1 Установка обновлений

Переместите предварительно скачанные обновления в папку "Updates".
После запуска программы они автоматически определятся и вы сможете их установить.

## 2 Обновление корневых сертификатов

Будет произведена установка новых корневых сертификатов для доступа к сайтам через браузеры

## 3 Установка библиотек

* Возможно для установки некоторых библиотек потребуется перезагрузка Windows

Переместите предварительно скачанные библиотеки в папку "Libs".
После запуска программы они автоматически определятся и вы сможете их установить.

## 4 Установка программ

Переместите предварительно скачанные программы в папку "Programs".
После запуска программы они автоматически определятся и вы сможете их установить.

## 5 Оптимизация Windows

Будут отключены следующие компоненты Windows:

- Платформа гаджетов Windows
- Игры

Будут отключены следующие службы:

- Windows Search
- Архивация Windows
- Служба ввода планшетного ПК
- Служба поддержки Bluetooth
- Служба шифрования дисков BitLocker
- Центр обновления Windows
- Теневое копирование тома
- Смарт-карта
- Защитник Windows

Будет настроен файл подкачки на 4 ГБ.

Будет включен показ расширения файлов.

## 6 Очистка временных файлов

Список директорий, которые будут очищены:

- C:\Windows\SoftwareDistribution\Download\
- C:\Windows\Prefetch\
- %temp%

## 7 Получение справки

Откроется данный документ.

## Удаление программы

После того, как вы установите всё что нужно, можете запустить "uninstall.bat".
Скрипт удалит все файлы и директорию программы.

!EN

# Program for semi-automatic configuration and installation of updates, libraries and programs for Windows 7

## Installation

Open the "setup.exe" on behalf of the Administrator.

Perhaps to run the program you will need "api-ms-win-core-path-l1-1-0-32.dll ".
It can be installed from the "Api" folder in the program folder by running "install.bat" of the Administrator's name.
After installation, open the "setup" file again.exe" on behalf of the Administrator.

Copying of files to the directory will be started "C:\INST ", from where the further installation will take place.
After the copy is completed, the program will restart with a different interface.

You will be offered several options for operations:

1 Installing updates
2 Updating root certificates
3 Installing Libraries
4 Installing programs
5 Windows Optimization
6 Clearing temporary files
7 Getting help
8 Restart the computer
0 Exit the program

##1 Installing Updates

Move the pre-downloaded updates to the "Updates" folder.
After launching the program, they will be automatically detected and you will be able to install them.

##2 Updating Root Certificates

New root certificates will be installed to access sites through browsers

##3 Installing Libraries

* You may need to restart Windows to install some libraries

Move the pre-downloaded libraries to the "Libs" folder.
After launching the program, they will be automatically detected and you will be able to install them.

##4 Installing Programs

Move the pre-downloaded programs to the "Programs" folder.
After launching the program, they will be automatically detected and you will be able to install them.

##5 Windows Optimization

The following Windows components will be disabled:

- Windows Gadget Platform
- Games

The following services will be disabled:

- Windows Search
- Windows Archiving
- Tablet PC input service
- Bluetooth Support Service
- BitLocker Disk Encryption Service
- Windows Update
- Shadow copy of the volume
- Smart card
- Windows Defender

A 4 GB swap file will be configured.

The display of file extensions will be enabled.

##6 Clearing temporary files

List of directories to be cleared:

- C:\Windows\SoftwareDistribution\Download\
- C:\Windows\Prefetch\
- %temp%

##7 Getting Help

This document opens.

## Removing the program

After you install everything you need, you can run "uninstall.bat".
The script will delete all files and the program directory.