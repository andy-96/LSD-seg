import os
root = '/home/chenandy/data/lsd-seg'
cmd = 'python train.py --dataroot ' + root + ' --gpu 0 --method LSD'
os.system(cmd)
