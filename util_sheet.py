
# -*- coding:utf-8 -*-
"""
    スプレッドシートを扱う
    json sheet key fileとシートキーが必要


"""
import gspread
import pandas as pd
from gspread_dataframe import get_as_dataframe, set_with_dataframe
import pysnooper


import os
from dotenv import load_dotenv
import logging

lg = logging.getLogger(__name__)

# 環境変数を参照
load_dotenv()
SHEET_JSON_FILE = os.getenv('SHEET_JSON_FILE')
SHEET_KEY = os.getenv('SHEET_KEY')
SHEET_NAME = os.getenv('SHEET_NAME')





#スプレッドシートからデータ取得用
@pysnooper.snoop()
def get_sheet_with_pd(sheetname=SHEET_NAME):
    try:
        gc = gspread.service_account(SHEET_JSON_FILE)
        sh = gc.open_by_key(SHEET_KEY)
        worksheet = sh.worksheet(sheetname)
        df = get_as_dataframe(worksheet, skiprows=0, header=0)
        return df
    except Exception as e:
        lg.exception(e)

@pysnooper.snoop()
def set_sheet_with_pd(sheetname, df):
    lg.debug(sheetname)
    try:
        gc = gspread.service_account(SHEET_JSON_FILE)
        sh = gc.open_by_key(SHEET_KEY)
        worksheet = sh.worksheet(sheetname)
        set_with_dataframe(worksheet, df)
        print("set df ok")
    except Exception as e:
        lg.exception(e)
    
    
# シート名、キャラ名,行の名前、書きこむ値が引数
@pysnooper.snoop()
def writeSheet(sheetname, col_name, row_name, input_val):
    gc = gspread.service_account(SHEET_JSON_FILE)
    sh = gc.open_by_key(SHEET_KEY)
    worksheet = sh.worksheet(sheetname)
    # 最初の列と列を読み込む
    row_num = worksheet.row_values(1)
    col_num = worksheet.col_values(1)
    # 読み込んだ最初の列の列番号のインデックス
    mycol = col_num.index(col_name) + 1
    myrow = row_num.index(row_name) + 1
    # 指定した行を出す
    worksheet.update_cell(mycol, myrow, input_val)