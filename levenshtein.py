import networkx as nx 
import matplotlib.pyplot as plt
#Basic algorithm using dynamic programming to find the Levenshtein distance between two strings:  
def LevenshteinDistance(str1, str2):
    # Create a table to store results of subproblems
    d = [[0 for x in range(len(str2)+1)] for x in range(len(str1)+1)]
 
    # Fill d[][] in bottom up manner
    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            if i == 0:
                d[i][j] = j    # Min. operations = j
            elif j == 0:
                d[i][j] = i    # Min. operations = i
            #check if last characters of the strings match 
            elif str1[i-1] == str2[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = 1 + min( d[i][j-1],        # Insert
                                   d[i-1][j],        # Delete
                                   d[i-1][j-1])   # Substitute
    return d[len(str1)][len(str2)]

str1 = "hello"
str2 = "shallow"

print(LevenshteinDistance(str1, str2))

def initial_row(word):
    return range(len(word)+1)
def step(word, row, c, distance):
    new_row = [row[0]+1]
    for i in range(len(row)-1):
        if word[i]==c:
            new_row.append(row[i])
        else:
            new_row.append(1 + min(new_row[i], 
                                   row[i], 
                                   row[i+1]))
    return [min(x, distance+1) for x in new_row]

def transitions(word, row, distance):
    l = []
    for i in range(len(word)):
        if row[i] <= distance:
            l.append(word[i])
    return set(l)

def is_match(word, row, distance):
    return row[-1] <= distance


index = 0 
states = {}
trans = []
match = []


def build_DFA(row,word,distance):
    k = tuple(row) 
    if k in states: 
        return states[k]
    global index
    i = index
    index+= 1
    states[k] = i
    if is_match(word,row,distance): 
        #match stores the end states where the two word match (no more than a specific distance from each other )
        match.append(i)
    for t in transitions(word,row,distance) | set(['*']):
        #calculate new state from the current state 
        newstate = step(word, row, t, distance)
        #continue to check from that new state
        j = build_DFA(newstate,word,distance)
        #trans stores the transitions we have from step to step 
        trans.append((i, j, t))
    return i

build_DFA(initial_row('hot'),'hot',1)
trans.sort(key=lambda (i,j,t): i)
print trans 
#print match

#print states
#print counter
d={}
for k in trans:
    d[(k[0],k[1])]=k[2]
print d

G = nx.DiGraph()
for x in range(0,trans[-1][0]+1):
    G.add_node(x)
for k in trans:
    G.add_edge(k[0],k[1],weight=1)
color_map=[]
for node in G:
    if node in match:
        color_map.append('red')
    else:
        color_map.append('blue')
pos=nx.spring_layout(G)
nx.draw(G,pos, with_labels=True, node_color=color_map)
labels = nx.get_edge_attributes(G,'weight')
#nx.draw_networkx_nodes(G,pos,with_labels=True)
nx.draw_networkx_edge_labels(G,pos,d,label_pos=0.3)
nx.draw_networkx_labels(G,pos)
plt.show()

