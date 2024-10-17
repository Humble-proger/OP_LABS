import pandas as pd
import numpy as np
import scipy.stats as sps

df = pd.read_excel(r"output2.xlsx")
#Оптимальные вероятности нормального закона
P4 = np.array([0.0833, 0.4167, 0.4167, 0.0833])
P5 = np.array([0.0449, 0.2004, 0.5094, 0.2004, 0.0449])
P8 = np.array([0.0141, 0.0587, 0.1431, 0.2841, 0.2841, 0.1431, 0.0587, 0.0141])
P10 = np.array([0.0077, 0.0317, 0.0748, 0.1438, 0.2420, 0.2420, 0.1438, 0.0748, 0.0317, 0.0077])
#Оптимальные вероятности для логистического закона
P10_logist = np.array([0.0153, 0.0510, 0.0946, 0.1441, 0.1950, 0.1950, 0.1441, 0.0946, 0.0510, 0.0153])
#Коэффициенты для нормального закона
mu4 = np.array([0.224374, 0.551252, 0.224374])
mu5 = np.array([0.108579, 0.391421, 0.391421, 0.108579])
mu8 = np.array([0.029871, 0.096902, 0.216939, 0.312575, 0.216939, 0.096902, 0.029871])
mu10 = np.array([0.016187, 0.050213, 0.107748, 0.196679, 0.258345, 0.196679, 0.107748, 0.050213, 0.016187])

sigma4 = np.array([-0.361428, 0, 0.361428])
sigma5 = np.array([-0.201360, -0.229872, 0.229872, 0.20136])
sigma8 = np.array([-0.070411, -0.147147, -0.166972, 0, 0.166972, 0.147147, 0.070411])
sigma10 = np.array([-0.040995, -0.091463, -0.132388, -0.123812, 0, 0.123812, 0.132388, 0.091463, 0.040995])

# Коэфициенты для логистического закона
mu10_logist = np.array([0.002907, 0.027965, 0.098968, 0.220560, 0.299200, 0.220560, 0.098968, 0.027965, 0.002907])
sigma10_logist = np.array([-0.043187, -0.114395, -0.176647, -0.161259, 0, 0.161259, 0.176647, 0.114395, 0.043187])

#Коэфициенты для распределения Коши
x0 = np.array([-0.030901, -0.042682, 0.080792, 0.292814, 0.399953, 0.292814, 0.080792, -0.042682, -0.030901])
scale_Coshi = np.array([-0.022447, -0.131427, -0.249032, -0.212590, 0, 0.212590, 0.249032, 0.131427, 0.022447])
#Оптимальные вероятности для распределения Коши
P10_Coshi = np.array([1/10 for i in range(10)])

values = df.to_numpy()
left = values.min()
P_step = 0
quantile_list = np.array([left])
for i in range(len(P10_Coshi)-1):
    P_step += P10_Coshi[i]
    val = np.quantile(values, P_step)
    quantile_list = np.append(quantile_list, val)
    left = val
quantile_list = np.append(quantile_list, values.max())
print(f"Quantile: {quantile_list}")

mu = 0
for i in range(len(x0)):
    mu += x0[i] * quantile_list[i+1]
scale = 0
for i in range(len(scale_Coshi)):
    scale += scale_Coshi[i] * quantile_list[i+1]
print(f"mu = {mu}, scale = {scale}")
#print(f"mu = {mu}, scale = {scale/np.sqrt(3)}")
