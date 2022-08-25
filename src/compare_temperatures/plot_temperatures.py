#!/usr/bin/env python
# coding: utf-8
import pandas

yesterday = '2022-08-23'

def read_adafruit_feed_csv(csv, datacol, yesterday):
    df = pandas.read_csv(csv, parse_dates=['created_at'])
    df.dropna(axis=1, how='all',inplace=True)
    df = df[df['created_at']>= yesterday]
    df = df.drop(columns=['id','feed_id'])
    df.rename(columns={'value' : datacol}, inplace=True)
    df['created'] = df['created_at'].map(lambda x: x.replace(second=0))
    df = df.drop(columns=['created_at'])
    df = df.set_index(df['created'])
    df = df.drop(columns=['created'])
    return df


bme280 = read_adafruit_feed_csv('data/bme280-temp-20220824-0701.csv', 'bme280', yesterday)
tmp36 = read_adafruit_feed_csv('data/temp-tmp36-20220824-0659.csv', 'tmp36', yesterday)



