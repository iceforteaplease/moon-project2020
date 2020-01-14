import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

name = 'testing'
sheet = client.open(name).sheet1
data = sheet.get_all_records(empty2zero=True, head=2)

print(data)
# data = [{'day': 'wed', 'pec': 1, 'migas': 1, 'bc': 1, 'vegan': 1}, {'day': 'thu', 'pec': 2, 'migas': 2, 'bc': 2, 'vegan': 2},
# {'day': 'fri', 'pec': 3, 'migas': 3, 'bc': 3, 'vegan': 3}, {'day': 'sat', 'pec': 4, 'migas': 4, 'bc': 4, 'vegan': 4},
#  {'day': 'sun', 'pec': 5, 'migas': 5, 'bc': 5, 'vegan': 5}, {'day': 'mon', 'pec': 6, 'migas': 6, 'bc': 6, 'vegan': 6},
#   {'day': 'tue', 'pec': 7, 'migas': 7, 'bc': 7, 'vegan': 7}, {'day': 'wed', 'pec': 1, 'migas': 1, 'bc': 1, 'vegan': 1},
#    {'day': 'thu', 'pec': 2, 'migas': 2, 'bc': 2, 'vegan': 2}, {'day': 'fri', 'pec': 3, 'migas': 3, 'bc': 3, 'vegan': 3},
#     {'day': 'sat', 'pec': 4, 'migas': 4, 'bc': 4, 'vegan': 4}, {'day': 'sun', 'pec': 5, 'migas': 5, 'bc': 5, 'vegan': 5},
#      {'day': 'mon', 'pec': 6, 'migas': 6, 'bc': 6, 'vegan': 6}, {'day': 'tue', 'pec': 7, 'migas': 7, 'bc': 7, 'vegan': 7},
#       {'day': 'wed', 'pec': 1, 'migas': 1, 'bc': 1, 'vegan': 1}, {'day': 'thu', 'pec': 2, 'migas': 2, 'bc': 2, 'vegan': 2},
#        {'day': 'fri', 'pec': 3, 'migas': 3, 'bc': 3, 'vegan': 3}, {'day': 'sat', 'pec': 4, 'migas': 4, 'bc': 4, 'vegan': 4},
#         {'day': 'sun', 'pec': 5, 'migas': 5, 'bc': 5, 'vegan': 5}, {'day': 'mon', 'pec': 6, 'migas': 6, 'bc': 6, 'vegan': 6},
#          {'day': 'tue', 'pec': 7, 'migas': 7, 'bc': 7, 'vegan': 7}, {'day': 'wed', 'pec': 1, 'migas': 1, 'bc': 1, 'vegan': 1},
#           {'day': 'thu', 'pec': 2, 'migas': 2, 'bc': 2, 'vegan': 2}, {'day': 'fri', 'pec': 3, 'migas': 3, 'bc': 3, 'vegan': 3},
#            {'day': 'sat', 'pec': 4, 'migas': 4, 'bc': 4, 'vegan': 4}, {'day': 'sun', 'pec': 5, 'migas': 5, 'bc': 5, 'vegan': 5},
#             {'day': 'mon', 'pec': 6, 'migas': 6, 'bc': 6, 'vegan': 6}, {'day': 'tue', 'pec': 7, 'migas': 7, 'bc': 7, 'vegan': 7},
#              {'day': 'wed', 'pec': 1, 'migas': 1, 'bc': 1, 'vegan': 1}, {'day': 'thu', 'pec': 2, 'migas': 2, 'bc': 2, 'vegan': 2},
#               {'day': 'fri', 'pec': 3, 'migas': 3, 'bc': 3, 'vegan': 3}]
#
# print(data)
print('============')

food_items = []
sun = {} # turn these into objects to loop later rather than repeating code down below
mon = {}
tue = {}
wed = {}
thu = {}
fri = {}
sat = {}
# days = {'sun' : {}, 'mon' : {}} think about dictionary instead of variables so don't have to do seven updates


print('=============')
# gets food items in list
print('food items:', food_items)
for k,v in data[0].items() :
    food_items.append(k)
food_items.pop(0)
print('food items:', food_items)

# gets dictionaries for each day with correct food items
#next test with sheet and changing items
print(sun)
print(mon)
print(tue)
print('etc..')
for food in food_items :
    sun.update({food: 0}) # what if days dic instead of variables (above)
    mon.update({food: 0})
    tue.update({food: 0})
    wed.update({food: 0})
    thu.update({food: 0})
    fri.update({food: 0})
    sat.update({food: 0})
print(mon)
print(tue)
print(wed)
print(thu)
print(fri)
print(sat)
print(sun)
print('============')

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

