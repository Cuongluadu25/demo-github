import pandas as pd
import numpy as np

dt= pd.read_csv("d:\TTNT\du_lieu_tao(4).csv")

p = np.array([dt['can nang'], dt['do chin']])
t = np.array([dt['t1'],dt['t2']])

r = 2 # sonoron dau ra
s = 2 # so thanh phan dau vao
m = 8 # so mau de tranning

a = np.array([[0,0]])
w = np.array([[1,0],[2,8]])
b = np.array([[-6, -9]])
k = 0

p=p.T
t=t.T

while True:
    d = True
    k +=1
    print("Lan lap thu ", k )
    for i in range(m):
        x = np.array([p[i]])
        n = w.dot(x.T) + b.T
        for j in range(s):
            if(n[j][0]>=0):
                a[0][j] = 1
            else:
                a[0][j] = 0
        if(np.array_equal([t[i]], a)==False):
            e = t[i] - a
            e1 = e.T
            w = w + e1.dot(x)
            b = b + e
            d = False
    print("w = ", w)
    print("b = ", b)
    if d==True:
        break
#kiem tra test
f = np.array([[9,3]])
n = w.dot(f.T) + b.T
for j in range(s):
    if(n[j][0]>=0):
                a[0][j] = 1
    else:
                a[0][j] = 0
print("lop cua f la : ", a)