import requests
from bs4 import BeautifulSoup
import smtplib
import openpyxl
from openpyxl import Workbook
from datetime import date
from amd import *
from intel import *

excel = Workbook()

planilha = excel.active
planilha['A1'] = 'AMD:'
planilha['A2'] = 'CPU:'
planilha['B1'] = 'Nome:'
planilha['B2'] = 'R5 1600AF'
planilha['D1'] = 'Preço:'
planilha['C1'] = 'Data:'
planilha['C2'] = '{}'.format(date.today())
planilha['D2'] = 'R${}'.format(price_R51600AF)
planilha['A3'] = 'CPU:'
planilha['B3'] = 'R3 2200G'
planilha['D3'] = 'R${}'.format(price_R32200G)
planilha['C3'] = '{}'.format(date.today())
planilha['A4'] = 'CPU:'
planilha['B4'] = 'R5 2600'
planilha['D4'] = 'R${}'.format(price_R52600)
planilha['C4'] = '{}'.format(date.today())
planilha['A5'] = 'CPU:'
planilha['B5'] = 'R7 2700'
planilha['D5'] = 'R${}'.format(price_R72700)
planilha['C5'] = '{}'.format(date.today())
planilha['A6'] = 'CPU:'
planilha['B6'] = 'R5 3600'
planilha['D6'] = 'R${}'.format(price_R53600)
planilha['C6'] = '{}'.format(date.today())
planilha['A7'] = 'CPU:'
planilha['B7'] = 'R7 3700X'
planilha['D7'] = 'R${}'.format(price_R73700X)
planilha['C7'] = '{}'.format(date.today())
planilha['A8'] = 'CPU:'
planilha['B8'] = 'R7 3800X'
planilha['D8'] = 'R${}'.format(price_R73800X)
planilha['C8'] = '{}'.format(date.today())
planilha['A9'] = 'CPU:'
planilha['B9'] = 'R9 3900X'
planilha['D9'] = 'R${}'.format(price_R93900X)
planilha['C9'] = '{}'.format(date.today())
planilha['A10'] = 'CPU:'
planilha['B10'] = 'R3 3300X'
planilha['D10'] = 'R${}'.format(price_R33300X)
planilha['C10'] = '{}'.format(date.today())
planilha['A11'] = 'CPU:'
planilha['B11'] = 'R3 3200G'
planilha['D11'] = 'R${}'.format(price_R33200G)
planilha['C11'] = '{}'.format(date.today())
planilha['A12'] = 'CPU:'
planilha['B12'] = 'R5 3600X'
planilha['D12'] = 'R${}'.format(price_R53600X)
planilha['C12'] = '{}'.format(date.today())

planilha['A20'] = 'CPU:'
planilha['B20'] = 'i3 9100F'
planilha['D20'] = 'R${}'.format(price_i39100F)
planilha['C20'] = '{}'.format(date.today())
planilha['A21'] = 'CPU:'
planilha['B21'] = 'i5 9400F'
planilha['D21'] = 'R${}'.format(price_i59400F)
planilha['C21'] = '{}'.format(date.today())
planilha['A22'] = 'CPU:'
planilha['B22'] = 'i5 9600K'
planilha['D22'] = 'R${}'.format(price_i59600K)
planilha['C22'] = '{}'.format(date.today())
planilha['A22'] = 'CPU:'
planilha['B22'] = 'i7 9700F'
planilha['D22'] = 'R${}'.format(price_i79700F)
planilha['C22'] = '{}'.format(date.today())
planilha['A22'] = 'CPU:'
planilha['B22'] = 'i7 9700K'
planilha['D22'] = 'R${}'.format(price_i79700K)
planilha['C22'] = '{}'.format(date.today())
excel.save('{}.xlsx'.format(date.today()))



























