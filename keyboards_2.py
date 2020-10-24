import json
from testsfile_2 import tests

def generate_oneline_keyboard(arr_arr):
    raw_keyboard = {
        "one_time": True,
        "buttons": [
            [{
                "action": {
                    "type": "text",
                    "payload": '{\"button\": \"1\"}',
                    "label": comand
                },
                "color": "default"
            } for comand in arr]
            for arr in arr_arr]
        }
    
    return(json.dumps(raw_keyboard))
keys = [["фыв","фыв","ы"],
        ["ыфв","ы"],
        ["фыв","фыв","фывфы","фывфы"]
        ]
keyboard_my = (keys)
keys = [["Хочешь тест?","Оменить тест"],["Давай ещё раз",],]
test_keyboard = generate_oneline_keyboard(keys)

keys = [list(tests), ["Оменить тест"]]
keyboard_with_tests  = generate_oneline_keyboard(keys)

keys = [["Хочешь тест?","о боте"],["ping","Это я...", "other"],]
nani_keyboard = generate_oneline_keyboard(keys)

keys = [["ARTS","Музыка"],["Мемчики"]]
other_keyboard = generate_oneline_keyboard(keys)

keys = [["Котейка","Собакен"],]
pet_keyboard = generate_oneline_keyboard(keys)

#return(json.dumps(raw_keyboard))

#test_keyboard = keys 
       




