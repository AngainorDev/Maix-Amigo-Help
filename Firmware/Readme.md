# MaixPy Amigo Firmware

- The factory firmware I got was v0.5.0-168-g306805c50-dirty 
- It had no LVGL
- It was an old version
- It was crashing with the demos

The custom firmware on MaixHub gives even older firmware, not consistent with what you choose.

I ended up tuning and compiling my own firmware from source.  
I hope I will not need to maintain them for long, just posting there in case this is useful to someone else.

Use recommended kflashgui to flash the firmware https://maixpy.sipeed.com/en/get_started/upgrade_firmware.html

## LVGL Version

I was mainly interested in playing with LVGL, despite its RAM footprint.  
This version has 1MB python heap instead of default 512KB.

v0.5.1-92-gf9bb0bb5e-dirty.lvgl.bin

## No LVGL Version

Same, just no LVGL
v0.5.1-92-gf9bb0bb5e-dirty.bin

## Compile your own

The official doc can be followed: https://github.com/sipeed/MaixPy/blob/master/build.md
Use recommended kflashgui to flash the firmware https://maixpy.sipeed.com/en/get_started/upgrade_firmware.html

Do not enable options you don't understand, you'll end up with a broken setup.
