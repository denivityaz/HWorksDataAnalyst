import math
import psycopg2
import numpy as np
import matplotlib.pyplot as plt

con = psycopg2.connect('host=127.0.0.1 port=5543 user=postgres password=1 dbname=lab91')
cur = con.cursor()
cur.execute('select id, cluster, x, y from clustering.points;')
res = cur.fetchall()
cur.close()
con.close()

id, cluster, x, y = np.array(res).T

def assign_clusters(dist):
    for i in range(0, len(res)):
        cluster[i] = 0

    for i in range(0, len(res)):
        if cluster[i] > 0:
            continue

        c = id[i]
        for j in range(0, len(res)):
            d = math.sqrt((x[j] - x[i]) ** 2 + (y[j] - y[i]) ** 2)
            if d < dist:
                cluster[j] = c

pts = plt.scatter(x, y, s=7, c=cluster, cmap='Set1')
plt.legend(handles=pts.legend_elements()[0], title='clusters', labels=['1', '2', '3', '4', '5'])
plt.gca().set_aspect('equal')
plt.title('points clustering')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()

plt.savefig('clusters.png')
plt.show()
