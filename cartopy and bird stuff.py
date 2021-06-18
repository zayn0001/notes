import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

birddata = pd.read_csv('C:\\Users\\mishal\\Desktop\\bird_tracking.csv')

bird_names = pd.unique(birddata.bird_name)
plt.figure(figsize=(7,7))

for bird_name in bird_names:
    ix = birddata.bird_name == bird_name
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    plt.plot(x,y,'.', label = bird_name)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(loc='lower right')

plt.figure(figsize=(7,7))
ix = birddata.bird_name == 'Eric'
speed = birddata.speed_2d[ix]

#np.isnan(speed).any()      true
#np.sum(np.isnan(speed))       85

ind = np.isnan(speed)
#plt.hist(speed[~ind], bins=np.linspace(0,30,20), density = 'True')
plt.xlabel('2D speed (m/s)')
plt.ylabel('frequency')

birddata.speed_2d.plot(kind='hist', range=[0,30])


import datetime
#datetime.datetime.today()
date_str = birddata.date_time[0]
date_time = datetime.datetime.strptime(date_str[:-3], "%Y-%m-%d %H:%M:%S")

timestamps = []
for i in range(len(birddata)):
    date_str = birddata.date_time[i]
    date_time = datetime.datetime.strptime(date_str[:-3], "%Y-%m-%d %H:%M:%S")
    timestamps.append(date_time)

birddata['timestamp'] = pd.Series(timestamps, index = birddata.index)

times = birddata.timestamp[birddata.bird_name == 'Eric']
elapsed_time = [time - times[0] for time in times]

i = elapsed_time[1000] / datetime.timedelta(hours=1)
print(i)        #in hours

elapsed_days1 = np.array(elapsed_time)/ datetime.timedelta(days=1)

plt.figure(figsize=(7,7))
plt.plot(np.array(elapsed_time)/ datetime.timedelta(days=1))
plt.xlabel('Observations')
plt.ylabel('Elapsed time (days)')


next_day = 1
inds = []
daily_mean_speed = []
for (i,t) in enumerate(elapsed_days1):
    if t<next_day:
        inds.append(i)
    else:
        daily_mean_speed.append(np.mean(birddata.speed_2d[inds]))
        next_day+= 1
        inds = []
plt.figure(figsize=(8,6))
plt.plot(daily_mean_speed)
plt.xlabel('Day')
plt.ylabel('Mean speed (m/s)')
        




import cartopy.crs as ccrs
import cartopy.feature as cfeature

proj = ccrs.Mercator()
ax = plt.axes(projection= proj)
ax.set_extent((-25,20,52,10))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=':')

for name in bird_names:
    ix = birddata.bird_name == name
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    ax.plot(x,y,'.', transform=ccrs.Geodetic(), label=name)
    
plt.legend(loc='lower right')


