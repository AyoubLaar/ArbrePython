class Arbre:
    def __init__(self , value:int = 0 , arbre : 'Arbre' = None):
        if not Arbre.isEmpty(self) and isinstance(arbre,Arbre):
         self.value = arbre.value
         self.left = arbre.left
         self.right = arbre.right
        else:
         self.value = value
         self.right = None
         self.left = None
    
    def parcours_prefix(self):
       if not Arbre.isEmpty(self):
        print(self.value,end = "  ")
        if not Arbre.isEmpty(self.left):
         self.left.parcours_infixe()
        if not Arbre.isEmpty(self.right):
         self.right.parcours_infixe()
    
    def parcours_infixe(self):
       if not Arbre.isEmpty(self):
        if not Arbre.isEmpty(self.left):
         self.left.parcours_infixe()
        print(self.value,end = "  ")
        if not Arbre.isEmpty(self.right):
         self.right.parcours_infixe()

    def parcours_suffixe(self):
       if not Arbre.isEmpty(self):
        if not Arbre.isEmpty(self.left):
         self.left.parcours_infixe()
        if not Arbre.isEmpty(self.right):
         self.right.parcours_infixe()
        print(self.value,end = "  ")

    def parcours_largeur(self,list_fifo : list = []):
        print(self.value,end = "  ")
        if not Arbre.isEmpty(self.left):
          list_fifo.append(self.left)
        if not Arbre.isEmpty(self.right):
          list_fifo.append(self.right)
        if list_fifo.__len__() != 0 :
          list_fifo.pop(0).parcours_largeur(list_fifo)
    
    def recherche_min(self):
      if not Arbre.isEmpty(self.left):
        return self.left.recherche_min()
      else:
        return self.value
      
    def recherche_max(self):
      if not Arbre.isEmpty(self.right):
        return self.right.recherche_max()
      else:
        return self.value
    
    def recherche_value(self,value : int):
        if self.value > value:
         if not Arbre.isEmpty(self.right):
           return self.right.recherche_value(value)
         else:
           return None
        else: 
          if self.value < value :
            if not Arbre.isEmpty(self.left):
              return self.left.recherche_value(value)
            else: 
              return None
          else: # self.value == value
            return self

    def successeur(self):
       if not Arbre.isEmpty(self.right):
          return self.right.recherche_min()
       else:
          return None
    
    def predecesseur(self):
        if not Arbre.isEmpty(self.left):
         return self.left.recherche_max()
        else:
          return None
        
    
    def insert(self , value : int):
      if value > self.value: 
        if Arbre.isEmpty(self.right) : 
          nouveau = Arbre(value = value)
          self.right = nouveau
        else :
          self.right.insert(value)
      else: # inferieur où égale
        if Arbre.isEmpty(self.left) : 
          nouveau = Arbre(value = value)
          self.left = nouveau
        else :
          self.left.insert(value)

    def remove(self, value):
        if self.value < value :
          if not Arbre.isEmpty(self.right): 
           self.right = self.right.remove(value)
        elif self.value > value : 
          if not Arbre.isEmpty(self.left):
            self.left = self.left.remove(value)
        else :
          if self.right is None and self.left is None :
            return None 
          elif self.right is None :
            print()
          else : 
            print()

"""
"""


    @staticmethod
    def test():
      valeurs = [1,2,3,4,5,6,7,8,9,1,0,25,36,99,-11]
      values_to_remove = [1,36,5,6]
      root = Arbre(2)
      for value in valeurs:
        root.insert(value)
      print("root.parcours_infixe()")
      root.parcours_infixe()
      print("")
      print("root.parcours_prefix()")
      root.parcours_prefix()
      print("")
      print("root.parcours_suffixe()")
      root.parcours_suffixe()
      print("")
      print("root.parcours_largeur()")
      root.parcours_largeur()
      print("")
      root.remove(1)
      root.parcours_infixe()

    @staticmethod 
    def isEmpty(arbre):
      return arbre is None
    

Arbre.test()