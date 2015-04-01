# -*- coding: utf-8 -*-

import pandas as pd
import json
import matplotlib.pyplot as plt
import sys
import numpy as np


##
# Read the data
df = pd.read_csv('donations_bigsample.csv', index_col=False)
oba = df[df['cand_nm'] == 'Obama, Barack']
mac = df[df['cand_nm'] == 'McCain, John S']
oba_amt = oba['contb_receipt_amt'].values
mac_amt = mac['contb_receipt_amt'].values


##
# Histogram of the contribution with increaments $100
bins = np.linspace(-4000, 6000, num=100)
n, b, p = plt.hist([oba_amt, mac_amt], bins=bins, color=['r', 'g'], rwidth=[0.5, 0.5])
plt.legend(['obama', 'macain'])
plt.savefig('histogram.png', dpi=300)
plt.close()


##
# Cumulative contribution
oba_cum = np.cumsum(oba_amt)
mac_cum = np.cumsum(mac_amt)
plt.plot(sorted(oba_amt), oba_cum)
plt.plot(sorted(mac_amt), mac_cum)
plt.legend(['obama', 'macain'], loc='upper left')
plt.xlim([-5000, 5000])
plt.savefig('cumulative.png', dpi=300)
plt.close()


##
"""
This part is not implement because the plotting functions in pycharm is not
familar to me.
"""
# Choropleth plot
sys.path.append("dataiap/resources/util")
import map_util as m
fig = plt.figure()

# Map of Counties
# data is a list of strings that contain fips values
county = fig.add_subplot(211)
data = json.load(file('dataiap/datasets/geo/id-counties.json'))
for fips in data:
    m.draw_county(county, fips)

# Map of States
s = fig.add_subplot(212)
data = json.load(file('dataiap/datasets/geo/id-states.json'))
for state in data:
    m.draw_state(s, state)

# # this creates an array of grey colors from white to black
# colors = ['0','1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f']
# colors = map(lambda s: '#%s' % (s*6), colors)
# colors.sort(reverse=True)
#
# # assume MAXDONATION was defined
# # assume curdonation is the donation to pick a color for
# ratio = (curdonation/float(MAXDONATION))
# color_idx = int( ratio * (len(colors) - 1) )
# colors[color_idx]











