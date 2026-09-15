from machine import Pin, ADC
import time

led = Pin(15, Pin.OUT)
buzzer = Pin(14, Pin.OUT)
fire_sensor = Pin(16, Pin.IN)
gas_sensor = ADC(Pin(26))  # ADC0

gas_threshold = 20000  # 16-bit ADC (0-65535), adjust based on testing

while True:
    gas_value = gas_sensor.read_u16()
    fire_detected = fire_sensor.value()  # usually 0 = fire detected

    print("Gas level:", gas_value, "| Fire sensor:", fire_detected)

    if gas_value > gas_threshold or fire_detected == 1:
        led.value(1)
        buzzer.value(1)
    else:
        led.value(0)
        buzzer.value(0)

    time.sleep(0.2)