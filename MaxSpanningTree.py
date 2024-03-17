def find_best_edges(graph, weights):
    best_edges = dict()
    for vertex in graph:
        best_edge = graph[vertex][0]
        for incoming_edge in graph[vertex]:
            if (weights[incoming_edge] > weights[best_edge]):
                best_edge = incoming_edge
        best_edges[vertex] = best_edge
    return best_edges


def update_weights(graph, weights, best_edges):
    for vertex in graph:
        best_weight = weights[best_edges[vertex]]
        for edge in graph[vertex]:
            weights[edge] -= best_weight
    return weights


def find_first_cycle(bottom_up_graph):
    visited = set()
    branch_visited = set()
    for vertex in bottom_up_graph:
        if vertex in visited:
            continue
        branch_visited.add(vertex)
        head = vertex
        while len(branch_visited) > 0:
            visited.add(head)
            incoming_edge = bottom_up_graph[head]
            head = incoming_edge.split()[0]
            if head in branch_visited:
                return branch_visited
            if head in visited:
                break
            if head == "root":
                break
            branch_visited.add(head)
        branch_visited.clear()
    return None


def fix_cycle(graph: dict, cycle: set, weights):
    best_edge = graph[next(iter(cycle))][0]
    for vertex in cycle:
        for incoming_edge in graph[vertex]:
            head = incoming_edge.split()[0]
            if head in cycle:
                continue
            if weights[incoming_edge] > weights[best_edge]:
                best_edge = incoming_edge
    graph[vertex] = [best_edge]
    return graph       


def find_max_spanning_tree(graph, weights):
    tree = find_best_edges(graph,weights)
    first_cycle = find_first_cycle(tree)
    if first_cycle is None:
        return tree
    
    update_weights(graph,weights,tree)    #TODO: can put this in find_best_edges
    fix_cycle(graph,first_cycle,weights)
    return find_max_spanning_tree(graph,weights) 