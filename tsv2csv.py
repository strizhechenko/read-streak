#!/usr/bin/env python3
# coding=utf-8

with open('x.txt', 'r') as fd:
    for line in fd.readlines():
        words = line.split()
        date = words[0]
        day, month, year = date.split('.')
        date = "-".join([year, month, day])
        pages = sum(map(int, words[1:]))
        print(",".join([date, str(pages)]))
