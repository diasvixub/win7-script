from os import system, chdir, mkdir, listdir
from time import sleep
from subprocess import run, DEVNULL
import sys
from progress.bar import IncrementalBar

path = 'C:\\INST'
p_name = '                                   WIN7-SCRIPT'
hr = '═══════════════════════════════════════════════════════════════════════════════'
updates_list = listdir('Updates')
libs_list = listdir('Libs')
programs_list = listdir('Programs')
certs_list = ['Certs\\rootsupd.exe', 'Certs\\updroots.exe', 'Certs\\roots.sst', 'Certs\\']
dism_list = ['/FeatureName:WindowsGadgetPlatform ', '/FeatureName:InboxGames', '/FeatureName:More Games',
             '/FeatureName:Solitaire', '/FeatureName:SpiderSolitaire', '/FeatureName:Hearts', '/FeatureName:FreeCell',
             '/FeatureName:Minesweeper', '/FeatureName:PurplePlace']
sc_list = ['wuauserv', 'WSearch', 'SDRSVC', 'TabletInputService', 'bthserv', 'BDESVC', 'VSS', 'SCardSvr', 'WinDefend']


def start():
    try:  # Attempt to go to the directory
        chdir(path)
    except FileNotFoundError:  # In the absence of a directory
        mkdir(path)  # Create a directory
        product()
        copy()  # Copy files from the current directory
        system(f'start {path}\\setup')  # Run the program from the created directory
        sys.exit()
    else:
        main()


def main():
    system('chcp 866')
    product()
    print('1 Installing Windows Updates')
    print('2 Updating Root Certificates')
    print('3 Installing Libraries')
    print('4 Installing Programs')
    print('5 Optimizing Windows')
    print('6 Cleaning Temporary Files')
    print('7 Get Help')
    print('8 Restart Windows')
    print('0 Exit the program')
    print(hr)
    operation = input('Operation number: ')
    system('cls')
    if operation == '1':
        updates(updates_list)
    elif operation == '2':
        certs(certs_list)
    elif operation == '3':
        libs(libs_list)
    elif operation == '4':
        programs(programs_list)
    elif operation == '5':
        boost(dism_list, sc_list)
    elif operation == '6':
        clean()
    elif operation == '7':
        system('notepad readme.txt')
        main()
    elif operation == '8':
        run(['shutdown', '/r', '/t', '5'], shell=False, stdout=DEVNULL)
    elif operation == '0':
        sys.exit()
    else:
        product()
        print('Invalid operation number entered')
        sleep(1)
        main()


def product():
    system('cls')
    print(p_name)
    print(hr)


def copy():
    print('Copying files...')
    run(['xcopy', '*', path, '/E', '/Y'], shell=False, stdout=DEVNULL)


def updates(a):
    if len(a) > 0:  # If there are files in the directory
        product()
        yesno = input(f'{len(a)} updates will be installed. Continue? (y/n) ')
        if yesno == 'y':
            product()
            print('Enabling Windows Update...')
            sleep(1)
            print(hr)
            run(['sc', 'config', sc_list[0], 'start=', 'demand'], shell=False, stdout=DEVNULL)
            run(['net', 'start', sc_list[0]], shell=False, stdout=DEVNULL)
            product()
            bar = IncrementalBar('Installing updates', max=len(updates_list))
            for i in range(0, len(a)):
                run(f'wusa.exe Updates\\{updates_list[i]} /quiet /norestart', shell=True, stdout=DEVNULL)
                bar.next()
            bar.finish()
            sleep(1)
            product()
            print('Installation was successful')
            sleep(1)
            main()
        elif yesno == 'n':
            main()
        else:
            product()
            print('Confirm (y) or reject (n) the installation')
            sleep(2)
            updates(updates_list)
    else:  # If there are no files in the directory
        product()
        print('Installers not found')
        sleep(1)
        main()


def certs(a):
    product()
    yesno = input('Root certificates will be updated. Continue? (y/n) ')
    if yesno == 'y':
        product()
        print('Updating root certificates...')
        print(hr)
        print('Click "No" in the windows that appear on the screen')
        run(f'{a[0]} /c /t:C:\\INST\\{a[3]}', shell=True, stdout=DEVNULL)
        sleep(1)
        run([a[1], a[2]], shell=False, stdout=DEVNULL)
        product()
        print('Certificate update completed successfully')
        sleep(1)
        main()
    elif yesno == 'n':
        main()
    else:
        product()
        print('Confirm (y) or reject (n) the update')
        sleep(2)
        certs(certs_list)


