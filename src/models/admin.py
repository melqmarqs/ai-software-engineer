from src.models.user import User

class Admin(User):
  def __init__(self, name: str, email: str, permissions: list[str]):
    super().__init__(name, email)
    self.permissions = permissions

  def get_role(self):
    return 'Administrator'

  def get_permissions(self) -> list[str]:
    return self.permissions