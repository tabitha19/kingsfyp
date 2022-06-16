import os
def Segment():
	f=open('SecureKey.txt', 'r') #read key
	con=f.read()
	f.close()
	count=0
	for char in con:
		count+=1
	k=0
	limit=int(count/5)
	for i in range(0,5):
		name=str(i)+".txt"
		path=os.path.join(os.getcwd()+"\Segments",name)
		f=open(path,'w')
		ctr=0
		for j in range(k,count):
			k+=1
			f.write(con[j])
			ctr+=1
			if(ctr==limit and i!=4):
				f.close()
				break
				break
		f.close()


def getInfo():
	path1=os.getcwd() #os. getcwd() returns the absolute path of the working directory where Python is currently running as a string str
	path1=path1+"/Infos/LengthFile.txt"
	path2=os.getcwd()
	path2=path2+"/Segments/"
	mainFile=open(path1,'w')
	lisDir=os.listdir(os.path.join(os.getcwd()+"\Segments"))
	for i in lisDir:
		f=open(path2+i,'r')
		content=f.read()
		mainFile.write(str(len(content)))
		mainFile.write('::::')
		f.close()
	mainFile.close()	

def trim():
	path1=os.getcwd()
	path1=path1+"/Infos/LengthFile.txt"
	mainFile=open(path1,'r')
	content=mainFile.read()
	mainFile.close()
	content=content.split('::::')
	path2=os.getcwd()
	path2=path2+"/Segments"
	lisDir=os.listdir(path2)
	tData=""
	c=0
	i=0

	for j in lisDir:
		path3=path2+"/"+j
		f=open(path3,'r')
		data=f.read()
		f.close()
		n=int(content[i])
		tData=data[:n]
		i+=1
		open(path3,'w').close()
		f=open(path3,'w')
		f.write(tData)
		f.close()
		tData=""
			


def Merge():
	mainFile=open("Output.txt","w")
	for i in range(0,5):
		name=os.path.join(os.getcwd()+"\Segments",str(i)+".txt")
		f=open(name,"r")
		cont=f.read()
		print(cont)
		mainFile.write(cont)
		f.close()
		os.remove(name)
	mainFile.close()