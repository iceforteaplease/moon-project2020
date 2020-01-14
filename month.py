# works

import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

name = 'testing'
sheet = client.open(name).sheet1
data = sheet.get_all_records(empty2zero=True, head=2)

# print(data)

# this gets the month number successfully
import datetime
from datetime import date

today = datetime.date.today()
str_today = str(today)
month = str_today[5:7]
month_year_for_email = str_today[5:8] + str_today[:4]
if month[0] == '0' : # makes one digit if first number is 0
    month = month[1:2]
int_month = int(month)
# print(int_month)

# gets correct weekdays for month in list, need to make month variable based on datetime
import calendar
weekdays = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
month_days = []
start_total = 0
end_total = 0
cal = calendar.Calendar(firstweekday=0)
for day in cal.itermonthdays(2020, int_month) :
    # print(x)
    if day == 0 :
        start_total = start_total + 1
    elif day == 1 :
        break

for day in cal.itermonthdays(2020, int_month) :
    if day > 0 :
        end_total = end_total + 1
# print(start_total, end_total)
start_day = weekdays[start_total]
# print('start day', start_day)
# print('====================')
day_num = 1
for each in weekdays[start_total:] : # starts loop midweek on correct day
    # print(day_num, each)
    month_days.append(each)
    day_num = day_num + 1

# gets correct number of days for the month
days_already = 7 - start_total
# print('how many already', days_already)
while days_already < end_total :
    # print('days already', days_already)
    if days_already > end_total - 7 :
        for each in weekdays[:end_total] :
            if day_num > end_total : # stops weekday loop at correct end day
                break
            # print(day_num, each)
            month_days.append(each)
            day_num = day_num + 1
    else :
        for each in weekdays :
            # print(day_num, each)
            month_days.append(each)
            day_num = day_num + 1

    days_already = days_already + 7
# print(month_days)

# update month/year cell
sheet.update_acell('A1', month_year_for_email)

# update day cells
row = 3
month_day = 0
if len(month_days) < 31 : # turn leftover days into blanks
    diff = 31 - len(month_days)
    while len(month_days) < 31 :
        month_days.append('')
# print('month days with extras', month_days)
while row < 34 :
    sheet.update_cell(row, 1, month_days[month_day])
    row = row + 1
    month_day = month_day + 1
print('Weekday cells updated')
