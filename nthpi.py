from datetime import date
import random


def get_pi(precision):
    try:
        # import version included with old SymPy
        from sympy.mpmath import mp
 
    except ImportError:
        # import newer version
        from mpmath import mp

    mp.dps = precision  # set number of digits
    return mp.pi

def number_to_digit_list(number):
    digit_list = list(str(number))
    if '.' in digit_list:
        digit_list.remove('.')
    map(int,digit_list)
    return digit_list

def find_sequence_in_list(base_list, sequence):
    for i in range(len(base_list)):
        for j in range(len(sequence)):
            if base_list[i+j] != sequence[j]:
                break
            if j == len(sequence) - 1:
                return i
    return -1

def write_message():
    start_date = date.today().replace(day=1, month=1).toordinal()
    end_date = date.today().toordinal()
    random_date = date.fromordinal(random.randint(start_date, end_date))
    formatted_date = int(str(random_date.month) + str(random_date.day))
    date_digits = number_to_digit_list(formatted_date)
    
    precision = 20000
    pi = get_pi(precision)
    pi_digits = number_to_digit_list(pi)
    
    d = random_date.strftime('%B %-d')
    n = find_sequence_in_list(pi_digits, date_digits)

    while n < 0:
        precision *= 2
        pi = get_pi(precision)
        pi_digits = number_to_digit_list(pi)
        n = find_sequence_in_list(pi_digits, date_digits)

    s = ''
    if 11 <= n % 100 <= 13:
        s = 'th'
    elif n % 10 == 1:
        s = 'st'
    elif n % 10 == 2:
        s = 'nd'
    elif n % 10 == 3:
        s = 'rd'
    else:
        s = 'th'

    return "{} is just another name for {}{}-Digit-of-Pi Day!\n".format(d,n,s)
