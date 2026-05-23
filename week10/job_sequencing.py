def job_sequence(jobs):

    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)

    slots = [-1] * max_deadline

    profit = 0

    for job, deadline, gain in jobs:

        for j in range(deadline-1,-1,-1):

            if slots[j] == -1:
                slots[j] = job
                profit += gain
                break

    return slots, profit


jobs = [
('A',2,100),
('B',1,19),
('C',2,27),
('D',1,25),
('E',3,15)
]

print(job_sequence(jobs))