"""
----------------------------------------
        PYTHON API Version 1.0.0        
----------------------------------------
works with results from 2014
"""
# imports
from bs4 import BeautifulSoup
import requests
import os
import json

# gets the current path the file is located
curr_path = os.path.dirname(os.path.abspath(__file__))
# example 2018-2020
# start_year = begining of the year to compare(2018)
# end_year = last year to compare with(2020)

def compare(name_of_school: str, type_of_exam: str, start_year: int, end_year = 0):
        
        name_of_school = name_of_school.lower()
        type_of_exam = type_of_exam.lower()
        # theres no other year to compare
        if end_year == 0:
                file = f'{curr_path}\\total-schools\{type_of_exam.upper()}-{start_year}.text'
                # print(file)
                file2 = open(file, 'r')
                for word in file2:
                        if name_of_school.upper() == word[5:].strip():
                                school_reg_number = (word[0:5]).lower()
                                break
                        else:
                                school_reg_number = ''
                if school_reg_number is not "":
                        data_json = {}
                        new_year = start_year
                        # check if exam level is advanced level or secondary level
                        if type_of_exam == "acsee":
                                if new_year == 2022:
                                        url = f"https://matokeo.necta.go.tz/acsee2022/results/{school_reg_number}.htm"
                                else:
                                        url = f"https://onlinesys.necta.go.tz/results/{new_year}/acsee/results/{school_reg_number}.htm"

                        elif type_of_exam == "csee":
                                if new_year > 2014:
                                        url = f"https://onlinesys.necta.go.tz/results/{new_year}/csee/results/{school_reg_number}.htm" 
                                else:
                                        url = f"https://onlinesys.necta.go.tz/results/{new_year}/csee/{school_reg_number}.htm"
                        
                        print(url)
                        response = requests.get(url)
                        soup = BeautifulSoup(response.text, 'html.parser')
                        # check for 200 response code if yes page is ok else 'not found'
                        if response.status_code == 200:
                                # calculates all students that sat for the exam
                        # for school results later than >2014 (2019, 20 and 21)
                                if type_of_exam =='csee':
                                        if new_year >= 2019:
                                                # performance summary in table format
                                                division_one = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][1]).text)
                                                division_two = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][2]).text)
                                                division_three = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][3]).text)
                                                division_four = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][4]).text)
                                                division_zero = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][5]).text)

                                                total_students = division_one + division_two + division_three + division_four + division_zero

                                                # calculates number of all absentees
                                                total_absentees = len(soup.body.findAll(text='ABS'))

                                                # calculates number of all students who withdrew
                                                total_withheld = len(soup.body.findAll(text='*W'))
                                                
                                                i=6
                                                # extracts the first exam number
                                                first_exam_number = soup.find_all('tr')[i].font.text
                                                total_students = total_students + 5 + total_absentees + total_withheld
                                                
                                        # for school results later than >2014 (2015, 16, 17 and 18)
                                        elif new_year > 2014:
                                                # performance summary in paragraph format
                                                division_one = int(soup.find('h3').find('p').find('h3').text.split(' ')[2].strip(';'))
                                                division_two = int(soup.find('h3').find('p').find('h3').text.split(' ')[6].strip(';'))
                                                division_three = int(soup.find('h3').find('p').find('h3').text.split(' ')[10].strip(';'))
                                                division_four = int(soup.find('h3').find('p').find('h3').text.split(' ')[14].strip(';'))
                                                division_zero = int(soup.find('h3').find('p').find('h3').text.split(' ')[18].strip(';'))
                                                
                                                # total number of all students(without absentees and withheld)
                                                total_students = division_one + division_two + division_three + division_four + division_zero
                                                
                                                # calculates number of all absentees
                                                total_absentees = len(soup.body.findAll(text='ABS'))

                                                # calculates number of all students who withdrew
                                                total_withheld = len(soup.body.findAll(text='*W'))
                                                
                                                i=1
                                                # extracts the first exam number
                                                first_exam_number = soup.find_all('tr')[i].font.text

                                                # total number of all students(with absentees and withheld)
                                                total_students = total_students + total_withheld + total_absentees
                                        # for advanced results
                                elif type_of_exam == 'acsee':
                                        if new_year >= 2020:
                                                # performance summary in table format
                                                division_one = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][1]).text)
                                                division_two = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][2]).text)
                                                division_three = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][3]).text)
                                                division_four = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][4]).text)
                                                division_zero = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][5]).text)

                                                total_students = division_one + division_two + division_three + division_four + division_zero

                                                # calculates number of all absentees
                                                total_absentees = len(soup.body.findAll(text='ABS'))
                                                
                                                # calculates number of all students who withdrew
                                                total_withheld = len(soup.body.findAll(text='*W'))
                                                
                                                i=6
                                                # extracts the first exam number
                                                first_exam_number = soup.find_all('tr')[i].font.text
                                                total_students = total_students + 5 + total_absentees + total_withheld
                                                
                                                # for school results later than >2013 (2014, 15, 16, 17 and 18)
                                        elif new_year > 2013:
                                                # performance summary in paragraph format
                                                division_one = int(soup.find('h3').find('p').find('h3').text.split(' ')[2].strip(';'))
                                                division_two = int(soup.find('h3').find('p').find('h3').text.split(' ')[6].strip(';'))
                                                division_three = int(soup.find('h3').find('p').find('h3').text.split(' ')[10].strip(';'))
                                                division_four = int(soup.find('h3').find('p').find('h3').text.split(' ')[14].strip(';'))
                                                division_zero = int(soup.find('h3').find('p').find('h3').text.split(' ')[18].strip(';'))
                                                
                                                # total number of all students(without absentees and withheld)
                                                total_students = division_one + division_two + division_three + division_four + division_zero
                                                
                                                # calculates number of all absentees
                                                total_absentees = len(soup.body.findAll(text='ABS'))

                                                # calculates number of all students who withdrew
                                                total_withheld = len(soup.body.findAll(text='*W'))
                                                
                                                i=1
                                                # extracts the first exam number
                                                first_exam_number = soup.find_all('tr')[i].font.text

                                                # total number of all students(with absentees and withheld)
                                                total_students = total_students + total_withheld + total_absentees
                                data = {
                                        new_year : {
                                        'school name' : name_of_school,
                                        'registration number' : school_reg_number, 
                                        'division-1' : division_one,
                                        'division-2' : division_two,
                                        'division-3' : division_three,
                                        'division-4' : division_four,
                                        'division-0' : division_zero}
                                        }         
                                data_json.update(data)

                                
                        print(json.dumps(data_json, indent=3))
                else:
                        print('school number not present in this new_year')
        else:
                # theres a gap btn the years selected
                diff = end_year - start_year
                year = start_year

                data_json = {}
                for i in range(diff+1):
                        new_year = (year + i)
                        file = f'{curr_path}\\total-schools\{type_of_exam.upper()}-{new_year}.text'
                        file2 = open(file, 'r')
                        for word in file2:
                                if name_of_school.upper() == word[5:].strip():
                                        school_reg_number = (word[0:5]).lower()
                                        break
                                else:
                                        school_reg_number = ''

                        if school_reg_number is not "":
                                # check if exam level is advanced level or secondary level
                                if type_of_exam == "acsee":
                                        if new_year == 2022:
                                                url = f"https://matokeo.necta.go.tz/acsee2022/results/{school_reg_number}.htm"
                                        else:
                                                url = f"https://onlinesys.necta.go.tz/results/{new_year}/acsee/results/{school_reg_number}.htm"

                                elif type_of_exam == "csee":
                                        if new_year > 2014:
                                                url = f"https://onlinesys.necta.go.tz/results/{new_year}/csee/results/{school_reg_number}.htm" 
                                        else:
                                                url = f"https://onlinesys.necta.go.tz/results/{new_year}/csee/{school_reg_number}.htm"
                                try:
                                        response = requests.get(url)
                                        soup = BeautifulSoup(response.text, 'html.parser')
                                        # check for 200 response code if yes page is ok else 'not found'
                                        if response.status_code == 200:
                                                # calculates all students that sat for the exam
                                                # for school results later than >2014 (2019, 20 and 21)
                                                if type_of_exam =='csee':
                                                        if new_year >= 2020:
                                                                # performance summary in table format
                                                                division_one = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][1]).text)
                                                                division_two = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][2]).text)
                                                                division_three = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][3]).text)
                                                                division_four = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][4]).text)
                                                                division_zero = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][5]).text)

                                                                total_students = division_one + division_two + division_three + division_four + division_zero

                                                                # calculates number of all absentees
                                                                total_absentees = len(soup.body.findAll(text='ABS'))

                                                                # calculates number of all students who withdrew
                                                                total_withheld = len(soup.body.findAll(text='*W'))
                                                                
                                                                p=6
                                                                # extracts the first exam number
                                                                first_exam_number = soup.find_all('tr')[p].font.text
                                                                total_students = total_students + 5 + total_absentees + total_withheld
                                                                
                                                        # for school results later than >2014 (2015, 16, 17 and 18)
                                                        elif new_year > 2014:
                                                                # performance summary in paragraph format
                                                                division_one = int(soup.find('h3').find('p').find('h3').text.split(' ')[2].strip(';'))
                                                                division_two = int(soup.find('h3').find('p').find('h3').text.split(' ')[6].strip(';'))
                                                                division_three = int(soup.find('h3').find('p').find('h3').text.split(' ')[10].strip(';'))
                                                                division_four = int(soup.find('h3').find('p').find('h3').text.split(' ')[14].strip(';'))
                                                                division_zero = int(soup.find('h3').find('p').find('h3').text.split(' ')[18].strip(';'))
                                                                
                                                                # total number of all students(without absentees and withheld)
                                                                total_students = division_one + division_two + division_three + division_four + division_zero
                                                                
                                                                # calculates number of all absentees
                                                                total_absentees = len(soup.body.findAll(text='ABS'))

                                                                # calculates number of all students who withdrew
                                                                total_withheld = len(soup.body.findAll(text='*W'))
                                                                
                                                                p=1
                                                                # extracts the first exam number
                                                                first_exam_number = soup.find_all('tr')[p].font.text

                                                                # total number of all students(with absentees and withheld)
                                                                total_students = total_students + total_withheld + total_absentees
                                                        # for advanced results
                                                elif type_of_exam == 'acsee':
                                                        if new_year > 2019:
                                                                # performance summary in table format
                                                                division_one = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][1]).text)
                                                                division_two = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][2]).text)
                                                                division_three = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][3]).text)
                                                                division_four = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][4]).text)
                                                                division_zero = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][5]).text)

                                                                total_students = division_one + division_two + division_three + division_four + division_zero

                                                                # calculates number of all absentees
                                                                total_absentees = len(soup.body.findAll(text='ABS'))
                                                                
                                                                # calculates number of all students who withdrew
                                                                total_withheld = len(soup.body.findAll(text='*W'))
                                                                
                                                                p=6
                                                                # extracts the first exam number
                                                                first_exam_number = soup.find_all('tr')[p].font.text
                                                                total_students = total_students + 5 + total_absentees + total_withheld
                                                                
                                                                # for school results later than >2013 (2014, 15, 16, 17 and 18)
                                                        elif new_year > 2013:
                                                                # performance summary in paragraph format
                                                                division_one = int(soup.find('h3').find('p').find('h3').text.split(' ')[2].strip(';'))
                                                                division_two = int(soup.find('h3').find('p').find('h3').text.split(' ')[6].strip(';'))
                                                                division_three = int(soup.find('h3').find('p').find('h3').text.split(' ')[10].strip(';'))
                                                                division_four = int(soup.find('h3').find('p').find('h3').text.split(' ')[14].strip(';'))
                                                                division_zero = int(soup.find('h3').find('p').find('h3').text.split(' ')[18].strip(';'))
                                                                
                                                                # total number of all students(without absentees and withheld)
                                                                total_students = division_one + division_two + division_three + division_four + division_zero
                                                                
                                                                # calculates number of all absentees
                                                                total_absentees = len(soup.body.findAll(text='ABS'))

                                                                # calculates number of all students who withdrew
                                                                total_withheld = len(soup.body.findAll(text='*W'))
                                                                
                                                                p=1
                                                                # extracts the first exam number
                                                                first_exam_number = soup.find_all('tr')[p].font.text

                                                                # total number of all students(with absentees and withheld)
                                                                total_students = total_students + total_withheld + total_absentees
                                                data = {
                                                        new_year : {
                                                        'school name' : name_of_school,
                                                        'registration number' : school_reg_number, 
                                                        'division-1' : division_one,
                                                        'division-2' : division_two,
                                                        'division-3' : division_three,
                                                        'division-4' : division_four,
                                                        'division-0' : division_zero}
                                                        }         
                                                data_json.update(data)
                                except requests.ConnectionError:
                                        print('internet connection is down')
                                
                        else:
                                print('school number not present in this new_year')
                print(json.dumps(data_json, indent = 3))

# hapa hapa
# call to action
compare('tabora boys','acsee', 2015, 2018)