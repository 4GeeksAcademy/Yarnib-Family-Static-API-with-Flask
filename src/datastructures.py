
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
# datastructures.py
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # Initialize with the specified family members
        self._members = [
            {
                "id": self._generateId(),
                "first_name": "Michael",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generateId(),
                "first_name": "Janet",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generateId(),
                "first_name": "Latoya",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # Append the member to the list of _members
        if "id" not in member:
            member["id"] = self._generateId()
        self._members.append(member)

    def delete_member(self, id):
        # Loop the list and delete the member with the given id
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return

    def update_member(self, id, member):
        # Loop the list and replace the member with the given id
        for i, existing_member in enumerate(self._members):
            if existing_member["id"] == id:
                self._members[i] = member
                return

    def get_member(self, id):
        # Loop all the members and return the one with the given id
        for member in self._members:
            if member["id"] == id:
                return member

    def get_all_members(self):
        return self._members
