#!/usr/bin/env python2
#*-* coding: utf-8 *-*

freq_list = {
    'Q' : 0.,
    'W' : 0.,
    'E' : 0.,
    'R' : 0.,
    'T' : 0.,
    'Y' : 0.,
    'U' : 0.,
    'I' : 0.,
    'O' : 0.,
    'P' : 0.,
    'A' : 0.,
    'S' : 0.,
    'D' : 0.,
    'F' : 0.,
    'G' : 0.,
    'H' : 0.,
    'J' : 0.,
    'K' : 0.,
    'L' : 0.,
    'Z' : 0.,
    'X' : 0.,
    'C' : 0.,
    'V' : 0.,
    'B' : 0.,
    'N' : 0.,
    'M' : 0.,
    '0' : 0.,
    '1' : 0.,
    '2' : 0.,
    '3' : 0.,
    '4' : 0.,
    '5' : 0.,
    '6' : 0.,
    '7' : 0.,
    '8' : 0.,
    '9' : 0.,
}

string = raw_input().upper()

for x in string:
    if x in freq_list:
        freq_list[x] += 1.

freq = [freq_list[x]*100/len(string) for x in freq_list]
freq.sort()
carac = [x for x in '0123456789WYKXJZFBQHGVPLCTUMDNIRSOEA']

for x in freq_list:
    for y in range(len(freq)):
        if freq[y] == freq_list[x]*100/len(string) and freq[y] > 0.0:
            string = string.replace(x, carac[y])
            break

print string
