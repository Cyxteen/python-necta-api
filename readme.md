# NECTA API IN PYTHON3
### `version 1.0.0`

#### currently works with secondary(csee) results and advanced(acsee) results

## USAGE
#### first clone the repository
    git clone https://github.com/Cyxteen/python-necta-api.git

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
