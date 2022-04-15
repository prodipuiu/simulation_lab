import matplotlib.pyplot as plt
fig = plt.figure()
#ax = fig.add_axes([0,0,1,1])
models = ['YOLOv3', 'YOLOv4-tiny']
time = [92.342000, 15.965000]
plt.bar(models,time)
plt.ylim(0,100)
plt.xlabel("Models")
plt.ylabel("milli-seconds")
plt.savefig('time_complexitycomp.png', dpi=1200)
plt.show()
#plt.show()