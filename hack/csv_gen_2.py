from pandas.io.json import json_normalize
import pandas as pd
f=open("ISIC_0000000", "r")
something=f.read()
print(something)
df = pd.DataFrame.from_dict(json_normalize(something),orient='columns')
print(df)