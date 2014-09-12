import pandas as pd
res_df = pd.DataFrame(in_data.to_numpy()[0].astype(int))
res_df.columns = ["PassengerId","Survived"]
res_df.to_csv("titanic_svm_rbf_C10_g0p1.csv",index=False)