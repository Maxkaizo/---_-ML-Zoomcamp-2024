## WIP

import pickle

input_file = 'model_C=1.0_T=0.7.bin'

with open(input_file, 'rb') as f_in: 
    dv, model = pickle.load(f_in)

student = {
  "resident_seq_number": 1,
  "sex": "male",
  "age": 13,
  "school_type": "public",
  "school_grade": "primary",
  "dropout": 0,
  "em_hw_projects": True,
  "em_tests": True,
  "em_multimedia_evidence": False,
  "em_class_participation": False,
  "em_class_work": True,
  "em_class_attendance": False,
  "em_other": False,
  "em_no_evaluation": False,
  "et_smartphone": True,
  "et_laptop": False,
  "et_desktop_pc": False,
  "et_tablet": False,
  "et_flat_screen": False,
  "et_didactic_material": False,
  "et_other": False,
  "et_none": False,
  "hr_mother": True,
  "hr_father": False,
  "hr_female_relative": False,
  "hr_male_relative": False,
  "hr_female_non_relative": False,
  "hr_male_non_relative": False,
  "hr_none": False,
  "help_hours": 0.0,
  "expected_grade": "bachelors",
  "ap_stressed": True,
  "ap_depressed": False,
  "ap_academic_desperation": False,
  "ap_social_difficulty": False,
  "ap_no_issues": False,
  "economic_participation": "studying_other",
  "work_hours": 0.0,
  "economic_consequences": "no_consequence",
  "state_number": 24,
  "period_type": "year",
  "period_number": 6.0
}


X = dv.transform([student])
y_pred = model.predict_proba(X)[0, 1]

print('input:', student)
print('output:', y_pred.round(4))
