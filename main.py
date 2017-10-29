from datetime import date


def number_to_digit_list(number):
  digit_list = list(str(number))
  if '.' in digit_list:
    digit_list.remove('.')
  map(int,digit_list)
  return digit_list

def get_pi_digits(precision):
  try:
      # import version included with old SymPy
      from sympy.mpmath import mp

  except ImportError:
      # import newer version
      from mpmath import mp

  mp.dps = precision  # set number of digits
  return number_to_digit_list(mp.pi)

def find_sequence_in_list(base_list, sequence):
  for i in range(len(base_list)):
    for j in range(len(sequence)):
      if base_list[i+j] != sequence[j]:
        break
      if j == len(sequence) - 1:
        return i
  return -1

def find_nth_digit(pi_list,today):
  '''
    TODO: Run again with a higher get_pi(digit) if 
    find_sequence_in_list returns -1 until a result is found
  '''
  formatted_date = int(str(today.month) + str(today.day))
  date_list = number_to_digit_list(formatted_date)
  return find_sequence_in_list(pi_list, date_list)

def write_message(pi_list,today):
  d = today.strftime('%B %-d')
  n = find_nth_digit(pi_list,today)
  s = ''
  if n % 10 == 1:
    s = 'th'
  elif n % 10 == 2:
    s = 'nd'
  elif n % 10 == 3:
    s = 'rd'
  else:
    s = 'th'
  
  return "{} is just another name for {}{}-Digit-of-Pi Day!\n".format(d,n,s)

def test():
  pi_digits = get_pi_digits(20000)  
  test_dates = [
    date(2017,3,14),
    date(2017,10,27),
    date(2017,4,15),
    date(2017,10,31),
    date(2017,9,21),
    date(2000,8,31),
    date(2017,1,1),
    date(2017,11,11),
    date(2017,12,12),
    date(2017,12,21),
    date(2017,12,25),
  ]
  for test_date in test_dates:
    print(write_message(pi_digits,test_date))

test()
