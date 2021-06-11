import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

df = pd.read_csv("network_outage_history.csv")
duration = df['end'] - df['start']
plt.figure(1)
ax = duration.plot()
ax.set_xlabel("Outage index")
ax.set_ylabel("Duration of outage")

'''
Plotting outages over time:
 - grab start[0] as the start, end[-1] as the end of the x line
 - create a linspace between those two indexes with .1 second resolution (end[-1]-start[0])*10
 - start is rising edges, end is falling
'''
plt.figure(2)
x = np.linspace(df['start'].iloc[0], df['end'].iloc[-1], int((df['end'].iloc[-1]-df['start'].iloc[0])*1.5))
y = np.zeros(len(x))

df['duration'] = duration
df = df[df['duration'] > 10]

for timeindex in range(len(x)):
    print(timeindex)
    for edgeindex in range(len(df['start'])):
        if x[timeindex] > df['start'].iloc[edgeindex] and x[timeindex] < df['end'].iloc[edgeindex]:
            y[timeindex] = 1


plt.plot(x, y)
plt.xlabel("Time")
plt.ylabel("0 = Connection, 1 = No Connection")
plt.show()

