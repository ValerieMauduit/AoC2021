class AocGraph:
    def __init__(self, paths):
        self.nodes = list(set([x[0] for x in paths] + [x[1] for x in paths]))
        sorted_paths = []
        for path in paths:
            path.sort()
            if path not in sorted_paths:
                sorted_paths += [path]
        self.paths = sorted_paths
        self.forbidden = []
        self.neighbours = {node: [] for node in self.nodes}
        for path in sorted_paths:
            self.neighbours[path[0]] += [path[1]]
            self.neighbours[path[1]] += [path[0]]

    def get_neighbours(self, node, available_only=False):
        if available_only:
            forbidden = self.forbidden
        else:
            forbidden = []
        return [neighbour for neighbour in self.neighbours[node] if neighbour not in forbidden]

    def forbid_node(self, node):
        self.forbidden += [node]


def count_paths(caves, from_node, to_node, no_loop=True, forbidden=None):
    if forbidden is None:
        forbidden = []
    if from_node == to_node:
        return 1
    else:
        total = 0
        for neighbour in caves.get_neighbours(from_node, True):
            if neighbour not in forbidden:
                if no_loop:
                    branch_forbidden = forbidden + [from_node]
                else:
                    branch_forbidden = forbidden
                total += count_paths(caves, neighbour, to_node, branch_forbidden)
        return total
