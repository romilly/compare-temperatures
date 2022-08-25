# Compare temperature readings from different sensors

I've been recording temperature data from a TMP36 temperature sensor
and a home-brew weather station, implemented in MicroPython running on two Raspberry Pi Pico W boards.

The weather station includes a light level sensor and a
BME280 which measures temperature, pressure and humidity.

Both devices use MQTT to transmit their readings to [Adafruit.IO](https://io.adafruit.com/).
The code they run is on [GitHub](https://github.com/romilly/pico-code/tree/master/src/pico_code/picow).

The temperature readings differ more than I'd expected, and I'm using Pandas to analyse the downloaded data.

The high-level analysis is done using a Jupyter notebook.
The preparation of the csv files is done by `plot_temperatures.py`

_Warning:_ I'm a novice user of Pandas, and there may be better ways of manipulation the data.

## Sample plot

![Sample data](notebooks/data/img/temp-diff.png)

The sensors are indoors just inside a window which is normally open during the day but closed at night.

The rapid exponential rise at 10 Pm and fall at 5:54 AM are due to the closing and opening of the window,

The peak at 11 AM is due to sunlight falling on both sensors.