def libs(a):
    if len(a) > 0:
        product()
        yesno = input('Libraries will be installed. Continue? (y/n) ')
        if yesno == 'y':
            product()
            bar = IncrementalBar('Installing libraries', max=len(a))
            for i in range(0, len(a)):
                run(f'Libs\\{a[i]}', shell=True, stdout=DEVNULL)
                bar.next()
            bar.finish()
            sleep(1)
            product()
            print('Installation was successful')
            sleep(1)
            main()
        elif yesno == 'n':
            main()
        else:
            product()
            print('Confirm (y) or reject (n) the installation')
            sleep(2)
            libs(libs_list)
    else:
        product()
        print('Installers not found')
        sleep(1)
        main()


def programs(a):
    if len(a) > 0:
        product()
        yesno = input('Programs will be installed. Continue? (y/n) ')
        if yesno == 'y':
            product()
            bar = IncrementalBar('Installing programs', max=len(a))
            for i in range(0, len(a)):
                run(f'Programs\\{a[i]}', shell=True, stdout=DEVNULL)
                bar.next()
            bar.finish()
            sleep(1)
            product()
            print('Installation was successful')
            sleep(1)
            main()
        elif yesno == 'n':
            main()
        else:
            product()
            print('Confirm (y) or reject (n) the installation')
            sleep(2)
            programs(programs_list)
    else:
        product()
        print('Installers not found')
        sleep(1)
        main()


def boost(a, b):
    product()
    yesno = input('Windows will be optimized. Continue? (y/n) ')
    if yesno == 'y':
        product()
        bar = IncrementalBar('Optimization', max=len(a)+len(b)+3)
        for i in range(0, len(a)):
            run(['Dism', '/online', '/Disable-Feature', a[i], '/norestart'], shell=False, stdout=DEVNULL)
            bar.next()
        run(['wmic', 'computersystem', 'set', 'AutomaticManagedPagefile=False'], shell=False, stdout=DEVNULL)
        bar.next()
        run(['wmic', 'pagefileset', 'where', 'name="C:\\pagefile.sys"' 'set', 'InitialSize=4096,MaximumSize=4096'],
            shell=False, stdout=DEVNULL)
        bar.next()
        run(['reg', 'add', 'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced', '/v',
             'HideFileExt', '/t REG_DWORD', '/d', '00000000', '/f'], shell=False, stdout=DEVNULL)
        bar.next()
        for i in range(0, len(b)):
            run(['sc', 'config', b[i], 'start=', 'disabled'], shell=False, stdout=DEVNULL)
            run(['net', 'stop', b[i]], shell=False, stdout=DEVNULL)
            bar.next()
        bar.finish()
        sleep(1)
        product()
        print('Optimization was successful')
        sleep(1)
        main()
    elif yesno == 'n':
        main()
    else:
        product()
        print('Confirm (y) or reject (n) the optimization')
        sleep(2)
        boost(dism_list, sc_list)


def clean():
    product()
    yesno = input('Temporary files will be deleted. Continue? (y/n) ')
    if yesno == 'y':
        product()
        bar = IncrementalBar('Cleaning', max=6)
        run('del C:\\Windows\\SoftwareDistribution\\Download\\*.* /s /q >nul 2>&1', shell=True, stdout=DEVNULL)
        bar.next()
        sleep(1)
        run('for /d %i in (C:\\Windows\\SoftwareDistribution\\Download\\*.*) do @rmdir /s /q "%i" >nul 2>&1',
            shell=True, stdout=DEVNULL)
        bar.next()
        sleep(1)
        run('del C:\\Windows\\Prefetch\\*.* /s /q >nul 2>&1', shell=True, stdout=DEVNULL)
        bar.next()
        sleep(1)
        run('for /d %i in (C:\\Windows\\Prefetch\\*.*) do @rmdir /s /q "%i" >nul 2>&1', shell=True, stdout=DEVNULL)
        bar.next()
        sleep(1)
        run('del %temp%\\*.* /s /q >nul 2>&1', shell=True, stdout=DEVNULL)
        bar.next()
        sleep(1)
        run('for /d %i in (%temp%\\*.*) do @rmdir /s /q "%i" >nul 2>&1', shell=True, stdout=DEVNULL)
        bar.next()
        sleep(1)
        bar.finish()
        sleep(1)
        product()
        print('Cleaning was successful')
        sleep(1)
        main()
    elif yesno == 'n':
        main()
    else:
        product()
        print('Confirm (y) or reject (n) the cleaning')
        sleep(2)
        clean()


start()
