""" is like objects in JS """

myDict= {
    'david': 35,
    'jaime': 50,
    'erika': 32,
}

myDict['jaime']

myDict.get('juan', 30)
""" if juan doesnt exists returns 30 """

""" reasign """
myDict['jaime']= 20

""" new assign """
myDict['pedro']= 15

""" delete """
del myDict['jaime']

""" iterations """
for key in myDict.keys():
    print(key)

for value in myDict.values():
    print(value)

for key, value in myDict.items():
    print(key, value)


'david' in myDict 
""" true """

