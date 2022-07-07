# Automated Testing

class Room(object):
2
3 def __init__(self, name, description):
4 self.name = name
5 self.description = description
6 self.paths = {}
7
8 def go(self, direction):
9 return self.paths.get(direction, None)
10
11 def add_paths(self, paths):
12 self.paths.update(paths)