import random
from flask import render_template, redirect, request, url_for

from IRA import app
from C45.helper import places, tree, post_question

@app.route('/')
def index():
    return render_template('index.html', places=places)

@app.route('/place')
def place():
    return render_template('place.html', places=places)

@app.route('/valid')
def valid():
    place = request.args.get('place')
    if place[-1] == '/':
        place = place[:-1]
    sex = False
    dictfound = True
    if place == '阴部':
        sex = True
    elif place == '脖颈' and random.choice([0, 1]) == 0:
        place = '喉咙'
    if places.get(place) is None:
        dictfound = False
    return render_template('valid.html', places=places, place=place, sex=sex, dictfound=dictfound)

@app.route('/query/<int:ans>')
def query(ans):
    if ans != 2 and ans % 10 == 2:
        ans = ans - 2 + random.choice([0, 1])
    q = post_question(ans)
    if q['status'] == 'continue':
        return render_template('query.html', ans=ans, question=q['question'])
    elif q['status'] == 'end':
        return redirect(url_for('result', answer=q['answer']))
    elif q['status'] == 'failing':
        return redirect(url_for('result', answer='fail'))
    elif q['status'] == 'dangerous':
        return redirect(url_for('result', answer='dangerous'))

@app.route('/result')
def result():
    answer = request.args.get('answer')
    if isinstance(answer, str):
        answer = [answer]
    prefix = '这里是智能导诊系统给您推荐的挂号科室：'
    if answer[0] == 'fail':
        answer = '智能导诊没能确定您应该挂号的科室，请联系人工咨询。'
    elif answer[0] == 'dangerous':
        answer = '智能导诊未能确定您应该挂号的科室，但也许您可以尝试挂号肿瘤科'
    else:
        answer = prefix + random.choice(answer)
    return render_template('result.html', answer=answer)