# Bag of words.... keep the .txt files in the same directory as 20176089_bw.py 

import os
import sys
import math
import time

e = os.getcwd()
print(e)

allt = [f for f in os.listdir(e) if f.endswith('.txt') and f!='Output_BOW.txt' and f!='Output_LCS.txt' and f!='stopwords.txt']
print(allt)
print("\n")

class lists1:
        
     def lis1(self,us1, us2):
                #print(str(us1) +" and "+ str(us2), end = '   ')
                def islis():
                        ch = ['_']
                        for i in range(97, 123):
                                ch.append(chr(i))
                        for j in range(48, 58):
                                ch.append(chr(j))
                        h = ''.join(ch)
                        return h
                def check(inp):
                        y = islis()
                        g = []
                        for c in inp:
                            a = []
                            i = 0
                            for char in c:
                                    if char in y:
                                            a.append(char)
                            d = ''.join(a)
                            g.append(d)
                        return g

                def file(y):
                        data = []
                        try:
                                fh = open(y, 'r')
                        except IOError:
                                print('There is no file with that name to open')
                                return 0
                        else:
                                for new1 in fh:
                                        if new1!='\n':
                                                new = new1.lower()
                                                ad = new[:].split(' ')
                                                le = len(ad)
                                                for i in range(le-1):
                                                        x = ad[i]
                                                        data.append(x)
                                        p1 = ad[-1:]
                                        q1 = p1[0]
                                        if q1[-1:]!= '\n':
                                                data.append(q1)
                                        else:
                                                data.append(q1[:-1])
                                da = check(data)
                                return da
                        fh.close()
        
                path1 = us1
                x = file(path1)
                path2 = us2
                y = file(path2)
                a = set(x)
                b = set(y)
                c = a | b
                d = list(c)

                def di(x):
                        ly = x[:]
                        lh = len(ly)
                        e = []
                        d = {}
                        for i in range(0,lh):
                                c = 0
                                for k in range(0,lh):
                                        if ly[i] == ly[k]:
                                                c = c+1
                                e.append(c)
                        d = dict(zip(x,e))
                        e1 = list(d.keys())
                        f1 = list(d.values())
                        s = 0
                        for i in f1:
                                s = s + (i**2)
                        r = math.sqrt(s)
                        return d, e1, f1, r
                w, s, t, r1 = di(x)
                z, u, v, r2 = di(y)
                #print(r1)
                #print(r2)

                q = []
                for k in d:
                        if k in w.keys():
                                q.append(w[k])
                        else:
                                q.append(0)
                #print(q)

                l = []
                for k in d:
                        if k in z.keys():
                                l.append(z[k])
                        else:
                                l.append(0)
                #print(l)
                m = 0
                for i in range(len(d)):
                        m = m + (q[i]*l[i])
                #print(m)
                        
                try:
                     cos = float(((m)/(r1*r2))*100)
                     return str(us1) +" and "+ str(us2)+"    "+str(cos)+" % Plagiarised"
                except ZeroDivisionError:
                     return str(us1) +" and "+ str(us2)+"    0 % Plagiarised"
         


"""
al = len(allt)
print (time.asctime( time.localtime(time.time()) )+"\n")
for i in range(al-1):
    j = i+1
    while j<al:
        x = lis1(allt[i], allt[j])
        print(x)
        j = j+1
        print("\n")
"""
"""
x = lis1('lcs1.txt', 'lcs2.txt')
print(x)
"""


al = len(allt)
f = open('Output_BOW.txt','a+')
print (time.asctime( time.localtime(time.time()) )+"\n")
f.write("     -----***-----     "+str(time.ctime())+"     -----***-----     "+"\n")
for i in range(al-1):
        j = i+1
        while j<al:
                obj= lists1()
                x = obj.lis1(allt[i], allt[j])
                print(x)
                f.write(str(x)+"\n")
                j = j+1
                print("\n")
f.close()






"""

#To print in the upper triangle of a square matrix form. make 13th line(print statement) as a comment.


al = len(allt)
j = 0
for i in range(al):
    for j in range(al):
        if j>i:
            x = lis1(allt[i], allt[j])
            print(x, end = '      ')
        else:
            print("          ", end = '      ')
    print("\n")


"""

