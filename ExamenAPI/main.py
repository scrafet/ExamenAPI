from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from datetime import datetime  # Importar datetime

# Configuración de la Aplicación
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializar extensiones
CORS(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
api = Api(app)


# Definición del Modelo Student
class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name_paternal = db.Column(db.String(100), nullable=False)
    last_name_maternal = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    enrollment_date = db.Column(db.DateTime, server_default=func.now(), nullable=False)

    def __repr__(self):
        return f"<Student {self.id} - {self.first_name} {self.last_name_paternal}>"


# Definición del Schema para Student
class StudentSchema(ma.Schema):
    class Meta:
        fields = (
            "id",
            "first_name",
            "last_name_paternal",
            "last_name_maternal",
            "birth_date",
            "email",
            "enrollment_date"
        )


student_schema = StudentSchema()
students_schema = StudentSchema(many=True)


# Recursos de la API
class StudentListResource(Resource):
    # Método GET - lista de estudiantes
    def get(self):
        students = Student.query.all()
        return students_schema.dump(students)

    # Método POST - crear estudiante nuevo
    def post(self):
        data = request.get_json()

        # Convertir birth_date de string a objeto datetime
        try:
            birth_date = datetime.strptime(data['birth_date'], '%Y-%m-%d')
        except ValueError:
            return {"error": "Formato de fecha incorrecto. Use 'YYYY-MM-DD'."}, 400

        new_student = Student(
            first_name=data['first_name'],
            last_name_paternal=data['last_name_paternal'],
            last_name_maternal=data['last_name_maternal'],
            birth_date=birth_date,
            email=data['email']
        )
        db.session.add(new_student)
        db.session.commit()
        return student_schema.dump(new_student), 201


class StudentResource(Resource):
    # Método GET <id> - estudiante por id
    def get(self, id):
        student = Student.query.get_or_404(id)
        return student_schema.dump(student)

    # Método PUT <id> - actualizar estudiante
    def put(self, id):
        student = Student.query.get_or_404(id)
        data = request.get_json()

        student.first_name = data.get('first_name', student.first_name)
        student.last_name_paternal = data.get('last_name_paternal', student.last_name_paternal)
        student.last_name_maternal = data.get('last_name_maternal', student.last_name_maternal)

        if 'birth_date' in data:
            try:
                student.birth_date = datetime.strptime(data['birth_date'], '%Y-%m-%d')
            except ValueError:
                return {"error": "Formato de fecha incorrecto. Use 'YYYY-MM-DD'."}, 400

        student.email = data.get('email', student.email)

        db.session.commit()
        return student_schema.dump(student)

    # Método DELETE <id> - eliminar estudiante
    def delete(self, id):
        student = Student.query.get_or_404(id)
        db.session.delete(student)
        db.session.commit()
        return '', 204


# Añadir los recursos a la API
api.add_resource(StudentListResource, '/students')  # Para la lista de estudiantes y crear estudiante nuevo
api.add_resource(StudentResource, '/students/<int:id>')  # Para operaciones con un estudiante específico por id

# Ejecutar la Aplicación
if __name__ == "__main__":
    app.run(debug=True)
