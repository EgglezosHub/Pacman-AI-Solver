# Pacman-AI-Solver
<h1>PacMan AI Solver</h1>

<h2>Project Overview</h2>

<p>
PacMan AI Solver is a Python-based project implementing classic and heuristic search algorithms (DFS, BFS, A*) to solve a simplified PacMan problem. The goal is for PacMan to eat all fruits ('f') and poisonous fruits ('d') from a linear grid of 6 cells, following specific movement and action rules.
</p>

<h2>Problem Definition</h2>

<h3>World Description</h3>
<p>
The world consists of <strong>6 cells</strong>, each of which can contain:
<ul>
    <li>PacMan ('p')</li>
    <li>Fruit ('f')</li>
    <li>Poisonous fruit ('d')</li>
    <li>Empty space ('')</li>
</ul>
</p>

<h3>Initial State</h3>
<p>
An example of an initial state is:
<pre>[['', 'd'], ['', 'f'], ['p', ''], ['', ''], ['', 'f'], ['', '']]</pre>
</p>

<p>
Constraints on the initial state:
<ul>
    <li>PacMan and a fruit cannot occupy the same cell initially.</li>
    <li>No more than one poisonous fruit ('d').</li>
    <li>No more than four fruits ('f') in total.</li>
</ul>
</p>

<h3>Goal State</h3>
<p>
A goal state is any state in which there are no fruits or poisonous fruits left on the grid. For example:
<pre>[['', ''], ['', ''], ['', ''], ['', ''], ['p', ''], ['', '']]</pre>
</p>

<h2>State Representation</h2>
<p>
Each state is represented as a list of lists:
<pre>
[
    ['', 'd'],
    ['', 'f'],
    ['p', ''],
    ['', ''],
    ['', 'f'],
    ['', '']
]
</pre>
- The first element in each sublist denotes the presence of PacMan ('p') or is empty ('').
- The second element denotes the presence of fruit ('f'), poisonous fruit ('d'), or is empty ('').
</p>

<h2>Operators (Transition Functions)</h2>

<p>The project defines the following operators:</p>

<ul>
    <li><strong>Move Left:</strong> PacMan moves one cell left if not at the leftmost edge.</li>
    <li><strong>Move Right:</strong> PacMan moves one cell right if not at the rightmost edge.</li>
    <li><strong>Eat:</strong> PacMan eats a fruit or poisonous fruit in the same cell. If PacMan eats a poisonous fruit ('d'), a new fruit ('f') is randomly generated in any empty cell.</li>
</ul>

<h2>Search Algorithms Implemented</h2>

<h3>1. Depth-First Search (DFS)</h3>
<p>
Explores paths as deep as possible before backtracking. DFS may explore many unnecessary paths and is not guaranteed to find the shortest solution.
</p>

<h3>2. Breadth-First Search (BFS)</h3>
<p>
Explores all nodes at the current depth before moving deeper. Guarantees the shortest path but consumes more memory.
</p>

<h3>3. A* Search</h3>
<p>
Uses the Manhattan distance as a heuristic to guide the search, combining path length (g-cost) with heuristic cost (h-cost). It is efficient for finding the optimal path while avoiding unnecessary exploration.
</p>

<h2>Heuristic Function: Manhattan Distance</h2>

<p>
The Manhattan distance is defined as:
<pre>distance = abs(pacman_index - fruit_index)</pre>
It measures how many steps PacMan needs to reach the nearest fruit or poisonous fruit.
</p>

<h2>Code Execution</h2>

<p>To run the program:</p>
<pre>
python pacman_solver.py
</pre>

<p>You will be prompted to select a search method:
<ul>
    <li>1 = DFS</li>
    <li>2 = BFS</li>
    <li>3 = A*</li>
</ul>
</p>

<h2>Sample Results</h2>

<h3>DFS Output:</h3>
<pre>
____BEGIN__SEARCHING____

_GOAL_FOUND_
Goal State: [['', ''], ['', ''], ['', ''], ['', ''], ['p', ''], ['', '']]

Path to Goal:
[['', 'd'], ['', 'f'], ['p', ''], ['', ''], ['', 'f'], ['', '']]
...
</pre>

<h3>BFS Output:</h3>
<pre>
____BEGIN__SEARCHING____

_GOAL_FOUND_
Goal State: [['', ''], ['', ''], ['', ''], ['', ''], ['p', ''], ['', '']]

Path to Goal:
[['', 'd'], ['p', ''], ['', ''], ['', ''], ['', 'f'], ['', '']]
...
</pre>

<h3>A* Output:</h3>
<pre>
____BEGIN__SEARCHING____

_GOAL_FOUND_
Goal State: [['', ''], ['', ''], ['', ''], ['', ''], ['p', ''], ['', '']]

Path to Goal:
[['', 'd'], ['p', ''], ['', ''], ['', ''], ['', 'f'], ['', '']]
...
</pre>

<h2>Comparison of Methods</h2>
<p>
<ul>
    <li><strong>DFS:</strong> Deep search, prone to exploring long, irrelevant paths. Memory-efficient but not always optimal.</li>
    <li><strong>BFS:</strong> Finds the shortest path but consumes significant memory due to storing many nodes.</li>
    <li><strong>A*:</strong> Most efficient, finding the optimal path quickly using heuristic guidance.</li>
</ul>
</p>

<h2>Conclusion</h2>
<p>
All implemented methods successfully solve the PacMan problem by finding a state where all fruits are eaten. Among the tested methods, A* provides the most efficient and optimal solution due to its heuristic guidance.
</p>
