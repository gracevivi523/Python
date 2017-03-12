raw_input_1 = int(raw_input("raw_input:"))
raw_input_2 = int(raw_input("raw_input:"))
raw_input_3 = int(raw_input("raw_input:"))


#Check if the number is multiples of all 3 specific numbers
def three_param_checked(e):
    global boolean_param_3
    if e%raw_input_1==0 and e%raw_input_2==0 and e%raw_input_3==0 :
        print 'FizzBuzzWhizz,'
        boolean_param_3 = 1

#Check if the number is multiple of 2 out of 3 specific numbers
def two_param_checked(e):
    global boolean_param_2
    if e%raw_input_1==0 and e%raw_input_2==0:
        print 'FizzBuzz,'
        boolean_param_2 = 1
    elif e%raw_input_2==0 and e%raw_input_3==0:
        print 'BuzzWhizz,'
        boolean_param_2 = 1
    elif e%raw_input_1==0 and e%raw_input_3==0:
        print 'FizzWhizz,'
        boolean_param_2 = 1

#Check if the number is multiple of 1 out of 3 specific number
def one_param_checked(e):
    global boolean_param_1
    if e%raw_input_1==0:
        print 'Fizz,'
        boolean_param_1 = 1
    elif e%raw_input_2==0:
        print 'Buzz,'
        boolean_param_1 = 1
    elif e%raw_input_3==0:
        print 'Whizz,'
        boolean_param_1 = 1
        
#Check if the number contains 1st specific number
def bit_param_checked(e):
    global boolean_bit_flag
    if str(e).__contains__(str(raw_input_1)):
        print 'Fizz,'
        boolean_bit_flag = 1

#Main logic
for i in xrange(1,101):
    boolean_param_3 = 0; boolean_param_2 = 0;boolean_param_1 =0
    boolean_bit_flag = 0
    bit_param_checked(i)
    
    #Follow rule 3,4 in README.txt if the number does not follow rule 5
    if boolean_bit_flag != 1:
        three_param_checked(i)
        if boolean_param_3 != 1:
            two_param_checked(i)
            if boolean_param_2 != 1:
                one_param_checked(i)
    
    if boolean_param_3 == 0 and boolean_param_2 ==0 and boolean_param_1 ==0 and boolean_bit_flag == 0:
        print '%d,' %(i)
