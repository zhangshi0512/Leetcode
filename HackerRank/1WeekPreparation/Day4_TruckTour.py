"""
Suppose there is a circle, there are N petrol pumps on that circle. 
Petrol pumps are numbered 0 to (N-1) (both inclusive). 

You have two pieces of information corresponding to each of the petrol pump: 
1. the amount of petrol that particular petrol pump will give. 
2. The distance from that petrol pump to the next petrol pump. 

Initially, you have a tank of infinite capacity carrying no petrol. 
You can start the tour at any of the petrol pumps. 
Calculate the first point from where the truck will be able to complete the circle. 
Consider that the truck will stop at each of the petrol pumps. 
The truck will move one kilometer for each litre of the petrol. 

The input format: the first line will contain the value of N, 
the next N lines will contain a pair of integers each, 
the amount of petrol pump will give and the distance between that petrol pump and the next petrol pump. 

The output should be an integer which will be the smallest index of the petrol pump from which we can start the tour. 

Sample input: [3, (1,5), (10, 3), (3, 4)] Sample output: 1
"""
# 对于这个问题，我们可以通过遍历加油站，然后在每一步计算可用燃油与到下一个加油站的距离之间的差值。
# 如果在任何步骤中，差值变为负数，那就意味着我们不能从上一个起点开始，所以将起点设置为当前的加油站并继续。
# 在最后的迭代后的起点将是卡车能够完成环路的第一个点。


def canCompleteCircuit(petrol_pumps):
    # 初始化起点索引和两个累计值
    start = 0   # 起始点的索引
    surplus = deficit = 0   # surplus为每步后剩余的燃油量，deficit为燃油短缺的总量

    # 遍历所有加油站
    for i in range(len(petrol_pumps)):
        # 计算每步后的剩余燃油量
        surplus += petrol_pumps[i][0] - petrol_pumps[i][1]
        # 如果剩余燃油量为负，将起点设置为当前加油站，并累计燃油短缺量
        if surplus < 0:
            start = i + 1   # 将起点设置为当前加油站的下一站
            deficit += surplus   # 累计燃油短缺量
            surplus = 0   # 将剩余燃油量重置为0

    # 如果总的燃油量大于等于总的行驶距离，返回起始加油站的索引，否则返回-1
    return start if surplus + deficit >= 0 else -1


print(canCompleteCircuit([(1, 5), (10, 3), (3, 4)]))   # 输出：1
