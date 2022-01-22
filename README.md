# Stocastic Optimization

Implementaion of stocastic optimization algorithms in python.

## Genetic Algorithm

Genetic Algorithm run in main.py and can be run py importing GA.

### 1. 

Initialize the population by randomly generating N binary strings (chromosomes)

### 2. 

Evaluate the individuals:

#### 2.1. 

Decode chromosome to variables with Binary decoding.

#### 2.2. 

Evaluate the objective function f using the variable values obtained in the previous step, and assign a fitness value for each chromosone.

#### 2.3. 

Repeat steps 2.1 and 2.2 until the entire population has been evaluated.

### 3.

Form the next generation:

#### 3.1. 

Select two individuals from the evaluated population, such that individuals with high fitness have a greater probability of being selected.

#### 3.2. 

From the two selected chromosones genrate two new chromosones.

#### 3.3. 

Mutate the two chromosomes generated in the previous step.

#### 3.4.

Repeat steps 3.1–3.3 until N new individuals have been generated. Then replace the N old individuals by the N newly generated individuals.

### 4.

Return to step 2, unless the termination criterion has been reached.

## Particel Swarm

TODO

## Ant System

### 1.

Initialize pheromone levels: \[ \tau \] ij = \tau max , ∀ i, j ∈ [1, n].
### 2. 

For each ant select a random starting node, and add it to the (initiallyempty) tabu list. Next, build the tour S. In each step of the tour, select the move from node j to node i with probability p(e ij |S), given by:


\beta
\tau ij \alpha η ij
p(e ij |S) = 
\alpha \beta
ν l ∈L
/ T (S) \tau lj η lj
.

In the final step, return to the node of origin, i.e. the first element in L T .
Finally, compute and store the length D k of the tour.
### 3. 

Update the pheromone levels:

#### 3.1.

For the best ant (either the best in the current iteration or the best so far)[b]
determine \tau ij as:
[b] \tau ij = 1 D b0
if the best ant traversed the edge otherwise.

#### 3.2. 

Modify \tau ij :[b] \tau ij ← (1 − ρ)\tau ij + \tau ij .

#### 3.3.

Impose pheromone limits, such that \tau min ≤ \tau ij ≤ \tau max , ∀ i, j ∈ [1, n].

#### 3.4.

If 1/(ρD b ) > \tau max then update \tau max as \tau max ← 1/(ρD b ).

### 4. Repeat steps 2 and 3 until a satisfactory solution has been found.


# TODO

* Finish Ant_Sysytem and ParticleSwarm

* Testing