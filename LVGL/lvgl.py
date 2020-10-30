import lvgl as lv
import lvgl_helper as lv_h
import lcd
import time
from machine import Timer
from machine import I2C
from touch import Touch, TouchLow

config_touchscreen_support = True
board_m1n = False


lcd.init()


TOUCH = None

def read_cb(drv, ptr):
    # print(ptr, b)
    data = lv.indev_data_t.cast(ptr)
    TOUCH.event()
    # print(TOUCH.state, TOUCH.points)
    data.point = lv.point_t({'x': TOUCH.points[1][0], 'y': TOUCH.points[1][1]})
    data.state = lv.INDEV_STATE.PR if TOUCH.state == 1 else lv.INDEV_STATE.REL
    return False


if config_touchscreen_support:
    i2c = I2C(I2C.I2C0, freq=1000*1000, scl=24, sda=27)  # 24 27)
    devices = i2c.scan()
    print("devs", devices)  # devs 0 [16, 38, 52, 56]
    TouchLow.config(i2c)
    TOUCH = Touch(480, 320, 200)

lv.init()

disp_buf1 = lv.disp_buf_t()
buf1_1 = bytearray(320*10)
lv.disp_buf_init(disp_buf1,buf1_1, None, len(buf1_1)//4)
disp_drv = lv.disp_drv_t()
lv.disp_drv_init(disp_drv)
disp_drv.buffer = disp_buf1
# disp_drv.rotated = 1
disp_drv.flush_cb = lv_h.flush
if board_m1n:
    disp_drv.hor_res = 240
    disp_drv.ver_res = 240
else:
    disp_drv.hor_res = 480
    disp_drv.ver_res = 320
lv.disp_drv_register(disp_drv)

if config_touchscreen_support:
    indev_drv = lv.indev_drv_t()
    lv.indev_drv_init(indev_drv)
    indev_drv.type = lv.INDEV_TYPE.POINTER
    indev_drv.read_cb = read_cb
    lv.indev_drv_register(indev_drv)



# lv.log_register_print_cb(lv_h.log)
lv.log_register_print_cb(lambda level,path,line,msg: print('%s(%d): %s' % (path, line, msg)))

scr = lv.obj()
btn = lv.btn(scr)
btn.align(lv.scr_act(), lv.ALIGN.CENTER, 0, 0)
label = lv.label(btn)
label.set_text("Button")
label.set_size(20,20)
lv.scr_load(scr)

def on_timer(timer):
    lv.tick_inc(5)

timer = Timer(Timer.TIMER0, Timer.CHANNEL0, mode=Timer.MODE_PERIODIC, period=5, unit=Timer.UNIT_MS, callback=on_timer, arg=None)

while True:
    tim = time.ticks_ms()
    lv.task_handler()
    while time.ticks_ms()-tim < 5:
        pass
