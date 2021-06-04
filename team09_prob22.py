import sys

graph = {
    "A":["B"],
    "B":["A","C"], 
    "C":["B","D","I","J"],
    "D":["C","E","c","d"],
    "E":["D","F","X","W"],
    "F":["G","E"],
    "G":["F","e"],
    "H":["I"],
    "I":["H","C"],
    "J":["C","K"],
    "K":["J","L","S","T"],
    "L":["K","M"],
    "M":["L","N","b","U"],
    "N":["M","O","W","V"],
    "O":["N","P"],
    "P":["O"],
    "Q":["R"],
    "R":["Q","S"],
    "S":["R","K"],
    "T":["K","U"],
    "U":["T","V","M","a"],
    "V":["U","N"],
    "W":["N","E"],
    "X":["Y","E"],
    "Y":["X"],
    "Z":["a"],
    "a":["Z","U"],
    "b":["c","M"],
    "c":["D","b"],
    "d":["D","e"],
    "e":["d","G"],
}
morning_edge ={
    "AB":15,
    "BC":16,
    "CD":3,
    "DE":4,
    "EF":30,
    "FG":16,
    "HI":8,
    "CI":4,
    "CJ":5,
    "JK":5,
    "KL":4,
    "LM":3,
    "MN":3,
    "NO":39,
    "OP":33,
    "QR":25,
    "RS":20,
    "KS":4,
    "KT":3,
    "TU":2,
    "UV":2,
    "NV":3,
    "NW":4,
    "EW":3,
    "EX":3,
    "XY":8,
    "Za":24,
    "Ua":17,
    "MU":3,
    "Mb":2,
    "bc":2,
    "Dc":4,
    "Dd":10,
    "de":10,
    "Ge":8
}
rush_edge ={
    "AB":19,
    "BC":20,
    "CD":4,
    "DE":5,
    "EF":38,
    "FG":20,
    "HI":10,
    "CI":5,
    "CJ":7,
    "JK":7,
    "KL":5,
    "LM":4,
    "MN":4,
    "NO":49,
    "OP":42,
    "QR":32,
    "RS":25,
    "KS":5,
    "KT":4,
    "TU":3,
    "UV":3,
    "NV":4,
    "NW":5,
    "EW":4,
    "EX":4,
    "XY":10,
    "Za":30,
    "Ua":22,
    "MU":4,
    "Mb":3,
    "bc":3,
    "Dc":5,
    "Dd":13,
    "de":13,
    "Ge":10
}
evening_edge ={
    "AB":17,
    "BC":18,
    "CD":4,
    "DE":5,
    "EF":33,
    "FG":18,
    "HI":9,
    "CI":5,
    "CJ":6,
    "JK":6,
    "KL":5,
    "LM":4,
    "MN":4,
    "NO":43,
    "OP":37,
    "QR":28,
    "RS":22,
    "KS":5,
    "KT":4,
    "TU":3,
    "UV":3,
    "NV":4,
    "NW":5,
    "EW":4,
    "EX":4,
    "XY":9,
    "Za":27,
    "Ua":19,
    "MU":4,
    "Mb":3,
    "bc":3,
    "Dc":5,
    "Dd":11,
    "de":11,
    "Ge":9
}


def find_heuristic(s, e):
    if s==e:
        return 0
    seen= set()
    seen.add(s)
    q = [] 
    q.append(s)
    now_distance = 0
    while(q):
        now_distance += 1
        nodes = []
        for i in q:
            nodes += graph[i]
        q = []
        if e in nodes:
            break
        for i in nodes:
            if i not in seen:
                q.append(i)
                seen.add(i)
    return now_distance*11


def get_edge(n1, n2, edge_mode):
    c = ""
    if n1 < n2:
        c = n1 + n2
    if n2 < n1:
        c = n2 + n1
    l = 0
    if edge_mode == 0:
        l = morning_edge[c]
    if edge_mode == 1:
        l = rush_edge[c]
    if edge_mode == 2:
        l = evening_edge[c]
    return l          


def find_path(s, e, t):
    if t>=0 and t<25200:
        m = 0
    elif t>=25200 and t<68400:
        m = 1
    elif t>=68400 and t<86400:
        m = 2
    seen = set()
    seen.add(s)
    queue = []
    queue.append([s, find_heuristic(s,e)])
    while queue:
        vertex = queue.pop(0)
        seen.add(vertex[0][-1])
        temp_t = (vertex[1] - find_heuristic(vertex[0][-1],e))*60 + t
        if temp_t>=0 and temp_t<25200:
            m = 0
        elif temp_t>=25200 and temp_t<68400:
            m = 1
        elif temp_t>=68400 and temp_t<86400:
            m = 2
#         print(temp_t)
#         print(m)
        if e in seen:
            print(vertex[0])
            print(vertex[1])
            break
        nodes = graph[vertex[0][-1]]
        for i in nodes:
            if i in seen:
                continue
            
            new_path = vertex[0] + i
            new_edge = vertex[1] + get_edge(i, vertex[0][-1], m) + find_heuristic(i,e) - find_heuristic(vertex[0][-1],e)
            new_node = [new_path, new_edge]
            if len(queue) == 0:
                queue.append(new_node)
            else:
                for j in range(len(queue)):
                    if new_edge < queue[j][1]:
                        queue.insert(j, new_node)
                        break
        print(queue)


now_time = int(str(sys.argv[1])[0:2])*60*60 + int(str(sys.argv[1])[2:4])*60 + int(str(sys.argv[1])[4:6])
strat_spot = str(sys.argv[2])
end_spot = str(sys.argv[3])

find_path(strat_spot, end_spot, now_time)