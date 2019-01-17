from stack import SStack


def parentheses(text, parens):
    """ 括号生成器，每次调用返回text里的下一括号及其位置 """
    i, text_len = 0, len(text)
    while True:
        while i < text_len and text[i] not in parens:
            i += 1
        if i >= text_len:
            return
        yield text[i], i
        i += 1


def check_parens(text):
    """ 括号匹配检查函数，text是被检查的正文串 """
    parens = '()[]{}'
    open_parens = '([{'
    opposite = {')': '(', ']': '[', '}': '{'}  # 表示配对关系的字典

    st = SStack()  # 保存括号的栈
    st_i = SStack()
    for pr, i in parentheses(text, parens):  # 对text里各括号和位置迭代
        if pr in open_parens:  # 开括号，压进栈并继续
            st.push(pr)
            st_i.push(i)
        elif st.is_empty() or st.pop() != opposite[pr]:  # 不匹配就是失败，退出
            if not st.is_empty():
                st_i.pop()
            print('Unmatching is found at', i, 'for', pr)
            return False
        else:  # 这是一次括号配对成功，什么也不做，继续
            st_i.pop()
    if not st.is_empty():
        st_i_ = ''
        st_ = ''
        while not st.is_empty():
            st_i_ = str(st_i.pop()) + st_i_
            st_ = st.pop() + st_

        print('Unmatching is found at', st_i_, 'for', st_)
        return False
    print('All parentheses are correctly matched.')
    return True


if __name__ == '__main__':
    check_parens('{[{})]}')
    check_parens('({[{}]')
    check_parens('{[{}]}}')
    check_parens('{[{}]}')
