# Basic Object-Oriented Analysis and Design

class Scene(object):
2
3 def enter(self):
4 pass

ptg20573278

168 LEARN PYTHON 3 THE HARD WAY

5
6
7 class Engine(object):
8
9 def __init__(self, scene_map):
10 pass
11
12 def play(self):
13 pass
14
15 class Death(Scene):
16
17 def enter(self):
18 pass
19
20 class CentralCorridor(Scene):
21
22 def enter(self):
23 pass
24
25 class LaserWeaponArmory(Scene):
26
27 def enter(self):
28 pass
29
30 class TheBridge(Scene):
31
32 def enter(self):
33 pass
34
35 class EscapePod(Scene):
36
37 def enter(self):
38 pass
39
40
41 class Map(object):
42
43 def __init__(self, start_scene):
44 pass
45
46 def next_scene(self, scene_name):
47 pass
48
49 def opening_scene(self):
50 pass
51
52
53 a_map = Map('central_corridor')
54 a_game = Engine(a_map)
55 a_game.play()