import imageio
from os import listdir
from os.path import isfile, join, getmtime
import os
mypath=os.getcwd()+"/img"
filenames = [f for f in listdir(mypath) if isfile(join(mypath, f))]
path_dict={}
for i in range(len(filenames)):
   path_dict[filenames[i]]=getmtime(join(mypath,filenames[i]))
sorted_filenames=sorted(path_dict.items(),key=lambda x:x[1],reverse=False)
with imageio.get_writer('./movie.gif', mode='I', fps=10) as writer:
    for filename in sorted_filenames:
        image = imageio.imread("./img/"+filename[0])
        writer.append_data(image)

