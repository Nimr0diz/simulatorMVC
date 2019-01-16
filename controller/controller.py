from model.model import Model

class Controller:
  def __init__(self):
    self.model = None
    self.view = None

  def check_for_model(self):
    if not self.model:
      raise ValueError("Model hasn't assigned for the Controller.")
  def check_for_view(self):
    if not self.view:
      raise ValueError("View hasn't assigned for the Controller.")
  # V -> M
  def load_world_from_file(self,path):
    self.check_for_model()
    return self.model.load_world_from_file(path)
    