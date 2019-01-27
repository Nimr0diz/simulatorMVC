import string
import subprocess as sp
import re
from controller.controller import Controller
from view.gui_screens.gui_classes.view import View
class ViewInterpreter:
  def __init__(self,controller):
    self.controller = controller

  def start(self):
    all_commands ={
      'exit': self.exit,
      'loadworld': self.load_world,
      'runalgo': self.run_algorithm,
    }

    self.print_opening_message()

    try_to_exit = False
    interrupted = False
    self.load_world({'f': './_data/simple_world.world'})
    self.run_algorithm({'a': 'greedy_a','t': 600})
    self.show_scenerio({})
    while not interrupted:
      try:
        user_input = input(">>> ")
      except KeyboardInterrupt as e:
        if try_to_exit:
          print("")
          interrupted = True
        else:
          print("\n(To exit, press ^C again)")
          try_to_exit = True
        continue
      try_to_exit = False
      command_name, args = self.parse_input(user_input)
      if command_name in all_commands:
        all_commands[command_name](args)
      else:
        print("the command '{}' doesn't exist.".format(command_name))
        continue        

  def parse_input(self,user_input):
    user_input = re.sub(" +"," ",user_input)
    strs = user_input.split(" ")
    args_strs = strs[1:]
    command = strs[0]
    args = {}
    i = 0
    while i < len(args_strs):
      arg = args_strs[i]
      next_arg = ""
      if i < len(args_strs) - 1 :
        next_arg = args_strs[i+1]
      if "-" == arg[0]:
        arg = arg[1:]
      else:
        return command, None
      if next_arg:
        if "-" == next_arg[0]:
          args[arg] = True
          i += 1
        else:
          args[arg] = next_arg
          i += 2
      else:
        args[arg] = True
        i += 1

    return command, args
      
  def print_opening_message(self):
    print("") 
    print("Welcome to the Simulator Interpreter!")
    print("To start just enter the command you want to execute.")
    print("If you want to use specific command just type: [COMMAND] -?")
    print("If you want to know what commands do you have just type: cmdlist")
    print("") 
  def exit(self):
    pass

  def load_world(self,args):
    path = args['f']
    success,error_msg = self.controller.load_world_from_file(path)
    if success:
      print("World loaded successfully!")
    else:
      print(error_msg)
  
  def run_algorithm(self,args):
    algo = args['a']
    tpd = args['t']
    success,error_msg = self.controller.run_algorithm_on_world(algo,tpd)
    if success:
      print("Algorithm run complete.\nrun 'infoscenerio' for details or 'showscenerio' for GUI view")
    else:
      print(error_msg)
  
  def show_scenerio(self,args):
    scenerio = self.controller.get_scenerio_for_gui()
    View(scenerio)

