from abc import ABC, abstractmethod

class User(ABC):
  def __init__(self, name: str, email: str):
    self.name = name
    self.email = email

  @property
  def name(self) -> str:
    return self._name

  @name.setter
  def name(self, value: str):
    if not value.strip():
      raise ValueError('Invalid name.')

    self._name = value.strip().upper()

  @property
  def email(self) -> str:
    return self._email

  @email.setter
  def email(self, value: str):
    if "@" not in value.strip():
      raise ValueError('Invalid email.')

    self._email = value.strip().casefold()

  @abstractmethod
  def get_role(self) -> str:
    pass