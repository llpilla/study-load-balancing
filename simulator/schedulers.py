"""Module containing scheduling algorithms.

Each scheduling algorithm receives a specific set of inputs and
outputs a mapping.

Implemented scheduling methods: round_robin, compact, uniformly_random,
list_scheduler.
Methods with interfaces but no implementation: lpt, lpt_with_limits,
list_scheduler_for_uniform_resources.
"""

import random  # for random mappings
import heapq   # for heaps (it implements only min-heaps)


def round_robin(
        num_tasks,
        num_resources,
        verbose=False):
    """Round-Robin scheduling algorithm.

    Parameters
    ----------
    num_tasks : int
        Number of tasks
    num_resources : int
        Number of resources
    verbose : bool [default=False]
        True if messages should be printed during scheduling

    Returns
    -------
    list of int
        Mapping of tasks to resources

    Notes
    -----
    A round-robin algorithm takes tasks in [lexicographical] order and
    maps them to a list of resources.
    The first task is mapped to the first resource.
    The second task is mapped to the second resource.
    When the list of resources is exhausted, we start again taking resources
    from the start.
    """
    if verbose:
        print(f'Round-Robin: starting with {num_tasks} tasks' +
              f' and {num_resources} resources.')
    # Empty mapping
    mapping = [None] * num_tasks

    # Iterates mapping tasks to resources in order
    for task in range(num_tasks):
        resource = task % num_resources
        mapping[task] = resource
        if verbose:
            print(f'- Mapping task {task} to resource {resource}')

    return mapping


def compact(
        num_tasks,
        num_resources,
        verbose=False):
    """Compact scheduling algorithm.

    Parameters
    ----------
    num_tasks : int
        Number of tasks
    num_resources : int
        Number of resources
    verbose : bool [default=False]
        True if messages should be printed during scheduling

    Returns
    -------
    list of int
        Mapping of tasks to resources

    Notes
    -----
    A compact algorithm takes tasks in [lexicographical] order and
    maps them to a list of resources.
    Tasks are partitioned in contiguous groups of similar size.
    The first group is mapped to the first resource.
    The second group is mapped to the second resource.
    Etc.
    """
    if verbose:
        print(f'Compact: starting with {num_tasks} tasks' +
              f' and {num_resources} resources.')
    # Empty mapping
    mapping = [None] * num_tasks

    # Size of partitions
    partition_size = num_tasks // num_resources
    # Number of resources that will have +1 tasks
    leftover = num_tasks % num_resources
    if verbose:
        print(f'- Size of partitions = {partition_size}')
        print(f'- Leftover = {leftover}')

    # Starting task identifier
    task = 0

    # Iterates over the resources mapping groups of tasks to them
    for resource in range(num_resources):
        # Sets the actual size of the group of tasks to map
        # to this resource based on the existence of any leftover
        if leftover > 0:
            group_size = partition_size + 1
            leftover -= 1
        else:  # No more resources with +1 tasks
            group_size = partition_size

        for i in range(group_size):
            mapping[task] = resource
            if verbose:
                print(f'- Mapping task {task} to resource {resource}')
            task += 1  # next task to map

    return mapping


def uniformly_random(
        num_tasks,
        num_resources,
        rng_seed=None,
        verbose=False):
    """Random scheduling algorithm.

    Parameters
    ----------
    num_tasks : int
        Number of tasks
    num_resources : int
        Number of resources
    rng_seed : int [default=None]
        Seed for the random number generator
    verbose : bool [default=False]
        True if messages should be printed during scheduling

    Returns
    -------
    list of int
        Mapping of tasks to resources

    Notes
    -----
    The random algorithm chooses resources uniformly at random for each task.
    """
    if verbose:
        print(f'Random: starting with {num_tasks} tasks' +
              f' and {num_resources} resources.')
        if rng_seed is not None:
            print(f'- RNG seed is {rng_seed}.')
    # Empty mapping
    mapping = [None] * num_tasks

    # Sets the RNG seed
    random.seed(rng_seed)

    # Iterates mapping tasks to resources in order
    for task in range(num_tasks):
        resource = random.randrange(num_resources)
        mapping[task] = resource
        if verbose:
            print(f'- Mapping task {task} to resource {resource}')

    return mapping


