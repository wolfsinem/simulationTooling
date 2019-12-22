import os
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

means = {}
is_traffic_jam = {}
path = "C:\\Users\\Martijn\\Downloads\\TouringMachines-master\\simulations\\results"

#open every txt file in 'results' folder
for filename in os.listdir(path):
    with open(path+"\\"+filename, "r") as f:
        lines = f.readlines()
        lines = [round(float(x.strip()), 2) for x in lines]
        means[filename[6:-4]] = [lines, float(filename.split("_")[1][:-4]), int(filename.split("_")[0][6:])]

#check if means are all equal to the max-speed
for mean in means:
    if all(x == means[mean][1] for x in means[mean][0]):
        is_traffic_jam[mean] = "green"
    elif any(x == means[mean][1] for x in means[mean][0]):
        is_traffic_jam[mean] = "yellow"
    else:
        is_traffic_jam[mean] = "red"

speed = [means[x][1] for x in means]
amount = [means[x][2] for x in means]
traffic_jams = list(is_traffic_jam.values())

#Plot scatter plot of speed/amount with coloring for is_traffic_jam [red,yellow,green]
plt.scatter(speed, amount, c=traffic_jams)
plt.xlabel("Snelheid (NetLogo Speed)")
plt.ylabel("Drukte (Aantal auto's)")
plt.title("File ten opzichte van snelheid en drukte")

green = mpatches.Patch(color="green", label="Geen file")
yellow = mpatches.Patch(color="yellow", label="File bij sommige runs")
red = mpatches.Patch(color="red", label="File bij alle runs")
plt.legend(handles=[green,yellow,red], bbox_to_anchor=(1.1, 1.05))

plt.show()