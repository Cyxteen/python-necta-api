from bs4 import BeautifulSoup
import requests
import json

# url = 'http://127.0.0.1/necta/index2.html'
# url = 'http://8.8.8.8'

# response = requests.get(url, timeout=3)

# soup = BeautifulSoup(response.text, 'html.parser')
# main function
def details(year, school_number, exam_number, exam_type):
    
    url = ''
    year = int(year)
    school_number = school_number.lower()
    exam_number = exam_number.lower()
    exam_type = exam_type.lower()

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
        # checks for response from the site if no then terminate after 3 tries
        response = requests.get(url, timeout=3)
        soup = BeautifulSoup(response.text, 'html.parser')
        # check for 200 response code if yes page is ok else 'not found'
        if response.status_code == 200:
            # calculates all students that sat for the exam
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
            # finish = soup.find_all('tr')[6].font.text[6:]
            
            total_students = total_students + 5 + total_absentees
            # print(total_absentees)
            while i <= total_students:
                if exam_number == soup.find_all('tr')[i].font.text:
                    # print("inside")
                    get_details(exam_number, i, soup)
                    break
                else:
                    if i == total_students:
                        print('Exam number does not exist')
                        break
                    i+=1

        else:
            print("webpage not found")
    
    # checks for connection(internet) error
    except requests.ConnectionError:
        print(url)
        print('internet connection is down')

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

    print(return_json['school_name'])

exam_number = '0072'
school_number = 'S0110'
year = 2019
exam_type = 'acsee'
details(year, school_number, exam_number, exam_type)
