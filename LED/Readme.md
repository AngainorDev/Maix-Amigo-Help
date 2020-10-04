# Amigo leds

The Maix Amigo has 3 mini RGB leds plus one large white led, to be used as camera flash.

Unless I missed something, the 3 RGB leds can only be addressed as one, so it's not 3 leds but more like one RGB Led behind 3 holes.

# Official Doc

Sipeed starter doc shares a snippet to test the Red led:

https://maixpy.sipeed.com/zh/get_started/get_started_led_blink.html

```
from fpioa_manager import *
from Maix import GPIO

fm.register(board_info.LED_R, fm.fpioa.GPIO0)

led_r=GPIO(GPIO.GPIO0, GPIO.OUT)
led_r.value(0)
```

This uses builtin module board_info, supposed to handle the peripherals pins.  
If the red pin is ok, the others are not!

Here are the correct pins to use (no need for board_info then)  
- LED_R: 14
- LED_G: 15
- LED_B: 17
- LED_WHITE: 32

## How to light the Maix Amigo flash?

```
from fpioa_manager import fm
from Maix import GPIO

fm.register(32, fm.fpioa.GPIO0)
led = GPIO(GPIO.GPIO0, GPIO.OUT)
led.value(0)
```
