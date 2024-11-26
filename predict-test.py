import requests

url = 'http://localhost:9696/predict'

student = {
  "resident_seq_number": 2,
  "sex": "male",
  "age": 26,
  "school_type": "public",
  "school_grade": "bachelors",
  "dropout": 1,
  "em_hw_projects": False,
  "em_tests": False,
  "em_multimedia_evidence": False,
  "em_class_participation": False,
  "em_class_work": False,
  "em_class_attendance": False,
  "em_other": False,
  "em_no_evaluation": False,
  "et_smartphone": False,
  "et_laptop": False,
  "et_desktop_pc": False,
  "et_tablet": False,
  "et_flat_screen": False,
  "et_didactic_material": False,
  "et_other": False,
  "et_none": False,
  "hr_mother": False,
  "hr_father": False,
  "hr_female_relative": False,
  "hr_male_relative": False,
  "hr_female_non_relative": False,
  "hr_male_non_relative": False,
  "hr_none": False,
  "help_hours": 0,
  "expected_grade": "unknown",
  "ap_stressed": False,
  "ap_depressed": False,
  "ap_academic_desperation": False,
  "ap_social_difficulty": False,
  "ap_no_issues": False,
  "economic_participation": "worked_one_hour",
  "work_hours": 60,
  "economic_consequences": "economic_unsustain",
  "state_number": 23,
  "period_type": "bimester",
  "period_number": 6
}

response = requests.post(url, json=student).json()

print(response)

if response['dropout'] == True:
    print('please reach out with the student')
else:
    print('not to worry')