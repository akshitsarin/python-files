class Species :
    def statement (self):
         print "I breathe."

class Human (Species):
    def new_statement (self):
        print "am human also breathe"

obj = Human()
obj.statement()
