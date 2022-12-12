# NECTA API IN PYTHON3
`version 1.0.0`

#### currently works with secondary(csee) results and advanced(acsee) results

## USAGE
#### first clone the repository
    git clone https://github.com/Cyxteen/python-necta-api.git
    

#### install all the requirements
    python install -r requirement.txt

#### run the different functions from the folder
#### to get a single student result
    python get-student.py
#### the details are hard coded in the get-student.py(change to your preference)
    # dummy data
    exam_number = '0056'
    school_number = 's0240'
    year = 2021
    exam_type = 'csee'
    # call to action
    details(year, school_number, exam_number, exam_type)
#### the code above returns json data format
    {
        "school_name": "S0240 ST. JOSEPH GIRLS SEMINARY",
        "exam_number": "S0240/0056",
        "gender": "F",
        "division": "I",
        "division-point": " 7",
        "subjects": [
            "CIV - 'B'",
            "HIST - 'A'",
            "GEO - 'A'",
            "B/KNOWL - 'C'",
            "KISW - 'A'",
            "ENGL - 'A'",
            "PHY - 'C'",
            "CHEM - 'A'",
            "BIO - 'A'",
            "B/MATH - 'A'"
        ]
    }
#### to get a single student result
    python result-comparison.py
#### the details are hard coded in the get-student.py(change to your preference)
    # call to action
    compare('tabora boys','acsee', 2015, 2018)
#### the code above returns json data format
    {
        "2015": {
            "school name": "tabora boys",
            "registration number": "s0155",
            "division-1": 48,
            "division-2": 50,
            "division-3": 29,
            "division-4": 2,
            "division-0": 0
        },
        "2016": {
            "school name": "tabora boys",
            "registration number": "s0155",
            "division-1": 83,
            "division-2": 68,
            "division-3": 2,
            "division-4": 0,
            "division-0": 0
        },
        "2017": {
            "school name": "tabora boys",
            "registration number": "s0155",
            "division-1": 80,
            "division-2": 43,
            "division-3": 6,
            "division-4": 0,
            "division-0": 0
        },
        "2018": {
            "school name": "tabora boys",
            "registration number": "s0155",
            "division-1": 86,
            "division-2": 72,
            "division-3": 8,
            "division-4": 0,
            "division-0": 0
        }
    }
