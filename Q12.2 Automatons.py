input = open('Q12_input.txt', 'r').readlines()

map5 = []
for line in input:
    str, nbs = line.split()
    map5.append([(str+'?')*4 + str+'.', tuple([int(c) for c in nbs.split('\n')[0].split(',')]*5)] )   # ALL STRINGS END WITH A .
    

def word(tuple):  #gives a word of # and ., starting and ending with .
    w = '.'
    for k in tuple:
        w += '#'*k
        w += '.'
    return w

def automaton_step(states, autom, c):   # update states of an automaton wgen applying character c
    updated_states = {}
    for i in states:  # for each (non-empty) state
        if c == '.' :
            if autom[i] == '.': updated_states[i]= updated_states.get(i,0) +  states[i]
            elif autom[i+1] == '.': updated_states[i+1]= updated_states.get(i+1,0) +  states[i]  # autom[i] = #
        if c == '#' :
            try:
                if autom[i+1] == '#' : updated_states[i+1] = updated_states.get(i+1,0) + states[i]
            except IndexError : pass # that was the end of the automaton
        if c == '?' : 
            if autom[i] == '.': updated_states[i]= updated_states.get(i,0) +  states[i]
            elif autom[i+1] == '.': updated_states[i+1]= updated_states.get(i+1,0) +  states[i]  # autom[i] = #
            try: 
                if autom[i+1] == '#' : updated_states[i+1] = updated_states.get(i+1,0) + states[i]  
            except IndexError : pass #that was the last character, which is a .
                
    return updated_states

def automaton_end(str, autom): # given a string str with ?, apply the automaton determined by word. Return the amount of elmt at the last position
    states = {0:1}  # nbs d'élmts en chaque position
    for c in str:
        states = automaton_step(states, autom, c)
    return states.get(len(autom)-1, 0)

print(sum([automaton_end(str, word(nbs)) for str, nbs in map5]))
