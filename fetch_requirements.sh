curl -s https://api.github.com/repos/freshollie/monkeyboard-radio-android/releases/latest | grep "apk" | cut -d '"' -f 4 | wget -i - -O apks/radio.apk

curl -s https://api.github.com/repos/freshollie/UsbGps4Droid/releases/latest | grep "apk" | cut -d '"' -f 4 | wget -i - -O apks/UsbGps4Droid.apk

curl -s https://api.github.com/repos/freshollie/headunit-controller-android/releases/latest | grep "apk" | cut -d '"' -f 4 | wget -i - -O apks/AndroidHeadunitController.apk

wget -O recovery/twrp-3.1.1-0-flo.img https://eu.dl.twrp.me/flo/twrp-3.1.1-0-flo.img

wget -O supersu/SuperSU-v2.82.zip https://s3-us-west-2.amazonaws.com/supersu/download/zip/SuperSU-v2.82-201705271822.zip

wget -O razor-mob30x.zip https://dl.google.com/dl/android/aosp/razor-mob30x-factory-52684dff.zip
unzip razor-mob30x.zip
rm razor-mob30x.zip

gplaydl configure
gplaydl download --packageId com.teslacoilsw.launcher 
gplaydl download --packageId com.spotify.music 
gplaydl download --packageId au.com.shiftyjelly.pocketcasts

mv com.teslacoilsw.launcher.apk patches/kernel-and-software/usb-host-and-apps/launcher/NovaLauncher.apk
mv com.spotify.music.apk apks/
mv au.com.shiftyjelly.pocketcasts.apk apks/

