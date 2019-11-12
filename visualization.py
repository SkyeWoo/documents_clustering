import os  # for os.path.basename
from tfidf import tfidf_matrix
from kmeans import clusters, keywords
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.manifold import MDS
import matplotlib.pyplot as plt
import pandas as pd

# dist is defined as 1 - the cosine similarity of each document. This calculation is for plotting.
dist = 1 - cosine_similarity(tfidf_matrix)
MDS()
# convert two components as we're plotting points in a two-dimensional plane
# "precomputed" because we provide a distance matrix
mds = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
pos = mds.fit_transform(dist)  # shape (n_components, n_samples)
xs, ys = pos[:, 0], pos[:, 1]

# TODO: 增加颜色以及修改名称
cluster_colors = {0: '#1b9e77', 1: '#d95f02', 2: '#7570b3', 3: '#e7298a', 4: '#66a61e', 5: '#fffa75'}

# create data frame that has the result of the MDS plus the cluster numbers and titles
kws = [i.split('\n')[0] for i in keywords]
df = pd.DataFrame(dict(x=xs, y=ys, label=clusters, title=kws))

# group by cluster
groups = df.groupby('label')

# set up plot
fig, ax = plt.subplots(figsize=(17, 9))  # set size
ax.margins(0.05)  # Optional, just adds 5% padding to the autoscaling

# iterate through groups to layer the plot
# note that I use the cluster_name and cluster_color dicts with the 'name' lookup to return the appropriate color/label
for name, group in groups:
    ax.plot(group.x, group.y, marker='o', linestyle='', ms=12, color=cluster_colors[name],
            # label=cluster_names[name],
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
for i in range(len(df)):
    ax.text(df.ix[i]['x'], df.ix[i]['y'], df.ix[i]['title'], size=8)

plt.show()  # show the plot
# plt.savefig('kmeans.png', dpi=200)