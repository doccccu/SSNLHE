#!/usr/bin/env python
# encoding: utf-8


poker_colours = ['s', 'h', 'c', 'd']
poker_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']


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

    # 判断range_a
    for one in range_a:
        for tmp in range_b:
            if one == tmp:
                return True
        for tmp in flop:
            if one == flop:
                return True
    # 判断range_b
    for one in range_b:
        for tmp in range_a:
            if one == tmp:
                return True
        for tmp in flop:
            if one == tmp:
                return True
    # 判断flop
    for one in flop:
        for tmp in range_a:
            if one == tmp:
                return True
        for tmp in range_b:
            if one == tmp:
                return True
    return False


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
    pass


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
    if flag_royal_flush_a and flag_royal_flush_b:
        return 0
    if flag_royal_flush_a:
        return 1
    if flag_royal_flush_b:
        return -1

    # 判断Straight Flush
    flag_straight_flush_a = judge_straight_flush(range_a)
    flag_straight_flush_b = judge_straight_flush(range_b)
    if flag_straight_flush_a and flag_straight_flush_b:
        # 通过返回的index判断flush大小
        if flag_straight_flush_a > flag_straight_flush_b:
            return 1
        if flag_straight_flush_a < flag_straight_flush_b:
            return -1
        if flag_straight_flush_a == flag_straight_flush_b:
            return 0
    if flag_straight_flush_a:
        return 1
    if flag_straight_flush_b:
        return -1

    return 0


if __name__ == '__main__':
    print "Hello SSNLHE!!! Hello NL200!!"
    range_a = ['As', 'Ah']
    range_b = ['Kd', 'Kh']
    flop = ['Kc', 'Qs', 'Js', 'Ts', '3d']
    input_check(range_a, range_b, flop)
    ret = judge(range_a, range_b, flop)
    print ret
