import json
from sys import exit

# Reading json data
with open('json_data_twitter.json', 'r') as file:
    data = json.loads(file.read())

list_of_names = []
for k in data:
    list_of_names.append(k)

# Iteration/Loops
def getKeyData(key):
    list_of_keys = []
    json_data = {}
    for name in list_of_names:
        json_data[name] = {}
        for version in data[name]:
            try:
                list_of_keys.append(data[name][version][key])
                avg_value = sum(list_of_keys) / len(list_of_keys)
                json_data[name][version] = {}
                json_data[name][version]["Value"] = data[name][version][key]
            except Exception:
                print("That key doesn't exist!")

        json_data[name]["Avg. Value"] = float("{:.2f}".format(avg_value))
        list_of_keys = []
    print(json.dumps(json_data))

run = True
while run:
    key_to_get = input("1. Get the key Success_Count\n2. Get the key Error_Count\n3. Get the key Request_Count\n4. Exit\n")

    # Check to see what data to get
    if key_to_get == "1":
        getKeyData("Success_Count")
    elif key_to_get == "2":
        getKeyData("Error_Count")
    elif key_to_get == "3":
        getKeyData("Request_Count")
    elif key_to_get == "4":
        run = False

exit()