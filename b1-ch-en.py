import os


def align(str, space):
    length = len(str.encode('gb2312'))
    space = space - length if space >= length else 0
    return str + ' ' * space


str1 = "abc1234"
print(align("abc中中中", 20), align(str1, 10))
print(align("abcdefg", 20), align(str1, 10))
print(align("是是是是是是是是", 20), align(str1, 10))