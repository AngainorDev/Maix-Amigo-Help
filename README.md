# Maix-Amigo-Help
Doc, snippets and code for Sipeed Maix Amigo - Micropython enabled dev widget.

## The Sipeed Maix Amigo

The Amigo is a pretty nice hardware, feature packed:  
https://www.seeedstudio.com/Sipeed-Maix-Amigo-p-4689.html

However, the software and documentation side is currently lagging behind and we were pretty disappointed when getting our Amigo.  
No code sample would work, defaults settings are not correct, doc is inexistent (at best) or misleading when available.

The Amigo has a huge potential and we wanted to help others avoid the pain we felt when getting our first one.  
This repo is there to compile our tries, fails and success.

# The firmware

## Do not use the maixhub service
This service is supposed to build a firmware for you.  
It uses older versions than factory defaults, and does not include what you ask for. For instance I asked lvgl builds, and got no lvgl.  

Build the firmware yourself. If you have a linux at hand, this is fast and troublefree.  
The official doc can be followed: https://github.com/sipeed/MaixPy/blob/master/build.md  
Use recommended kflashgui to flash the firmware https://maixpy.sipeed.com/en/get_started/upgrade_firmware.html

# MaixPy IDE

It's good, especially the integrated framebuffer view.  
https://maixpy.sipeed.com/en/get_started/maixpyide.html

# Other useful tools

rshell is good.  
WIP

# LEDS

- 1 Mini RGB Side LED  
- 1 Large White Rear LED  

See https://github.com/AngainorDev/Maix-Amigo-Help/tree/main/LED

# Cameras

- Front: GC0328
- Rear: OV7740

In a nutshell: 
- Lower sensor frequency to 5000000 instead of default 20000000 or you'll get insane colors, bars on the image, unusable images
- Do not use `sensor.RGB565` as told in the official doc. Amigo uses YUV. Use `sensor.YUV422` or `sensor.GRAYSCALE`.
- Add `sensor.set_vflip(1)` and `sensor/set_hmirror(1)`
- Do not compile the firmware with double buffer, you won't have enough RAM to use them
- We'll detail custom firmware builds to get more RAM and really use the images instead of getting OOM errors everywhere.

To be detailled:  
- How to use the Amigo front cam
- How to use windowing and POI

# Screen

- ILI9486
- 480x320 px

# Touchscreen

- FT6x36
- i2c address 0x38
- scl=24, sda=27
- freq = 1000000

MaixUI has a pure python implementation of the touch screen semi working.  
See https://github.com/sipeed/MaixUI/blob/5646aa3899d126e579e99d38bb8020857cd3abe3/driver/touch.py and https://github.com/sipeed/MaixPy_scripts/issues/79 for a better alternative.

# LVGL

Demos with touchscreen not working, fix to be published here.  
See https://github.com/AngainorDev/Maix-Amigo-Help/tree/main/LVGL/

# /flash

- No subdirectory support
- 3MB spiffs in default firmware

# SD Card

- Only support FAT32


# Tip when building your firmware

Raise heap from 8000 to F0000 (not sure if we can do even more?)

This will give more ram when using LVGL or many pictures functions, or everything crashes with OOM.


# Contributions

Are welcome!
