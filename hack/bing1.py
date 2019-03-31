import json
import pprint
import pandas as pd
import glob
import csv



path = 'Descriptions/*'
files = glob.glob(path)

with open('bingcsv.csv','w',newline='') as bingcsv:
    fn = ["Filename","age_approx","anatom_site_general","benign_malignant","diagnosis","diagnosis_confirm_type","melanocytic","sex","diagnosis","localization"]
    csvw = csv.DictWriter(bingcsv, fieldnames = fn)
    csvw.writeheader()

    for name in files:
        try:
            with open(name) as f:
                datastore = json.load(f)
                if 'benign_malignant' in datastore["meta"]["clinical"]:
                    csvw.writerow({"Filename": name,
                                  "benign_malignant":datastore["meta"]["clinical"]["benign_malignant"],
                                  })
            f.close()
        except IOError as ex:
            if ex.errno != errno.EISDIR:
                raise

bingcsv.close()


'''
path = 'bingfile/*'
files = glob.glob(path)

for name in files:
    try:
        with open(name) as f:
            print(name)
            datastore = json.load(f)
            print(datastore["meta"]["clinical"]["age_approx"])
            #pprint.pprint (datastore)
            #print(datastore["meta"]["acquisition"])
        f.close()
    except IOError as ex:
        if ex.errno != errno.EISDIR:
            raise

print(datastore["meta"]["acquisition"]["image_type"])
'''


'''     
ISIC_000000
| age_approx
| anatom_site_general
| benign_malignant
| diagnosis
| diagnosis_confirm_type
| melanocytic
| sex
| diagnosis (from unstructured)
| localisation (from unstructured)
'''




'''
with open ("bingfile/ISIC_0000000",'r') as f:
    datastore = json.load(f)


f.close()

pprint.pprint (datastore)

df_struct = pd.read_json("bingfile/ISIC_0000000")
#print(df_struct)

print(datastore["meta"]["acquisition"])
'''
