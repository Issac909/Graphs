
def earliest_ancestor(ancestors, starting_node):
    fam_tree = dict()
    
    for pair in ancestors:
        relative = pair[1]
        if relative not in fam_tree:
            fam_tree[relative] = set()
            fam_tree[relative].add(pair[0])
            
        else:
            fam_tree[relative].add(pair[0])
            
    relatives = list(fam_tree.keys())
    
    parents = set()
    
    for pair in ancestors:
        parents.add(pair[0])
    
    parents = list(parents)
    
    if starting_node not in relatives:
        return -1
    
    marked = list()
    marked.append(starting_node)
    
    seen = set()
    rents_ids = list()
    path = list()

    while len(marked) > 0:
        # Sorting s forces the smallest value on any particular traversed level to go last
        marked.sort()
        current = marked.pop()

        if current not in seen:
            seen.add(current)
            path.append(current)
            
            if current in relatives:
                rents_ids = list(fam_tree[current])
                for ids in rents_ids:
                    marked.append(ids)
    return path[-1]


            