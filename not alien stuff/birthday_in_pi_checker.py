def load_pi(file_name):
    pi_string = ''
    with open(file_name) as f_o:
        for line in f_o:
            pi_string += line.rstrip()
    return pi_string

def million_check(bd):
    pi_string = load_pi('work_ch_5_up/pi_digits.txt')
    if bd in pi_string:
        print("your birthday appears!")
        print(f'it starts at digit # {pi_string.find(bd)},\n (where 3.14 are digits 1 2 and 3)')
        again_or_exit()
    else:
        choiceyn = input("sorry, its not! would you like to check the first BILLION digits? Y or N:  ")
        if choiceyn == 'Y' or choiceyn == 'y':
            billion_check(bd)
        if choiceyn == 'N' or choiceyn == 'n':
            again_or_exit()
        
def billion_check(bd):
    pi_string = load_pi('work_ch_5_up/pi-billion.txt')
    if bd in pi_string:
        print("your birthday appears!")
        print(f'it starts at digit # {pi_string.find(bd)},\n (where 3.14 are digits 1 2 and 3)')
    else: 
        print('bad luck! not in the first billion either!!')
        again_or_exit()
        
def again_or_exit():
    choiceyn = input('would you like to check a different birthday (Y or N)?  ')
    if choiceyn == 'Y' or choiceyn == 'y':
            start_checker()
    if choiceyn == 'N' or choiceyn == 'n':
            print('bye!')
            quit()

def start_checker():
    print('lets find your birthday in the first million pi digits!')
    birthday = input("enter your bday as mmddyy:  ")
    million_check(birthday)
    
start_checker()