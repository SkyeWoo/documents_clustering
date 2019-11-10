import os  # for os.path.basename
from tfidf import xs, ys
from kmeans import clusters, keywords
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

# TODO: 增加颜色以及修改名称
#set up colors per clusters using a dict
cluster_colors = {0: '#1b9e77', 1: '#d95f02', 2: '#7570b3', 3: '#e7298a', 4: '#66a61e', 5: '#fffa75'}

cluster_names = {1: 'representation learning, data selection, CNN', 0: 'cross-domain, transfer learning', 2: 'network, robotics, NLP',
                 3: 'Learning, Optimization', 4: 'Search', 5: 'ML, Game Theory'}

# create data frame that has the result of the MDS plus the cluster numbers and titles
df = pd.DataFrame(dict(x=xs, y=ys, label=clusters, title=keywords))

# group by cluster
groups = df.groupby('label')

# set up plot
fig, ax = plt.subplots(figsize=(17, 9))  # set size
ax.margins(0.05)  # Optional, just adds 5% padding to the autoscaling

# iterate through groups to layer the plot
# note that I use the cluster_name and cluster_color dicts with the 'name' lookup to return the appropriate color/label
for name, group in groups:
    ax.plot(group.x, group.y, marker='o', linestyle='', ms=12,
            label=cluster_names[name], color=cluster_colors[name],
            mec='none')
    ax.set_aspect('auto')
    ax.tick_params( \
        axis='x',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        bottom='off',  # ticks along the bottom edge are off
        top='off',  # ticks along the top edge are off
        labelbottom='off')
    ax.tick_params( \
        axis='y',  # changes apply to the y-axis
        which='both',  # both major and minor ticks are affected
        left='off',  # ticks along the bottom edge are off
        top='off',  # ticks along the top edge are off
        labelleft='off')

ax.legend(numpoints=1)  # show legend with only 1 point

# add label in x,y position with the label as the film title
for i in range(len(df)):
    ax.text(df.ix[i]['x'], df.ix[i]['y'], df.ix[i]['title'], size=8)

plt.show()  # show the plot

# uncomment the below to save the plot if need be
# plt.savefig('clusters_small_noaxes.png', dpi=200)