import json
import os
import sys
fol_path = input("enter the folder path: ")
ip_base = input("enter the input file base name: ")
op_base = input("enter the output file base name: ")
max_size = int(input("enter the maximum file size in bytes: "))
l = []  # to append the various json files
for i in os.listdir(fol_path):  # folder which contains json files.
    with open(i) as a:
        y = json.load(a)
        l.append(y)
dict3 = {}  # to merge all the json array of objects into single json object.
s = set()  # to store the key values of all the json files without duplicate values.
for i in l:  # to iterate over the json files.
    for j in i.keys():
        s.add(j)  # to add the unique key values.
for x in s:  # creating empty list for the unique keys of the json objects.
    dict3[x] = []
for i in l:
    for a in s:
        if a in i:
            for j in i[a]:
                temp = json.dumps(dict3)
                json_size = sys.getsizeof(temp)
                if json_size <= max_size:# to maintain the size of the jason file
                    dict3[a].append(j)
                else:
                    break
        else:
            pass
base_name = op_base + ".json"
with open(base_name, 'w') as json_file:  # to write a single file containing one json object which contains the json array of objects.
    json.dump(dict3, json_file)


