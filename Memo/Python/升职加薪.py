# 2022/9/14 08:49
info_employees = {
    '王力宏': {
        '部门': '科技部',
        '工资': 3000,
        '级别': 1
    },
    '周杰伦': {
        '部门': '市场部',
        '工资': 5000,
        '级别': 2
    },
    '林俊杰': {
        '部门': '市场部',
        '工资': 7000,
        '级别': 3
    },
    '张学友': {
        '部门': '科技部',
        '工资': 4000,
        '级别': 1
    },
    '刘德华': {
        '部门': '市场部',
        '工资': 6000,
        '级别': 2
    }
}
print(info_employees)
print('\n')

for name in info_employees:
    if info_employees[name]['级别'] == 1:
        info_employees[name]['级别'] += 1
        info_employees[name]['工资'] += 1000
print(info_employees)
