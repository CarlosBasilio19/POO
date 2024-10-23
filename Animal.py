class Animal:


 def __init__(self,nome,cor,habitat):
    self.nome = nome
    self.cor  = cor
    self.habitat = habitat
    self.idade = 3

 def fazer_som(self):
     print("O animal faz um som.")
 def informaçoes(self):
     print(self.nome,"é",self.cor,"seu habitat é ",self.habitat,"e tem",self.idade,"anos de idade" )


