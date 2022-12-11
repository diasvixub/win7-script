from os import system, chdir, mkdir, listdir
from time import sleep
from subprocess import run, DEVNULL
import sys
from progress.bar import IncrementalBar

# Переменные
path = 'C:\\INST'
p_name = '                                   WIN7-SCRIPT'
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
    try:
        chdir(path)
    except FileNotFoundError:
        mkdir(path)
        product()
        copy()
        system(f'start {path}\\setup')
        sys.exit()
    else:
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
    run(['xcopy', '*', path, '/Y', '/S'], shell=False, stdout=DEVNULL)


def updates(a):
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
            if i == 0:
                run([updates_list[i]], shell=False, stdout=DEVNULL)
                bar.next()
            else:
                run(['wusa.exe', updates_list[i], '/quiet', '/norestart'], shell=False, stdout=DEVNULL)
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
    product()
    yesno = input('Libraries will be installed. Continue? (y/n) ')
    if yesno == 'y':
        product()
        bar = IncrementalBar('Installing libraries', max=len(a))
        for i in range(0, len(a)):
            run([a[i]], shell=False, stdout=DEVNULL)
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


main()
