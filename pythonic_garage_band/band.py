

class Musician :
   '''
   in this class we create some function and method
   to handle some functionality to the childs classes like 
   __str__ and __repr__ and get instrument 
   '''
   def __init__(self,name) :
      self.name = name
      
   def __str__(self):
    return f'My name is {self.name} and I play {self.type}'  
            
   def __repr__(self):
      return f'{self.type2} instance. Name = {self.name}'
    
    
   def get_instrument(self):
    return f'{self.type}'
    
    
class Guitarist(Musician):
   """
   this is a guitarist class from musician parent class 
   which have a gitar as instrument

  
   """
   type ='guitar'
   type2='Guitarist'
   
   def play_solo(self):
     return 'face melting guitar solo'
   



class Bassist(Musician):
    """ 
    this is a Bassist class from musician parent class
    which have a gitar as instrument
    """
    type ='bass'
    type2='Bassist'
    
    def play_solo(self):
     return 'bom bom buh bom'



class Drummer(Musician):
    """
    this is a drummer class from musician parent class 
    which have a drums as instrument 
    """
    type ='drums'
    type2='Drummer'
    
    def play_solo(self):
     return 'rattle boom crash'
    
    
 
 
 
 
 
 
 
 
 
    
class Band():
   """
    this band class will create some methods and functions for members
    
   """
   instances = []

   def __init__(self,name,members) :
      self.name = name
      self.members = members
      Band.instances.append(self)

      
   def play_solos(self):
    member_list=[]
    for i in self.members:
      member_list.append(i.play_solo())
      
      
   
 
    return member_list
 
   @classmethod
   
   def to_list(cls):
        return cls.instances
 
   
       
  
  
  
  
  












if __name__ == '__main__':
    print(1)
malek=Guitarist("malik")