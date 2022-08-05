import json

data = '{"var1":"harry", "var2":56}'
print(data)

parsed = json.loads(data)
# print(parsed)
print(parsed['var1'])
# print(type(parsed))

data2 = {
    "channel_name": "CodeWithHarry",
    "cars": ['bmw', 'audi a8', 'ferrari'],
    "fridge": ('roti', 540),
    "isbad": False
}
# json.dumps() kya karta hai ki vo aapka data2 le lega  aur kya karega ki ek javascript compatible object mujhe return karega !
jscomp = json.dumps(data2)
print(jscomp)


# loads() takes in a string and returns a json object. json. dumps() takes in a json object and returns a string