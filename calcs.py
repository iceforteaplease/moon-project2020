# works

import gspread
from oauth2client.service_account import ServiceAccountCredentials

def count_day(day):
    count = 0
    for dic in data:
        if dic['day'] == day:
            count += 1
    return count

def each_days_total(day, which) :
    if dic['day'] == day:
        which[food] += dic[food]
    return which

def average(day, count) :
    for food in food_items :
        av = day[food] / count
        string = str(av)
        slice = string[:4]
        if len(slice) == 3 : # makes each output 4 characters
            slice = slice + '0'
        day[food] = slice
    return day

def output(full_weekday, day_dic) :
    print('  ' + full_weekday + ' - ')
    print('    ', end='')
    for k,v in day_dic.items() :
        print(k + ':', v, '| ', end='')
    print('\n')

# connect to google sheet
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

name = 'testing'
sheet = client.open(name).sheet1
data = sheet.get_all_records(empty2zero=True, head=2)

# print(data)

food_items = []

sun = {} # turn these into objects to loop later rather than repeating code down below
mon = {}
tue = {}
wed = {}
thu = {}
fri = {}
sat = {}

# gets food items in list
for key,value in data[0].items() :
    food_items.append(key)
food_items.pop(0)

# sets up dictionaries for each day with correct food items set to zero
for food in food_items :
    sun.update({food: 0}) # loop through ojects mentioned above?
    mon.update({food: 0})
    tue.update({food: 0})
    wed.update({food: 0})
    thu.update({food: 0})
    fri.update({food: 0})
    sat.update({food: 0})

sun_count = count_day('sun')
mon_count = count_day('mon')
tue_count = count_day('tue')
wed_count = count_day('wed')
thu_count = count_day('thu')
fri_count = count_day('fri')
sat_count = count_day('sat')

for food in food_items :
    for dic in data :
        each_days_total('sun', sun)
        each_days_total('mon', mon)
        each_days_total('tue', tue)
        each_days_total('wed', wed)
        each_days_total('thu', thu)
        each_days_total('fri', fri)
        each_days_total('sat', sat)

average(sun, sun_count) # could probably make this into loop if sun/mon/tue etc were in an object
average(mon, mon_count)
average(tue, tue_count)
average(wed, wed_count)
average(thu, thu_count)
average(fri, fri_count)
average(sat, sat_count)

# calculates total waste
total_waste = 0
for dic in data:
    for key,value in dic.items():
        try:
            num = int(value)
        except:
            continue
        total_waste = total_waste + num

# outputs
print('======================')
print('Total Waste:', total_waste, 'items')
print('======================')

print('Averages: \n')
output('Sunday', sun) # same as above, could make loop if sun/mon etc were in an object
output('Monday', mon)
output('Tuesday', tue)
output('Wednesday', wed)
output('Thursday', thu)
output('Friday', fri)
output('Saturday', sat)
