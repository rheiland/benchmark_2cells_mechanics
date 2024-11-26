import scipy
import matplotlib.pyplot as plt
import sys,string

argc=len(sys.argv)
print('argv=',sys.argv)
# print('argv[0]=',sys.argv[0])

# if argc < 4:
#     print(f'Usage: {sys.argv[0]} <speed> <persistence> <bias>')
#     sys.exit(-1)

# speed_str = sys.argv[1]
# persistence_str = sys.argv[2]
# bias_str = sys.argv[3]
# print('bias_str=',bias_str)


info_dict = {}
xy = []
# full_fname="paths_all.mat"
# full_fname="path_1cell.mat"
full_fname="time_dist.mat"
scipy.io.loadmat(full_fname, info_dict)
xy = info_dict['time_dist']
print("xy.shape = ",xy.shape)  # (315, 2) for 3 brief plots; each not necessarily same length

# plt.plot(xy[:,0], xy[:,1],'black', linestyle='dashed', linewidth=3.0)
# plt.plot(xy[:,0], xy[:,1],'black', linewidth=1.0)
plt.plot(xy[:,0], xy[:,1]/40.0,'black', linewidth=1.0)

plt.xlabel('Time (mins)')
plt.title(f'PhysiCell: normalized dist(cell1,cell2)')
plt.show()