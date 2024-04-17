from C45 import places, tree

def post_question(ans):
    ret = { 'question' : None, 'answer' : None, 'status' : 'continue'}
    if tree[ans][0] == '#':
        ret['status'] = 'end'
    elif tree[ans][0] == '&':
        ret['status'] = 'dangerous'
    elif tree[ans][0] == '*':
        ret['status'] = 'failing'
    if ret['status'] == 'end':
        ret['answer'] = tree[ans][2:].split(',')
    elif ret['status'] == 'continue':
        ret['question'] = tree[ans]
    return ret