#---------------------------------------
datne=open("txt/admin.txt")
datne2=open("txt/viesis.txt")
sum=0
num=[]
#---------------------------------------
for rinda in datne:
  dati= rinda.split(" ")
  sum += int(dati[2]) #ADMIN SUMMA GADIEM
  vid = sum / 2 #ADMIN APREKINATS VIDEJAIS
  minv=min(dati[:3]) #1 ADMIN MIN GADI
  num.append(minv) #2 ADMIN MIN GADI
  maxv=max(dati[2]) #1 ADMIN MAX GADI
  num.append(maxv) #2 ADMIN MAX GADI
#---------------------------------------
#VID ADMIN VECUMS
print("vid=",vid)
#JAUNAKAIS ADMIN
print("Jaunakais=",min(num)) 
#VECAKAIS ADMIN
print("Vecakais=",max(num))
#---------------------------------------
#CIK IR ADMINI, CIK IR VIESI?
with open("txt/admin.txt") as fp:
  for count, line in enumerate(fp):
    pass
print("Adminu skaits=",count+1)

with datne2 as fp:
  for count, line in enumerate(fp):
    pass
print("Viesu skaits=",count+1)
#---------------------------------------