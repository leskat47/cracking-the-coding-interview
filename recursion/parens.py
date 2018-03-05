def print_parens(n):
    find_combs(n-1, ['('], '(')

def find_combs(n, stack , p):

    # base case: empty stack and n is zero
    if not stack and not n:
        print p
        return

    # if we have reached n open parens add a close paren
    if stack and not n:
        find_combs(n, stack[:-1], p + ')')

    # if stack is empty, current parens are balanced,
    # if we haven't reached n, we must open
    if not stack and n:
        find_combs(n-1, stack + ['('], p + '(')

    # if stack isn't empty, parens are unbalanced
    # try adding open and adding close
    if stack and n:
        find_combs(n, stack[:-1], p + ')')
        find_combs(n-1, stack + ['('], p + '(')


print_parens(3)
