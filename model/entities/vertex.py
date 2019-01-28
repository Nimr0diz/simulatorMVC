import model.utils.global_utils as global_utils

class Vertex:

    def __init__(self, probability, starvation_time, point):
        self.point = point
        self.p = probability
        self.lv = 0  # last visit time
        self.ts = 0  # total starvation time
        self.st = starvation_time

    def cst(self, current_time):
        return global_utils.time_function(current_time - self.lv - self.st)

    def __update_lv(self, current_time):
        self.lv = current_time

    def visit(self, current_time):
        temp_cst = self.cst(current_time)
        self.lv = current_time
        if self.cst(current_time) == 0: 
            self.ts += temp_cst
        #print("visited vertex ({},{})".format(self.point.x, self.point.y))

    def print_details(self):
        print("____________________________")
        print("Vertex Details: ({},{})".format(self.point.x, self.point.y))
        print("probability: {}, last visited at: {}, starvation time limit: {}".format(self.p, self.lv, self.st))
        print("total starvation until last visit: {}".format(self.ts))
        print("____________________________")
