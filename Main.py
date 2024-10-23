from Animal import Animal

class Cachorro(Animal):
    def fazer_som(self):
        print(f"{self.nome} faz: Au Au!")

class Gato(Animal):
    def fazer_som(self):
        print(f"{self.nome} faz: Miau!")

cachorro = Cachorro("Rex","preto","domestico")
gato = Gato("Felix","Branco com manchas pretas","domestico")

cachorro.fazer_som()
gato.fazer_som()

cachorro.informaçoes()
gato.informaçoes()