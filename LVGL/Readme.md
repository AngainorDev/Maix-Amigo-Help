# Amigo LVGL and Touchscreen

See https://github.com/sipeed/MaixPy_scripts/issues/79

## Stock demo error

No LVGL touchscreen demo does work with MaixPy Amigo.

For once, the i2c pins are not right    
MaixPy_scripts/application/lvgl/lvgl_button.py  
Line 11:  
`i2c = I2C(I2C.I2C0, freq=400000, scl=30, sda=31)`  
 
These should be 24 and 27 for Amigo.  
Then, there is a further error "OSError: [Errno 5] EIO" when calling ts.init(i2c).

Got it finally working by coding a pure python input callback for lvgl, using sample code from MaixUI.
Not perfect, but allows to get touch screen semi working with LVGL at least.
Will post it later on.

A better option would be to include the full C driver of FT6x36.
It's been done for ESP32, could be added as a module to the MaixPy firmware build, see
https://github.com/lvgl/lv_port_esp32/pull/48/files

## Temp. test

touch.py, from MaixUI slightly edited   
See lvgl.py for usage and handler.

Slow and not tracking gestures right, at least that's something to play with.

Right way is a full C driver with lvgl callback, hoping someone cal help with this!
