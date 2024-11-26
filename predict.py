## WIP

import pickle

input_file = 'G:\Mi unidad\###_ ML Zoomcamp 2024\model_C=1.0_T=0.7.bin'

with open(input_file, 'rb') as f_in: 
    dv, model = pickle.load(f_in)
