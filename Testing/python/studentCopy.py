#Couldn't import it so I modified it just so i can work with the data
# good luck connecting them hehehe

class StudentCopy():
  def __init__(self):
    self.firstname = None
    self.middlename = None
    self.lastname = None
    self.section = None
    self.batch = None
    self.receipts = None

    @property
    def name(self):
        return f"{self.firstname} {self.middlename} {self.lastname}"

# class Student():
#     firstname = db.StringField(max_length=100, required=True)
#     lastname = db.StringField(max_length=100, required=True)
#     middlename = db.StringField(max_length=100, required=False, default="")
#     batch = db.IntField(min_value=2023, max_value=2028)
#     receipts = db.ListField(db.ReferenceField(Receipt))

#     @property
#     def name(self):
#         return f"{self.firstname} {self.middlename} {self.lastname}"