import os
import sys
import math
import time

e = os.getcwd()

allt = [f for f in os.listdir(e) if f.endswith('.txt') and f!='Output_BOW.txt' and f!='Output_LCS.txt' and f!='stopwords.txt']
print(allt)
print("\n")

class lists1:
    def lis1(self, us1, us2):
        #list to verify
        #print(str(z) +" and "+ str(n)+"  ", end = '')
        def islis():
            ch = ['_']
            for i in range(97, 123):
                ch.append(chr(i))
            for j in range(48, 58):
                ch.append(chr(j))
            h = ''.join(ch)
            return h
        def check(inp):                                                            #removing all delimiters
            y = islis()
            g = []
            for c in inp:
                a = []
                i = 0
                for char in c:
                    if char in y:
                        a.append(char)
                d = ''.join(a)
                f = len(d)
                if f>0:
                    g.append(d)
            return g

        def file(y):                                                                     #1st def --- file content -> list
            data = []
            try:
                fh = open(y, 'r')
            except IOError:
                print('There is no file with that name to open')
                return 0
            else:
                si = 0
                c = 0
                for new1 in fh:
                    si = si + len(new1)
                    c = c+1
                    if new1!='\n':
                        new = new1.lower()
                        ad = new.split(' ')
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
                pi = si-(c-1)
                da = check(data)
                return da
                fh.close()
   
        path1 = us1
        x = file(path1)
        maz = len(x)

        q1 = 0                                                                          #file length after removing delimiters and spaces
        for k in x:
            q1 = q1 + len(k)       
        path2 = us2
        y = file(path2)
        q2 = 0
        for cha in y:
            q2 = q2 + len(cha)
        q3 = q1+q2    
        zi = []    
        x1 = len(x)
        y1 = len(y)    
        xo = []
        yo = []
        j = 0
    
        for i in range(x1):                                                                  #list of total words in both files
            for j in range(y1):
                if x[i]==y[j] and (j not in yo):
                    zi.append(x[i])
                    xo.append(i)
                    yo.append(j)
                    break
        lr = []
        for i in range(len(xo)):
            lr.append(x[xo[i]])
        lq = []
        for i in range(len(yo)):
            lq.append(y[yo[i]])    
        le = len(zi)
        gi = []
    
        if le>2:
            j = 0                                                                  #longest commoon substring
            mq = []
            g = []
            mo = 0
            for k in range(len(xo)):
                #print(k, j)
                if xo[k]==yo[j]:
                    mq.append(x[xo[k]])
                
                    j = j+1
                else:
                
                    g.append(mq)
                    mq = []
                    if (k+1)<len(xo):
                        if xo[(k+1)]==yo[j]:
                            mq.append(x[xo[k]])
                            k = k+1
                        elif xo[k]==yo[j+1]:
                            mq.append(x[xo[k]])
                            j = j+2
                        else:
                            k = k+1
                            j = j+1
                        
            g.append(mq)        
            f = []        
            for a in g:
                ly = 0
                for b in a:
                    ly = ly+len(b)
                f.append(ly)           
            li = max(f)        
        elif le==2:
            a = len(zi[0])
            b = len(zi[1])
            if (xo[1]== (xo[0]+1)):
                if yo[1]==(yo[0]+1):
                    li = a+b
            else:
                if a>b:
                    gi = zi[0]
                    li = a
                else:
                    gi = zi[1]
                    li = b
        elif le == 1:
            gi = zi[0]
            li = len(zi[0])
        else:
            gi = []
            li = 0
        if x == y:
            fi = 100
        else:
            fi = (((li)*2)/q3)*100

        return str(us1) +" and "+ str(us2)+"    "+str(fi)+" % Plagiarised"
        
al = len(allt)
f = open('Output_LCS.txt','a+')
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
al = len(allt)
#print(al)
for i in range(al-1):
    j = i+1
    while j<al:
        x = lis1(allt[i], allt[j])
        print(x)
        j = j+1
        print("\n")
"""       
#lis1('lcs1.txt', 'lcs2.txt')

"""

#To print in the upper triangle of a square matrix form.


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
