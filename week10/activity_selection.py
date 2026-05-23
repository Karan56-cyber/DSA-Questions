def activity(start, finish):

    activities = list(zip(start, finish))
    activities.sort(key=lambda x: x[1])

    count = 1
    last = activities[0][1]

    print(activities[0])

    for i in range(1, len(activities)):
        if activities[i][0] >= last:
            print(activities[i])
            count += 1
            last = activities[i][1]

    return count


start = [1,3,0,5,8,5]
finish = [2,4,6,7,9,9]

print(activity(start, finish))