class Student:
    school_name="Hitit Üniversitesi"
    def __init__(self,name,surname,age,gano):
        self.name=name
        self.surname=surname
        self.age=age
        self.gano=gano

    def information(self):
        print(f"name: {self.name} {self.surname} | age: {self.age} | GANO: {self.gano} | School: {self.school_name}")

    def update_gano(self,new_gano):
        self.gano=new_gano

    @staticmethod
    def state(gano):
        if gano>=2.0: return f"geçti"
        else: return 'kaldi'

o1=Student('Burak','Kaya',23,3)

print(f"{o1.name} in durumu {o1.state(3)}")
