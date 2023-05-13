

class Musician :
 
   def __init__(self,name) :
      self.name = name
      
   def __str__(self):
    return f'My name is {self.name} and I play {self.type}'  
            
   def __repr__(self):
      return f'{self.type2} instance. Name = {self.name}'
    
    
   def get_instrument(self):
    return f'{self.type}'
    
    
class Guitarist(Musician):
   type ='guitar'
   type2='Guitarist'
  
   def play_solo(self):
     return 'face melting guitar solo'
   

class Bassist(Musician):
    type ='bass'
    type2='Bassist'
    
    def play_solo(self):
     return 'bom bom buh bom'

class Drummer(Musician):
    type ='drums'
    type2='Drummer'
    
    def play_solo(self):
     return 'rattle boom crash'
    
    
    
class Band():
   def __init__(self,name,members) :
      self.name = name
      self.members = members
    
      
   def play_solos(self):
    member_list=[]
    for i in self.members:
      member_list.append(i.play_solo())
      
    return member_list
  
  
  
  
   def to_list(self):
      
     return self.ininstances












if __name__ == '__main__':
    print(1)
    