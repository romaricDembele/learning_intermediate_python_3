class School:
  def __init__(self, name, level, numberOfStudents):
    self._name = name
    self._level = level
    self._numberOfStudents = numberOfStudents

  def get_name(self):
    return self._name

  def get_level(self):
    return self._level

  def get_numberOfStudents(self):
    return self._numberOfStudents

  def set_numberOfStudents(self, numberOfStudents):
    self._numberOfStudents = numberOfStudents

  def __repr__(self):
    return f"A {self._level} school named {self._name} with {self._numberOfStudents} students."

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self._pickupPolicy = pickupPolicy
  
  def get_pickupPolicy(self):
    return self._pickupPolicy

  def __repr__(self):
    return super().__repr__() + f"The pickup policy of the primary school is {self._pickupPolicy}."

class MiddleSchool(School):
  def __init__(self, name, numberOfStudents):
    super().__init__(name, "middle", numberOfStudents)


class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportTeams):
    super().__init__(name, "high", numberOfStudents)
    self._sportTeams = sportTeams

  def get_sportTeams():
    return self._sportTeams

  def __repr__(self):
    return super().__repr__() + f"The sport teams of the high school are {self._sportTeams}."


school = School("School of greatness", "primary", 300)
print(school)

primary_school = PrimarySchool("primary_school", 200, "Pickup after 3pm")
print(primary_school)

high_school = HighSchool("School of god", 110, ['basketball', 'tennis'])
print(high_school)
