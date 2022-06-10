import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./topic/人民日报评人教版数学教材配图争议.csv')

content = df['content']
time = df['publish_time']

date = ['2022-05-26','2022-05-27','2022-05-28','2022-05-29']
hours = ['0'+str(i) if i <= 9 else str(i) for i in range(24)]
time_dict = {}
for d in date:
    for h in hours:
        time_dict[d+' '+h+':00'] = 0

for t in time:
    time_dict[t[0:-2]+'00'] += 1
print(time_dict)

x = [key.split('-')[2].split(':')[0] for key in time_dict]
x = [key.split('2022-')[1].split(':')[0] for key in time_dict]
y = [time_dict[key] for key in time_dict]

print(x)
print(y)
plt.plot(x, y, 'ro-', color='#4169E1', alpha=0.8, linewidth=1, label='一些数字')
plt.show()