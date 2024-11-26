
# Import libraries
import pandas as pd
import warnings
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.exceptions import ConvergenceWarning
from imblearn.over_sampling import SMOTE
import pickle

# Suppress ConvergenceWarning
warnings.filterwarnings("ignore", category=ConvergenceWarning)

# Suppress ConvergenceWarning
warnings.filterwarnings("ignore", category=ConvergenceWarning)

# Data loading
df = pd.read_csv('G:\Mi unidad\###_ ML Zoomcamp 2024\enape_raw_dataset.csv')


# Filter and format 
df = df[df['EDAD'] > 2]
df = df[df['PA3_1'] == 1 ]
df = df[df['PA3_4'].notnull()]


# Replace values in PA3_2
df['SEXO'] = df['SEXO'].replace({1: 'male', 2: 'female'})

# Rename the column
df.rename(columns={'SEXO': 'sex'}, inplace=True)

# Replace values in PA3_2
df['PA3_2'] = df['PA3_2'].replace({1: 'public', 2: 'private'})

# Rename the column
df.rename(columns={'PA3_2': 'school_type'}, inplace=True)

# new value dictionary
education_levels = {
    1: 'daycare',
    2: 'preschool',
    3: 'primary',
    4: 'secondary',
    5: 'tech_school',
    6: 'high_school',
    7: 'tech_bacc',
    8: 'univ_tech',
    9: 'bachelors',
    10: 'specialty',
    11: 'masters',
    12: 'doctorate'
}

# Replace values
df['PA3_3_NIVEL'] = df['PA3_3_NIVEL'].replace(education_levels)

# Rename the column
df.rename(columns={'PA3_3_NIVEL': 'school_grade'}, inplace=True)


# Create new columns
df['period_type'] = None
df['period_number'] = None

# identify period type and number
def identify_period(row):
    if not pd.isna(row['PA3_3_BIMESTRE']):
        return 'bimester', row['PA3_3_BIMESTRE']
    elif not pd.isna(row['PA3_3_TRIMESTRE']):
        return 'trimester', row['PA3_3_TRIMESTRE']
    elif not pd.isna(row['PA3_3_CUATRIMESTRE']):
        return 'quadrimester', row['PA3_3_CUATRIMESTRE']
    elif not pd.isna(row['PA3_3_SEMESTRE']):
        return 'semester', row['PA3_3_SEMESTRE']
    elif not pd.isna(row['PA3_3_ANIO']):
        return 'year', row['PA3_3_ANIO']
    elif not pd.isna(row['PA3_3_MODMAT']):
        return 'module', row['PA3_3_MODMAT']
    else:
        return None, None

# Aplicar la función a cada fila
df[['period_type', 'period_number']] = df.apply(
    lambda row: pd.Series(identify_period(row)), axis=1
)

df.drop(columns=['PA3_3_BIMESTRE','PA3_3_TRIMESTRE','PA3_3_CUATRIMESTRE','PA3_3_SEMESTRE','PA3_3_ANIO','PA3_3_MODMAT'], inplace=True)


# new value dictionary
expected_grd = {
    1: 'primary',
    2: 'secondary',
    3: 'tech_school',
    4: 'high_school',
    5: 'tech_bacc',
    6: 'univ_tech',
    7: 'bachelors',
    8: 'masters',
    9: 'unknown'
}

# Replace values
df['PB3_15'] = df['PB3_15'].replace(expected_grd)

# Rename the column
df.rename(columns={'PB3_15': 'expected_grade'}, inplace=True)


# new value dictionary
economic_part = {
    1: 'worked_one_hour',
    2: 'sold_product',
    3: 'family_business_help',
    4: 'paid_other_work',
    5: 'apprentice_service',
    6: 'job_search',
    7: 'studying_other',
    8: 'unknown'
}

# Replace values
df['PD3_1'] = df['PD3_1'].replace(economic_part)

# Rename the column
df.rename(columns={'PD3_1': 'economic_participation'}, inplace=True)

