#!/usr/bin/env python3

import unittest
import sys
# Add the parent directory to the path so we can import
# code from our simulator
sys.path.append('../')

from simulator.schedulers import lpt, lpt_with_limits                  # noqa
from simulator.schedulers import list_scheduler_for_uniform_resources  # noqa


class LPTTest(unittest.TestCase):
    def test_five_tasks(self):
        num_resources = 3
        task_loads = [5, 3, 2, 7, 4]
        mapping = lpt(task_loads, num_resources)
        self.assertEqual(mapping[0], 1)
        self.assertEqual(mapping[1], 2)
        self.assertEqual(mapping[2], 1)
        self.assertEqual(mapping[3], 0)
        self.assertEqual(mapping[4], 2)

    def test_ten_tasks(self):
        num_resources = 5
        task_loads = [5, 3, 2, 7, 4, 1, 9, 6, 8, 10]
        mapping = lpt(task_loads, num_resources)
        self.assertEqual(mapping[0], 4)
        self.assertEqual(mapping[1], 2)
        self.assertEqual(mapping[2], 1)
        self.assertEqual(mapping[3], 3)
        self.assertEqual(mapping[4], 3)
        self.assertEqual(mapping[5], 0)
        self.assertEqual(mapping[6], 1)
        self.assertEqual(mapping[7], 4)
        self.assertEqual(mapping[8], 2)
        self.assertEqual(mapping[9], 0)


class LPTWithLimitsTest(unittest.TestCase):
    def test_five_tasks(self):
        num_resources = 3
        task_loads = [1, 1, 1, 5, 6]
        mapping = lpt_with_limits(task_loads, num_resources, 2)
        self.assertEqual(mapping[3], 1)
        self.assertEqual(mapping[4], 0)

        resource_loads = [0] * 3
        tasks_per_resource = [0] * 3
        for task in range(5):
            resource = mapping[task]
            resource_loads[resource] += task_loads[task]
            tasks_per_resource[resource] += 1

        self.assertEqual(max(resource_loads), 6)
        self.assertEqual(min(resource_loads), 2)
        self.assertEqual(max(tasks_per_resource), 2)
        self.assertEqual(min(tasks_per_resource), 1)


class LSForUniformTest(unittest.TestCase):
    def test_five_tasks(self):
        num_resources = 3
        task_loads = [5, 3, 2, 6, 4]
        resource_speeds = [1, 2, 3]
        mapping = list_scheduler_for_uniform_resources(
                task_loads,
                num_resources,
                resource_speeds)
        self.assertEqual(mapping[0], 2)
        self.assertEqual(mapping[1], 1)
        self.assertEqual(mapping[2], 0)
        self.assertEqual(mapping[3], 2)
        self.assertEqual(mapping[4], 1)


if __name__ == '__main__':
    unittest.main()
