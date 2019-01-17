from stack import SStack


class ESStack(SStack):
    def depth(self):
        return len(self._elems)


def suf_exp_evaluator(exp):
    operators = '+-*/'
    st = ESStack()  # 扩展功能的栈，可用depth()检查栈元素个数

    for x in exp:
        if x not in operators:
            st.push(float(x))  # 不能转换将自动引发异常
            continue

        if st.depth() < 2:  # x必为运算符，栈元素不够时引发异常
            raise SyntaxError('Short of operand(s).')

        a = st.pop()  # 取得第二个运算对象
        b = st.pop()  # 取得第一个运算对象

        if x == '+':
            c = b + a
        elif x == '-':
            c = b - a
        elif x == '*':
            c = b * a
        elif x == '/':
            c = b / a
        else:
            break
        # else分支不可能出现，写在这里是为了清晰

        st.push(c)

    if st.depth() == 1:
        return st.top()

    raise SyntaxError('Extra operand(s).')


def suffix_exp_calculator():
    while True:
        try:
            line = input('Suffix Expression: ')
            if line == 'end':
                return
            res = suf_exp_evaluator(line)
            print(res)
        except Exception as ex:
            print('Error:', type(ex), ex.args)


if __name__ == '__main__':
    suffix_exp_calculator()

    '''
        23+
        3545-*/
        3545-*/+
        23
        23a+-
        +abv5--
    '''