# new value dictionary
economic_cons = {
    1: 'hire_replacement',
    2: 'economic_unsustain',
    3: 'income_decrease',
    4: 'workload_increase',
    5: 'allocate_income',
    6: 'education_stop',
    7: 'other_consequence',
    8: 'no_consequence'
}

# Replace values
df['PD3_3'] = df['PD3_3'].replace(economic_cons)

# Rename the column
df.rename(columns={'PD3_3': 'economic_consequences'}, inplace=True)

columns_to_transform = ['PA3_8_1','PA3_8_2','PA3_8_3','PA3_8_4','PA3_8_5','PA3_8_6','PA3_8_7','PA3_8_8']

# Replace Values: 1 -> True, else -> False
df[columns_to_transform] = df[columns_to_transform] == 1

column_rename_map = {
    "PA3_8_1": "em_hw_projects",
    "PA3_8_2": "em_tests",
    "PA3_8_3": "em_multimedia_evidence",
    "PA3_8_4": "em_class_participation",
    "PA3_8_5": "em_class_work",
    "PA3_8_6": "em_class_attendance",
    "PA3_8_7": "em_other",
    "PA3_8_8": "em_no_evaluation"
}

df.rename(columns=column_rename_map, inplace=True)


columns_to_transform = ['PB3_12_1','PB3_12_2','PB3_12_3','PB3_12_4','PB3_12_5','PB3_12_6','PB3_12_7','PB3_12_8']
# Replace Values: 1 -> True, else -> False
df[columns_to_transform] = df[columns_to_transform] == 1


# Rename
column_rename_map = {
    "PB3_12_1": "et_smartphone",
    "PB3_12_2": "et_laptop",
    "PB3_12_3": "et_desktop_pc",
    "PB3_12_4": "et_tablet",
    "PB3_12_5": "et_flat_screen",
    "PB3_12_6": "et_didactic_material",
    "PB3_12_7": "et_other",
    "PB3_12_8": "et_none"
}

df.rename(columns=column_rename_map, inplace=True)


columns_to_transform = ['PB3_13_1','PB3_13_2','PB3_13_3','PB3_13_4','PB3_13_5','PB3_13_6','PB3_13_7']
# Replace Values: 1 -> True, else -> False
df[columns_to_transform] = df[columns_to_transform] == 1
# Rename
column_rename_map = {
    "PB3_13_1": "hr_mother",
    "PB3_13_2": "hr_father",
    "PB3_13_3": "hr_female_relative",
    "PB3_13_4": "hr_male_relative",
    "PB3_13_5": "hr_female_non_relative",
    "PB3_13_6": "hr_male_non_relative",
    "PB3_13_7": "hr_none"
}

df.rename(columns=column_rename_map, inplace=True)

columns_to_transform = ['PB3_16_1','PB3_16_2','PB3_16_3','PB3_16_4','PB3_16_5']
# Replace Values: 1 -> True, else -> False
df[columns_to_transform] = df[columns_to_transform] == 1

# Rename
column_rename_map = {
    "PB3_16_1": "ap_stressed",
    "PB3_16_2": "ap_depressed",
    "PB3_16_3": "ap_academic_desperation",
    "PB3_16_4": "ap_social_difficulty",
    "PB3_16_5": "ap_no_issues",
}

df.rename(columns=column_rename_map, inplace=True)


# Replace Values: 1 -> True, else -> False
df['PA3_4'] = df['PA3_4'] == 1


# Renombrar la columna 'old_name' a 'new_name'
df.rename(columns={'PA3_4': 'finished_grade'}, inplace=True)


# Rename
column_rename_map = {
    "N_REN": "resident_seq_number",
    "EDAD": "age",
    "PB3_14": "help_hours",
    "PD3_2": "work_hours",
    "ENT": "state_number",
}

df.rename(columns=column_rename_map, inplace=True)


