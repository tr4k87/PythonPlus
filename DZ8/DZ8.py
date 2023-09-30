import os
import json
import csv
import pickle

def wolk(dir):
    res = {}
    for adress, dirs, files in os.walk(dir):
        for name in files:  
            path = os.path.join(adress, name)
            size = os.path.getsize(path)
            isfile = os.path.isfile(path)
            res[name] = adress, size, isfile
        for name in dirs:
            isfile = os.path.isfile(os.path.join(adress, name))
            size_path = get_size(os.path.join(adress, name))
            res[name] = adress, isfile, size_path
            print(size_path)

    with open('wolk.txt', 'w', encoding='utf=8') as f:
        json.dump(res, f)
    with open('wolk.csv', 'w', encoding='utf=8', newline='') as f:
        dict_csv = csv.DictWriter(f, fieldnames=['Name', 'adress', 'size', 'isfile'], dialect='excel-tab')
        dict_csv.writeheader()
        dict_csv.writerows(res)

    with open('wolk.pickle', 'wb') as f:
        pickle.dump(res,f)

def get_size(dir):
    full_size = 0
    for adress, dir, names in os.walk(dir):
        for f in names:
            full_path = os.path.join(adress, f)
            full_size += os.path.getsize(full_path)
    return full_size
wolk('my_folder')