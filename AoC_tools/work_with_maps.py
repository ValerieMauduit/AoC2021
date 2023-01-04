class AocMap:
    def __init__(self, data, position=None, origin=None, numbers=False):
        # Instantiation - Create a map from a data input of type "AoC input file data"
        # Attributes:
        # map: represents the map as a list of lists (kind of numpy array)
        #       x goes from left to right, y from top to bottom
        # origin: coordinates [x, y] of the top left point of the map
        # x, y: coordinates of the point where we are (position)
        # width, height
        if numbers:
            self.map = [[int(x) for x in line] for line in data]
        else:
            self.map = [[x for x in line] for line in data]
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
        # Constructor - Create an empty map, full of '.' defining only its width and height
        data = ['.' * width for line in range(height)]
        return cls(data)

    @classmethod
    def from_coord(cls, coordinates, x_min=None, y_min=None, x_max=None, y_max=None):
        # Constructor - Create a map made of '.' for the eempty places and '#' for all the coordinates that are entered
        # in the parameters.
        # Optional inputs: x_min, x_max, y_min, y_max, that will define the size of the map + the origin.
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
        # Method to display the map in the terminal
        for line in self.map:
            print("".join([str(x) for x in line]))

    def get_position(self):
        # Method to get the position coordinates
        return [self.x, self.y]

    def set_position(self, position):
        # Method to change x and y by indicating the new position
        self.x, self.y = position[0], position[1]

    def move(self, direction):
        # Method to change the position, but by indicating a direction (like 'U') and move for 1 cell
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
        # Method to get the value in the map for a specific set of coordinates [x, y]
        return self.map[position[1] - self.origin[1]][position[0] - self.origin[0]]

    def set_point(self, position, marker='#'):
        # Method to change the map on a specific set of coordinates [x, y]
        self.map[position[1] - self.origin[1]][position[0] - self.origin[0]] = marker

    def set_points(self, coordinates, markers='#'):
        # Method to change the map with the same marker (by default '#') on a list of coordinates.
        # If the marker option is set to a list: change the map to the values of the markers list, given in the same
        # order as the coordinates.
        if type(markers) == str:
            for coord in coordinates:
                self.set_point(coord, markers)
        else:
            for n in range(len(coordinates)):
                self.set_point(coordinates[n], markers[n])

    def get_neighbours(self, diagonals=True):
        # Method to get the values of the map for all the neighbours of the position.
        # Optional: diagonals can be set to False not to get them in the neighbourhood.
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
        # Method to count a specific value of marker in the neighbourhood of the position.
        # Optional: diagonals can be set to False not to get them in the neighbourhood.
        return sum([n == marker for n in self.get_neighbours(diagonals)])

    def count_marker(self, marker):
        # Method to count how many times a specific marker is present in the total map
        return sum([sum([x == marker for x in line]) for line in self.map])
