import os
import subprocess

OS_PACKAGE_FOLDER = "razor-mob30x/"

THIRDPARTY = [
    "au.com.shiftyjelly.pocketcasts",
    "org.crape.rotationcontrol",
    "com.teslacoilsw.launcher",
    "com.spotify.music",
    "com.autobright.kevinforeman.autobright"
]

TO_DISABLE = [
    "com.google.android.apps.docs.editors.docs",
    "com.google.android.apps.enterprise.dmagent",
    "com.google.android.apps.docs.editors.sheets",
    "com.google.android.apps.docs.editors.slides",
    "com.google.android.marvin.talkback",
    "com.google.android.gm",
    "com.google.android.music",
    "com.google.android.apps.cloudprint",
    "com.google.android.apps.docs",
    "com.google.android.apps.plus",
    "com.google.android.nfcprovision",
    "me.twrp.twrpapp",
    "com.google.android.contacts",
    "com.google.android.gm.exchange",
    "com.google.android.calculator",
    "com.google.android.videos",
    "com.google.android.apps.photos",
    "com.google.android.calendar",
    "com.google.android.inputmethod.korean",
    "com.google.android.inputmethod.pinyin",
    "com.google.android.apps.books",
    "com.nuance.xt9.input",
    "com.google.android.keep",
    "com.google.android.talk",
    "jp.co.omronsoft.iwnnime.ml",
    "com.google.android.play.games",
    "com.google.android.apps.magazines",
    "com.google.android.GoogleCamera",
    "com.android.launcher"
]

# headunit tool

def unlock_bootloader():
    os.system("fastboot oem unlock")


def pull_thirdparty_apks():
    if not os.path.exists("apks"):
        os.makedirs("apks")
        
    for package in THIRDPARTY:
        location = subprocess.check_output("adb shell pm path " + package + " | sed -e 's/^package://'", shell=True).strip()
        os.system("adb pull " + location + " apks/" + package + ".apk")


def disable_packages():
    os.system("adb root")
    
    for package in TO_DISABLE:
        os.system("adb shell pm disable " + package)


def disable_volume_warning():
    os.system("adb root")
    
    os.system("adb shell \"mount -o remount -t rw /system; echo 'audio.safemedia.bypass=true' >> /system/build.prop; chmod 644 /system/build.prop\"")


def reinstall_os():
    os.chdir(OS_PACKAGE_FOLDER)
    os.system("sudo ./flash-all.sh")
    os.chdir("../")

    
def adb_boot_bootloader():
    os.system("adb reboot bootloader")


def fastboot_boot_recovery():
    os.system("sudo fastboot boot recovery/twrp-3.1.1-0-flo.img")


def adb_boot_system():
    os.system("adb reboot system")


def adb_boot_recovery():
    os.system("adb reboot recovery")


def flash_recovery():
    os.system("sudo fastboot flash recovery recovery/twrp-3.1.1-0-flo.img")

    
def flash_timurs_kernel():
    for patch in os.listdir("headunit-files/kernel-patches"):
        os.system("adb shell twrp install /sdcard/headunit-files/kernel-patches/" + patch)

        
def install_packages():
    for apk in os.listdir("apks"):
        os.system("adb install " + "apks/" + apk);


def add_required_files():
    os.system("adb push headunit-files/ /sdcard")


def fresh_installation_wizard():
    os.system("sudo echo")
    raw_input("Please follow instructions exactly. Boot the device to the lock screen, enable developer tools, and press enter to start")
    adb_boot_bootloader()
    unlock_bootloader()
    reinstall_os()
    print("-------------------------------------------")
    raw_input("Installation complete, please follow device installation process, enable developer tools, and press enter when complete")
    print("Copying files to device")
    add_required_files()
    
    print("Flashing recovery")
    adb_boot_bootloader()
    flash_recovery()
    
    print("Flashing timurs kernel")
    flash_timurs_kernel()
    adb_boot_system()
    print("Flash complete")
    raw_input("Press enter when os booted")
    
    print("Starting software install")
    disable_packages()
    install_packages()
    disable_volume_warning()
    adb_boot_system()
    
    os.system("adb shell ls")
    raw_input("Ok, to finish installation: Restore nova launcher backup, set your PEM settings, set device sleep to None in developer options, enable rotation lock")


#install_packages()
fresh_installation_wizard()