
from utils.recorder import Recorder
from sorting.merge_sort import merge_sort
from sorting.merge_sort_iterative import merge_sort_iter
from sorting.quick_sort import quick_sort
from sorting.quick_sort_3way import quick_sort_3way
from sorting.selection_sort import selection_sort
from sorting.insertion_sort import insert_sort_optimized
from sorting.insertion_sort import insert_sort
import numpy as np

from time import time
from threading import Thread


if __name__ == '__main__':
    s = time()
    recorder = Recorder()
    start, end = 2, 6

    for x in range(start,end):
        data = list(np.random.rand(np.power(10, x)))

        p1 = Thread(target=recorder.execute, args=(selection_sort, data))
        p2 = Thread(target=recorder.execute, args=(insert_sort, data))

        p3 = Thread(target=recorder.execute, args=(insert_sort_optimized, data))
        p4 = Thread(target=recorder.execute, args=(merge_sort, data, [0, len(data)-1]))
        p5 = Thread(target=recorder.execute, args=(merge_sort_iter, data))
        p6 = Thread(target=recorder.execute, args=(quick_sort, data, [0, len(data)-1]))
        p7 = Thread(target=recorder.execute, args=(quick_sort_3way, data, [0, len(data)-1]))

        p1.start()
        p2.start()
        p3.start()
        p4.start()
        p5.start()
        p6.start()
        p7.start()

        p1.join()
        p2.join()
        p3.join()
        p4.join()
        p5.join()
        p6.join()
        p7.join()

    print(time()-s)
    print(recorder.get_record_df())