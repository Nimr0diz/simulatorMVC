from controller.controller import Controller
from view.viewInterpreter import ViewInterpreter
from model.model import Model

def run():
  c = Controller()
  v = ViewInterpreter(c)
  m = Model(c)
  c.model = m
  c.view = v

  v.start()

run()