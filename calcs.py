import gspread
from oauth2client.service_account import ServiceAccountCredentials


# scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
# client = gspread.authorize(creds)
#
# name = 'testing'
# sheet = client.open(name).sheet1
# data = sheet.get_all_records(empty2zero=True, head=2)
#
# print(data)
data = [{'day': 'wed', 'pec': 1, 'migas': 3}, {'day': 'thu', 'pec': 2, 'migas': 3}, {'day': 'fri', 'pec': 2, 'migas': 1},
 {'day': 'sat', 'pec': 1, 'migas': 4}, {'day': 'sun', 'pec': 5, 'migas': 2}, {'day': 'mon', 'pec': 5, 'migas': 1},
  {'day': 'tue', 'pec': 0, 'migas': 0}, {'day': 'wed', 'pec': 25, 'migas': 25}, {'day': 'mon', 'pec': 15, 'migas': 15}]

wed = {'pec' : 0, 'migas' : 0} # need to automate this for variablity
mon = {'pec' : 0, 'migas' : 0} # need to automate this for variablity

print(data)
def count_day(day):
    count = 0
    for each in data:
        if each['day'] == day:
            count += 1
    return count

print(count_day('wed'))

# food_items = sheet.row_values(2)
food_items = ['day', 'pec', 'migas']
food_items.pop(0)
print(food_items)
total_waste = 0

for each in data:
    for key,value in each.items():
        try:
            num = int(value)
        except:
            continue
        total_waste = total_waste + num

print('total', total_waste)
print('========')
def each_days_total(day, which) :
    if dic['day'] == day:
        which[food] += dic[food]
        #which['migas'] += each['migas'] #thinking about looping possibilities here to account for variable items
        # which['migas'] += each['migas']
        # which['potato'] += each['pec']
        # which['vegan'] += each['vegan']
    return which
print(wed)
for food in food_items :
    for dic in data :
        each_days_total('wed', wed) #assuming wed dic and food_items created automatically already
        each_days_total('mon', mon)

print('weds', wed)
print('mons', mon)
# for each in data :
#     each_days_total('wed', wed)
# print('weds', wed)
#
# for each in food_items :
#     each_days_total('wed', wed)
