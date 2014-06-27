#!/usr/bin/env python
# Author: Wesley Tanaka <http://wtanaka.com/>
import datetime
import matplotlib.pyplot as plot # 1.2.1

dates = ("1980-01-02", "1981-01-02", "1982-01-04", "1983-01-03", "1984-01-03")
dd = (6.72, 7.00, 6.38, 5.97, 8.53)
xom = (1.68, 2.54, 3.86, 3.62, 4.58)
ge = (1.01, 1.29, 1.22, 1.91, 2.40)

dates = tuple(datetime.datetime.strptime(date, "%Y-%m-%d") for date in dates)

def do_plot(y, color, label):
  plot.plot(dates, y, color=color, label=label)
  plot.plot(dates, y, color=color, linestyle='None', marker="o",
    markersize=7, markeredgecolor='w', markeredgewidth=1.5)
  plot.fill_between(dates, y, facecolor=(color,), alpha=0.5)

do_plot(dd, '#748BA7', "DD")
do_plot(xom, '#4C688B', "XOM")
do_plot(ge, '#2B4970', "GE")

plot.legend()
plot.ylabel("Price")
plot.xlabel("Date")
plot.grid()
plot.gcf().autofmt_xdate()
plot.gcf().set_size_inches(4, 4)
plot.savefig('matplotlib-line.png', dpi=100)
