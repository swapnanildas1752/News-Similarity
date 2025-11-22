import pandas as pd
import json

data = []
with open("/Users/swapnanildas/Downloads/News_Category_Dataset_v3.json", "r") as f:
    for i, line in enumerate(f):
        if i >= 50000:
            break
        data.append(json.loads(line))

df = pd.DataFrame(data)

df = df[['category', 'headline', 'short_description']]

df.to_csv("Newsdatasets.csv", index=False)
print("CSV file 'Newsdatasets.csv' created successfully.")