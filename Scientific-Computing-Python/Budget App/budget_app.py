class Category:
    def __init__(self, name):
        self.name = name
        self.funds = 0
        self.ledger = []
       
    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        total = 0
        for i in range(len(self.ledger)):
            items += f"{self.ledger[i]['description'][0:23]:23}" + \
            f"{self.ledger[i]['amount']:>7.2f}" + '\n'
            total += self.ledger[i]['amount']
        output = title + items + "Total: " + str(total)
        return output


    def deposit(self, amount, description=''):
        self.ledger.append({'amount':amount, 'description':description})
        self.funds += amount
    
    def withdraw(self, amount, description=''):
        new_amount = - amount
        if self.check_funds(amount) == True:
            self.ledger.append({'amount':new_amount, 'description':description})
            self.funds -= amount
            return True
        else:
            return False
    
    def get_balance(self):
        return self.funds

    def check_funds(self, amount):
        if self.funds - amount >= 0:
            return True
        else:
            return False

    def transfer(self, amount, category):
        if self.check_funds(amount) == True:
            self.withdraw(amount,'Transfer to {}'.format(category.name))
            category.deposit(amount,'Transfer from {}'.format(self.name))
            return True
        else:
            return False

def round_ten(n):
    if n < 10:
        return 0
    else:
        return round(n/10.0)*10


def create_spend_chart(categories):
  total_spent = 0
  spent_percat = []
  max_len = 0
  for category in categories:
    total_cat = 0  
    for i in range(len(category.ledger)):
      if category.ledger[i]['amount'] < 0:
        total_cat -= category.ledger[i]['amount']
        total_spent -= category.ledger[i]['amount']
        
    spent_percat.append([category.name,total_cat])

    if len(category.name) > max_len:
      max_len = len(category.name)

  for i in range(len(categories)):
    spent_percat[i][1] = round_ten((spent_percat[i][1] / total_spent)*100)
    

  bars = 'Percentage spent by category\n'
    
  for i in range(100,-10,-10):
    bars += str(i).rjust(3) + '|' + ' '
    for j in range(len(categories)):
      if spent_percat[j][1] >= i:
        bars += 'o' + '  '
      else:
        bars += '   '
    bars += '\n'

  bars += "    "+("-" * 3 * len(categories) + '-')+"\n"

  count = 0

  for i in range(max_len):
    bars += '     '
    for j in range(len(spent_percat)):
      if len(spent_percat[j][0]) - 1 < count:
        bars += '   '
      else:
        bars += spent_percat[j][0][count] + '  '
    count += 1
    if i!=(max_len)-1:
      bars += '\n'
  
  return bars
