####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Colluders'
strategy_name = 'Collude until betrayed or untill our opponets guard is down'
strategy_description = '''I will collude with my opponent untill they betray me or until they have colluded with me 90 times in a row.'''

   
def move(my_history, their_history, my_score, their_score):
    collude = 0
    if len(my_history)==0:
        return 'c'

    if len(their_history)>0 and their_history[-1] == 'c':
        collude += 1
    else:
        collude = 0
    if 'b' in their_history or collude > 90:
        return 'b'
    else:
        return 'c'
 
        
         

            
    
    