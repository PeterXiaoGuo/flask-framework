# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 16:58:56 2017

@author: VickyQian
"""

from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class TickerForm(Form):
    ticker_symbol = StringField('ticker_symbol', validators=[DataRequired()])
    closing_price = BooleanField('closing_price',default=False)
    adj_close = BooleanField('adj_close',default=False)
    opening_price = BooleanField('opening_price',default=False)
    adj_opening = BooleanField('adj_opening',default=False)
    #yesno = BooleanField('yesno', default=False)