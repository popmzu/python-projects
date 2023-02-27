import requests
import json

print("Welcome to the AA Calculator\n"
    "Please select one of the following options:\n"
    "1. Have a look at the previous entry.\n""2. Make a new entry.\n"
    "3. Close the program.\n")

entry = input("Enter entry: " )

#loop for as long entry is not 3

#while entry != "3":

if entry == "2":
    print("How many meters have you travelled?")

    meters_travelled = int(input("Enter distance: "))
    conversion = meters_travelled/1000
    print(conversion,"kilometers\n")

    print("Here is the list of vehicles, please select one:\n"
    "1. Hatcback\n""2. SUV\n""3. Sport Car")

    import requests

    AA_Calc = 'https://raw.githubusercontent.com/tyrone0501/AA-Petrol-Price/main/Cars.json'
    response = requests.get(AA_Calc)
    response_json = response.json()

    siteresponse1 = response_json["Hatchback"]

    siteresponse2 = response_json["SUV"]

    siteresponse3 = response_json["SportsCar"]


    vehicle_type = int(input(""))

    if vehicle_type == 1:
        cost = conversion*siteresponse1
    elif vehicle_type == 2:
        cost = conversion*siteresponse2
    elif vehicle_type == 3:
        cost = conversion*siteresponse3
    else:
        print("invalid vehicle selection.")

    print("Please type your description of where you travelled and why")
    description = input("")

    vehicle_rates = {
        "Cost" : cost,
        "KM" : conversion,
        "Description" : description
        }


    with open("data.json", "w") as f:
        json.dump(vehicle_rates, f)

if entry == "1":
    print("Here is the previous entry: ")
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
        print("The amount of kilometers is " + str(data.get("KM")) + "KM")
        print("Your total cost is " + "R" + str(data.get("Cost")))
        print("Your description: " + str(data.get("Description")))
    except Exception:
        print("No previous entries were found!")