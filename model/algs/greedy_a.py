import model.utils.global_utils as global_utils 

class Greedy_a:

    # @staticmethod
    # def cluster_h(cluster, current_time):
    #     sum = 0
    #     for v in cluster.vertexes:
    #         sum += algo_utils.h(v.cst(current_time), v.p)
    #     cluster.vertexes.sort(reverse=True, key=lambda vert: algo_utils.h(vert.cst(current_time), vert.p))
    #     return sum

    # @staticmethod
    # def next_step(clusters, map, current_loc, current_time):
    #     max_cluster = clusters[0]
    #     max_val = Greedy_a.cluster_h(max_cluster, current_time)
    #     for c in clusters:
    #         if Greedy_a.cluster_h(c, current_time) > max_val:
    #             max_cluster = c
    #             max_val = Greedy_a.cluster_h(c, current_time)
    #     return max_cluster

    # @staticmethod
    # def is_using_clustering():
    #     return True


  @staticmethod
  def next_step(current_vertex_ind, vertexes, distance_matrix,current_time):
    max_ind = current_vertex_ind
    max_price = 0
    for i,v in enumerate(vertexes):
      current_v_price = global_utils.price(v.cst(current_time),v.p)
      if current_v_price > max_price:
        max_ind = i
        max_price = current_v_price
    return max_ind