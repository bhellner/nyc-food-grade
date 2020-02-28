import pandas
import matplotlib.pyplot as plt
import seaborn as sns
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon

street_map = gpd.read_file('/Users/Brittney/Desktop/sh/nyu_2451_34522.shp')
#street_map = gpd.read_file('/Users/Brittney/Desktop/shape/nyu_2451_34510.shp')
#street_map = gpd.read_file('/Users/Brittney/Desktop/shapefile/geo_export_b26025d3-6ab4-477a-8234-ad60cb10a1b5.shp')
fig,ax = plt.subplots(figsize = (8,8))
street_map.plot(ax = ax)
plt.show()

df = pandas.read_csv('/Users/Brittney/Desktop/NYCdata.csv')
crs = {'init': 'epsg:4326'}
df.head()

geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
geometry[:3]

geo_df = gpd.GeoDataFrame(df, crs=crs, geometry = geometry)
print(geo_df.head())
#geo_df.plot()
#plt.xlim(-74.4,-73.6)
#plt.ylim(40.4,41.0)
#plt.show()

fig,ax = plt.subplots(figsize = (8,8))
street_map.plot(ax=ax, alpha = 0.4, color = 'grey')
geo_df[geo_df['GRADE'] == 'Z'].plot(ax=ax, markersize=5, color = 'blue', marker = 'o', label = 'Z')
#geo_df[geo_df['CRITICAL FLAG'] == 'Y'].plot(ax=ax, markersize=5, color = 'blue', marker = 'o', label = 'Critical')
#geo_df[geo_df['CRITICAL FLAG'] == 'N'].plot(ax=ax, markersize=5, color = 'red', marker = '^', label = 'Not Critical')
plt.legend(prop={'size':8})
plt.xlim(-74.06,-73.90)
plt.ylim(40.675,40.875)
plt.show()