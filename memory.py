import tracemalloc
tracemalloc.start(5)  # save upto 5 stack frames
time1 = tracemalloc.take_snapshot()
ref = 'Sarah ' * 51200
time2 = tracemalloc.take_snapshot()
stats = time2.compare_to(time1, 'lineno')
for stat in stats[:4]:
    print(stat)