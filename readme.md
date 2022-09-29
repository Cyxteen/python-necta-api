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
    #dummy data
    exam_number = '0051'
    school_number = 's0848'
    year = 2016
    exam_type = 'csee'
    # call to action
    details(year, school_number, exam_number, exam_type)
