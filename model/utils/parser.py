import math

def json_to_world(json):
  width = json["width"]
  height = json["height"]
  robot = json_to_robot(json["robot"])
  obstacles = json_to_obstacles(json["obstacles"])
  visit_points = json_to_visit_points(json["vertexes"])

def json_to_robot(json):
  robot = {
    'walk_speed': 10,
    'rotation_speed': math.pi / 20,
    'start_angle': 0
  }

  robot.update(j)
  if "start_point" in json:
    robot["start_point"] = json_to_point(json["start_point"])
  else:
    raise ValueError("robot's start_point is missing")

  return robot

def json_to_obstacles(json):
  obstacles = []
  for json_obs in json:
    obs = [json_to_point(p) for p in json_obs]
    obstacles.append(obs)
  return obs

def json_to_visit_points(json):
  visit_points = []
  for vp in json:
    vis_po = {}
    vis_po.update(vp)
    vp['position'] = json_to_point(vp['position'])
    visit_points.append(vis_po)
  return visit_points