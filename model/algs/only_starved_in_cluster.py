from collections import deque
import model.utils.global_utils as global_utils 
import model.utils.algo_utils as algo_utils

class Only_starved_in_cluster:

  def __init__(self,world,distance_matrix,alg_args):
    self.world = world
    self.distance_matrix = distance_matrix
    self.args = alg_args
    self.queue = deque([])

  def start(self):
    self.clusters = algo_utils.dbscan_clustering(self.world['visit_points'],int(self.args['maxd']),int(self.args['minp']))

  def next_step(self, current_vertex_ind, vertexes,current_time):
    if not self.queue:
      max_cluster = self.clusters[0]
      max_price = 0
      # v_prices = []
      for cluster in self.clusters:
        cluster_price = 0
        for v_i in cluster:
          v = vertexes[v_i]
          cluster_price += global_utils.price(v.cst(current_time),v.p)
        if cluster_price > max_price:
          max_cluster = cluster
          max_price = cluster_price


      vs_of_cluster = [(i,global_utils.price(vertexes[i].cst(current_time),vertexes[i].p)) for i in max_cluster]
      vs_of_cluster = [v for v in vs_of_cluster if v[1] > 0]
      vs_of_cluster.sort(key = lambda v:v[1], reverse = True)
      self.queue.extend(map(lambda v:v[0],vs_of_cluster))

    if self.queue:
      next_v = self.queue.popleft()
    else:
      next_v = current_vertex_ind
    return next_v
