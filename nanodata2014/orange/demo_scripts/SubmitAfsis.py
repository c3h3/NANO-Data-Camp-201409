import pandas as pd
columns = "PIDN,Sand,Ca,P,pH,SOC".split(",")
df = pd.DataFrame(list(in_data),columns=columns)
submit_cols = "PIDN,Ca,P,pH,SOC,Sand".split(",")
df = df[submit_cols]
df.to_csv("afsis_hello_RFs_submit.csv",index=None)