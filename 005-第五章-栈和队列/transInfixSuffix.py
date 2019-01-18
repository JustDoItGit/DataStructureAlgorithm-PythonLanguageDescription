from stack import SStack
from sufExpEvaluator import suf_exp_evaluator

priority = {'(': 1, '+': 3, '-': 3, '*': 5, '/': 5}
infix_operators = '+-*/()'  # 把'('、')'也看作运算符，但特殊处理


def trans_infix_suffix(line):
    st = SStack()
    exp = []

    for x in tokens(line):  # tokens是一个待定义的生成器
        if x not in infix_operators:  # 运算对象直接送出
            exp.append(x)
        elif st.is_empty() or x == '(':  # 左括号进栈
            st.push(x)
        elif x == ')':  # 处理右括号的分支
            while not st.is_empty() and st.top() != '(':
                exp.append(st.pop())
                if st.is_empty():  # 没有找到左括号，就是不配对
                    raise SyntaxError('Missing "(".')
                st.pop()  # 弹出左括号，右括号也不进栈
        else:  # 处理运算符，运算符都看作左结合
            while (not st.is_empty()) and priority[st.top()] >= priority[x]:
                exp.append(st.pop())
            st.push(x)  # 算数运算符进栈

    while not st.is_empty():  # 送出栈里剩下的运算符
        if st.pop() == '(':  # 如果还有左括号，就是不配对
            raise SyntaxError('Extra "(".')
        exp.append(st.pop())

    return exp


def tokens(line):
    """ 生成器函数，逐一生成 line 中的一个个项。项是浮点数或或运算符。
    本函数不能处理一元运算符，也不能处理带符号的浮点数。 """
    i, llen = 0, len(line)
    while i < llen:
        while line[i].isspace():
            i += 1
        if i >= llen:
            break
        if line[i] in infix_operators:  # 运算符的情况
            yield line[i]
            i += 1
            continue

        j = i + 1  # 下面处理运算对象
        while j < llen and not line[j].isspace() and line[j] not in infix_operators:
            if (line[j] == 'e' or line[j] == 'E') and j + 1 < llen and line[j + 1] == '-':  # 处理负指数
                j += 1
            j += 1
        yield line[i:j]  # 成运算符对象子串
        i = j


def test_trans_infix_suffix(s):
    print(s)
    print(trans_infix_suffix(s))
    print('Value:', suf_exp_evaluator(trans_infix_suffix(s)))


if __name__ == '__main__':
    test_trans_infix_suffix('((1+2) * 3)')
