#!/usr/bin/env python
# encoding: utf-8


def judge(range_a, range_b, flop):
    # 用来判断手牌a和手牌b在flop下的输赢
    # range_a, range_b, flop均为list类型
    # 如果手牌a赢   返回1
    # 如果手牌b赢   返回-1
    # 如果平局      返回0
    pass
    # 先进行输入检查
    # 检查长度
    if len(range_a) != 2 or len(range_b) != 2 or len(flop) != 3:
        raise Exception("输入数据格式错误，长度异常")


if __name__ == '__main__':
    print "Hello SSNLHE!!! Hello NL200!!"
