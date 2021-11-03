import csv

'''
 normal_rounds_data and alternate_bloon_rounds_data are a list of dictionaries. 
 The index is the round number minus 1 (e.g. Round 10 is index 9 in =the list).

 Each element is a dictionary in this format:
 {
     'RBE/Damage': int (the number of red bloons if the round was converted to all red bloons),
     'Money from Bloons': int (the amount of money made from popping every bloon),
     'Money from Income' : int (the amount of money made in between rounds)
 }
'''

normal_rounds_data = []
alternate_bloon_rounds_data = []

with open("../data/rounds_normal.csv", newline="") as normal_rounds:
    file_reader = csv.reader(normal_rounds, delimiter=",", quotechar="|")
    headers = []
    
    row_num = 0
    for row in file_reader:
        if row_num != 0:
            normal_rounds_data.append({})
        for element in row:
            if row_num == 0:
                headers.append(element)
            else:
                for header_num in range(1, len(headers)):
                    normal_rounds_data[row_num-1][headers[header_num]] = int(row[header_num])
        row_num+=1

with open("../data/rounds_abr.csv", newline="") as alternate_bloon_rounds:
    file_reader = csv.reader(alternate_bloon_rounds, delimiter=",", quotechar="|")
    headers = []
    
    row_num = 0
    for row in file_reader:
        if row_num != 0:
            alternate_bloon_rounds_data.append({})
        for element in row:
            if row_num == 0:
                headers.append(element)
            else:
                for header_num in range(1, len(headers)):
                    alternate_bloon_rounds_data[row_num-1][headers[header_num]] = int(row[header_num])
        row_num+=1

print(normal_rounds_data)
print(alternate_bloon_rounds_data)