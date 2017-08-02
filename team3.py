import random

####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Scott Andy remix' # Only 10 chars displayed.
strategy_name = 'Andy and Scott'
strategy_description = 'Betray for guesses 1-3, random for 7-10, then we look at last 10 values of their guesses and if there are more than 5 colludes, we betray.  Otherwise, we collude. every 20th move, we choose 3 random guesses'
    
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    if len(their_history)<4:
        return 'c'
    
    #elif len(their_history)<10:
    #    a = random.randint(1,2)
    #    if a == 1:
    #        return 'b'
    #    else:
    #        return 'c'
    
    # The code below is for "Crazy Ivans"
    #elif len(their_history) % 20 == 0:
    #    a = random.randint(1,2)
    #    if a == 1:
    #        return 'b'
    #    else:
    #        return 'c'
    #elif len(their_history)-1 % 20 == 0:
    #    a = random.randint(1,2)
    #    if a == 1:
    #        return 'b'
    #    else:
    #        return 'c'
    #elif len(their_history)-2 % 20 == 0:
    #    a = random.randint(1,2)
    #    if a == 1:
    #        return 'b'
    #    else:
    #        return 'c'
    
    else:
        temp = their_history[-1]

        #This section below would be to look at more of their history...
        '''stepper = int(0)
        print(stepper)
        tempsum = int(0)
        while stepper < 10:
            if temp[stepper] == 'c':
                tempsum=tempsum+1
                stepper = stepper +1
            else:
                stepper = stepper + 1
        stepper = int(0)
        if tempsum > 2:
            return 'c'
        else:
            return 'b'
        '''
        
        if their_history[1]=="b":
            return 'b'
        else:
            return 'c'
