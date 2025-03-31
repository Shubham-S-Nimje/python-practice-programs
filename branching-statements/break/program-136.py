# Write a program to find input number is prime
while True:
  print('1. Deposit')
  print('2. Withdraw')
  print('3. Check Balance')
  print('4. Exit')
  opt=int(input('Enter your option :'))
  match(opt):
    case 1:
      print('Selected Deposit Option')
    case 2:
      print('Selected Withdraw Option')
    case 3:
     print('Selected Check Balance Option')
    case 4:
      print('Thanks for using ATM')
      break
    case _:
      print('Invalid Option Try Again...')