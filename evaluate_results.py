import pandas as pd

df = pd.read_csv('./testing_result_dataset.csv')

score = 0

for row in df.itertuples():
    label = row.label
    result = row.negativity_label

    if label == 'REAL' and (result == 'Trustable.' or result == 'Likely Trustable.'):
        score += 1
    if label == 'FAKE' and (result == 'Likely Fake.' or result == 'Most Likely Fake.' or result == 'Fake.'):
        score += 1


print(f"Score: {(score/len(df))*100}")