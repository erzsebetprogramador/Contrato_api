# Tarea individual 7 - API

Implementación en Python (Flask) del contrato de API definido en el documento
`Contrato-api_Tarea7`. Usa datos en memoria (no requiere base de datos) solo
para poder probar los endpoints fácilmente.

## Instalación

```bash
pip install -r requirements.txt
```

## Ejecución

```bash
python app.py
```

El servidor queda disponible en `http://127.0.0.1:5000`.

## Endpoints

| Acción | Método | Endpoint |
|---|---|---|
| Consultar tareas | GET | `/api/tareas/` |
| Consultar una tarea | GET | `/api/tareas/{id}/` |
| Filtrar por estado | GET | `/api/tareas/?estado=pendiente` |
| Completar tarea | PATCH | `/api/tareas/{id}/` |
| Eliminar tarea | DELETE | `/api/tareas/{id}/` |
| Consultar estudiantes | GET | `/api/estudiantes/` |
| Consultar un estudiante | GET | `/api/estudiantes/{id}/` |
| Crear estudiante | POST | `/api/estudiantes/` |
| Modificar estudiante | PUT | `/api/estudiantes/{id}/` |
| Eliminar estudiante | DELETE | `/api/estudiantes/{id}/` |

## Ejemplos con curl

```bash
# Consultar todas las tareas
curl http://127.0.0.1:5000/api/tareas/

# Consultar una tarea
curl http://127.0.0.1:5000/api/tareas/1/

# Filtrar por estado
curl "http://127.0.0.1:5000/api/tareas/?estado=pendiente"

# Marcar una tarea como completada
curl -X PATCH http://127.0.0.1:5000/api/tareas/1/ \
  -H "Content-Type: application/json" \
  -d '{"estado": "completada"}'

# Eliminar una tarea
curl -X DELETE http://127.0.0.1:5000/api/tareas/1/

# Consultar todos los estudiantes
curl http://127.0.0.1:5000/api/estudiantes/

# Crear un estudiante
curl -X POST http://127.0.0.1:5000/api/estudiantes/ \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Luis Gómez", "email": "luis.gomez@correo.com"}'

# Modificar un estudiante
curl -X PUT http://127.0.0.1:5000/api/estudiantes/1/ \
  -H "Content-Type: application/json" \
  -d '{"nombre": "Ana López Ramírez", "email": "ana.lopez@correo.com"}'

# Eliminar un estudiante
curl -X DELETE http://127.0.0.1:5000/api/estudiantes/1/
```
