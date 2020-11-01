import os
import sys
import subprocess
import time

FNULL = open(os.devnull, 'w')

OS_FOLDER = "razor-mob30x/"

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
    "com.google.android.GoogleCamera"
]

# headunit tool

##### Android functions ########

def pull_thirdparty_apks():
    if not os.path.exists("apks"):
        os.makedirs("apks")
        
    for package in THIRDPARTY:
        location = str(subprocess.check_output("adb shell pm path " + package + " | sed -e 's/^package://'", shell=True)).strip()
        os.system("adb pull " + location + " apks/" + package + ".apk")


def disable_packages():
    for package in TO_DISABLE:
        os.system("adb shell pm disable " + package)


def delete_supersu_package():
    os.system("adb shell pm uninstall eu.chainfire.supersu")


def disable_volume_warning():
    os.system("adb shell mount -o remount -t rw /system")
    os.system("adb shell \"echo 'audio.safemedia.bypass=true\\n' >> /system/build.prop\"")
    os.system("adb shell chmod 644 /system/build.prop")


def disable_lockscreen():
    os.system("adb shell settings put secure lockscreen.disabled 1")
    os.system("adb shell mkdir /data/system/lock_old")
    os.system("adb shell mv /data/system/locksettings* /data/system/lock_old")

	
def disable_nfc():
	os.system("svc nfc disable")
	

def disable_sounds():
    os.system("adb shell settings put system sound_effects_enabled 0")
    os.system("adb shell settings put system volume_notification 0")


def enable_always_awake():
    os.system("adb shell svc power stayon true")


def enable_gps_driver():
    os.system("adb shell pm grant org.broeuschmeul.android.gps.usb.provider android.permission.ACCESS_FINE_LOCATION")
    os.system("adb shell appops set org.broeuschmeul.android.gps.usb.provider android:mock_location allow")


def enable_headunit_controller():
    os.system("adb shell appops set com.freshollie.headunitcontroller android:get_usage_stats allow")
    os.system("adb shell settings put secure enabled_notification_listeners " +
              "com.freshollie.headunitcontroller/com.freshollie.headunitcontroller.service.GoogleMapsListenerService")

    # Allows the widget
    os.system("adb shell appwidget grantbind --package com.teslacoilsw.launcher")


def push_launcher_settings():
    os.system("adb shell am start -n com.teslacoilsw.launcher/.PresetsActivity")

    os.system("adb shell pm hide com.android.launcher")
    os.system("adb push patches/launcher/launcher.db /data/user/0/com.teslacoilsw.launcher/databases/launcher.db")
    os.system("adb push patches/launcher/com.teslacoilsw.launcher_preferences.xml /data/user/0/com.teslacoilsw.launcher/shared_prefs/com.teslacoilsw.launcher_preferences.xml")


def unlock_screen():
    os.system("adb shell input keyevent 82 && adb shell input keyevent 66")


def install_packages():
	# installs all apks in the apks folder and grants all permissions
    for apk in os.listdir("apks"):
        os.system("adb install -g " + "apks/" + apk)


def push_patch_files():
    for patch in os.listdir("patches/kernel-and-software"):
        if patch.endswith(".zip"):
            os.system("adb push patches/kernel-and-software/" + patch + " /sdcard/headunit-files/patches/" + patch)

    for patch in os.listdir("patches/supersu"):
        if patch.endswith(".zip"):
            os.system("adb push patches/supersu/" + patch + " /sdcard/headunit-files/patches/" + patch)

######## Kernel and OS #########


def compile_patch_files():
    os.chdir("patches/kernel-and-software")
    os.system("./pack-usb-host-and-apps.sh")
    os.chdir("../../")


def unlock_bootloader():
    os.system("fastboot oem unlock")


def flash_os():
    os.chdir(OS_FOLDER)
    os.system("sudo ./flash-all.sh")
    os.chdir("../")

    
def adb_reboot_bootloader():
    os.system("adb reboot bootloader")


def adb_reboot_system():
    os.system("adb reboot system")


def adb_reboot_recovery():
    os.system("adb reboot recovery")


def adb_wait_for_device():
    while True:
        try:
            output = subprocess.check_output("adb shell echo test", shell=True, stderr=FNULL).decode(sys.stdout.encoding)
            print(output)
            if output.startswith("test"):
                break
        except Exception as e:
            print(e)
            pass

        time.sleep(0.5)
    time.sleep(1)


def fastboot_boot_recovery():
    os.system("fastboot boot recovery/twrp-3.1.1-0-flo.img")


def enable_power_on_charge():
    os.system("fastboot oem off-mode-charge 0")


def flash_recovery():
    os.system("sudo fastboot flash recovery recovery/twrp-3.1.1-0-flo.img")

    
def flash_software_and_kernel():
    for patch in os.listdir("patches/kernel-and-software"):
        if patch.endswith(".zip"):
            os.system("adb shell twrp install /sdcard/headunit-files/patches/" + patch)


def flash_root():
    for patch in os.listdir("patches/supersu"):
        if patch.endswith("zip"):
            os.system("adb shell twrp install /sdcard/headunit-files/patches/" + patch)
            break


######### Installation wizard ############
def fresh_installation_wizard():
    os.system("sudo echo")
    input("Please follow instructions exactly. Boot the device, enable developer tools, and press enter to start")

    adb_reboot_bootloader()

    print("Unlocking bootloader")
    unlock_bootloader()

    print("Installing OS")
    flash_os()
    
    print("-------------------------------------------")
    input("Installation complete, please follow device installation process, enable developer tools, and press enter when complete")

    compile_patch_files()
    print("Copying files to device")
    push_patch_files()
    adb_reboot_bootloader()

    print("Flashing and booting into recovery")
    flash_recovery()
    fastboot_boot_recovery()
    
    adb_wait_for_device()
    time.sleep(10)

    print("Flashing headunit files")
    flash_software_and_kernel()
    flash_root()
    adb_reboot_system()
    
    print("Flash complete")
    adb_wait_for_device()

    input("Press enter when os booted")

    print("-------------------------------------------")
    print("Starting software install")

    
    print("Installing apps")
    install_packages()

    print("Disabling tap sounds")
    disable_sounds()

    print("Setting up headunit controller")
    enable_headunit_controller()

    print("Setting up GPS driver")
    enable_gps_driver()
	
    
    print("Disabling nfc")
    disable_nfc()
	
    print("Enabling always awake")
    enable_always_awake()
    
    os.system("adb root")

    print("Disabling unneeded packages")
    disable_packages()

    print("Disabling volume warning")
    disable_volume_warning()

    print("Removing supersu warnings")
    delete_supersu_package()

    print("Disabling lockscreen")
    disable_lockscreen()

    print("Unlocking screen")
    unlock_screen()
    
    print("Setting up launcher")
    push_launcher_settings()

    time.sleep(3)

    adb_reboot_system()
    
    adb_wait_for_device()
    input("Headunit built")
    
fresh_installation_wizard()
