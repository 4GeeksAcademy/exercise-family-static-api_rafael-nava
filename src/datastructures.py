"""
Actualiza este archivo para implementar los siguientes métodos ya declarados:
- add_member: Debería agregar un miembro a la lista self._members
- delete_member: Debería eliminar un miembro de la lista self._members
- update_member: Debería actualizar un miembro de la lista self._members
- get_member: Debería devolver un miembro de la lista self._members
"""

from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # Lista de ejemplo de miembros
        self._members = [
            {   "id": 1,
                "first_name": "john",
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": 2,
                "first_name": "jane",
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": 3,
                "first_name": "jimmy",
                "age": 5,
                "lucky_numbers": [7]
            }
        ]

    # Solo lectura: Usa este método para generar IDs aleatorios para los miembros cuando se agregan a la lista
    def _generateId(self):
        return randint(0, 99999999)

    # Método para agregar un miembro a la lista
    def add_member(self, member):
        # Si el miembro no tiene un ID, se genera uno aleatoriamente
        if not member.get("id"):
            member["id"] = self._generateId()  # Genera un ID aleatorio si no hay uno proporcionado
        self._members.append(member)  # Agrega el miembro a la lista de miembros

    # Método para eliminar un miembro de la lista según su ID
    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)  # Elimina el miembro de la lista
                return True  # Retorna Verdadero indicando que se encontró y eliminó el miembro
        return False  # Retorna Falso si no se encontró el miembro con el ID dado

    # Método para actualizar un miembro de la lista según su ID
    def update_member(self, id, member):
        for family_member in self._members:
            if family_member["id"] == id:
                self._members.remove(family_member)  # Elimina el miembro existente
                member["id"] = id  # Actualiza el ID del miembro nuevo o modificado
                self._members.append(member)  # Agrega el miembro actualizado a la lista
                return True  # Retorna Verdadero indicando que se actualizó el miembro
        return False  # Retorna Falso si no se encontró el miembro con el ID dado

    # Método para obtener un miembro de la lista según su ID
    def get_member(self, id):
        for family_member in self._members:
            if family_member["id"] == id:
                return family_member  # Retorna el miembro si se encuentra en la lista
        return False  # Retorna Falso si no se encuentra el miembro con el ID dado

    # Este método devuelve una lista con todos los miembros de la familia
    def get_all_members(self):
        return self._members  # Retorna la lista completa de miembros
