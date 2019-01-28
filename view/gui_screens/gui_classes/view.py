import threading
from tkinter import *
import time

from view.gui_screens.gui_classes.controlWidgets import ControlWidgets
from view.gui_screens.gui_classes.controller import Controller
from view.gui_screens.gui_classes.monitor import Monitor


class View:

    def __init__(self,scenerio,width=600,height=600):
        root = Tk()
        monitor = Monitor(root, width, height)
        control_widgets = ControlWidgets(root, len(scenerio['frames']),width)
        controller = Controller(control_widgets, monitor, scenerio)
        control_widgets.setController(controller)
        monitor.setController(controller)
        try:
            controller.start()
        except TclError as e:
            print("GUI closed.")