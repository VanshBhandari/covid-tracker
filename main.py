import requests
import time

url = "https://api.covid19tracker.ca/summary/split"
response = requests.get(url)
js = response.json()

file = open('provincecodes.txt')
codes = file.read()
file.close()
print(codes)

province = input("enter a province code: ").upper()

while True:
    if province in codes:
        for i in js['data']:
            if i['province'] == province:
                province_data = i
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)                
        result_date = province_data['date']
        cases = province_data['total_cases']
        deaths = province_data['total_fatalities']
        tests = province_data['total_tests']
        vaccinations = province_data['total_vaccinations']
        vaccinated = province_data['total_vaccinated']
        result = f'{province} covid data:\ndate: {result_date}\ntime: {current_time}\ntotal cases: {cases}\ntotal deaths: {deaths}\ntotal tests : {tests} \ntotal vaccines administered: {vaccinations}\nnumber of fully vaccinated: {vaccinated}\n'
        print(result)
        with open(f"./province covid data/{province}coviddata.txt", "a") as f:
            f.write(result)
        break

    else:
        print('enter a valid province code')
        province = input("enter the province code: ").upper()
