import sys
import os
import math
import time
e = os.getcwd()
allt = [f for f in os.listdir(e) if f.endswith('.txt') and f!='Output_BOW.txt' and f!='Output_LCS.txt' and f!='stopwords.txt']
print(allt)
print("\n")
d1 = []

fs = open('stopwords.txt', 'r')
d1 = []
for ne in fs:
    if ne!='\n':
        if ne[-1:]!='\n':
            d1.append(ne)
        else:
            d1.append(ne[:-1])
#print(d1)
fs.close()

def file_1(d1, y1):
    fh = open(y1, 'r')           # k value
    data = []
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
            #print(data)
            print("\n")
            fi = []
            kv = []
            for i in data:
                l = []
                for k in i:
                    if k.isalnum() or k == '_':
                        l.append(k)
                fi.append(''.join(l))
            #print(fi)
            sr = []
            for k in fi:
                if k not in d1:
                    sr.append(k)
            #print(sr)
            for m in sr:
                kv.append(len(m))
            #print(kv)
            mi = min(kv)
            ma = max(kv)
            avg = (mi+ma)//2
            #print(avg)

            return sr, avg

def k_gram(kval, y1):
    y = len(y1)
    c = 0
    g = []
    f = []
    j = 0
    for k in range(y):
        j = k
        g.append(y1[j])
        c = c+1
        m = 1
        while m<kval and (j+1)<y:
            c = c+1
            g.append(y1[j+1])
            j = j+1
            if c == kval:
                f.append(g)
                g = []
                c = 0
            m = m+1
    return f




x, kval = file_1(d1, allt[0])
#print(x)
#print(kval)
al = len(allt)
for i in range(al-1):
    j = i+1
    while j<al:
        f1, tr1 = file_1(d1, allt[i])
        f2, tr2 = file_1(d1, allt[j])
        print(str(allt[i]) +" and "+ str(allt[j]), end = '   ')
        j = j+1
        #print("\n")
        
        s1 = ''.join(map(str, f1))           #list to string
        #print(s1)
        y1 = k_gram(kval, s1)
        h1 = len(y1)
        #print(y1)

        s2 = ''.join(map(str, f2))           #list to string
        #print(s2)
        y2 = k_gram(kval, s2)
        h2 = len(y2)
        #print(y2)
        h3 = h1+h2
        #print(h3)
        #------- nth prime ---------
        pn = h3+1
        pnu = 4
        pp = 2
        while pp < pn:
            if all(pnu%k!=0 for k in range(2, pnu)):
                pp = pp+1
            pnu = pnu+1
        nthp = pnu-1
        #print(nthp)


        def modp(nthp, kval, f):
            sy = 0
            wq = []
            for k in f:
        
                u = kval-1
                se = 0
                for i in k:
            
                    se = se + (ord(i)*(kval**u))
                    u = u-1
                #print(se)
                if se%kval==0:
                    wq.append(se%kval)
                    sy = sy+1
                #print(wq)
            return wq

        wq1 = modp(nthp, kval, y1)
        #print(wq1)
        wq2 = modp(nthp, kval, y2)
        #print(wq2)
     

        
        """
        #print(wq1)
        if wq1!=wq2:
            cq = 0
            for k in wq1:
    
                for m in wq2:
                    if k==m:
                        cq = cq+1

            fq = ((2*(cq)/h3)*100)
            print(fq)
        else:
            print(100)

        """

        cq = 0
        for k in wq1:
    
            for m in wq2:
                if k==m:
                    cq = cq+1
                    break
        fq = ((2*(cq)/h3)*100)
        print(fq)







