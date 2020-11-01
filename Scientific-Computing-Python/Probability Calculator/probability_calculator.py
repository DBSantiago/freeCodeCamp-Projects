import random
import copy


class Hat:
    def __init__(self,**balls):
        self.contents = []
        for k,v in balls.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self,number):
        balls_drawn = []
        if number > len(self.contents):
            return self.contents            
        for i in range(number):
            ball = random.choice(self.contents)
            self.contents.remove(ball)
            balls_drawn.append(ball)
        
        return balls_drawn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    counter = 0
    for i in range(num_experiments):
      hat_copy = copy.deepcopy(hat)
      drew = hat_copy.draw(num_balls_drawn)

      check = {ball:drew.count(ball) for ball in set(drew)}
  
      dummy = True
      for k in expected_balls.keys():
        if k not in check.keys() or check[k] < expected_balls[k]:
          dummy = False
          break
  
      if dummy==True:
        counter += 1
    
    probability = counter / num_experiments

    return probability
