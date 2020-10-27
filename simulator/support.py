"""Module containing supporting classes and methods for the simulator."""

import random                    # for random numbers
import statistics                # for metrics
import matplotlib.pyplot as plt  # for plotting


def generate_uniform_loads(
        size=10,
        low=1,
        high=10,
        rng_seed=None):
    """Returns a list of loads from a uniform distribution.

    Parameters
    ----------
    size : int
        Number of loads to generate (size of the list).
    low : int [default=1]
        Lower boundary of the load interval.
    high : int [default=10]
        Upper boundary of the load interval.
    rng_seed : int [default=None]
        Random number generator seed.

    Returns
    -------
    list of int
        List of loads of length 'size'
    """
    random.seed(rng_seed)
    loads = [random.randrange(low, high) for i in range(size)]
    return loads


def evaluate_mapping(
        mapping,
        task_loads,
        num_resources,
        verbose=True):
    """Provides basic statistics from a task mapping.

    Parameters
    ----------
    mapping : list of int
        Mapping of tasks to resources
    task_loads : list of int or float
        Load of the tasks
    num_resources : int
        Number of resources
    verbose : bool [default=True]
        True if messages should be printed

    Returns
    -------
    list of int or float
        Load of the resources

    Notes
    -----
    List of metrics:
    - average resource load
    - median resource load
    - maximum resource load
    - minimum resource load
    - load standard deviation
    - load imbalance (maximum/average - 1)
    """
    # Number of tasks
    num_tasks = len(task_loads)
    # Computes the load per resource (and the number of tasks per resource)
    resource_loads = [0] * num_resources
    tasks_per_resource = [0] * num_resources
    for task in range(num_tasks):
        resource = mapping[task]
        resource_loads[resource] += task_loads[task]
        tasks_per_resource[resource] += 1

    # Prints information if verbose
    if verbose:
        # Computes metrics
        avg_load = statistics.mean(resource_loads)
        median_load = statistics.median(resource_loads)
        max_load = max(resource_loads)
        min_load = min(resource_loads)
        stdev_load = statistics.stdev(resource_loads)
        load_imbalance = max_load/avg_load - 1
        # Prints metrics
        print('** Mapping report **')
        print(f'- Number of tasks: {num_tasks}')
        print(f'- Number of resources: {num_resources}')
        print(f'- Task loads: {task_loads}')
        print(f'- Task mapping: {mapping}')
        print(f'- Tasks per resource: {tasks_per_resource}')
        print(f'- Resource loads: {resource_loads}')
        print(f'* Metrics *')
        print(f'- Average resource load: {avg_load}')
        print(f'- Median resource load: {median_load}')
        print(f'- Maximum resource load: {max_load}')
        print(f'- Minimum resource load: {min_load}')
        print(f'- Load standard deviation: {stdev_load}')
        print(f'- Load imbalance: {load_imbalance}')
        print('** End of report **')

    return resource_loads


def plot_mapping(
        mapping,
        task_loads,
        num_resources,
        filename=None):
    """Creates a bar plot representing the mapping.

    Parameters
    ----------
    mapping : list of int
        Mapping of tasks to resources
    task_loads : list of int or float
        Load of the tasks
    num_resources : int
        Number of resources
    filename : string [default=None]
        Name of the file to store the plot

    Notes
    -----
    The bar plot represents each resource in the horizontal axis and
    its load in the vertical axis.
    """
    # Compute the resource loads
    resource_loads = evaluate_mapping(
            mapping,
            task_loads,
            num_resources,
            False)

    # Plots
    plt.bar(range(num_resources), resource_loads)
    plt.ylabel('Load (a.u.)')
    plt.xlabel('Resources')
    plt.title('Resource loads')

    # Saves the plot in a file if a filename is given
    if filename is not None:
        plt.savefig(filename, bbox_inches='tight')

    # Shows plot
    plt.show()
