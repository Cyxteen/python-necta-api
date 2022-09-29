"""
______________________________________
            PYTHON API Version 1.0.0
--------------------------------------
works with results from 2014
"""
from bs4 import BeautifulSoup
import requests
import json

# main function
def details(year, school_number, exam_number, exam_type):
    
    url = ''
    year = int(year)
    school_number = school_number.lower()
    exam_number = exam_number.lower()
    exam_type = exam_type.lower()
    exam_number = f'{school_number}/{exam_number}'

    # check if exam level is advanced level or secondary level
    if exam_type == "acsee":
        if year == 2022:
            url = f"https://matokeo.necta.go.tz/acsee2022/results/{school_number}.htm"
        else:
            url = f"https://onlinesys.necta.go.tz/results/{year}/acsee/results/{school_number}.htm"

    elif exam_type == "csee":
            if int(year) == 2021:
                url = f"https://matokeo.necta.go.tz/results2021/csee/results/{school_number}.htm"
            elif int(year) > 2014:
                url = f"https://onlinesys.necta.go.tz/results/{year}/csee/results/{school_number}.htm" 
            else:
                url = f"https://onlinesys.necta.go.tz/results/{year}/csee/{school_number}.htm"
    try:
        # url = 'http://127.0.0.1/necta/index2.html'
        # checks for response from the site if no then terminate after 3 tries
        response = requests.get(url, timeout=3)
        soup = BeautifulSoup(response.text, 'html.parser')
        # check for 200 response code if yes page is ok else 'not found'
        if response.status_code == 200:
            # calculates all students that sat for the exam
            # for school results later than >2014 (2019, 20 and 21)
            if year > 2019:
                range_1 = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][1]).text)
                range_2 = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][2]).text)
                range_3 = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][3]).text)
                range_4 = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][4]).text)
                range_5 = int((soup.find('table').find_all('tr')[3].find_all('p')[1:][5]).text)

                total_students = range_1 + range_2 + range_3 + range_4 + range_5

                # calculates number of all absentees
                total_absentees = len(soup.body.findAll(text='ABS'))
                
                i=6
                # extracts the first exam number
                first_exam_number = soup.find_all('tr')[i].font.text
                total_students = total_students + 5 + total_absentees
            
            # for school results later than >2015 (2016, 17 and 18)
            elif year > 2015:
                range_1 = int(soup.find('h3').find('p').find('h3').text.split(' ')[2].strip(';'))
                range_2 = int(soup.find('h3').find('p').find('h3').text.split(' ')[6].strip(';'))
                range_3 = int(soup.find('h3').find('p').find('h3').text.split(' ')[10].strip(';'))
                range_4 = int(soup.find('h3').find('p').find('h3').text.split(' ')[14].strip(';'))
                range_5 = int(soup.find('h3').find('p').find('h3').text.split(' ')[18].strip(';'))
            
                # total number of all students(without absentees and withheld)
                total_students = range_1 + range_2 + range_3 + range_4 + range_5
                
                # calculates number of all absentees
                total_absentees = len(soup.body.findAll(text='ABS'))

                # calculates number of all students who withdrew
                total_withheld = len(soup.body.findAll(text='*W'))
                
                i=1
                # extracts the first exam number
                first_exam_number = soup.find_all('tr')[i].font.text

                # total number of all students(with absentees and withheld)
                total_students = total_students + total_withheld + total_absentees

            while i <= total_students:
                if exam_number == (soup.find_all('tr')[i].font.text).lower():
                    get_details(exam_number, i, soup)
                    break
                else:
                    if i == total_students:
                        print('Exam number does not exist')
                        break
                    i+=1

        else:
            print(url)
            print("webpage not found")
    
    # checks for connection(internet) error
    except requests.ConnectionError:
        print('internet connection is down')
    
    except requests.exceptions.ReadTimeout:
        print('Not Found: The requested URL was not found on this server')

def get_details(exam_number, i, soup):

    uncleaned_school_name = soup.select_one("h3").p
    cleaned_one = soup.find_all('h3')[0].p.text

    # cleaned school name
    cleaned_school_name = cleaned_one.split('\n')[0].strip()

    name = soup.find_all('tr')[i]
    student_exam_number = name.find_all('p')[0].text
    student_gender = name.find_all('p')[1].text
    student_points = name.find_all('p')[2].text
    student_division = name.find_all('p')[3].text
    subject_length = len(name.find_all('p')[4].text.split('  '))

    # creates subjects list for storing subjects
    subjects = []
    for a in range(subject_length-1):
        # print(name.find_all('p')[4].text.split('  ')[a].strip(' '))
        subjects.append(name.find_all('p')[4].text.split('  ')[a].strip(' '))
    
    return_json = {
        'school_name' : cleaned_school_name,
        'exam_number' :  student_exam_number,
        'gender' : student_gender,
        'division' : student_division,
        'subjects': subjects
    }
    
    # converts the python dictionary into a json file
    jsonify_data = json.dumps(return_json)
    print(return_json)

exam_number = '0051'
school_number = 's0848'
year = 2016
exam_type = 'csee'
details(year, school_number, exam_number, exam_type)
