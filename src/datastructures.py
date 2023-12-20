
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name 

        # example list of members

        self._members = [{
            "id": self._generateId(),
            "first_name": "John",
            "last_name": self.last_name,
            "age": 33,
            "lucky_number": [7,13,12],
        },
        {
            "id": self._generateId(),
            "first_name": "Jane",
            "last_name": self.last_name,
            "age": 35,
            "lucky_number": [10,14,3],
        },
           {
            "id": self._generateId(),
            "first_name": "Jimmy",
            "last_name": self.last_name,
            "age": 5,
            "lucky_number": [1],
        }]


    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 10)

    def add_member(self, member):
        inner_member = {
            "id": self._generateId(),
            "first_name": member ["first_name"],
            "last_name": self.last_name,
            "age": member["age"],
            "lucky_number": member ["lucky_number"],
        }
        self._members.append(inner_member)
        return inner_member

    def delete_member(self, member_id):
        member_to_delete = self.get_a_member(member_id)
        self._members.remove(member_to_delete)
        return {"message": "Member deleted successfully"}

    def get_a_member(self, member_id):
        for member in self._members:
            if member["id"] == member_id:
                print(member)
                return member
        return None
        

    def get_all_members(self):
         return self._members
