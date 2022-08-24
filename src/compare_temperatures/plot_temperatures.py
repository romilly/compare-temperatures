#!/usr/bin/env python
# coding: utf-8
import pandas

yesterday = '2022-08-23'

def read_adafruit_feed_csv(csv, datacol, yesterday):
    df = pandas.read_csv(csv, parse_dates=['created_at'])
    df.dropna(axis=1, how='all',inplace=True)
    df = df[df['created_at']>= yesterday]
    del df['id']
    del df['feed_id']
    df.rename(columns={'value' : datacol}, inplace=True)
    return df


bme280 = read_adafruit_feed_csv('data/bme280-temp-20220824-0701.csv', 'bme280', yesterday)
tmp36 = read_adafruit_feed_csv('data/temp-tmp36-20220824-0659.csv', 'tmp36', yesterday)



