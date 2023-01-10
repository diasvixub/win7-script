from os import system, listdir
from time import sleep
from subprocess import run, DEVNULL
import sys
from progress.bar import IncrementalBar

p_name = 'WIN7-SCRIPT'.center(79)
hr = '═══════════════════════════════════════════════════════════════════════════════'
updates_list = ['Updates\\windowsupdateagent-7.6-x64.exe', 'Updates\\Windows6.1-KB3102810-x64.msu',
                'Updates\\Windows6.1-kb2533552-x64.msu', 'Updates\\Windows6.1-kb2545698-x64.msu',
                'Updates\\Windows6.1-kb2547666-x64.msu', 'Updates\\Windows6.1-kb2574819-v2-x64.msu',
                'Updates\\Windows6.1-kb2603229-x64.msu', 'Updates\\Windows6.1-kb2667402-v2-x64.msu',
                'Updates\\Windows6.1-kb2670838-x64.msu', 'Updates\\Windows6.1-kb2676562-x64.msu',
                'Updates\\Windows6.1-kb2685811-x64.msu', 'Updates\\Windows6.1-kb2685813-x64.msu',
                'Updates\\Windows6.1-kb2698365-x64.msu', 'Updates\\Windows6.1-kb2706045-x64.msu',
                'Updates\\Windows6.1-kb2729094-v2-x64.msu', 'Updates\\Windows6.1-kb2732059-v5-x64.msu',
                'Updates\\Windows6.1-kb2750841-x64.msu', 'Updates\\Windows6.1-kb2761217-x64.msu',
                'Updates\\Windows6.1-kb2773072-x64.msu', 'Updates\\Windows6.1-kb2813347-x64.msu',
                'Updates\\Windows6.1-kb2830477-x64.msu', 'Updates\\Windows6.1-kb2834140-v2-x64.msu',
                'Updates\\Windows6.1-kb2862330-v2-x64.msu', 'Updates\\Windows6.1-kb2894844-x64.msu',
                'Updates\\Windows6.1-kb2900986-x64.msu', 'Updates\\Windows6.1-kb2919469-x64.msu',
                'Updates\\Windows6.1-kb2952664-v25-x64.msu', 'Updates\\Windows6.1-kb2970228-x64.msu',
                'Updates\\Windows6.1-kb2984972-x64.msu', 'Updates\\Windows6.1-kb3004375-v3-x64.msu',
                'Updates\\Windows6.1-kb3006137-x64.msu', 'Updates\\Windows6.1-kb3020369-x64.msu',
                'Updates\\Windows6.1-kb3021917-x64.msu', 'Updates\\Windows6.1-kb3046269-x64.msu',
                'Updates\\Windows6.1-kb3059317-x64.msu', 'Updates\\Windows6.1-kb3068708-x64.msu',
                'Updates\\Windows6.1-kb3080149-x64.msu', 'Updates\\Windows6.1-kb3102429-v2-x64.msu',
                'Updates\\Windows6.1-kb3118401-x64.msu', 'Updates\\Windows6.1-kb3123479-x64.msu',
                'Updates\\Windows6.1-kb3125574-v4-x64.msu', 'Updates\\Windows6.1-kb3138612-x64.msu',
                'Updates\\Windows6.1-kb3140245-x64.msu', 'Updates\\Windows6.1-kb3150513-x64.msu',
                'Updates\\Windows6.1-kb3156016-x64.msu', 'Updates\\Windows6.1-kb3159398-x64.msu',
                'Updates\\Windows6.1-kb3161102-x64.msu', 'Updates\\Windows6.1-kb3161949-x64.msu',
                'Updates\\Windows6.1-kb3172605-x64.msu', 'Updates\\Windows6.1-kb3179573-x64.msu',
                'Updates\\Windows6.1-kb3184143-x64.msu', 'Updates\\Windows6.1-KB4019990-x64.msu',
                'Updates\\Windows6.1-kb4040980-x64.msu', 'Updates\\Windows6.1-kb4088878-x64.msu',
                'Updates\\Windows6.1-kb4099950-x64.msu', 'Updates\\Windows6.1-kb4474419-v3-x64.msu',
                'Updates\\Windows6.1-kb4490628-x64.msu', 'Updates\\Windows6.1-kb4524752-x64.msu',
                'Updates\\Windows6.1-kb5010798-x64.msu', 'Updates\\Windows6.1-kb5013637-x64.msu',
                'Updates\\Windows6.1-kb5017397-x64.msu', 'Updates\\Windows6.1-kb5018454-x64.msu',
                'Updates\\Windows6.1-kb5020000-x64.msu']
certs_list = ['Certs\\rootsupd.exe', 'Certs\\updroots.exe', 'Certs\\roots.sst', 'Certs\\']
libs_list = ['Libs\\dxwebsetup.exe', 'Libs\\ndp48-x86-x64-allos-enu.exe',
             'Libs\\VisualCppRedist_AIO_x86_x64.exe']
programs_list = listdir('Programs')
dism_list = ['/FeatureName:WindowsGadgetPlatform ', '/FeatureName:InboxGames', '/FeatureName:More Games',
             '/FeatureName:Solitaire', '/FeatureName:SpiderSolitaire', '/FeatureName:Hearts', '/FeatureName:FreeCell',
             '/FeatureName:Minesweeper', '/FeatureName:PurplePlace']
