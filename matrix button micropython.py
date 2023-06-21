 #from machine import Pin, Timer
#from machine import PWM
import utime
# import servo 

from machine import Pin as pin
from utime import sleep

led = pin(16, pin.OUT)
ir = pin(0,pin.IN)


# def blink():
#     while True:
#         print(ir.value())
#         if ir.value()==1:
#             led.value(0)
#         else:
#             led.value(1)
# 
# blink()

# def bk():
#     while True:
#         led(1)
#         utime.sleep(1)
#         led(0)
#         utime.sleep(1)
#         
# bk()

#from machine import Pin, Timer
#from machine import PWM
# import utime
# # import servo 

from machine import Pin as pin
from machine import ADC, reset
from utime import sleep
# 
# led1 = pin(16, pin.OUT)
# led2 = pin(0,pin.OUT)
# 
# 
# def blink():
#     while True:
#         print(ir.value())
#         if ir.value()==1:
#             led.value(0)
#         else:
#             led.value(1)
# 
#blink()
led3 = pin(16,pin.OUT)
led4 = pin(17,pin.OUT)
led5 = pin(18,pin.OUT)
led6 = pin(19,pin.OUT)
key_up = const(0)
key_down = const(1)

keys = [['rightdown', 'rightup'], ['leftdown', 'leftup']]

left = [0,1]
right = [2,3]

left_pins = [pin(pin_name, mode=pin.OUT) for pin_name in left]

right_pins = [pin(pin_name, mode=pin.IN, pull=pin.PULL_DOWN) for pin_name in right]

def init():
    for left in range(0,2):
        for right in range(0,2):
            left_pins[left].low()
            
def scan(left, right):
    """scan the keypad"""
    
    left_pins[left].high()
    key = None
    
    if right_pins[right].value() == key_down:
        key = key_down
    if right_pins[right].value() == key_up:
        key = key_up
    left_pins[left].low()
    
    return key

print("start entering the keys")

init()

while True:
    for left in range(2):
        for right in range(2):
            key = scan(left, right)
            if key == key_down:
                print("key pressed is", keys[left][right])
                last_key_press = keys[left][right]
                
                if(keys[left][right] == "leftdown"):
                     led3(1)
                     sleep(0.1)
                     led3(0)
                elif(keys[left][right] == "rightdown"):
                     led4(1)
                     sleep(0.1)
                     led4(0)
                elif(keys[left][right] == "leftup"):
                     led5(1)
                     sleep(0.1)
                     led5(0)
                elif(keys[left][right] == "rightup"):
                    led6(1) 
                    sleep(0.1)
                    led6(0)
                    

