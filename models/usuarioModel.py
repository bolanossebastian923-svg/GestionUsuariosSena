from database import db


class Usuario(db.Model):
    __tablename__='usuarios'

    idusuario= db.Column(db.Integer, primary_key=True, autoincrement=True)
    idPersona= db.Column(db.Intiger, db.Foreingkey('personas.idPersona'), nullable=False, unique=True)
    username= db.Column(db.String(50), nullable=False, unique=True)
    password= db.Column(db.String(100), nullable=True)
    tipo= db.Column(db.Enum('aprendiz', 'Instructor', name='tipo_enum'), nullable=False)
    estado=db.Column(db.Enum('Activo', 'Inactivo', name='estado_enum'), nullable=False, default='Activo')


    def to_dict(self):
        return{
            "idusuario":self.idusuario,
            "idPersona":self.idPersona,
            "username":self.username,
            "password":self.password,
            "tipo":self.tipo,
            "estado":self.estado,
            "persona": self.persona.to_dict() if self.persona else None
        }