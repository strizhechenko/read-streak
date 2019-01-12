#!/usr/bin/env python3
# coding=utf-8

with open('x.txt', 'r') as fd:
    for line in fd.readlines():
        words = line.split()
        date = words[0]
        day, month, year = date.split('.')
        if int(month) < 10:
            month = '0' + month
        if int(day) < 10:
            day = '0' + day
        date = "-".join([year, month, day])
        pages = sum(map(int, words[1:]))
        print(",".join([date, str(pages)]))
