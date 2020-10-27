#!/usr/bin/env python3

import unittest
import sys
# Add the parent directory to the path so we can import
# code from our simulator
sys.path.append('../')

from simulator.support import generate_uniform_loads   # noqa
from simulator.support import evaluate_mapping         # noqa


class GULTest(unittest.TestCase):
    def test_seed_one(self):
        task_loads = generate_uniform_loads(rng_seed=1)
        self.assertEqual(task_loads[0], 3)
        self.assertEqual(task_loads[1], 2)
        self.assertEqual(task_loads[2], 5)
        self.assertEqual(task_loads[3], 2)
        self.assertEqual(task_loads[4], 8)
        self.assertEqual(task_loads[5], 8)
        self.assertEqual(task_loads[6], 8)
        self.assertEqual(task_loads[7], 7)
        self.assertEqual(task_loads[8], 4)
        self.assertEqual(task_loads[9], 2)

    def test_seed_ten(self):
        task_loads = generate_uniform_loads(5, 11, 41, 10)
        self.assertEqual(task_loads[0], 29)
        self.assertEqual(task_loads[1], 12)
        self.assertEqual(task_loads[2], 24)
        self.assertEqual(task_loads[3], 26)
        self.assertEqual(task_loads[4], 29)


class EMTest(unittest.TestCase):
    def test_small_mapping(self):
        task_loads = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        mapping = [0, 0, 0, 0, 1, 1, 1, 1, 3, 3]
        num_resources = 5
        resource_loads = evaluate_mapping(
                mapping,
                task_loads,
                num_resources,
                False)

        self.assertEqual(resource_loads[0], 10)
        self.assertEqual(resource_loads[1], 26)
        self.assertEqual(resource_loads[2], 0)
        self.assertEqual(resource_loads[3], 19)
        self.assertEqual(resource_loads[4], 0)


if __name__ == '__main__':
    unittest.main()
