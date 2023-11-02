## Answer the following questions in a file called ps1_answers.

### Problem A.5 - Writeup

1. What were your results from compare_cow_transport_algorithms? Which
algorithm runs faster? Why?

- The greedy algorithm runs faster, the difference is more noticeable when the number of items is bigger.
For 8 items there is no visible difference in runtime, but for 13 items the greedy algorithm finds a solution quick while the brute force solution could not find an answer.

2. Does the greedy algorithm return the optimal solution? Why/why not?

- Not always, because it selects the biggest cow for each trip the solution is not the optimal

3. Does the brute force algorithm return the optimal solution? Why/why not?

- Yes, because it generate all the posible combinations and finds the first that satisfies all the criteria.

### Problem B.2 - Writeup

1. Explain why it would be difficult to use a brute force algorithm to solve this problem if there 
were 30 different egg weights. You do not need to implement a brute force algorithm in order to 
answer this

- Because the number of iterations and calculations for the brute force solutions will be so high that a current computer could not calculate in a human time.

2. If you were to implement a greedy algorithm for finding the minimum number of eggs 
needed, what would the objective function be? What would the constraints be? What strategy 
would your greedy algorithm follow to pick which coins to take? You do not need to implement a 
greedy algorithm in order to answer this.

- The objective function will be the number of eggs, with the constraint of the weight. The greedy algorithm strategy will consist in picking every time the heaviest egg posible in each iteration.

3. Will a greedy algorithm always return the optimal solution to this problem? Explain why it is 
optimal or give an example of when it will not return the optimal solution. Again, you do not need 
to implement a greedy algorithm in order to answer this.

Not always the greedy algorithm will return the optimal solution. For example if we have a weight of 8 and eggs (1,4,5): the greedy algorithm will pick (5,1,1,1) and the optimal will be (4,4)