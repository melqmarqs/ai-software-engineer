from src.models.address import Address
from src.models.admin import Admin
from src.models.customer import Customer
from src.services.user_service import UserService


def main():
  user_service = UserService()

  address = Address(
    street='White Street',
    city='Outbell',
    postal_code='32010'
  )

  customers = ['John Doe', 'Taylor Carl', 'Anna Swey']
  for customer in customers:
    new_customer = Customer(
      name=customer,
      email='.'.join(customer.strip().split()) + '@email.com',
      address=address
      )
    user_service.create_user(new_customer)

  admin = Admin(
    name='Jane Doe',
    email='jane.doe@email.com',
    permissions=['CREATE_USER', 'DELETE_USER']
  )

  user_service.create_user(admin)
  user_service.create_user(admin)

  user_service.delete_user(admin.email)

  users = user_service.get_all_users()
  for user in users:
    print(f'Name: {user.name}')
    print(f'Email: {user.email}')
    print(f'Role: {user.get_role()}\n')

  emails = ['jane.doe@email.com', 'blabla@email.com', 'blabla', 'Anna.swey@email.com']
  for email in emails:
    found_user = user_service.get_user_by_email(email)
    if found_user:
      print(f'Found user: {found_user.name} ({found_user.email})')

  

if __name__ == '__main__':
  main()