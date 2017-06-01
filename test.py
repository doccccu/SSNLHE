#!/usr/bin/env python
# encoding: utf-8


poker_colours = ['s', 'h', 'c', 'd']
poker_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
poker_dict = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}


def is_poker_str(range_a):
    # 用来判断一个list中的每一个元素 是不是满足poker字符要求
    # range_a为list类型
    # 如果满足      返回True
    # 如果不满足    返回False

    # 判断花色是否满足格式要求
    # 黑桃  spades(s)
    # 红桃  heards(h)
    # 草花  clubs(c)
    # 方块  diamonds(d)
    for one in range_a:
        # 默认不满足
        flag = False
        for clr in poker_colours:
            if one[1] == clr:
                # 如果能找到一个相等 那么证明满足
                flag = True
                break
        if flag is False:
            return False

    # 判断数值是否满足格式要求
    # 2-9 T J K Q A
    for one in range_a:
        # 默认不满足
        flag = False
        for val in poker_values:
            if one[0] == val:
                # 如果能找到一个相等 那么证明满足
                flag = True
                break
        if flag is False:
            return False

    # 通过两个函数判断之后
    return True


def is_repeat(range_a, range_b, flop):
    # 用来判断手牌a和手牌b和flop有么有重复牌
    # 有重复返回True
    # 没有返回False

    tmp = range_a + range_b + flop
    if len(list(set(tmp))) == len(tmp):
        return False

    return True


def input_check(range_a, range_b, flop):
    # 先进行输入检查
    # 检查长度
    if len(range_a) != 2 or len(range_b) != 2 or len(flop) != 5:
        raise Exception("输入数据格式错误，长度异常")

    # 检查数值和格式
    if is_poker_str(range_a) is False:
        raise Exception("输入数据格式错误，手牌a异常")
    if is_poker_str(range_b) is False:
        raise Exception("输入数据格式错误，手牌b异常")
    if is_poker_str(flop) is False:
        raise Exception("输入数据格式错误，flop异常")

    # 检查重复
    if is_repeat(range_a, range_b, flop):
        raise Exception("输入数据格式错误，有重复")


def judge_inside(range_a, tmp):
    # 判断tmp中每个元素 是不是都存在于range中
    # range包含tmp返回True
    # range不包含tmp返回False

    for one in tmp:
        if one not in range_a:
            return False
    return True


def judge_royal_flush(range_a):
    # 判断是否存在royal flush
    # 存在返回True  不存在返回False

    # 手写版本 有待提高
    royal_s = ['As', 'Ks', 'Qs', 'Js', 'Ts']
    royal_h = ['Ah', 'Kh', 'Qh', 'Jh', 'Th']
    royal_c = ['Ac', 'Kc', 'Qc', 'Jc', 'Tc']
    royal_d = ['Ad', 'Kd', 'Qd', 'Jd', 'Td']

    if judge_inside(range_a, royal_s):
        return True
    if judge_inside(range_a, royal_h):
        return True
    if judge_inside(range_a, royal_c):
        return True
    if judge_inside(range_a, royal_d):
        return True

    return False


def judge_straight_flush(range_a):
    # 判断是否存在straight flush
    # 存在返回第一个牌的index  不存在返回-1

    # 第一张牌的范围 6 - K
    # index范围   4 － 11
    for i in range(11, 3, -1):
        for j in range(0, len(poker_colours)):
            tmp = [poker_values[i] + poker_colours[j],
                   poker_values[i - 1] + poker_colours[j],
                   poker_values[i - 2] + poker_colours[j],
                   poker_values[i - 3] + poker_colours[j],
                   poker_values[i - 4] + poker_colours[j]]
            if judge_inside(range_a, tmp) is True:
                return i
    # 考虑第一张牌为5的特殊情况
    for j in range(0, len(poker_colours)):
        tmp = ['A' + poker_colours[j],
               '2' + poker_colours[j],
               '3' + poker_colours[j],
               '4' + poker_colours[j],
               '5' + poker_colours[j]]
        if judge_inside(range_a, tmp) is True:
            # 5 的index为 3
            return 3

    # 不存在straight flush
    return -1


