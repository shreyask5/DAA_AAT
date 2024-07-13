# DAA_AAT
Data Algorithms & Analysis AAT

## Knapsack
[Link to Knapsack submission](https://www.hackerrank.com/challenges/unbounded-knapsack/submissions/code/391221785)
<a href="https://www.hackerrank.com/challenges/unbounded-knapsack/submissions/code/391221785" style="font-size: 100px;">Link to Knapsack submissionk</a>

```python
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'unboundedKnapsack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def unboundedKnapsack(k, arr):
    max_sum = [0] * (k + 1)
    
    for i in range(1, k + 1):
        for num in arr:
            if num <= i:
                max_sum[i] = max(max_sum[i], max_sum[i - num] + num)
    
    return max_sum[k]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for _ in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])
        k = int(first_multiple_input[1])

        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)

        fptr.write(str(result) + '\n')

    fptr.close()

```

## Cloudy Day

###[Link to Cloudy Day submission](https://www.hackerrank.com/challenges/cloudy-day/submissions/code/391222519)

```python
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumPeople function below.
from collections import defaultdict


def maximumPeople(towns, cloud_start, cloud_end):
    towns = sorted(towns)
    cloud_start = sorted(cloud_start)
    cloud_end = sorted(cloud_end)

    cloud_start_i = 0
    cloud_end_i = 0
    clouds = set()

    d = defaultdict(int)
    free = 0
    for town_i in range(len(towns)):
        town_x = towns[town_i][0]
        while cloud_start_i < len(cloud_start) and cloud_start[cloud_start_i][0] <= town_x:
            clouds.add(cloud_start[cloud_start_i][1])
            cloud_start_i += 1
        while cloud_end_i < len(cloud_end) and cloud_end[cloud_end_i][0] < town_x:
            clouds.remove(cloud_end[cloud_end_i][1])
            cloud_end_i += 1
        if len(clouds) == 1:
            towns[town_i][2] = list(clouds)[0]
            d[list(clouds)[0]] += towns[town_i][1]
        elif len(clouds) == 0:
            free += towns[town_i][1]

    return max(d.values(), default=0) + free

if __name__ == "__main__":
    n = int(input().strip())
    p = [int(x) for x in input().strip().split()]
    x = [int(x) for x in input().strip().split()]
    towns = [[xi, pi, -1] for xi, pi in zip(x, p)]
    m = int(input().strip())
    y = [int(x) for x in input().strip().split()]
    r = [int(x) for x in input().strip().split()]
    cloud_start = [[y[i]-r[i], i] for i in range(m)]
    cloud_end = [[y[i]+r[i], i] for i in range(m)]
    result = maximumPeople(towns, cloud_start, cloud_end)
    print(result)

```

## QuickSort

###[Link to QuickSort submission](https://www.hackerrank.com/challenges/quicksort1/submissions/code/391223331)

```python
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quickSort(arr):
    center = arr[0]
    arr = sorted(arr)
    sorted_list = [center]
    for element in arr:
        if element < center:
            sorted_list.insert(0, element)
        elif element > center:
            sorted_list.insert(arr.index(element), element)
    return sorted_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
```

## String Construction

###[Link to String Construction submission](https://www.hackerrank.com/challenges/string-construction/submissions/code/391226669)

```python
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stringConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringConstruction(s):
    unique_list = []
    cost = 0
    for char in s:
        if char not in unique_list:
            unique_list.append(char)
            cost += 1
    return cost

        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
```



