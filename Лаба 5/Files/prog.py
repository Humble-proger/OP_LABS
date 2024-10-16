import pandas as pd
import numpy as np
import scipy.stats as sps

df = pd.read_excel(r"output.xlsx")

P4 = np.array([0.0833, 0.4167, 0.4167, 0.0833])
P5 = np.array([0.0449, 0.2004, 0.5094, 0.2004, 0.0449])
P8 = np.array([0.0141, 0.0587, 0.1431, 0.2841, 0.2841, 0.1431, 0.0587, 0.0141])
P10 = np.array([0.0077, 0.0317, 0.0748, 0.1438, 0.2420, 0.2420, 0.1438, 0.0748, 0.0317, 0.0077])
values = df.to_numpy()

left = values.min()
P_step = 0
for i in range(len(P10)):
    P_step += P10[i]
    val = np.quantile(values, P_step)
    #val = sps.norm(loc=0, scale=4).ppf(P_step)
    #print(f"[{left}, {val}]")
    print(val)
    left = val