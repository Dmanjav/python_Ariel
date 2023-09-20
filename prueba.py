def main():
  print(primo(7))
  print(primo(13))

def primo(number):
  if number < 2:
    return 'NO'
  for i in range(2, int(number/2)+1):
    if number % i == 0:
      return 'NO'
  return 'SI'


main()