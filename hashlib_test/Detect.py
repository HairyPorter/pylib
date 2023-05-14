import os
from py2neo import Graph,Node,Relationship,NodeMatcher,RelationshipMatcher
import hashlib
import time

time_start=time.time()

check_root=os.getcwd()
print("检测目录：\t",check_root)
allfiles=[]
for root,dirs,files in os.walk(".",topdown=False):
    # print(root)
    for name in files:
        name_t=os.path.join(root,name)
        allfiles.append(name_t)
        # print(name_t)

# print(allfiles)


files_name_sha256=[]
for filedir in allfiles:
    with open(filedir,'rb') as f:
        file_sha256=hashlib.sha256(f.read()).hexdigest()
        files_name_sha256.append((file_sha256,filedir))

# print(files_name_sha256)




g = Graph('http://192.168.100.32:7474', auth=('neo4j','neo4j'), name='neo4j')

nodes=NodeMatcher(g)
mw_nodes=[]
for sha256,n in files_name_sha256:
    node_single= nodes.match("Malware",sha256=sha256).first()
    # print(node_single)
    if node_single:
        mw_nodes.append(node_single)

# print(mw_nodes)
mw_nodes_dict_list=[]
# 如果是空的
if not mw_nodes:
    print('-'*10,"未检测到疑似恶意代码",'-'*10)
else:
    print('-'*10,"检测到疑似恶意代码",'-'*10)
    for n in mw_nodes:
        
        # 前3个
        mw_node_dict=dict(n)
        # 路径
        fns_dict=dict(files_name_sha256)
        mw_node_dict['local_dir']=fns_dict[mw_node_dict['sha256']]
        # magic，filetype
        end_nodes=[]
        mw_node_dict['magic']=set()
        mw_node_dict['file_type']=set()
        relationships_all=RelationshipMatcher(g).match([n]).all()
        for rel in relationships_all:
            end_nodes.append(rel.end_node)
        for end_n in end_nodes:
            if(set(end_n.labels)=={'Magic'}):
                mw_node_dict['magic'].add(end_n['name'])
            if(set(end_n.labels)=={'FileType'}):
                mw_node_dict['file_type'].add(end_n['name'])

        # print(mw_node_dict)

        mw_nodes_dict_list.append(mw_node_dict)


    print('发现',len(mw_nodes_dict_list),'个疑似恶意代码')
    for n in mw_nodes_dict_list:
        print(str(n).replace(',',',\n'))
    
time_end=time.time()
print('检测时间',time_end-time_start,'s')
input('按Enter键退出')



