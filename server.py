import homefun
import time

powLimit = 1800

while True:
    power = homefun.get_solar_power()
    homefun.print_power(power, powLimit)
    time.sleep(1)
