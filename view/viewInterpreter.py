import string
import subprocess as sp
import re
from controller.controller import Controller

class ViewInterpreter:
  def __init__(self,controller):
    self.controller = controller

  def start(self):
    all_commands ={
      'exit': self.exit,
      'loadworld': self.load_world,
    }

    self.print_opening_message()

    try_to_exit = False
    interrupted = False
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
      print("success!")
    else:
      print(error_msg)