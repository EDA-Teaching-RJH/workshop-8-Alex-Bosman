data =  [ 
		{"name":  "Rupert",  "age":  "20",  "grade":  "A"}, 
		{"name":  "Emma",  "age":  "21",  "grade":  "B"}, 
		{"name":  "Charlie",  "age":  "19",  "grade":  "C"}
]

csvData = [f"{x['name']}, {x['age']}, {x['grade']}\n" for x in data]


with open("dataFile.csv", "w") as file:
    file.writelines(csvData)

with open("dataFile.csv", "r") as file:
    outputData = file.readlines()
    for x in outputData[0]:
        formatData[x] = dict()