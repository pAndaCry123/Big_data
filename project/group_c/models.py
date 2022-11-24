from group_c import  db

class Exsam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(30), nullable=False)
    race = db.Column(db.String(30),  nullable=False)
    parenta_level = db.Column(db.String(30),  nullable=False)
    lunch = db.Column(db.String(20), nullable=False)
    test_prep = db.Column(db.String(120), nullable=False)
    math_score = db.Column(db.Integer, nullable=False)
    reading_score = db.Column(db.Integer, nullable=False)
    writing_score = db.Column(db.Integer, nullable=False)


    def __init__(self,args):
        self.gender = args[0]
        self.race = args[1]
        self.parenta_level = args[2]
        self.lunch = args[3]
        self.test_prep = args[4]
        self.math_score = args[5]
        self.reading_score = args[6]
        self.writing_score = args[7]


    def __str__(self):
        return "{0} , {1} , {2}".format(self.gender,self.race,self.parenta_level)

    def __repr__(self):
        return "{0} , {1} , {2}".format(self.gender, self.race, self.parenta_level)