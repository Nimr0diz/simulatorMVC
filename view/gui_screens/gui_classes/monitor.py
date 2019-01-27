from tkinter import *
import math
from view.gui_screens.gui_classes.drawer import *
class Monitor:

    def __init__(self,root,width,height):
        self.root = root
        self.width = width
        self.height = height
        self.create_canvas()
    

    def setController(self, controller):
        self.controller = controller
    

    def create_canvas(self):
        self.canvas = Canvas(self.root, width=self.width, height = self.height)
        self.canvas.pack()
    
    def init_objects(self, vertexes, robot_location, obstacles):
        self.canvas.create_rectangle(1,1,self.width,self.height)
        self.robot = create_robot(self.canvas,robot_location['position'])
        self.verts = [create_vertex(self.canvas,v) for v in vertexes]
        for ob in obstacles:
            self.canvas.create_line(ob[0].x, ob[0].y, ob[1].x, ob[1].y)
    
    def drawFrame(self,frame,ind):
        print(frame)
        pos = frame['position']
        ang = frame['angle']
        update_robot(self.canvas,self.robot,pos,ang)
        # for v,v_data in zip(self.verts,frame['vertexes']):
        #     update_vertex(self.canvas,v,v_data,ind,self.controller.show_text)
        if 'message' in frame:
            print("MONITOR[{0}]: {1}".format(ind,frame['message']))
        self.canvas.update()

