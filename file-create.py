# works

import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

name = 'testing'
sheet = client.open(name).sheet1
data = sheet.get_all_records(empty2zero=True, head=2)

print(data)
# data = [{'day': 'wed', 'taco': 2, 'pastry': 3, 'vegan' : '2', 'scone' : '2'}, {'day': 'thu', 'taco': 5, 'pastry': 4}, {'day': 'fri', 'taco': 7, 'pastry': 6},
#  {'day': 'sat', 'taco': 0, 'pastry': 0}, {'day': 'sun', 'taco': 0, 'pastry': 0, 'muffin' : '3'}]

# print(data)

# correct formatting and file creation
f_list = []
f1 = open('test-raw-data.txt', 'w+')
count = 0
for dic in data :
    for key,value in dic.items() :
        f_list.append(str(key))
        f_list.append(' | ')
        f_list.append(str(value))
        f_list.append(' | ')
        count = count + 1
        if count >= len(dic) :
            f_list.append('\n')
            count = 0

f1.writelines(f_list)
f1.close()
