# 桶排序适合有范围的外部排序，比如高考分数，员工年龄这样的排序
# 将分数分为0-100，然后分100个桶，然后读取一遍数据，就会将所有数据分到100桶中，然后依次读出来就是有序的
# 桶排序适合外部排序，比如订单，订单金额在0到10万，然后将数据分别写入到100个文件中，（0 - 1000）（1001 - 2000）
# 然后对小文件进行快速排序，快排时间复杂度是O(nlogn)。n 个数据 分m 个桶中，k = n/m,klogk 当m 接近n 时候，log(n/m) 趋近于小值，
# m*k = n 所以时间复杂度趋近于O(n)。如果不是均匀的分到100个桶中，那就将数据大的那个桶，再次划分成多个桶

# 1，2，5，4，6 范围是0到7
def bucketSort(a):
    if a == None:
        return
    bucket = [ None for _ in range(7)]
    for i in a:
        bucket[i] = 1
    
    for i in range(len(bucket)):
        if bucket[i]:
            print(i)

a = [1,2,5,4,6]
bucketSort(a)