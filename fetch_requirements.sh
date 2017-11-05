wget -O apks/radio.apk https://github.com/freshollie/monkeyboard-radio-android/raw/master/app/build/outputs/apk/app-debug.apk 

wget -O patches/kernel-and-software/usb-host-and-apps/usbgps4droid/UsbGps4Droid.apk https://github.com/freshollie/UsbGps4Droid/raw/master/app/build/outputs/apk/app-debug.apk

wget -O patches/kernel-and-software/usb-host-and-apps/headunitcontroller/AndroidHeadunitController.apk https://github.com/freshollie/AndroidHeadunitController/raw/master/app/build/outputs/apk/app-debug.apk

wget -O recovery/twrp-3.1.1-0-flo.img https://eu.dl.twrp.me/flo/twrp-3.1.1-0-flo.img

wget -O supersu/SuperSU-v2.82.zip https://s3-us-west-2.amazonaws.com/supersu/download/zip/SuperSU-v2.82-201705271822.zip

wget -O razor-mob30x.zip https://dl.google.com/dl/android/aosp/razor-mob30x-factory-52684dff.zip
unzip razor-mob30x.zip
rm razor-mob30x.zip

gplaycli -d com.teslacoilsw.launcher com.spotify.music au.com.shiftyjelly.pocketcasts -p
mv com.teslacoilsw.launcher.apk patches/usb-host-and-apps/launcher/NovaLauncher.apk
mv com.spotify.music.apk apks/
mv au.com.shiftyjelly.pocketcasts.apk apks/

