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

def number_to_suffix(number):
    if 11 <= number % 100 <= 13:
        return 'th'
    elif number % 10 == 1:
        return 'st'
    elif number % 10 == 2:
        return 'nd'
    elif number % 10 == 3:
        return 'rd'
    else:
        return 'th'

def write_message():
    today = date.today()
    formatted_date = int(str(today.month) + str(today.day))
    date_digits = number_to_digit_list(formatted_date)
    
    precision = 20000
    pi = get_pi(precision)
    pi_digits = number_to_digit_list(pi)
    
    d = today.strftime('%B %-d')
    n = find_sequence_in_list(pi_digits, date_digits)

    while n < 0:
        precision *= 2
        pi = get_pi(precision)
        pi_digits = number_to_digit_list(pi)
        n = find_sequence_in_list(pi_digits, date_digits)
    
    s1, s2 = number_to_suffix(today.day), number_to_suffix(n)
    
    return "{}{} is just another name for {}{}-Digit-of-Pi Day!\n".format(d,s1,n,s2)
