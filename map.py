            # [demo,rep]
repVSdemo = {'New Jersey': [0,0], 'Rhode Island': [0,0], 'Massachusetts': [0,0], 'Connecticut': [0,0],
             'Maryland': [0,0], 'New York': [0,0],'Delaware': [0,0], 'Florida': [0,0], 'Ohio': [0,0],
             'Pennsylvania': [0,0], 'Illinois': [0,0], 'California': [0,0], 'Hawaii': [0,0], 'Virginia': [0,0],
             'Michigan': [0,0], 'Indiana': [0,0], 'North Carolina': [0,0], 'Georgia': [0,0], 'Tennessee': [0,0],
             'New Hampshire': [0,0], 'South Carolina': [0,0], 'Louisiana': [0,0], 'Kentucky': [0,0],
             'Wisconsin': [0,0], 'Washington': [0,0], 'Alabama': [0,0], 'Missouri': [0,0], 'Texas': [0,0],
             'West Virginia': [0,0], 'Vermont': [0,0], 'Minnesota': [0,0], 'Mississippi': [0,0], 'Iowa': [0,0],
             'Arkansas': [0,0], 'Oklahoma': [0,0], 'Arizona': [0,0], 'Colorado': [0,0], 'Maine': [0,0],
             'Oregon': [0,0], 'Kansas': [0,0], 'Utah': [0,0], 'Nebraska': [0,0], 'Nevada': [0,0], 'Idaho': [0,0],
             'New Mexico': [0,0], 'South Dakota': [0,0], 'North Dakota': [0,0], 'Montana': [0,0], 'Wyoming': [0,0],
             'Alaska': [0,0]}

states = {'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California', 'CO': 'Colorado',
          'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida',
          'GA': 'Georgia', 'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
          'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana','ME': 'Maine',
          'MD': 'Maryland', 'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi',
          'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska',
          'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York',
          'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma',
          'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota',
          'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
          'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'}


import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
fileName = "President_Project/State_Count_slow.json"

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
searchfile = open(fileName, "r")
line = searchfile.readline()
demo = False
rep = False
candidate = "nothing"
while(line):
    words = line.split()
    if(len(words) > 0):
        if len(words) < 2:
            if (words[0] == "Trump") or (words[0] == "Cruz") or (words[0] == "Kasich"):
                rep = True
                demo = False
                candidate = words[0]
                print(candidate + "      Republican")
            elif (words[0] == "Clinton") or (words[0] == "Bernie"):
                demo = True
                rep = False
                candidate = words[0]
                print(candidate + "      Democratic")

        elif len(words) == 2:
            if demo is True:
                print(candidate + "      Democratic")
                repVSdemo[states[words[0]]][0] += int(words[1])
            if rep is True:
                print(candidate + "      Republican")
                repVSdemo[states[words[0]]][1] += int(words[1])
    line = searchfile.readline()


# get state and draw the filled polygon
seg = [len(repVSdemo)]
i = 0
for j, k in repVSdemo.items():
    seg.append(map.states[state_names.index(j)])
    i += 1
    print(str(k[0]))

    if k[0] > k[1]:
        poly = Polygon(seg[i], facecolor='blue', edgecolor='blue')
        ax.add_patch(poly)
    elif k[1] > k[0]:
        poly = Polygon(seg[i], facecolor='red', edgecolor='red')
        ax.add_patch(poly)
    elif k[0] == k[1]:
        poly = Polygon(seg[i], facecolor='purple', edgecolor='purple')
        ax.add_patch(poly)



plt.show()