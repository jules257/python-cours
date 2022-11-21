class Mere:
    def bonjour(self):
        return "salut à tous!" 
class Fille(Mere):
    def salut(self):
        return "salut go!"
if __name__ == "__main__":
    c1 = Fille()
    print(c1.bonjour())
    print(c1.salut())   
    