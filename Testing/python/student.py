#Couldn't import it so I modified it just so i can work with the data
# good luck connecting them hehehe

class Student():
  def __init__(self, first_name, middle_name, last_name, section, batch):
    self.first_name = first_name
    self.middle_name = middle_name
    self.last_name = last_name
    self.section = section
    self.batch = batch
    self.receipts = None

    @property
    def name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"

# class Student():
#     first_name = db.StringField(max_length=100, required=True)
#     last_name = db.StringField(max_length=100, required=True)
#     middle_name = db.StringField(max_length=100, required=False, default="")
#     batch = db.IntField(min_value=2023, max_value=2028)
#     receipts = db.ListField(db.ReferenceField(Receipt))

#     @property
#     def name(self):
#         return f"{self.first_name} {self.middle_name} {self.last_name}"