from src.models.user import User


class UserService:
  def __init__(self):
    self.users: list[User] = []

  def get_all_users(self) -> list[User]:
    return self.users

  def get_user_by_email(self, email: str) -> User | None:
    try:
      found_users = [
        user
        for user in self.users
        if user.email == email.strip().casefold()
      ]
      if not found_users:
        raise ValueError(f'User ({email}) not found.')

      return found_users[0]
    except Exception as error:
      print('Error: ', error)

  def create_user(self, newUser: User) -> User | None:
    try:
      already_exists = any(
        user.email == newUser.email
        for user in self.users
      )
      
      if already_exists:
        raise ValueError(f'User ({newUser.email}) already exists')

      self.users.append(newUser)
      print(f'User {newUser.email} created.')
      return newUser
    except Exception as error:
      print('Error: ', error)

  def delete_user(self, email: str) -> bool:
    found_users = [
      user
      for user in self.users
      if user.email == email.strip().casefold()
    ]

    if not found_users:
      print('User does not exist')
      return False

    self.users.remove(found_users[0])
    print(f'User {found_users[0].name} was deleted.')
    return True
