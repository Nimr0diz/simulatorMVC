import json
import model.utils.parser as parser
import model.utils.dispatcher as dispatcher

class Model:
  def __init__(self,controller):
    self.controller = controller
    self.current_world = None
    self.current_world_path = None
    self.current_scenerio = None

  def load_world_from_file(self, path):
    try:
      world_json = open(path).read()
      world_data = json.loads(world_json)
      self.current_world = parser.json_to_world(world_data)
      self.current_world_path = path
    except FileNotFoundError:
      return False,"File not found"
    except Exception as e:
      return False,e
    return True,""

  def run_algorithm_on_world(self,algo,tpd):
    try:
      self.current_scenerio = dispatcher.run_algorithm_on_world(self.current_world,algo,tpd)
      print(self.current_scenerio)
    except FileNotFoundError as e:
      return False,e
    return True,""
