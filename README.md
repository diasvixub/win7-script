# Win7 Script - release v1.0.0

## Program appearance

![image](https://user-images.githubusercontent.com/113109541/206895443-611782be-89c3-4d25-866f-ab8b0a706277.png)

**For the script to work correctly, you need to run it as an administrator**

## The script can

1. Installing updates
2. Updating root certificates
3. Installing libraries
4. Installing programs (_not included_)
5. Windows optimization
6. Clearing temporary files

## What updates are included (current for November 2022)

- WindowsUpdateAgent
- kb3102810
- kb2533552
- kb2545698
- kb2547666
- kb2574819-v2
- kb2603229
- kb2667402-v2
- kb2670838
- kb2676562
- kb2685811
- kb2685813
- kb2698365
- kb2706045
- kb2729094-v2
- kb2732059-v5
- kb2750841
- kb2761217
- kb2773072
- kb2813347
- kb2830477
- kb2834140-v2
- kb2862330-v2
- kb2894844
- kb2900986
- kb2919469
- kb2952664-v25
- kb2970228
- kb2984972
- kb3004375-v3
- kb3006137
- kb3020369
- kb3021917
- kb3046269
- kb3059317
- kb3068708
- kb3080149
- kb3102429-v2
- kb3118401
- kb3123479
- kb3125574-v4
- kb3138612
- kb3140245
- kb3150513
- kb3156016
- kb3159398
- kb3161102
- kb3161949
- kb3172605
- kb3179573
- kb3184143
- kb4019990
- kb4040980
- kb4088878
- kb4099950
- kb4474419-v3
- kb4490628
- kb4524752
- kb5010798
- kb5013637
- kb5017397
- kb5018454
- kb5020000

## Which libraries are included

- [DirectX](https://www.microsoft.com/en-us/download/details.aspx?id=35)
- [.NET Framework 4.8](https://dotnet.microsoft.com/en-us/download/dotnet-framework/net48)
- [Visual C++ Redistributable 2005-2022](https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170)

## How to use Program Installers

To install programs using a script, you must first download the programs you need and move them to the "Programs" folder in the script directory and run the script.

## What is meant by optimization

**Disabling components**

- Windows Gadget Platform
- Games

**Disabling services**

- Windows Search
- Windows Archiving
- Tablet PC input service
- Bluetooth Support Service
- BitLocker Disk Encryption Service
- Windows Update
- Shadow copy of the volume
- Smart card
- Windows Defender

**A 4 GB swap file will be configured**

**The display of file extensions will be enabled**

## Cleaning temporary files includes the following directories

- `C:\Windows\SoftwareDistribution\Download\`
- `C:\Windows\Prefetch\`
- `%temp%`

## Removing the program

After you install everything you need, you can run `uninstall.bat`.
The script will delete all files and the program directory.
