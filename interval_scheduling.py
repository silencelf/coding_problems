#! /usr/bin/python

"""
Weighted interval scheduling

Given N jobs where every job is represented by following three elements of it.
    1. Start Time
    2. Finish Time
    3. Profit or Value Associated (>= 0)

Input: Number of Jobs n = 4
       Job Details {Start Time, Finish Time, Profit}
       Job 1:  {1, 2, 50} 
       Job 2:  {3, 5, 20}
       Job 3:  {6, 19, 100}
       Job 4:  {2, 100, 200}
Output: The maximum profit is 250.
We can get the maximum profit by scheduling jobs 1 and 4.
Note that there is longer schedules possible Jobs 1, 2 and 3 
but the profit with this schedule is 20+50+100 which is less than 250.
"""
from collections import namedtuple
from operator import attrgetter

Job = namedtuple('Job', 'start finish val')

def wis(input):
    end_sorted = sorted(input, key=attrgetter('finish'))
    print(end_sorted)
    # O(n^2) to generate compatible sets
    comp_sets = { j: [i for i in end_sorted if i.start >= j.finish] for j in
            end_sorted }
    #print(finish_arr)
    print(comp_sets)

    def dp(jobs):
        if not jobs:
            return 0
        first = jobs[0]
        return max(first.val + dp(comp_sets[first]), dp(jobs[1:]))

#    def dp2(jobs, i):
#        if not jobs:
#            return 0
#        first = jobs[0]
#        return max(first.val + dp2(comp_sets[first]), dp2(jobs, i + 1))

    return dp(end_sorted)


def tests():
    job1 = Job(1, 2, 50)
    job2 = Job(3, 5, 20)
    job3 = Job(6, 19, 100)
    job4 = Job(2, 100, 200)
    jobs = [job1, job2, job3, job4]

    ret = wis(jobs)
    print(f'Max value: {ret} for jobs {jobs}')

    jobs = [ Job(1, 2, 50),
            Job(3, 5, 20),
            Job(6, 19, 200),
            Job(2, 100, 200) ]

    ret = wis(jobs)
    print(f'Max value: {ret} for jobs {jobs}')

tests()
