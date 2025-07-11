import copy
import random
import sys 
sys.setrecursionlimit(10**6) 


""" Helper functions for checking operator's conditions """

def can_eat(state):
    for eatable in state:
        # Check if 'p' and either 'd' or 'f' are in the same sublist
        if 'p' in eatable and ('d' in eatable or 'f' in eatable):
            return True
    return False


def can_move_right(state):
    #if 'p' is anywhere except the right corner of the list it can move right
    return not state[5][0]=='p'

def can_move_left(state):
    #if 'p' is anywhere except the left corner of the list it can move left
    return not state[0][0]=='p'


""" Operator function: eat, move right, move left """

def eat(state, i):
    if state[i][1] == 'f':
        state[i][1] = ''
    elif state[i][1] == 'd':
        #Ganerate a random food in any of the available places in state
        positions = []
        for x in range(len(state)):
            if state[x][1] == '':
                #keeps the positions that are available (no 'p', 'f' or 'd' inside them)
                positions.append(x)
        if positions:
            """
                -Genarates a random number from 0-(lenght of positions)
                -Uses this number as index for the positions list and takes the position that is stored
                -Uses this position to access and place a new 'f' in the state 
                -Then the d that the Pac Man  ate is removed from the state
            """
            ran = random.randint(0,len(positions)-1)
            state[positions[ran]][1] = 'f'
        state[i][1] = ''
    return

def move_right(state):
    if can_move_right(state):
        for i in range(len(state)):
            if state[i][0]=='p':
                state[i][0]=''
                state[i+1][0]='p'   #Move PacMan one place to the right
                if can_eat(state): #if there is 'f' or 'd' in the sublist, use the functions above to eat it
                    eat(state, i+1)
                return state
    else:
        return None
    

def move_left(state):
    if can_move_left(state):
        for i in range(len(state)):
            if state[i][0]=='p':
                state[i][0]=''
                state[i-1][0]='p'   #Move PacMan one place to the left
                if can_eat(state):
                    eat(state, i-1)
                return state
    else:
        return None

""" Function that checks if current state is a goal state """  

def is_goal_state(state):
    """
    -Goes through all the cells of the state and checks if there is any 'd' or 'f'.
    -If not, then we have reached the goal state and the function returns True
    """
    for cell in state:
        if 'd' in cell or 'f' in cell:
            return False
    return True

""" Function that finds the children of current state """

def find_children(state, path):
    children = []
    #Genarate the left child of the state, which is the pacman moving left
    left_state = copy.deepcopy(state)
    child_left = move_left(left_state)
    if child_left is not None:
        children.append((child_left, path + [child_left])) #Put left child in the children list
    #Genarate the right child of the state, which is the pacman moving right
    right_state = copy.deepcopy(state)
    child_right = move_right(right_state)
    if child_right is not None:
        children.append((child_right, path + [child_right])) #Put right child in the children list

    return children


def manhattan_distance(state):
    """
    - Calculates the Manhattan distance between the pacman and the closest food or 'd' in the given state.
    - If no pacman or food/destination is found, it returns infinity.
    """

    # Index of the Pacman in the grid. Initialized to -1 (not found).
    pacman_index = -1

    # List of indices where food ('f') or destination ('d') is located in the grid.
    food_indices = []

    # Iterate over the grid to find Pacman and 'f'/'d' locations.
    for i, cell in enumerate(state):
        # Check if Pacman ('p') is in the current cell.
        if cell[0] == 'p':
            pacman_index = i
        # Check if 'f' or 'd' is in the second position of the cell.
        if cell[1] == 'f' or cell[1] == 'd': 
            food_indices.append(i)

    # If no Pacman or no f/d is found, return infinity.
    if pacman_index == -1 or not food_indices:  
        return float('inf')

    # Return the minimum Manhattan distance between Pacman and any f/d.
    # Manhattan distance in this context is simplified to absolute index difference.
    return min(abs(pacman_index - food_index) for food_index in food_indices)



def make_front(state):
    # Initializes the front with the starting state.
    # The front is a list of tuples, where:
    # - The first element of each tuple is a state.
    # - The second element is the path taken to reach that state (initially just the starting state).
    return [(state, [state])]
    

def expand_front(front, method):  
    if method == 'DFS':        
        if front:
            #Erases the first element of front and puts it in node - path
            node, path = front.pop(0)   #node: The state of front[0]    path: A list of the path towards the current node
            children = find_children(node, path)    #Uses find_children() to genarate the left and right child of the state
            for child in children:
                front.insert(0, child)  #DFS inserts child at the front of the front list 
    elif method == 'BFS':
        if front:
            node, path = front.pop(0)
            children = find_children(node, path)
            for child in children:
                front.append(child) #BFS inserts child at the back of the front list 
    elif method == 'A*':
        if front:
            node, path = front.pop(0)
            children = find_children(node, path)
            for child, child_path in children:
                # Calculate the total cost: path length (g-cost) + Manhattan distance (h-cost).
                cost = len(child_path) + manhattan_distance(child)

                # Check if this child node is already in the front. 
                existing = next((f for f in front if f[0] == child), None)
                if existing:
                    # If the child node is already in the front, compare costs.
                    existing_cost = len(existing[1]) + manhattan_distance(existing[0])
                    if cost < existing_cost:
                        # If the new path to the child node is cheaper, replace the old one.
                        front.remove(existing)
                        front.append((child, child_path))  
                else:
                    # If the child node is not in the front, add it to the front.
                    front.append((child, child_path))
            # Sort the front by total cost (f-cost = g-cost + h-cost) in ascending order.
            front.sort(key=lambda x: len(x[1]) + manhattan_distance(x[0]))
    
    return front


def find_solution(front, closed, method):
    # Base case: If the front is empty, no solution is found.
    if not front:
        print('_NO_SOLUTION_FOUND_')
        return
    
    # Get the first node and its path from the frontier.
    node, path = front[0]

    # If the current node has already been visited, skip it and continue with the rest of the frontier.
    if node in closed:
        find_solution(front[1:], closed, method)
    # If the current node is the goal state, print the solution and the path leading to it.
    elif is_goal_state(node):
        print('_GOAL_FOUND_')
        print(f"Goal State: {node}")
        print("\nPath to Goal:")
        for state in path:
            print(state)
    # Otherwise, expand the node:
    else:
        # Add the node to the closed list to mark it as visited.
        closed.append(node)
        # Expand the front by generating children nodes and their respective paths.
        # `expand_front` adds the new states to the front according to the chosen search method.
        front_copy = expand_front(front, method)
        # Recursively call `find_solution` with the updated front and closed list.
        find_solution(front_copy, closed, method)

           
def main():

    initial_state=[['','d'],['','f'],['p',''],['',''],['','f'],['','']]   

    ans1 = int(1)
    while ans1 == 1:        
        ans2 = int(input("How you want to run the game?\n1.DFS\n2.BFS\n3.A*\n\nGive the number you want: "))
        if ans2 == 1:
            method='DFS'
        elif ans2 == 2:
            method='BFS'
        elif ans2 == 3:
            method='A*'

        print("______________________________________________________________________")
        print('____BEGIN__SEARCHING____\n')
        find_solution(make_front(initial_state), [], method)
        print("______________________________________________________________________")
        input("\n\nPress [ENTER] to continue. . .")
        print("\n" * 3)
        ans1 = int(input("Would you like to play again?\n0.No\n1.Yes\nGive your number: "))
        print("\n" * 3)




if __name__ == "__main__":
    main()