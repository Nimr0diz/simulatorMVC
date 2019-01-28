import string
import subprocess as sp
import re
from controller.controller import Controller
from view.gui_screens.gui_classes.view import View
class ViewInterpreter:
  def __init__(self,controller):
    self.controller = controller
  def prestart(self,script_file):
    self.all_commands = { 
        'exit': self.exit,
        'loadworld': self.load_world,
        'runalgo': self.run_algorithm,
        'showscenerio': self.show_scenerio,
        'infoscenerio': self.print_scenerio_info,
    }

    self.load_scripts_from_file(script_file)

    
  def start(self):
    self.print_opening_message()

    try_to_exit = False
    interrupted = False
    # self.load_world({'f': './_data/simple_world.world'})
    # self.run_algorithm({'a': 'greedy_a','t': 600})
    # self.show_scenerio({})
    while not interrupted:
      try:
        user_input = input(">>> ")
      except KeyboardInterrupt:
        if try_to_exit:
          print("")
          interrupted = True
        else:
          print("\n(To exit, press ^C again)")
          try_to_exit = True
        continue

      try_to_exit = False
      self.handle_input(user_input)

  def load_scripts_from_file(self,file_path):
    try:
      with open(file_path) as f:
        lines = f.readlines()
      for line in lines:
        print(">>>",line.rstrip())
        self.handle_input(line.rstrip())
    except FileNotFoundError as e:
      print("Script file not found in path {}, continue usual".format(file_path))

  def handle_input(self, user_input):
    command_name, args = self.parse_input(user_input)
    if command_name in self.all_commands:
      self.all_commands[command_name](args)
    else:
      print("the command '{}' doesn't exist.".format(command_name))

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

  def exit(self,args):
    exit()

  def load_world(self,args):
    path = args['f']
    success,error_msg = self.controller.load_world_from_file(path)
    if success:
      print("World loaded successfully!")
    else:
      print(error_msg)
  
  def run_algorithm(self,args):
    algo = args['a']
    tpd = int(args['t'])
    success,error_msg = self.controller.run_algorithm_on_world(algo,tpd)
    if success:
      print("Algorithm run complete.\nrun 'infoscenerio' for details or 'showscenerio' for GUI view")
    else:
      print(error_msg)
  
  def show_scenerio(self,args):
    response = self.controller.get_scenerio_for_gui()
    success = response[0]
    if success:
      scenerio = response[1]
      View(scenerio)
    else:
      error_msg = response[1]
      print(error_msg)

  def print_scenerio_info(self,args):
    details = self.controller.get_scenerio_info()
    text_lines = [" {}: {} ".format(k,v) for k,v in details.items()]
    size = max([len(tl) for tl in text_lines])
    print(text_lines)
    print("#" + size*"#" + "#")
    for tl in text_lines:
      print("#" + tl.ljust(size) + "#")
    print("#" + size*"#" + "#")

