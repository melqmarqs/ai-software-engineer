def structures_manipulation():
  technologies = [
    'Python',
    'C#',
    'JavaScript',
    'Python',
    'TypeScript',
    'C#'
  ]

  # remove duplicated values
  unique_technologies = set(technologies)

  # parse to list
  techs = list(unique_technologies)

  # tuple storing the first 3 techs
  used_techs = (techs[0], techs[1], techs[2])

  project_description = {
    'name': 'card02',
    '# technologies': len(techs),
    'used techs': used_techs
  }

  print(project_description)

def list_and_lambda():
  scores = [0.85, 0.92, 0.45, 0.78, 0.98, 0.61]
  approved = [
    score
    for score in scores
    if score > 0.80
  ]
  scores_ = [score * 100 for score in scores]
  ordered = sorted(scores, reverse=True)

  print(scores)
  print(approved)
  print(scores_)
  print(ordered)

def calculate_average(numbers: list[float]) -> float | None:
  if not numbers:
    return None

  negativeNumbers = [
    number
    for number in numbers
    if number < 0
  ]

  if negativeNumbers:
    raise ValueError('Only positive numbers are allowed')

  return sum(numbers) / len(numbers)

def divide(dividend: float, divisor: float) -> float | None:
  if divisor <= 0:
    raise ValueError('Numbers must be positive')
  
  return dividend / divisor

def find_technology(techs: list[str], search: str) -> bool:
  # Pythonic
  return any(
    tech.casefold() == search.casefold()
    for tech in techs
  )

def main():
  print('----- Manipulation of structures -----')
  structures_manipulation()
  print()

  print('----- Lists and lambda -----')
  list_and_lambda()
  print()

  print('----- Calculate average -----')
  try:
    print(calculate_average([2, 5, -1, 20, 18, 102, 3]), '\n')
  except ValueError as error:
    print(f'Invalid value: {error} \n')

  print('----- Divide -----')
  try:
    dividend = float(input('Enter the dividend: '))
    divisor = float(input('Enter the divisor: '))
    result = divide(dividend, divisor)
    print(f'Result: {result}')
  except ValueError as error:
    print(f'Invalid value: {error}')
  finally:
    print()

  print('----- Find my technology -----')
  technologies = [
    'React.js',
    'Next.js',
    'Go',
    'C#',
    'Node.js'
  ]
  search_for = 'go'
  result = find_technology(technologies, search_for)
  print(f'{search_for}: {result}')

if __name__ == '__main__':
  main()