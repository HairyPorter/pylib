# import py2neo as p2n
from py2neo import Graph,Node,Relationship

g = Graph('http://192.168.100.42:7474', auth=('neo4j','neo4j'), name='neo4j')
tn1=Node("Person",name="test_node_1")
tn2=Node("Person",name="test_node_2")
# g.create(tn1)
# g.create(tn2)
node_1_call_node_2 = Relationship(tn1,'CALL',tn2)
node_1_call_node_2['count'] = 1
node_2_call_node_1 = Relationship(tn2,'CALL',tn1)
node_2_call_node_1['count'] = 2
g.create(node_1_call_node_2)
g.create(node_2_call_node_1)
