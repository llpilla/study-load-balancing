#!/usr/bin/env python3

import unittest
import sys
# Add the parent directory to the path so we can import
# code from our simulator
sys.path.append('../')

from simulator.schedulers import round_robin, compact              # noqa
from simulator.schedulers import uniformly_random, list_scheduler  # noqa


class RRTest(unittest.TestCase):
    def test_five_tasks(self):
        num_tasks = 5
        num_resources = 2
        mapping = round_robin(num_tasks, num_resources)
        self.assertEqual(mapping[0], 0)
        self.assertEqual(mapping[1], 1)
        self.assertEqual(mapping[2], 0)
        self.assertEqual(mapping[3], 1)
        self.assertEqual(mapping[4], 0)

    def test_more_resources(self):
        num_tasks = 5
        num_resources = 10
        mapping = round_robin(num_tasks, num_resources)
        self.assertEqual(mapping[0], 0)
        self.assertEqual(mapping[1], 1)
        self.assertEqual(mapping[2], 2)
        self.assertEqual(mapping[3], 3)
        self.assertEqual(mapping[4], 4)


class CompactTest(unittest.TestCase):
    def test_five_tasks(self):
        num_tasks = 5
        num_resources = 2
        mapping = compact(num_tasks, num_resources)
        self.assertEqual(mapping[0], 0)
        self.assertEqual(mapping[1], 0)
        self.assertEqual(mapping[2], 0)
        self.assertEqual(mapping[3], 1)
        self.assertEqual(mapping[4], 1)

    def test_more_resources(self):
        num_tasks = 5
        num_resources = 10
        mapping = compact(num_tasks, num_resources)
        self.assertEqual(mapping[0], 0)
        self.assertEqual(mapping[1], 1)
        self.assertEqual(mapping[2], 2)
        self.assertEqual(mapping[3], 3)
        self.assertEqual(mapping[4], 4)


class RandomTest(unittest.TestCase):
    def test_seed_one(self):
        num_tasks = 5
        num_resources = 3
        mapping = uniformly_random(num_tasks, num_resources, 1)
        self.assertEqual(mapping[0], 0)
        self.assertEqual(mapping[1], 2)
        self.assertEqual(mapping[2], 0)
        self.assertEqual(mapping[3], 1)
        self.assertEqual(mapping[4], 0)

    def test_seed_two(self):
        num_tasks = 5
        num_resources = 3
        mapping = uniformly_random(num_tasks, num_resources, 2)
        self.assertEqual(mapping[0], 0)
        self.assertEqual(mapping[1], 0)
        self.assertEqual(mapping[2], 0)
        self.assertEqual(mapping[3], 1)
        self.assertEqual(mapping[4], 0)


class LSTest(unittest.TestCase):
    def test_five_tasks(self):
        num_resources = 3
        task_loads = [5, 3, 2, 7, 4]
        mapping = list_scheduler(task_loads, num_resources)
        self.assertEqual(mapping[0], 0)
        self.assertEqual(mapping[1], 1)
        self.assertEqual(mapping[2], 2)
        self.assertEqual(mapping[3], 2)
        self.assertEqual(mapping[4], 1)

    def test_ten_tasks(self):
        num_resources = 5
        task_loads = [5, 3, 2, 7, 4, 1, 9, 3, 2, 7]
        mapping = list_scheduler(task_loads, num_resources)
        self.assertEqual(mapping[0], 0)
        self.assertEqual(mapping[1], 1)
        self.assertEqual(mapping[2], 2)
        self.assertEqual(mapping[3], 3)
        self.assertEqual(mapping[4], 4)
        self.assertEqual(mapping[5], 2)
        self.assertEqual(mapping[6], 1)
        self.assertEqual(mapping[7], 2)
        self.assertEqual(mapping[8], 4)
        self.assertEqual(mapping[9], 0)


if __name__ == '__main__':
    unittest.main()
