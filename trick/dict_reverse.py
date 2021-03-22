#字典反转的两种方法：
m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#zip压缩
ret = dict(zip(m.values(), m.keys()))

#字典推导式
ret = {v: k for k, v in m.items()}
