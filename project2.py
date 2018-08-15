#Team J.A.R.V.I.S. (Members:Sohel,Arghadip,Shankhadeep,Firaque)
#DrAIveX Project 1 part 2.
import pandas as pd
r= pd.read_excel("dataset.xlsx")
count_all=r.Name.count()   #con1 start and end
count_str=r[r['Department']=='CE'].count()   #con2 start
count_ce=count_str.Name
count_str1=r[r['Department']=='ME'].count()
count_me=count_str1.Name
count_ceme=count_ce+count_me
per_ceme=(count_ceme/count_all)*100#con2 end
#con3 start
l=[]
for i in r.values.tolist():
    if i[2]=='3rd' or i[2]=='4th' :
        x=0
        for j in i[0].split(' ')[0]:
            if j.lower() in i[1].split('@')[0]:
                x=1
                break
        for j in i[0].split(' ')[1]:
            if j.lower() in i[1].split('@')[0]:
                x=1
                break
        if x==0:
            l.append(i)
    else:
        l.append(i)
nd=pd.DataFrame(l,columns=["Name","Email","Year","Department"])
nd.to_excel("new.xlsx")
if len(r)==len(nd):
    k=0
else:
    k=1        
# con3 end
#output of con1,con2 and con3.
if (count_all <= 30):
    print("There is a total of %d students in DrAIveX and it can't be held with less than 30 students." % count_all)
else:
    print("Total number of students=%d" % count_all)
if (per_ceme <= 10):
    print("There are less than 10% students from CE and ME departments combined,so DrAIveX can't be held.")
else:
    print("%d% students of DrAIveX are from CE and ME department.")
if (k==0):
    print("The dataset for DrAIveX members is-\n")
    print(r)
else:
    print( "Few students from 3rd year are removed as the data of their Email ID in the dataset contains their first or last name.")
    print("New dataset for DrAIveX is-\n")
    print(nd)
#Project End . 