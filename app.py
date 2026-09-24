"""
Tarea individual 7 - API
Implementa el contrato definido en Contrato-api_Tarea7:
  - Tareas: consultar todas, consultar una, filtrar por estado, completar, eliminar
  - Estudiantes: consultar todos, consultar uno, crear, modificar, eliminar

Los datos se guardan en memoria (listas de diccionarios) solo para fines
de la tarea; no hay base de datos real.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

ESTADOS_VALIDOS = {"pendiente", "completada"}

# ---------------------------------------------------------------------------
# "Base de datos" en memoria
# ---------------------------------------------------------------------------

estudiantes = [
    {"id": 1, "nombre": "Ana López", "email": "ana.lopez@correo.com"},
    {"id": 2, "nombre": "Carlos Pérez", "email": "carlos.perez@correo.com"},
]

tareas = [
    {
        "id": 1,
        "titulo": "Ensayo de historia",
        "curso": "Historia Universal",
        "fechaEntrega": "2026-10-05",
        "estado": "pendiente",
        "estudiante_id": 1,
    },
    {
        "id": 2,
        "titulo": "Práctica de laboratorio",
        "curso": "Química",
        "fechaEntrega": "2026-09-28",
        "estado": "completada",
        "estudiante_id": 2,
    },
]


def next_id(coleccion):
    return max((item["id"] for item in coleccion), default=0) + 1


def buscar_por_id(coleccion, item_id):
    return next((item for item in coleccion if item["id"] == item_id), None)


# ---------------------------------------------------------------------------
# TAREAS
# ---------------------------------------------------------------------------

@app.get("/api/tareas/")
def listar_tareas():
    """1. Consultar todas las tareas / 3. Filtrar tareas por estado"""
    estado = request.args.get("estado")
    if estado is not None:
        if estado not in ESTADOS_VALIDOS:
            return jsonify({"error": "Valor de estado inválido"}), 400
        return jsonify([t for t in tareas if t["estado"] == estado]), 200
    return jsonify(tareas), 200


@app.get("/api/tareas/<int:tarea_id>/")
def obtener_tarea(tarea_id):
    """2. Consultar una tarea específica"""
    tarea = buscar_por_id(tareas, tarea_id)
    if tarea is None:
        return jsonify({"error": "No existe una tarea con ese id"}), 404
    return jsonify(tarea), 200


@app.patch("/api/tareas/<int:tarea_id>/")
def completar_tarea(tarea_id):
    """4. Marcar una tarea como completada"""
    tarea = buscar_por_id(tareas, tarea_id)
    if tarea is None:
        return jsonify({"error": "No existe una tarea con ese id"}), 404

    data = request.get_json(silent=True) or {}
    estado = data.get("estado")
    if estado not in ESTADOS_VALIDOS:
        return jsonify(
            {"error": "Body inválido (campo faltante o valor de estado no permitido)"}
        ), 400

    tarea["estado"] = estado
    return jsonify(tarea), 200


@app.delete("/api/tareas/<int:tarea_id>/")
def eliminar_tarea(tarea_id):
    """5. Eliminar una tarea"""
    tarea = buscar_por_id(tareas, tarea_id)
    if tarea is None:
        return jsonify({"error": "No existe una tarea con ese id"}), 404
    tareas.remove(tarea)
    return "", 204


# ---------------------------------------------------------------------------
# ESTUDIANTES
# ---------------------------------------------------------------------------

@app.get("/api/estudiantes/")
def listar_estudiantes():
    """6. Consultar todos los estudiantes"""
    return jsonify(estudiantes), 200


@app.get("/api/estudiantes/<int:estudiante_id>/")
def obtener_estudiante(estudiante_id):
    """7. Consultar un estudiante específico"""
    estudiante = buscar_por_id(estudiantes, estudiante_id)
    if estudiante is None:
        return jsonify({"error": "No existe un estudiante con ese id"}), 404
    return jsonify(estudiante), 200


@app.post("/api/estudiantes/")
def crear_estudiante():
    """8. Crear un estudiante"""
    data = request.get_json(silent=True) or {}
    nombre = data.get("nombre")
    email = data.get("email")
    if not nombre or not email:
        return jsonify(
            {"error": "Body inválido (campo faltante o email con formato incorrecto)"}
        ), 400

    nuevo = {"id": next_id(estudiantes), "nombre": nombre, "email": email}
    estudiantes.append(nuevo)
    return jsonify(nuevo), 201


@app.put("/api/estudiantes/<int:estudiante_id>/")
def modificar_estudiante(estudiante_id):
    """9. Modificar un estudiante"""
    estudiante = buscar_por_id(estudiantes, estudiante_id)
    if estudiante is None:
        return jsonify({"error": "No existe un estudiante con ese id"}), 404

    data = request.get_json(silent=True) or {}
    nombre = data.get("nombre")
    email = data.get("email")
    if not nombre or not email:
        return jsonify(
            {"error": "Body inválido (campo faltante o valor no permitido)"}
        ), 400

    estudiante["nombre"] = nombre
    estudiante["email"] = email
    return jsonify(estudiante), 200


@app.delete("/api/estudiantes/<int:estudiante_id>/")
def eliminar_estudiante(estudiante_id):
    """10. Eliminar un estudiante"""
    estudiante = buscar_por_id(estudiantes, estudiante_id)
    if estudiante is None:
        return jsonify({"error": "No existe un estudiante con ese id"}), 404
    estudiantes.remove(estudiante)
    return "", 204


if __name__ == "__main__":
    app.run(debug=True)
