# clear out/update current month in month file

import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

name = 'testing'
sheet = client.open(name).sheet1
data = sheet.get_all_records(empty2zero=True, head=2)

print(data)

# clearing out sheet, needs some work
sheet.update_acell('A1', 'current month')
cell_list = sheet.range('B3:J31')

for cell in cell_list:
    cell.value = '0'

sheet.update_cells(cell_list)
