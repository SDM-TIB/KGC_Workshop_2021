# -*- coding: utf-8 -*-
import csv
import requests
import json
from tqdm import tqdm

def bioFalcon_call(term):
    url = "https://labs.tib.eu/sdm/biofalcon/api?mode=long"

    payload = json.dumps({
      "text": term
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()['entities_UMLS'][0][1][0]





f = open("../data/drug.csv", 'r',encoding="utf-8" )
reader = csv.reader(f,delimiter=',')
rows=list(reader)
f.close()
drugs=rows
file_header=drugs.pop(0)
file_header.append('CUI')

global count
        
for row in tqdm(drugs):
    cui=bioFalcon_call(row[1])
    row.append(cui)

    
with open("../data/drugs.csv", "w", encoding="utf-8") as output:
        writer = csv.writer(output, delimiter=',', lineterminator='\n')
        writer.writerow(file_header)
        for item in drugs:
            writer.writerow(item)
    
