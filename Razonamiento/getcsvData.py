import pandas as pd

df = pd.read_csv("datos.csv")
for _ in range(3):
    for segm in range(2, 7, 2):
        print("Segm"+str(segm))
        df = df.sort_values(by="segm"+str(segm), ascending=False)
        print(df.iloc[_+1]["ID"])
    print()

#print(df[["segm2", "segm4", "segm6"]], '\n')