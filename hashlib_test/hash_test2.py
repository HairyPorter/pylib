from py2neo import Graph,Node,Relationship,NodeMatcher
import hashlib
import os

#takeout files
print(os.getcwd())
allfiles=[]
for root,dirs,files in os.walk(".",topdown=False):
    
    for name in files:
        allfiles.append(os.path.join(root,name))
        
#read files
files_name_sha256=[]
for filedir in allfiles:
    with open(filedir,'rb') as f:
        sha256=hashlib.sha256(f.read()).hexdigest()
        files_name_sha256.append((filedir,sha256))
print("files_name_sha256",files_name_sha256)
#sign in
g = Graph('http://192.168.100.32:7474', auth=('neo4j','neo4j'), name='neo4j')
#check files
Malfile=[]
nodes=NodeMatcher(g)

for file_name,file_sha256 in files_name_sha256:
    node_single= nodes.match("Malware",sha256=file_sha256).first()
    if node_single:
        Malfile.append((file_name,file_sha256))
    print(node_single)
print('mal::',Malfile)


