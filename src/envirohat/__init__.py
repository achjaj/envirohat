from bme280 import BME280
from ltr559 import LTR559
from enviroplus import gas
from enviroplus.noise import Noise
# import ST7735
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

import time


class EnviroHAT:
    def __init__(self):
        self.bme = BME280(i2c_dev=SMBus(1))
        self.ltr = LTR559()
        self.noise = Noise()
        # self.display = ST7735.ST7735(port=0, cs=1, dc=9, backlight=12, rotation=270, spi_speed_hz=10000000)

    def __mean_measure__(self, fn, num, delay=0):
        if num < 2:
            return fn()

        values = list()
        for i in range(num):
            values.append(fn())
            time.sleep(delay)

        return sum(values)/len(values)

    def get_temperature(self, num=1, delay=0):
        return self.__mean_measure__(self.bme.get_temperature, num, delay)

    def get_humidity(self, num=1, delay=0):
        return self.__mean_measure__(self.bme.get_humidity, num, delay)

    def get_pressure(self, num=1, delay=0):
        return self.__mean_measure__(self.bme.get_pressure, num, delay)

    def get_altitude(self, qnh=1013.25, num=1, delay=0):
        return self.__mean_measure__(lambda: self.bme.get_altitude(qnh), num, delay)

    def get_lux(self, passive=False, num=1, delay=0):
        return self.__mean_measure__(lambda: self.ltr.get_lux(passive), num, delay)

    def get_proximity(self, passive=False, num=1, delay=0):
        return self.__mean_measure__(lambda: self.ltr.get_proximity(passive), num, delay)

    def gas_read_all(self, num=1, delay=0):
        return self.__mean_measure__(gas.read_all, num, delay)

    def gas_read_oxidising(self, num=1, delay=0):
        return self.__mean_measure__(gas.read_oxidising, num, delay)

    def gas_read_reducing(self, num=1, delay=0):
        return self.__mean_measure__(gas.read_reducing, num, delay)

    def gas_read_nh3(self, num=1, delay=0):
        return self.__mean_measure__(gas.read_nh3, num, delay)

    def get_amplitudes_at_frequency_ranges(self, ranges, num=1, delay=0):
        return self.__mean_measure__(lambda: self.noise.get_amplitudes_at_frequency_ranges(ranges), num, delay)

    def get_amplitude_at_frequency_range(self, start, end, num=1, delay=0):
        return self.__mean_measure__(lambda: self.noise.get_amplitude_at_frequency_range(start, end), num, delay)

    def get_noise_profile(self, noise_floor=100, low=0.12, mid=0.36, high=None, num=1, delay=0):
        return self.__mean_measure__(lambda: self.noise.get_noise_profile(noise_floor, low, mid, high), num, delay)
