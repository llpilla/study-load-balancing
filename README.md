# Practical load balancing activity

This repository is intended for use by students to practice concepts related to load balancing algorithms.
It contains a few scheduling algorithms and some support functions.
A set of activities using this repository is presented in the [activities section](#activities) below.

## How To

- The code in this repository is written using Python3 and a few of its modules.
In order to check and install any missing modules, run `python3 setup.py`.

- To run a code example, try `python3 complete_example.py`.

- To learn more about the schedulers and support functions, try the code below in your Python3 interpreter:

```python
>>> import simulator.schedulers as schedulers
>>> help(schedulers)
>>> import simulator.support as support
>>> help(support)
```

- To check if the code you downloaded or changed is still working properly, try the following commands:

```bash
$ cd unitary_tests
$ ./test_implemented_schedulers.py 
$ ./test_support.py
```

- To check if the new schedulers you have implemented are working as intended, try the following commands:

```bash
$ cd unitary_tests
$ ./test_other_schedulers.py 
```

## Activities

**Basic steps**

0. Run `python3 complete_example.py` and try to understand its results. Check how to write code to use this simple load balancing simulator.

1. Run experiments with the available algorithms for small and large numbers of tasks and resources and compare their performance.

2. Focus on the list scheduling algorithm (*list\_scheduler*). Try to create an adversary (i.e., worst-case) scenario that leads to a schedule that is (*2 - 1/m*) from the optimal for *m=2* and *m=3* resources. For instance, if the optimal schedule on two resources has a makespan equal to 10, then the worst-case schedule by the list scheduling algorithm should result in a makespan equal to *10x(2-1/2)=15*. Experiment with small numbers of tasks and small loads for a better result.

3. Write the Largest Processing Time (LPT) list scheduling algorithm (complete function *lpt* in [the schedulers file](simulator/schedulers.py)). Check if it passes the test in [the unitary tests' file](unitary_tests/test_other_schedulers.py). Compare how LPT performs for the adversary case of the basic list scheduler from step 2.

4. Run experiments the basic list scheduler and the LPT policy with small and large numbers of tasks and resources. Analyze how similarly or differently they behave in the different scenarios.

5. Write the LPT algorithm with an additional restriction on the maximum number of tasks per resource (complete function *lpt\_with\_limits*). Check if it passes the test in the unitary tests' file.

6. Compare how this new LPT algorithm performs compared with its original code for increasingly restrictive scenarios. Show a situation where their makespans differ significantly for the same set of tasks and resources.

**Additional challenge**

7. Focus on the LPT algorithm. Try to create an adversary scenario that leads to a schedule that is (*4/3 - 1/3m*) from the optimal for *m=3* resources.

8. Write the list scheduling algorithm for uniform resources (complete function *list\_scheduler\_for\_uniform\_resources*). Check if it passes the test in the unitary tests' file. Describe your solution and show how it performs for one scenario of your choice.


