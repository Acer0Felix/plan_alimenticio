from . import db 

class PlanAlimenticio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128), unique=True, nullable=False)
    descripcion = db.Column(db.String(255), unique=True, nullable=False)
    #detalle = db.Column(db.Array)
    
def to_json(self):
    return {
        'id': self.id,
        'nombre': self.nombre,
        'descripcion': self.descripcion
        #'detalle': self.detalle
    }

