from travel import db

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(64), unique = True, nullable = False)
    city_rank = db.Column(db.Integer, unique = True, nullable = False)


    def __repr__(self):
        return f"City('{self.city_name}', {self.city_rank}, {self.is_visited})"