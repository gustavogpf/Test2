# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:36:27 2019

@author: gflorido
"""
import pandas as pd
from workalendar.america import Chile, Mexico
from workalendar.africa import SouthAfrica

cal = SouthAfrica()
cal = Mexico()

yr_ls = range(2000, 2079)
holidays = []

for yr in yr_ls:
#    holidays = holidays + cal.holidays(yr)
    holidays = holidays + cal.holidays(yr) + [(cal.get_holy_thursday(yr), 'Holy Thursday'), (cal.get_good_friday(yr), 'Good Friday')]
    
holidays_df = pd.DataFrame(holidays, columns = ['Data', 'Feriado'])
holidays_df.to_clipboard(sep = ';')