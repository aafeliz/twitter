
popdensity = {
'New Jersey': 438.00,
'Rhode Island': 387.35,
'Massachusetts': 312.68,
'Connecticut': 271.40,
'Maryland': 209.23,
'New York': 155.18,
'Delaware': 154.87,
'Florida': 114.43,
'Ohio': 107.05,
'Pennsylvania': 105.80,
'Illinois': 86.27,
'California': 83.85,
'Hawaii': 72.83,
'Virginia': 69.03,
'Michigan': 67.55,
'Indiana': 65.46,
'North Carolina': 63.80,
'Georgia': 54.59,
'Tennessee': 53.29,
'New Hampshire': 53.20,
'South Carolina': 51.45,
'Louisiana': 39.61,
'Kentucky': 39.28,
'Wisconsin': 38.13,
'Washington': 34.20,
'Alabama': 33.84,
'Missouri': 31.36,
'Texas': 30.75,
'West Virginia': 29.00,
'Vermont': 25.41,
'Minnesota': 23.86,
'Mississippi': 23.42,
'Iowa': 20.22,
'Arkansas': 19.82,
'Oklahoma': 19.40,
'Arizona': 17.43,
'Colorado': 16.01,
'Maine': 15.95,
'Oregon': 13.76,
'Kansas': 12.69,
'Utah': 10.50,
'Nebraska': 8.60,
'Nevada': 7.03,
'Idaho': 6.04,
'New Mexico': 5.79,
'South Dakota': 3.84,
'North Dakota': 3.59,
'Montana': 2.39,
'Wyoming': 1.96,
'Alaska': 0.42}

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

# create the map
map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=33,lat_2=45,lon_0=-95)

# load the shapefile, use the name 'states'
map.readshapefile('MapData/st99_d00', name='states', drawbounds=True)

# collect the state names from the shapefile attributes so we can
# look up the shape obect for a state by it's name
state_names = []
for shape_dict in map.states_info:
    state_names.append(shape_dict['NAME'])

ax = plt.gca() # get current axes instance

# get Texas and draw the filled polygon
seg = map.states[state_names.index('Texas')]
poly = Polygon(seg, facecolor='red',edgecolor='red')
ax.add_patch(poly)

plt.show()