# Examen API-DEVELOPER
### Berrocal Garcia Waldo Anthony- Examen Final API DEVELOPER-Cibertec
# Proyecto API REST con Flask - Gestión de Estudiantes

Este proyecto es una API REST creada con Flask que permite gestionar estudiantes, utilizando una base de datos SQLite. La API tiene métodos para listar, crear, actualizar y eliminar registros de estudiantes.

# Instalación del Proyecto
### Paso 1: Crear un Entorno Virtual

```
python -m venv .venv
```
### Paso 2: Activar el Entorno Virtual
```
source .venv/bin/activate
```
### Paso 3: Instalar Dependencias
```
pip install -r requirements.txt
```
### Paso 4: Inicializar la Base de Datos
#### Inicializar las Migraciones:
```
flask --app main db init
```
#### Crear Migración:
```
flask --app main db migrate -m "Migración inicial"
```
#### Aplicar Migración:
#### ejecutar el servidor Flask:
```
flask --app main run --reload
```

## Rutas de la API y Métodos para Usar en Postman

| **Dirección (URL)**                  | **Método**  | **Acción**                        | **Ejemplo de Datos Enviados (Cuerpo de la Petición)**                                                                                               |
|--------------------------------------|-------------|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| `/students`                          | **GET**     | Obtener lista de estudiantes      | N/A                                                                                                                                                |
| `/students/<int:id>`                 | **GET**     | Obtener estudiante por ID         | N/A                                                                                                                                                |
| `/students`                          | **POST**    | Crear un nuevo estudiante         | ```json { "first_name": "Carlos", "last_name_paternal": "Ramírez", "last_name_maternal": "Gómez", "birth_date": "2001-02-15", "email": "carlos.ramirez@example.com" } ``` |
| `/students/<int:id>`                 | **PUT**     | Actualizar un estudiante por ID   | ```json { "first_name": "Carlos", "email": "carlos.ramirez_updated@example.com" } ``` (Solo incluir los campos que desees actualizar)              |
| `/students/<int:id>`                 | **DELETE**  | Eliminar estudiante por ID        | N/A                                                                                                                                                |

### Licencia
Este proyecto está bajo la licencia MIT. 

### Autor
Berrocal García Waldo Anthony
