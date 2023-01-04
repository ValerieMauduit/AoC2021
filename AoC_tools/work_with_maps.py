class AocMap:
    def __init__(self, data, position=None, origin=None, numbers=False):
        if numbers:
            self.map = [[int(x) for x in line] for line in data]
        else:
            self.map = [[int(x) for x in line] for line in data]
        if origin is None:
            self.origin = [0, 0]
        else:
            self.origin = origin
        if position is None:
            self.x, self.y = self.origin[0], self.origin[1]
        else:
            self.x, self.y = position[0], position[1]
        self.width = len(data[0])
        self.height = len(data)

    @classmethod
    def empty_from_size(cls, width, height):
        data = ['.' * width for line in range(height)]
        return cls(data)

    @classmethod
    def from_coord(cls, coordinates, x_min=None, y_min=None, x_max=None, y_max=None):
        if x_min is None:
            x_min = min([coord[0] for coord in coordinates])
        if y_min is None:
            y_min = min([coord[1] for coord in coordinates])
        if x_max is None:
            x_max = max([coord[0] for coord in coordinates])
        if y_max is None:
            y_max = max([coord[1] for coord in coordinates])
        map_from_coord = cls.empty_from_size(x_max - x_min + 1, y_max - y_min + 1)
        map_from_coord.origin = [x_min, y_min]
        map_from_coord.set_points(coordinates)
        return map_from_coord

    def display(self):
        for line in self.map:
            print("".join([str(x) for x in line]))

    def get_position(self):
        return [self.x, self.y]

    def set_position(self, position):
        self.x, self.y = position[0], position[1]

    def move(self, direction):
        displacements = {
            'U': [0, -1], 'D': [0, 1], 'L': [-1, 0], 'R': [1, 0],
            'N': [0, -1], 'S': [0, 1], 'W': [-1, 0], 'E': [1, 0]
        }
        if direction in displacements:
            self.x += displacements[direction][0]
            self.y += displacements[direction][1]
            self.x = min([max([self.origin[0], self.x]), self.origin[0] + self.width - 1])
            self.y = min([max([self.origin[0], self.y]), self.origin[1] + self.height - 1])
        else:
            raise Exception(f"The direction {direction} is not recognized by the system.")

    def get_point(self, position):
        return self.map[position[1] - self.origin[1]][position[0] - self.origin[0]]

    def set_point(self, position, marker='#'):
        self.map[position[1] - self.origin[1]][position[0] - self.origin[0]] = marker

    def set_points(self, coordinates, marker='#'):
        for coord in coordinates:
            self.set_point(coord, marker)

    def get_neighbours(self, diagonals=True):
        if diagonals:
            return [
                self.map[y - self.origin[1]][x - self.origin[0]]
                for x in range(max([self.origin[0], self.x - 1]), min([self.x + 2, self.width + self.origin[0]]))
                for y in range(max([self.origin[1], self.y - 1]), min([self.y + 2, self.height + self.origin[1]]))
                if [x, y] != [self.x, self.y]
            ]
        else:
            return [
                self.map[self.y - self.origin[1]][x - self.origin[0]]
                for x in range(max([self.origin[0], self.x - 1]), min([self.x + 2, self.width + self.origin[0]]))
                if x != self.x
            ] + [
                self.map[y - self.origin[1]][self.x - self.origin[0]]
                for y in range(max([self.origin[1], self.y - 1]), min([self.y + 2, self.height + self.origin[1]]))
                if y != self.y
            ]

    def count_neighbours(self, marker, diagonals=True):
        return sum([n == marker for n in self.get_neighbours(diagonals)])
