from src.models.user import User
from src.models.address import Address

class Customer(User):
  def __init__(self, name: str, email: str, address: Address):
    super().__init__(name, email)
    self.address = address

  def get_role(self):
    return 'Customer'