sun_count = count_day('sun')
mon_count = count_day('mon')
tue_count = count_day('tue')
wed_count = count_day('wed')
thu_count = count_day('thu')
fri_count = count_day('fri')
sat_count = count_day('sat')
print('=============================')
print(sun_count)
print(mon_count)
print(tue_count)
print(wed_count)
print(thu_count)
print(fri_count)
print(sat_count)
print('==============================')

for food in food_items :
    for dic in data :
        each_days_total('sun', sun)
        each_days_total('mon', mon)
        each_days_total('tue', tue)
        each_days_total('wed', wed)
        each_days_total('thu', thu)
        each_days_total('fri', fri)
        each_days_total('sat', sat)
print('suns', sun)
print('mons', mon)
print('tues', tue)
print('weds', wed)
print('thus', thu)
print('fris', fri)
print('sats', sat)

print('===================')
print('===================')
#food_items = ['pec', 'migas', 'bc', 'vegan']
# sun_av = []
# mon_av = []
# tue_av = []
# wed_av = []
# thu_av = []
# fri_av = []
# sat_av = []
#
# big_list = []
# def average(day, count, av_lst) :
#     for food in food_items :
#         av = day[food] / count
#         string = str(av)
#         slice = string[:4]
#         if len(slice) == 3 : # makes each output 4 characters
#             slice = slice + '0'
#         av_lst.append(slice)
#         # big_list.append(av_lst)
#     return av_lst
    # beans = two_decimals(bean)
    # bacons = two_decimals(bacon)
    # migass = two_decimals(migas)
    # potatos = two_decimals(potato)
    # vegans = two_decimals(vegan)

sun_av = {'sun' : [], 'mon' : []}

def average(day, count, av_lst, strday) :
    for food in food_items :
        av = day[food] / count
        string = str(av)
        slice = string[:4]
        if len(slice) == 3 : # makes each output 4 characters
            slice = slice + '0'
        av_lst[strday].append(slice)
        # big_list.append(av_lst)
    return av_lst

def aver(day, count) :
    for food in food_items :
        av = day[food] / count
        string = str(av)
        slice = string[:4]
        if len(slice) == 3 : # makes each output 4 characters
            slice = slice + '0'
        day[food] = slice
    return day

# print('newest test hope to stop going in circles:', aver(sun, sun_count))
# print(sun)
aver(sun, sun_count) # could probably make this into loop if sun/mon/tue etc were in an object
aver(mon, mon_count)
aver(tue, tue_count)
aver(wed, wed_count)
aver(thu, thu_count)
aver(fri, fri_count)
aver(sat, sat_count)

print('Averages: \n')

# print('  Sunday - ')
# print('    ', end='')
# for k,v in sun.items() :
#     print(k + ':', v, '| ', end='')
# print('\n')
#
# print('  Monday - ')
# print('    ', end='')
# for k,v in mon.items() :
#     print(k + ':', v, '| ', end='')
# print('\n')

def output(full_weekday, day_dic) :
    print('  ' + full_weekday + ' - ')
    print('    ', end='')
    for k,v in day_dic.items() :
        print(k + ':', v, '| ', end='')
    print('\n')

output('Sunday', sun) # same as above, could make loop if sun/mon etc were in an object
output('Monday', mon)
output('Tuesday', tue)
output('Wednesday', wed)
output('Thursday', thu)
output('Friday', fri)
output('Saturday', sat)

# counter = 0
# for each in day_list :
#
#     output(each, )

# print('average tesssssst now:', average(sun, sun_count, sun_av, 'sun'))
# print('average tesssssst now:', average(mon, mon_count, sun_av, 'mon'))
#
# for each in day_list :
#     print(sun_av[each])
#
# for k,v in sun_av.items() :
#     print(k,v)

# average(mon, mon_count, mon_av)
# average(tue, tue_count, tue_av)
# average(wed, wed_count, wed_av)
# average(thu, thu_count, thu_av)
# average(fri, fri_count, fri_av)
# average(sat, sat_count, sat_av)



print('===================')
print('===================')

# total waste
total_waste = 0
for dic in data:
    for key,value in dic.items():
        try:
            num = int(value)
        except:
            continue
        total_waste = total_waste + num

print('total', total_waste)

# print('Averages - \n') #replace with days of week
# print(sun_av)
# print(mon_av)
# print('======')
# print('day -', end="")
# for each in food_items :
#     print(each, ' | ', end="")
# print('\n')
# print('sun -', end="")
# for each in sun_av :
#     print(each, ' | ', end="")
# print('\n')
