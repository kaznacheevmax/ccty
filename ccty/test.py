import RegFullApp
import json

reg = RegFullApp
with open(Input_client_data.json, r, encoding=utf-8) as file:
    data = json.load(file)

count = data[app_count]
if count == 0 or count > 30:
    print("Fill correct"
          " app_count")
    exit()
else:
    for i in range(count):
        reg.full_registration_app()
        # reg.verification_app()
        if reg.verification_app():
            reg.agreement_acceptance()
