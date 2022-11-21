class Jules:
    note = "francais"
    def __init__(self,annee = "2020",):
        self.annee = annee
    def exemple(self):
        print(f"est {self.annee},{self.note}")
if __name__ == "__main__":
    c1 = Jules()
    c1.exemple() 