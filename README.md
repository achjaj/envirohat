# Envirohat

*Enviro+ sensors in one place*

## Installation

`pip intall envirohat`

## Reference

`get_temperature()` - get current temperature

`get_humidity()` - get current humidity

`get_pressure()` - get current pressure

`get_altitude(qnh=1013.25)` - get altitude

`get_lux(passive=False)` - get ambient light in lux

`get_proximity(passive=False)` - get raw proximity value, closer object produce larger value

`gas_read_all()` - get gas resistance for oxidising, reducing and NH3

`gas_read_oxidising()` - get gas resistance for oxidising (calls `read_all`)

`gas_read_reducing()` - get gas resistance for reducing (calls `read_all`)

`gas_read_nh3()` - get gas resistance for NH3 (calls `read_all`)

`get_amplitudes_at_frequency_ranges(ranges)` - get the mean amplitude of frequencies in the given ranges
 - `ranges`: List of ranges including a start and end range

`get_amplitude_at_frequency_range(start, stop)` - get the mean amplitude of frequencies in the specified range
 - `start`: Start frequency (in Hz)
 - `end`: End frequency (in Hz)

`get_noise_profile(noise_floor=100,
                          low=0.12,
                          mid=0.36,
                          high=None)` - get a noise characteristic profile
 - `noise_floor`: "High-pass" frequency, exclude frequencies below this value
 - `low`: Percentage of frequency ranges to count in the low bin (as a float, 0.5 = 50%)
 - `mid`: Percentage of frequency ranges to count in the mid bin (as a float, 0.5 = 50%)
 - `high`: Optional percentage for high bin, effectively creates a "Low-pass" if total percentage is less than 100%

`bme` - the BME280 sensor

`ltr` - the LTR559 sensor

`noise` - the noise sensor

All functions support reading a time averaged value. For example
`get_temperature(num=5, delay=0.3)` returns average of 5 temperature readings, `delay` is time between each reading in seconds.
The default values are: `num=1` and `delay=0`.

## Example

``` Python
from envirohat import EnviroHAT
    
hat = EnviroHAT()
    
print("Tepmerature:", hat.get_temperature(), "°C")
print("Humiditi:", hat.get_humidity(num=5, delay=0.3), "%")
print("Raw ALS:", hat.ltr.get_raw_als())
```