def judge_high_card(range_a, range_b):
    # 用高牌来判断大小
    # 返回1，0，－1
    flag_a = -1
    flag_b = -1
    for i in range(12, -1, -1):
        for j in range(0, len(poker_colours)):
            tmp = poker_values[i] + poker_colours[j]
            if tmp in range_a and flag_a == -1:
                flag_a = i
        if flag_a != -1:
            break
    for i in range(12, -1, -1):
        for j in range(0, len(poker_colours)):
            tmp = poker_values[i] + poker_colours[j]
            if tmp in range_b and flag_b == -1:
                flag_b = i
        if flag_b != -1:
            break

    if flag_a == flag_b:
        return 0
    if flag_a > flag_b:
        return 1
    if flag_a < flag_b:
        return -1

    return 10000


def judge_four(range_a, range_b):
    # 用四条来判断大小
    # 如果可以判断大小 那么返回1，0，－1
    # 如果不能判断大小 也就是a，b均不存在四条那么返回10000
    
    # 炸弹的第一张牌范围 2 - A
    for i in range(12, -1, -1):
        flag_a = False
        flag_b = False
        tmp = []
        for j in range(0, len(poker_colours)):
            tmp.append(poker_values[i] + poker_colours[j])

        if judge_inside(range_a, tmp):
                flag_a = True
        if judge_inside(range_b, tmp):
                flag_b = True
        if flag_a is True and flag_b is True:
            # a和b存在一样大小的四条 需要判断单张大小
            # 将手牌信息复制一份 并去掉四条
            tmp_a = range_a[:]
            tmp_b = range_b[:]
            for one in range_a:
                if one[0] == poker_values[i]:
                    tmp_a.remove(one)
            for one in range_b:
                if one[0] == poker_values[i]:
                    tmp_b.remove(one)

            return judge_high_card(tmp_a, tmp_b)

        if flag_a is True:
            # a存在大的四条
            return 1
        if flag_b is True:
            return -1

    # a和b均不存在任何四条
    return 10000


def judge(range_a, range_b, flop):
    # 用来判断手牌a和手牌b在flop下的输赢
    # range_a, range_b, flop均为list类型
    # 如果手牌a赢   返回1
    # 如果手牌b赢   返回-1
    # 如果平局      返回0

    # 对手牌进行扩展 把flop加入到每个手牌末尾
    range_a.extend(flop)
    range_b.extend(flop)

    # 判断Royal Flush
    flag_royal_flush_a = judge_royal_flush(range_a)
    flag_royal_flush_b = judge_royal_flush(range_b)
    if flag_royal_flush_a is True and flag_royal_flush_b is True:
        return 0
    if flag_royal_flush_a is True:
        return 1
    if flag_royal_flush_b is True:
        return -1


    # 判断Straight Flush
    flag_straight_flush_a = judge_straight_flush(range_a)
    flag_straight_flush_b = judge_straight_flush(range_b)
    if flag_straight_flush_a > 0 and flag_straight_flush_b > 0:
        # 通过返回的index判断flush大小
        if flag_straight_flush_a > flag_straight_flush_b:
            return 1
        if flag_straight_flush_a < flag_straight_flush_b:
            return -1
        if flag_straight_flush_a == flag_straight_flush_b:
            return 0
    if flag_straight_flush_a > 0:
        return 1
    if flag_straight_flush_b > 0:
        return -1

    # 判断Four of a Kind
    flag_four_of_a_kind = judge_four(range_a, range_b)
    if flag_four_of_a_kind != 10000:
        # 如果可以比较出结果 那么就返回这个结果
        return flag_four_of_a_kind

    return 0


if __name__ == '__main__':
    print "Hello SSNLHE!!! Hello NL200!!"
    range_a = ['As', 'Ah']
    range_b = ['Ks', 'Qs']
    flop = ['Ad', 'Ac', 'Ts', 'Js', '9s']
    input_check(range_a, range_b, flop)
    ret = judge(range_a, range_b, flop)
    print ret
