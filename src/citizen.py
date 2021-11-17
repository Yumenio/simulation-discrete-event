class Citizen:
  def __init__(self, age, sex):
    self.age = age
    self.sex = sex
    self.pregnant = False
    self.looking_for_partner = False
    self.engaged = False
    self.max_children = 

  def belongs_to(self,lbound,rbound):
    return self.age >= lbound and self.age <=rbound