
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
        self.last_name = Jackson 

        # example list of members

          self._members = [
        {
            "id": self_generatedId()
            "first_name": "John"
            "last_name": self.last_name
            "age": 33
            "lucky_number": [7,13,12]
        },
        self._members = [{
            "id": self_generatedId()
            "first_name": "Jane"
            "last_name": self.last_name
            "age": 35
            "lucky_number": [10,14,3]
        },
          self._members = {
            "id": self_generatedId()
            "first_name": "Jimmy"
            "last_name": self.last_name
            "age": 5
            "lucky_number": [1]
        }]


    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        inner_member = {
            "id": self_generatId().
            "first_name": member ["first_name"],
            "last_name": self.last_name,
            "age": member["age"]
            "lucky_number": member ["lucky_number"]
        }
        pass

    def delete_member(self, id):
        # fill this method and update the return
        pass

    def get_member(self, id):
        # fill this method and update the return
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