df.drop(
    columns=[
        'FOLIO',
        'P3_1',
        'P3_2',
        'PA3_1',
        'PA3_5',
        'PA3_6',
        'PA3_7_1',
        'PA3_7_2',
        'PA3_7_3',
        'PB3_1',
        'PB3_2',
        'PB3_3',
        'FILTRO_A',
        'PB3_4',
        'PB3_5_NIVEL',
        'PB3_5_BIMESTRE',
        'PB3_5_TRIMESTRE',
        'PB3_5_CUATRIMESTRE',
        'PB3_5_SEMESTRE',
        'PB3_5_ANIO',
        'PB3_5_MODMAT',
        'PB3_6',
        'PB3_7',
        'PB3_8',
        'PB3_9_1',
        'PB3_9_2',
        'PB3_9_3',
        'PB3_10_1',
        'PB3_10_2',
        'PB3_10_3',
        'PB3_10_4',
        'PB3_10_5',
        'PB3_11_1',
        'PB3_11_2',
        'PB3_11_3',
        'PB3_11_4',
        'PB3_11_5',
        'FILTRO_B',
        'FILTRO_C',
        'PC3_1',
        'PC3_2',
        'PC3_3_1',
        'PC3_3_2',
        'PC3_4',
        'PC3_5',
        'PC3_6',
        'PC3_7',
        'PC3_8',
        'FILTRO_D',
        'NIVEL_A',
        'GRADO_A',
        'NIVEL_B',
        'GRADO_B',
        'ESC',
        'FACTOR'
    ],
    inplace=True
)



numerical = list(df.select_dtypes(include=['float64', 'int64']).columns)
categorical = list(df.select_dtypes(include=['object', 'category', 'string']).columns)
boolean = list(df.select_dtypes(include=['bool']).columns)


#adjust Data types

df['period_number'] = df['period_number'].astype('string')
df['state_number'] = df['state_number'].astype('string')


# Fill missing values
df['help_hours'] = df['help_hours'].fillna(0)
df['expected_grade'] = df['expected_grade'].fillna('unknown')
df['economic_participation'] = df['economic_participation'].fillna('studying_other')
df['work_hours'] = df['work_hours'].fillna(0)
df['economic_consequences'] = df['economic_consequences'].fillna('no_consequence')

## Deal with outliers

# Replace values in help_hours
df['help_hours'] = df['help_hours'].replace({98: 0, 99: 0})

# Replace values in work_hours
df['work_hours'] = df['work_hours'].replace({99: 0})

## Convert finished_grade to dropout
df.finished_grade = (df.finished_grade == False).astype(int)
df.columns = df.columns.str.replace('finished_grade', 'dropout')

###### Model Training
### (Logistic Regression with SMOTE)

# Hyperparameters
c=1.0
t=0.7


# split dataset
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)

df_full_train = df_full_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_full_train = df_full_train.dropout.values
y_test = df_test.dropout.values

del df_full_train['dropout']
del df_test['dropout']

# Drop columns
columns_to_drop = [
    'em_hw_projects',
    'em_tests',
    ]

df_full_train = df_full_train.drop(columns=columns_to_drop, axis=1)
df_test = df_test.drop(columns=columns_to_drop, axis=1)

# Train function
def train_wsmote(df_train, y_train, C=c,cw=None):
    dict = df_train.to_dict(orient='records')

    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dict)
    
    smote = SMOTE(random_state=42)
    X_train, y_train = smote.fit_resample(X_train, y_train)

    model = LogisticRegression(C=C, max_iter=1000,class_weight=cw)
    model.fit(X_train, y_train)
    
    return dv, model


# Invoke trainning
dv, model = train_wsmote(df_full_train, y_full_train, C=1.0,cw="balanced")
output_file = f'model_C={c}_T={t}.bin'

# Export Model
with open(output_file, 'wb') as f_out: 
    pickle.dump((dv, model), f_out)

# Print conclusion
print(f'the model is saved to {output_file}')
