# !/usr/bin/env python3
# -*- coding: utf-8 -*-


print('Hello World!')
print(divmod(7, 3))

s = '今天是个好天气，我好想和我的好朋友出去旅行。'
print(s.replace('好', '女').replace('女', '好', 2))
print(s[::-1].replace('好', '女', 1)[::-1])

pi = 3.1415926535897932384626
print(str(pi).count('3', str(pi).index('.')))

def get_perator_name(number):
    number = int(number)
    for i in range(len(perator_dict)):
        if number in list(perator_dict.values())[i]:
            return list(perator_dict.keys())[i]


mobile = [134, 135, 136, 137, 138, 139, 147, 150, 151, 152, 157, 158, 159, 178, 182, 183, 184, 187, 188]
unicom = [130, 131, 132, 145, 155, 156, 171, 175, 176, 185, 186]
telecom = [133, 149, 153, 173, 177, 180, 181, 189, 199]
perator_num = [mobile, unicom, telecom]
perator_name = ['中国移动', '中国联通', '中国电信']
perator_dict = dict(zip(perator_name, perator_num))
num = input('请输入手机号码前三位：')
print(get_perator_name(num))

lst = ['邢佳栋', '李学庆', '高昊', '潘粤明', '戴军', '薛之谦', '贾宏声', '于波', '李连杰', '王斑', '蓝雨', '刘恩佑', '任泉',
       '李光洁', '姜文', '黑龙', '张殿菲', '邓超', '张杰', '杨坤', '沙溢', '李茂', '黄磊', '于小伟', '刘冠翔', '秦俊杰', '张琳',
       '陈坤', '黄觉', '邵峰', '陈旭', '马天宇', '杨子', '邓安奇', '赵鸿飞', '马可', '黄海波', '黄志忠', '李晨', '后弦', '王挺',
       '何炅', '朱亚文', '胡军', '许亚军', '张涵予', '贾乃亮', '陆虎', '印小天', '于和伟', '田亮', '夏雨', '李亚鹏', '胡兵', '王睿',
       '保剑锋', '于震', '苏醒', '胡夏', '张丰毅', '刘翔', '李玉刚', '林依轮', '袁弘', '朱雨辰', '丁志诚', '黄征', '张子健', '许嵩']


def get_index(lst, str, lower, upper):
    if lower == upper:
        return upper
    else:
        middle = (lower + upper) // 2
        if str in lst[lower:middle + 1]:  # 注意：切片操作的终止位置是截取不到的，所以要+1才能正常判断。
            return get_index(lst, str, lower, middle)
        else:
            return get_index(lst, str, middle + 1, upper)


print(get_index(lst, input('请输入姓名：'), 0, len(lst)))
