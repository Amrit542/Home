import json
import os

file = "data.json"

w_dir = os.path.dirname(os.path.abspath(__file__))

# r = os.path.abspath(__file__)
# print(r)
r = os.path.join(w_dir, file)




# value = data["claim_form_data"]

def ff():
    with open(r) as f:
        data = json.load(f)
    return data

ww = ff()["claim_form_data"]
print(ww)