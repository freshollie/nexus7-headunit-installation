curl -s https://api.github.com/repos/freshollie/monkeyboard-radio-android/releases/latest | grep "apk" | cut -d '"' -f 4 | wget -i - -O apks/radio.apk

curl -s https://api.github.com/repos/freshollie/UsbGps4Droid/releases/latest | grep "apk" | cut -d '"' -f 4 | wget -i - -O apks/UsbGps4Droid.apk

curl -s https://api.github.com/repos/freshollie/headunit-controller-android/releases/latest | grep "apk" | cut -d '"' -f 4 | wget -i - -O apks/AndroidHeadunitController.apk

wget -O recovery/twrp-3.1.1-0-flo.img https://eu.dl.twrp.me/flo/twrp-3.3.1-0-flo.img --referer https://eu.dl.twrp.me/flo/twrp-3.1.1-0-flo.img.html

wget -O patches/supersu/SuperSU-v2.82.zip "https://download.chainfire.eu/1220/SuperSU/SR5-SuperSU-v2.82-SR5-20171001224502.zip?retrieve_file=1"

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

