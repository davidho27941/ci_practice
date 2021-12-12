from module import psudo_data_generator
from module import psudo_chi2_calculator



def test_psudo_data_generator():
    MODEL_TEST = 'A'
    if MODEL_TEST == 'A':
        target = psudo_data_generator(MODEL_TEST)
        if target.shape[1] == 2:
            return True
        else: 
            return False

def test_psudo_chi2_calculator():
    MODEL_TEST = 'A'
    if MODEL_TEST == 'A':
        DATA_TEST = psudo_data_generator(MODEL_TEST)
        target_CHI2 = psudo_chi2_calculator(MODEL_TEST, DATA_TEST)
        if target_CHI2 > 0:
            return True
        else:
            return False
        
