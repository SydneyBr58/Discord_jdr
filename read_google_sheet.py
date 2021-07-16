import pandas as pd
import gspread
from gspread_pandas import Spread, conf
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

def read_gsheet(sheetname, tab, first_row=0):
    #first_row has to be an integer, it helps to set the df headers as the correct columns if not starting from the top
    workbook = client.open(sheetname)
    ws = workbook.worksheet(tab)
    sheet = ws.get_all_values() 
    column_name = sheet[first_row]
    df = pd.DataFrame(sheet[first_row+1:], columns=column_name)
    return df

# The entire tab is now in the dataframe