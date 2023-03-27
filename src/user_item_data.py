import pandas as pd
import json

with open('../old data/australian_users_items.json') as f:
    lines = f.readlines()

# adjusting json to correct format with double quotes
revision = '[' + ','.join(lines) + ']'
revision = revision.replace("'", '"')

with open('user_item_data_fixed.json', 'w') as json_file:
    json.dump(revision, json_file)
df = pd.DataFrame(revision)
print(df.head())


