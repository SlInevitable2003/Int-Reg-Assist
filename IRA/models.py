from IRA import db

class illnessModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    sympton1 = db.Column(db.String(50))
    sympton2 = db.Column(db.String(50))
    sympton3 = db.Column(db.String(50))
    sympton4 = db.Column(db.String(50))
    sympton5 = db.Column(db.String(50))
    sympton6 = db.Column(db.String(50))
    department = db.Column(db.String(20))

    # for test and debug
    def item_print(self):
        print('item' + str(self.id) + ' ' + self.name + ', department: ' + self.department)
        if self.sympton1 is not None:
            print('sympton 1: ' + self.sympton1)
        if self.sympton2 is not None:
            print('sympton 2: ' + self.sympton2)
        if self.sympton3 is not None:
            print('sympton 3: ' + self.sympton3)
        if self.sympton4 is not None:
            print('sympton 4: ' + self.sympton4)
        if self.sympton5 is not None:
            print('sympton 5: ' + self.sympton5)
        if self.sympton6 is not None:
            print('sympton 6: ' + self.sympton6)