sc_list = ['wuauserv', 'WSearch', 'SDRSVC', 'TabletInputService', 'bthserv', 'BDESVC', 'VSS', 'SCardSvr', 'WinDefend']


def main():
    system('title MENU')
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


def updates(a):
    system('title UPDATES')
    product()
    yesno = input(f'{len(a)} updates will be installed. Continue? (y/n) ')
    if yesno == 'y':
        system('title ENABLING WINDOWS UPDATE')
        product()
        print('Enabling Windows Update...')
        sleep(1)
        print(hr)
        run(['sc', 'config', sc_list[0], 'start=', 'demand'], shell=False, stdout=DEVNULL)
        run(['net', 'start', sc_list[0]], shell=False, stdout=DEVNULL)
        product()
        bar = IncrementalBar('Installing updates', max=len(a))
        for i in range(0, len(a)):
            bar.next()
            if i == 0:
                system('title INSTALLING WINDOWS AGENT...')
                try:
                    run([a[i]], shell=False, stdout=DEVNULL)
                except FileNotFoundError:
                    pass
            else:
                system(f'title INSTALLING {a[i][19:28]}...')
                try:
                    run(['wusa.exe', a[i], '/quiet', '/norestart'], shell=False, stdout=DEVNULL)
                except FileNotFoundError:
                    pass
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


def certs(a):
    system('title CERTS')
    product()
    yesno = input('Root certificates will be updated. Continue? (y/n) ')
    if yesno == 'y':
        system('title UPDATING ROOT CERTIFICATES')
        product()
        print('Updating root certificates...')
        print(hr)
        print('Click "No" in the windows that appear on the screen')
        try:
            run(f'{a[0]} /c /t:{a[3]}', shell=True, stdout=DEVNULL)
        except FileNotFoundError:
            pass
        sleep(1)
        try:
            run([a[1], a[2]], shell=False, stdout=DEVNULL)
        except FileNotFoundError:
            pass
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
    system('title LIBS')
    product()
    yesno = input('Libraries will be installed. Continue? (y/n) ')
    if yesno == 'y':
        system('title INSTALLING LIBRARIES...')
        product()
        bar = IncrementalBar('Installing libraries', max=len(a))
        for i in range(0, len(a)):
            bar.next()
            try:
                run([a[i]], shell=False, stdout=DEVNULL)
            except FileNotFoundError:
                pass
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


def programs(a):
    system(f'title PROGRAMS')
    if len(a) > 0:
        product()
        yesno = input('Programs will be installed. Continue? (y/n) ')
        if yesno == 'y':
            system('title INSTALLING PROGRAMS...')
            product()
            bar = IncrementalBar('Installing programs', max=len(a))
            for i in range(0, len(a)):
                bar.next()
                try:
                    run(f'Programs\\{a[i]}', shell=True, stdout=DEVNULL)
                except FileNotFoundError:
                    pass
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
    system('title OPTIMIZING')
    product()
    yesno = input('Windows will be optimized. Continue? (y/n) ')
    if yesno == 'y':
        system('title OPTIMIZATION...')
        product()
        bar = IncrementalBar('Optimization', max=len(a)+len(b)+3)
        for i in range(0, len(a)):
            bar.next()
            run(f'Dism /online /Disable-Feature {a[i]} /norestart', shell=False, stdout=DEVNULL)
        run('wmic computersystem set AutomaticManagedPagefile=False', shell=False, stdout=DEVNULL)
        bar.next()
        run('wmic pagefileset where name="C:\\\\pagefile.sys" set InitialSize=4096,MaximumSize=4096',
            shell=False, stdout=DEVNULL)
        bar.next()
        run('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced /v HideFileExt /t REG_DWORD /d 00000000 /f',
            shell=False, stdout=DEVNULL)
        bar.next()
        for i in range(0, len(b)):
            run(f'sc config {b[i]} start= disabled', shell=False, stdout=DEVNULL)
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
    system('title CLEANING TEMPORARY FILES')
    product()
    yesno = input('Temporary files will be deleted. Continue? (y/n) ')
    if yesno == 'y':
        system('title CLEANING...')
        product()
        bar = IncrementalBar('Cleaning', max=6)
        bar.next()
        run('del C:\\Windows\\SoftwareDistribution\\Download\\*.* /s /q >nul 2>&1', shell=True, stdout=DEVNULL)
        bar.next()
        run('for /d %i in (C:\\Windows\\SoftwareDistribution\\Download\\*.*) do @rmdir /s /q "%i" >nul 2>&1',
            shell=True, stdout=DEVNULL)
        bar.next()
        run('del C:\\Windows\\Prefetch\\*.* /s /q >nul 2>&1', shell=True, stdout=DEVNULL)
        bar.next()
        run('for /d %i in (C:\\Windows\\Prefetch\\*.*) do @rmdir /s /q "%i" >nul 2>&1', shell=True, stdout=DEVNULL)
        bar.next()
        run('del %temp%\\*.* /s /q >nul 2>&1', shell=True, stdout=DEVNULL)
        bar.next()
        run('for /d %i in (%temp%\\*.*) do @rmdir /s /q "%i" >nul 2>&1', shell=True, stdout=DEVNULL)
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


main()
