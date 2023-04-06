import numpy as np
import matplotlib.pyplot as plt
import csv

Bz = []
Dst = []
Time = []

"""
La première étape consiste à ouvrir le document CSV contenant nos 
données et à les récupérer. Celui-ci a été réduit pour ne compter 
les observations du 23/08 au 02/09/2018 afin d'épurer un peu le graphique.
"""
with open("OMNI2_H0_MRG1HR_36448.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    dir(reader)
    t = -2
    for row in reader:
        Bz.append(float(row["Bz"]))
        Dst.append(float(row["Dst"]))
        t += 1
    Time = np.array(range(t))

"""
On retire les deux dernières mesures du champ magnétique et les deux 
premières du Dst pour faire coïncider leur minima. C'est comme si on 
décalait le champ magnétique 2h vers l'avant.
"""        
Bz.pop(-2)
Bz.pop(-1)
Dst.pop(1)
Dst.pop(0)

"""
Ensuite, il suffit de plotter les données. On se donne une intuition de
progression dans le temps grâce à un code couleur et à des pointillés.
"""        
plt.scatter(Bz, Dst, c = Time, alpha = 0.75)
plt.colorbar(ticks = [0, Time[-1]])
plt.plot(Bz, Dst, "--", alpha = 0.25)
plt.xlabel("Bz (nT)")
plt.ylabel("Dst (nT)")
plt.title("Dst en fonction du champ magnétique\n interplanétaire vertical 2h plus tôt")
plt.show
        
#%% ANIMATION   
"""
Pour encore mieux visualiser la relation entre les deux variables, 
regardons le déplacement d'un point sur le plot pendant l'orage magnétique. 
"""
 
import matplotlib.animation as animation

"""Format légèrement différent"""
fig, ax = plt.subplots()
fig.set_figheight(8)
fig.set_figwidth(10)

"""Fond sur lequel le point va se déplacer"""
plt.scatter(Bz, Dst, c = Time, alpha = 0.75)
plt.plot(Bz, Dst, "--", alpha = 0.25)
plt.xlabel("Bz (nT)", fontsize = 20)
plt.ylabel("Dst (nT)", fontsize = 20)
plt.title("Dst en fonction du champ magnétique\n interplanétaire vertical 2h plus tôt", fontsize = 24)
    
"""Animation"""
ims = []
for i in range(t) :
    im = ax.plot(Bz[i], Dst[i], "ro", animated = True)
    ims.append(im)

ani = animation.ArtistAnimation(fig, ims, interval = 5)
ani.save("anim.gif")        
plt.show        
        
        
        
        
        
        
        
        
        
        
        