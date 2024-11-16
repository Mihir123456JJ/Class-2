class x:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def display(self):
        print("Name is:",self.name)
        print("ID is:",self.id)
class y(x):
    def __init__(self,name,id,sallary,post):
        self.sallary=sallary
        self.post=post
        x.__init__(self,name,id)

emp1=y("Jake",2343414,"42k","Instructor")
emp1.display()
print("Post is:",emp1.post) 
print("His sallary is:",emp1.sallary)       