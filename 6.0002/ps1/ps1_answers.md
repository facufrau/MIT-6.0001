## Answer the following questions in a file called ps1_answers.

1. What were your results from compare_cow_transport_algorithms? Which
algorithm runs faster? Why?

- The greedy algorithm runs faster, the difference is more noticeable when the number of items is bigger.
For 8 items there is no visible difference in runtime, but for 13 items the greedy algorithm finds a solution quick while the brute force solution could not find an answer.

2. Does the greedy algorithm return the optimal solution? Why/why not?

- Not always, because it selects the biggest cow for each trip the solution is not the optimal

3. Does the brute force algorithm return the optimal solution? Why/why not?

- Yes, because it generate all the posible combinations and finds the first that satisfies all the criteria.