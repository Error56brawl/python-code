graph = { 
    'A': {'B'}, 'B': {'C'},
    'C': {'A'}, 
    'D': {'E'}, 'E': set() 
    }
cycle_exists = False
visited=set()
for node,child in graph.items(): 

    if node not in visited:
        visited.add(node)

        for x in child:
            if x in visited:
                cycle_exists = True
                break

    else:
        cycle_exists=True
        break

if cycle_exists:
    print("Cycle Exists")
else:
    print("Cycle Do not Exist")


