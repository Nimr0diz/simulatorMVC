import json

class Model:
  def __init__(self,controller):
    self.controller = controller
    self.current_world = None
    self.current_world_path = None
  def load_world_from_file(self, path):
    try:
      world_json = open(path).read()
      world_data = json.loads(world_json)
      
    except FileNotFoundError as e:
      return False,"File not found"
    return True,""