def list_scheduler(
        task_loads,
        num_resources,
        verbose=False):
    """Basic list scheduling algorithm.

    Parameters
    ----------
    task_loads : list of int or float
        Load of the tasks
    num_resources : int
        Number of resources
    verbose : bool [default=False]
        True if messages should be printed during scheduling

    Returns
    -------
    list of int
        Mapping of tasks to resources

    Notes
    -----
    The list scheduling algorithm takes tasks in [lexicographical] order
    and maps them to the least loaded resources.
    """
    if verbose:
        print(f'List Scheduler: starting with {len(task_loads)} tasks' +
              f' and {num_resources} resources.')
    # Empty mapping
    num_tasks = len(task_loads)
    mapping = [None] * num_tasks

    # Prepares the min-heap for the resources
    # Each item in the heap follows the convention (load, resource)
    resource_heap = [(0, resource) for resource in range(num_resources)]
    heapq.heapify(resource_heap)

    # Iterates over tasks mapping them to the least loaded resource
    for task in range(num_tasks):
        # Finds the least loaded resource
        resource_load, resource = heapq.heappop(resource_heap)
        mapping[task] = resource
        if verbose:
            print(f'- Mapping task {task} to resource {resource}')
        # Load of this task
        load = task_loads[task]
        # Updates the heap
        heapq.heappush(resource_heap, (resource_load + load, resource))

    return mapping


def lpt(
        task_loads,
        num_resources,
        verbose=False):
    """Largest Processing Time list scheduling algorithm.
    To implement.

    Parameters
    ----------
    task_loads : list of int or float
        Load of the tasks
    num_resources : int
        Number of resources
    verbose : bool [default=False]
        True if messages should be printed during scheduling

    Returns
    -------
    list of int
        Mapping of tasks to resources

    Notes
    -----
    This list scheduling algorithm takes tasks in decreasing load order
    and maps them to the least loaded resources.
    """
    if verbose:
        print(f'LPT: starting with {len(task_loads)} tasks' +
              f' and {num_resources} resources.')
    # Empty mapping
    num_tasks = len(task_loads)
    mapping = [None] * num_tasks
    # TODO

    return mapping


def lpt_with_limits(
        task_loads,
        num_resources,
        task_limit,
        verbose=False):
    """Largest Processing Time list scheduling algorithm with a
    constraint on the number of tasks per resource.
    To implement.

    Parameters
    ----------
    task_loads : list of int or float
        Load of the tasks
    num_resources : int
        Number of resources
    task_limit : int
        Maximum limit on the number of tasks per resource
    verbose : bool [default=False]
        True if messages should be printed during scheduling

    Returns
    -------
    list of int
        Mapping of tasks to resources

    Notes
    -----
    This list scheduling algorithm takes tasks in decreasing load order
    and maps them to the least loaded resources while respecting the
    maximum limit on the number of tasks per resource.
    """
    if verbose:
        print(f'LPT w/ limits: starting with {len(task_loads)} tasks' +
              f' and {num_resources} resources.')
    # Empty mapping
    num_tasks = len(task_loads)
    mapping = [None] * num_tasks
    # TODO

    return mapping


def list_scheduler_for_uniform_resources(
        task_loads,
        num_resources,
        resource_speeds,
        verbose=False):
    """Basic list scheduling algorithm used for uniform (or related)
    resources.
    To implement.

    Parameters
    ----------
    task_loads : list of int or float
        Load of the tasks
    num_resources : int
        Number of resources
    resource_speeds : list of int or float
        Speed of each resource
    verbose : bool [default=False]
        True if messages should be printed during scheduling

    Returns
    -------
    list of int
        Mapping of tasks to resources

    Notes
    -----
    The list scheduling algorithm takes tasks in [lexicographical] order
    and maps them to the least loaded resources.
    The load of a uniform or related resource is equal to the load
    of its tasks divided by its speed.
    """
    if verbose:
        print(f'List Scheduler for Uniform Resources:' +
              f' starting with {len(task_loads)} tasks' +
              f' and {num_resources} resources.')
    # Empty mapping
    num_tasks = len(task_loads)
    mapping = [None] * num_tasks
    # TODO

    return mapping
