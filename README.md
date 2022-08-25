# Compare temperature readings from different sensors

I've been recording temerature data from a TMP36 temperature sensor
and a home-breaw weather station.

The weather station includes a light level sensor and a
BME280 which measures temperature, pressure and humidity.

Both devices use MQTT to transmit their readings to [Adafruit.IO](https://io.adafruit.com/).

The temperature readings differ more than I'd expected, and I'm using Pandas to analyse the downloaded data.

The higih-level analysis is done using a Jupyter notebook. The prepratation of the csv files

