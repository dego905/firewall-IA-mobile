import sys
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

ip = sys.argv[1]
proc = sys.argv[2]

df = pd.read_csv('.conn_raw.csv', header=None, names=["time", "ip", "proc"])
df['ip_code'] = df['ip'].apply(lambda x: sum([int(i) for i in x.split('.') if i.isdigit()]) if '.' in x else 0)
df['proc_len'] = df['proc'].apply(len)
X = df[['ip_code', 'proc_len']].values

if len(X) < 3:
open(".decision.log", "a").write("normal\n")
sys.exit()

model = KMeans(n_clusters=2, random_state=0).fit(X)
latest = np.array([[df['ip_code'].iloc[-1], df['proc_len'].iloc[-1]]])
predict = model.predict(latest)[0]
center = model.cluster_centers_[predict]
dist = np.linalg.norm(latest - center)

if dist > 20:
open(".decision.log", "a").write("anomalo\n")
else:
open(".decision.log", "a").write("normal\n")
