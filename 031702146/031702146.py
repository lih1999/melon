# \d{11}表示十一位数字  {n}表示前面的字符还需要n个；\d表示数字
import re
import json

customer = {
    '姓名': '',
    '手机': '',
    '地址': [],
}

s = input('')

op1 = s.split(r'!')
tag = op1[0]  # 提取难度标识


tel = re.findall(r'\d{11}', s)  # 找出号码
tel = tel[0]  # 将号码转化为字符串
s = re.sub(r'\d{11}', '', s)  # 删去号码

num = re.sub(r',.*$', "", s)  # 提取人名

s = re.sub(num, '', s)  # 删去人名
s = re.sub(r',', '', s)  # 删去逗号

customer['姓名'] = num
customer['手机'] = tel

# 一级地址
zhixiashi = ['北京', '上海', '天津', '重庆']
if "自治区" in s:
    one = re.sub(r'自治区.*$', "", s)  # 提取自治区
    one += '自治区'
    s = s.replace(one, '', 1)  # 删去自治区
elif '省' not in s:
    for direc in zhixiashi:
        if direc in s:
            one = direc
            break
        else:
            one = ""  # 该级地址为空
else:
    one = re.sub(r'省.*$', "", s)
    one += '省'
    s = s.replace(one, '', 1)  # 删去一级地址
customer['地址'].append(one)

# 二级
erji = ['市', '地区', '盟', '自治州']
for tw in erji:
    if tw in s:

        two = re.sub(tw + '.*$', "", s)
        two += tw
        s = s.replace(two, '', 1)  # 删去二级地址
        break
    else:
        two = ""

customer['地址'].append(two)

# 三级地址
xianji = ['区', '县', '市', '自治县', '旗', '自治旗', '林区']
for tr in xianji:
    if tr in s:
        three = re.sub(tr + '.*$', "", s)
        three += tr
        s = s.replace(three, '', 1)  # 删去三级地址
        break
    else:
        three = ""

customer['地址'].append(three)

# 四级地址
zhenji = ['街道', '镇', '乡', '民族乡', '苏木', '民族苏木']
for fr in zhenji:
    if fr in s:
        four = re.sub(fr + '.*$', "", s)
        four += fr
        s = s.replace(four, '', 1)  # 删去四级地址
        break
    else:
        four = ""
customer['地址'].append(four)

s = s.replace('.', '', 1)  # 删去句号
# 五级地址
cunji = ['街', '路', '村']
if tag == '1':
    five = s
    customer['地址'].append(five)
elif tag == '2' or '3':  # 继续划分五级以后的地址
    for fv in cunji:
        if fv in s:
            five = re.sub(fv + '.*$', "", s)
            five += fv
            customer['地址'].append(five)
            s = s.replace(five, '', 1)  # 删去五级地址
            break
        else:
            five = ""
    # 六级地址
    if '号' not in s:
        six = ""
    else:
        six = re.sub(r'号.*$', "", s)
        six += '号'
        s = s.replace(six, '', 1)  # 删去六级地址

    customer['地址'].append(six)

    # 七级地址
    seven = s
    customer['地址'].append(seven)

json_str = json.dumps(customer, ensure_ascii=False)
print(json_str)
