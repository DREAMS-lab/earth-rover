import os

directory = r'/root/Desktop/wheelie/'
names = ['spectrometer', 'odometery',]
for filename in os.listdir(directory):
    if filename.endswith(".bag") or filename.endswith(".bag.active"):
        for idx, topic in enumerate(['/data', '/mavros/odometry/out']):
            cmd = 'rostopic echo -b %s/%s %s -p > %s-%s.csv' % (directory, filename, topic, names[idx], filename)
            print(cmd)
            os.system(cmd)
    else:
        continue


