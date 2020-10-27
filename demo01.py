"""
    生成器表达式
    复习：列表推导式
"""
# 需求1：将list01中大于10的数字，存入另外一个空列表中
list_result = [item for item in list01 if item > 10]
print(list_result)

generator02 = (number ** 3 for number in range(1, 11))
