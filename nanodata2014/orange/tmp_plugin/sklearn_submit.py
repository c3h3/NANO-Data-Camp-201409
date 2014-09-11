
import numpy as np
import pandas as pd

ans = in_data.to_numpy()[1]
results_df = pd.DataFrame(ans.astype(int))
results_df = results_df.reset_index()
results_df.columns = ["Id", "Solution"]
results_df.Id += 1
results_df.to_csv("sklearn_submit.csv", index=None)