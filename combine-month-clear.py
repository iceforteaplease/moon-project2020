# update month, number, weekdays, clear out data cells

import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

store = input('Store name (lower case): ')
name = store + ' food waste log'
try :
    sheet = client.open(name).sheet1
except :
    print('Problem opening spreadsheet, check store name spelling and case.')
    quit()

# name = 'westlake food waste log'
# sheet = client.open(name).sheet1
# data = sheet.get_all_records(empty2zero=True, head=2)
# print(data)

# this gets the month number successfully
import datetime
from datetime import date

today = datetime.date.today()
str_today = str(today)
month = str_today[5:7]
if month[0] == '0' : # makes one digit if first number is 0
    month = month[1:2]

current_month = int(month)
current_year = int(str_today[:4])
month_year_for_email = str_today[5:8] + str_today[:4]
# print(current_month)
# print(current_year)

import calendar
from calendar import monthrange

month_range = monthrange(current_year, current_month)
how_many_month_days = month_range[1]

# clears last day nums for month
cell_list = sheet.range('A31:A33')
for cell in cell_list:
    cell.value = ''

sheet.update_cells(cell_list)

# updates day nums for current month
day_nums = 29
row = 31
while day_nums <= how_many_month_days :
    sheet.update_cell(row, 1, day_nums)
    row = row + 1
    day_nums = day_nums + 1
print('Day numbers updated')

# gets correct weekdays for month in list
weekdays = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
month_days = []
start_total = 0
end_total = 0
cal = calendar.Calendar(firstweekday=0)

for day in cal.itermonthdays(current_year, current_month) :
    # print(day)
    if day == 0 :
        start_total = start_total + 1
    elif day == 1 :
        break

for day in cal.itermonthdays(current_year, current_month) :
    if day > 0 :
        end_total = end_total + 1
start_day = weekdays[start_total]

# starts loop midweek on correct day
day_num = 1
for each in weekdays[start_total:] :
    month_days.append(each)
    day_num = day_num + 1

# gets correct number of days for the month
days_already = 7 - start_total
while days_already < end_total :
    if days_already > end_total - 7 :
        for each in weekdays[:end_total] :
            if day_num > end_total : # stops weekday loop at correct end day
                break
            month_days.append(each)
            day_num = day_num + 1
    else :
        for each in weekdays :
            month_days.append(each)
            day_num = day_num + 1

    days_already = days_already + 7

# update month/year cell
sheet.update_acell('A1', month_year_for_email)
print('Month/year updated')

# update day cells
row = 3
month_day = 0
if len(month_days) < 31 : # turn leftover days into blanks
    diff = 31 - len(month_days)
    while len(month_days) < 31 :
        month_days.append('')
# print('month days with extras', month_days)

while row < 34 :
    sheet.update_cell(row, 2, month_days[month_day])
    row = row + 1
    month_day = month_day + 1

print('Weekday cells updated')

# clear all input cells
cell_list = sheet.range('C3:AZ36') # can't figure out variable end column, for now it clears up to 50 item columns/items

for cell in cell_list:
    cell.value = ''

sheet.update_cells(cell_list)
print('Cells cleared out')
