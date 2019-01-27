from tkinter import *

class ControlWidgets:

    def __init__(self,root,num_of_frames, width):
        self.root = root
        self.width = width
        self.num_of_frames = num_of_frames
        self.create_controllers()


    def setController(self, controller ):
        self.controller = controller


    def create_controllers(self):
        self.frame = Frame(self.root, width=self.width, height=40)
        self.frame.pack(fill='x', pady=10)
        self.play_pause_button = Button(self.frame,width=10, text='Play', height=2, command=self.play_or_pause)
        self.play_pause_button.pack(side='left', padx=10)
        self.reset_button = Button(self.frame,width=10, text='Reset', height=2, command=self.jump_to_start)
        self.reset_button.pack(side='left', padx=10)
        self.timeline = Scale(self.frame, orient=HORIZONTAL, length=250, to=self.num_of_frames, command=self.jump_to_frame)
        self.timeline.pack(side='left')
        self.starvation_checkbox = Checkbutton(self.frame,text='Show starvation',command=self.toggle_starvation_text)
        self.starvation_checkbox.pack(side='top')
        self.probability_checkbox = Checkbutton(self.frame,text='Show probability',command=self.toggle_probability_text)
        self.probability_checkbox.pack(side='top')


    def play_or_pause(self):
        isPlaying = self.controller.play_or_pause()
        if isPlaying:
            self.play_pause_button.config( text = 'Pause')
        else:
            self.play_pause_button.config( text = 'Play')


    def jump_to_start(self):
        self.jump_to_frame(0)


    def update_timeline(self,value):
        self.timeline.set(value)

    
    def jump_to_frame(self,newFrame):
        self.controller.jump_to_frame(int(newFrame))

    def toggle_starvation_text(self):
        isOn = self.controller.toggle_starvation_text()
        if isOn:
            self.starvation_checkbox.select()
        else:
            self.starvation_checkbox.deselect()

            
    def toggle_probability_text(self):
        isOn = self.controller.toggle_probability_text()
        if isOn:
            self.probability_checkbox.select()
        else:
            self.probability_checkbox.deselect()
