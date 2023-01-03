class AocMap:
    def __init__(self, data, position=None):
        self.map = [[x for x in line] for line in data]
        if position is None:
            self.x, self.y = 0, 0
        else:
            self.x, self.y = position[0], position[1]
        self.width = len(data[0])
        self.height = len(data)

    def display(self):
        for line in self.map:
            print("".join(line))

    def position(self):
        return [self.x, self.y]

    def move(self, direction):
        displacements = {
            'U': [0, -1], 'D': [0, 1], 'L': [-1, 0], 'R': [1, 0],
            'N': [0, -1], 'S': [0, 1], 'W': [-1, 0], 'E': [1, 0]
        }
        if direction in displacements:
            self.x += displacements[direction][0]
            self.y += displacements[direction][1]
            self.x = min([max([0, self.x]), self.width - 1])
            self.y = min([max([0, self.y]), self.height - 1])
        else:
            raise Exception(f"The direction {direction} is not recognized by the system.")

    def change_point(self, x, y, marker):
        self.map[y][x] = marker

    def change_points(self, coordinates, marker):
        for coord in coordinates:
            self.change_point(coord[0], coord[1], marker)

    def neighbours(self):
        return [
            self.map[y][x]
            for x in range(max([0, self.x - 1]), min([self.x + 2, self.width]))
            for y in range(max([0, self.y - 1]), min([self.y + 2, self.height]))
            if [x, y] != [self.x, self.y]
        ]

    def count_neighbours(self, marker):
        return sum([n == marker for n in self.neighbours()])