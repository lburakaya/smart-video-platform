class Matris:
    def __init__(self,line,column):
        self.line=line
        self.column=column
        self.matris=[]
        self.total=0

    def make_matris(self):
        for j in range(self.column):   
            line_list=[]
            for i in range(self.line):
                value = int(input(f"Lütfen matrisin {i+1}. satır {j+1}. sütun elemanını giriniz: "))
                line_list.append(value)
            self.matris.append(line_list)

    def add_matris(self):
        for row in self.matris:
            for element in row:
                self.total += element
        return self.total

    def __str__(self):
        results=""
        for row in self.matris:
            for element in row:
                results += str(element) + " "
            results += "\n"
        return f" {results} \n toplam: {str(self.total)}"
    
o1=Matris(3,3)
o1.make_matris()
o1.add_matris()
print(o1)
