#Group Members: Caroline Ek, Serafina Yu, Zeid Zawaideh 

from search import *

class WolfGoatCabbage(Problem):
    """This method serves as the constructor for the WolfGoatCabbage class. It initializes the initial state and goal state of the problem."""
    def __init__ (self, initial = frozenset({'F','G','C','W'}) , goal = set()):
        super().__init__(initial,goal)
        self.initial = initial
        self.goal = goal
    
    def goal_test(self, state):
        """This method returns True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        return state == self.goal
    
    def result(self, state, action):
        """This method returns the state that results from executing the given action in the given state. 
        This function initializes an empty set called new state which will be used to create a copy of the current given state.
        It will check the given state (new state) and see if 'F' (farmer) exists.
        If so, this means 'F' is on the left bank. Then, it will iterate through the action and remove it from the given state (Moving items from left bank to right bank)
        item and travels to the right bank). If 'F' does not exist, add it to the new state (Moving items from right bank to left bank). 
        Since the program only keeps track of items on the left bank, this ensures
        the direction of item movement. It returns the frozenset state, representing the state after applying
        the action.
        
        EX: ({'F', 'W', 'C', 'G'}, {'F', 'G'}) 
        - The first set is the given state, second set is the action. 
        - Since 'F' exists in the given set, iterate through actions
        and remove it from the given set. 
        - New state: {'W', 'C'}. The farmer and goat have moved to the right bank.
        
        EX: ({'F', 'G'}, {'F', 'W', 'C', 'G'}) 
        - The first set is the given state, second set is the action. 
        - Since 'F' does not exist in the given set, iterate through actions and add it to the given set.
        - New state: {'F', 'W', 'C', 'G'}. The farmer and goat have moved to the left bank."""
        
        new_state = set() #make a copy
        for i in state: 
            new_state.add(i)
        
        #Moving to the right bank; else move to the left bank
        if 'F' in new_state:
            for i in action:
                new_state.remove(i)
        else:
            for i in action:
                new_state.add(i)

        frozen_new = frozenset(new_state)
        return frozen_new
        
    def actions(self, state):
        """This method determines the possible actions that can be taken from a given state. 
        It evaluates the current state and returns a list of possible actions that can be performed from that state."""
        
        possible_actions = []
        
        if state == {'F', 'W', 'C', 'G'}:
            possible_actions.append({'F', 'G'})
        if state == {'C', 'W'}:
            possible_actions.append({'F'})
            possible_actions.append({'F', 'G'})
        if state == {'F', 'C', 'W'}:
            possible_actions.append({'F'})
            possible_actions.append({'F', 'C'})
            possible_actions.append({'F', 'W'})
        if state == {'W'}:
            possible_actions.append({'F', 'C'})
            possible_actions.append({'F', 'G'})
        if state == {'C'}:
            possible_actions.append({'F', 'W'})
            possible_actions.append({'F', 'G'})
        if state == {'F', 'G', 'W'}:
            possible_actions.append({'F', 'G'})
            possible_actions.append({'F', 'W'})
        if state == {'F', 'C', 'G'}:
            possible_actions.append({'F', 'G'})
            possible_actions.append({'F', 'C'})
        if state == {'G'}:
            possible_actions.append({'F', 'W'})
            possible_actions.append({'F', 'C'})
            possible_actions.append({'F'})
        if state == {'F', 'G'}:
            possible_actions.append({'F'})
            possible_actions.append({'F', 'G'})
        if state == {}:
            possible_actions.append({'F', 'G'})
            
        return possible_actions
            
if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)