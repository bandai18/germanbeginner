from flask import Flask, render_template, request, logging, Response, redirect, flash
from flask_wtf.csrf import CSRFProtect, CSRFError
import main
import date_function as dt


app = Flask(__name__)


@app.route('/', methods=["GET"])
def index():

    return render_template('index.html')


@app.route('/', methods=["POST"])
def index_post():
    enter_time = request.form['time_id']
    time = main.get_time(enter_time)
    error = ""
    rotates = []
    if time is None:
        error = "Input value is not valid. Enter correct value: "
    else:
        rotates = main.get_rotate(enter_time)

    return render_template('index.html', time_id=time, entered_time=enter_time, rotates=rotates, error=error)


@app.route('/practice', methods=["GET", "POST"])
def practice():
    display_value = main.get_practice_time_value()
    rotates = main.get_rotate(display_value)

    if request.method == "POST":
        response = request.form['entered_value']
        if response != "clear":
            time = main.get_time(response)
            res_rotate = main.get_rotate(response)

            return render_template('practice.html', display_value=response, time_value=time, rotates=res_rotate)

    return render_template('practice.html', display_value=display_value, rotates=rotates)


@app.route('/duration', methods=["GET", "POST"])
def duration():
    display_value = main.get_duration()
    if request.method == "POST":
        subject = request.form['subject_id']
        answer = main.get_duration_answer(subject)

        if answer is None:
            error = "Input value is not valid. Enter correct value: "
            return render_template('duration.html', display_value=display_value, error=error)
        else:
            answer_input = request.form['duration_id']
            evaluate = main.evaluate_answer(answer, answer_input)
            return render_template('duration.html', display_value=display_value, answer_value=answer_input,
                                   answer=answer, evaluate=evaluate)
    else:
        return render_template('duration.html', display_value=display_value)


@app.route('/modalverbs', methods=["GET", "POST"])
def modalverb():
    display_value = main.get_modalverb()
    pronoun = main.get_pronoun()

    if request.method == "POST" and request.form['clear'] == "none":
        key = request.form['questionkey']
        modalverb = request.form['modalverb']
        entered_answer = request.form['answer']
        question_body = request.form['questionbody']
        check_answer = main.evaluate_answer(entered_answer, modalverb)

        return render_template('modalverbs.html', display_value=display_value, pronoun=pronoun,
                               questionkey=key, questionbody=question_body, answer=entered_answer, result=check_answer)
    else:
        display_question = main.get_modal_questions()

        return render_template('modalverbs.html', display_value=display_value, pronoun=pronoun,
                               modal_question=display_question)


@app.route('/order', methods=["GET", "POST"])
def order():
    return render_template('order.html')


@app.route('/perfect', methods=["GET"])
def perfect_get():
    verbs = main.get_all_verbs()

    return render_template('perfect.html', verbs=verbs)


@app.route('/perfect', methods=["POST"])
def perfect():

    if request.form['verbtype'] == "none":
        past_answer = request.form['pastanswer']
        perfect_answer = request.form['perfectanswer']

        past_key = request.form['pastkey']
        perfect_verb = request.form['perfectverb']
        return_verb = request.form['verb']
        result = main.evaluate_perfect(past_answer, past_key, perfect_answer, perfect_verb)
        question = main.get_verb_same_question(return_verb)
        return render_template('perfect.html', question=question, result=result)
    else:
        items = [1, 1, 1]

        if request.form['verbtype'] == "regwopre":
            items[1] = 0
            items[2] = 0
            explanation = 'ge --- t'
        elif request.form['verbtype'] == "regwzpreni":
            items[1] = 0
            explanation = '--- t'
        elif request.form['verbtype'] == "iregwopre":
            items[0] = 0
            items[1] = 0
            items[2] = 0
            explanation = 'ge --- en'
        elif request.form['verbtype'] == "iregwzpretre":
            items[0] = 0
            explanation = '(pre) ge --- en'
        elif request.form['verbtype'] == "iregwzpreni":
            items[0] = 0
            items[1] = 0
            explanation = '--- en'
        else:
            explanation = '(pre) ge --- t'

        verbs = main.get_verbs(items)
        question = main.get_verb_question(verbs)
        verbs = main.get_verbs(items)

        return render_template('perfect.html', verbs=verbs, explanation=explanation, question=question)


@app.route('/date', methods=["GET"])
def dates():
    dates = dt.get_dates()
    whole_date = dt.get_date()
    month = whole_date.month
    date = whole_date.day
    year = whole_date.year

    return render_template('date.html', dates=dates, month=month, year=year, date=date)


@app.route('/date', methods=["POST"])
def dates_post():
    dates = dt.get_dates()
    date = request.form['date']
    month = request.form['month']
    year = request.form['year']
    answer = request.form['answer']

    validation = dt.validate_date_answer(date, month, answer)

    return render_template('date.html', dates=dates, month=month, year=year,
                          date=date,  answer=answer, validation=validation)


@app.route('/pronoun', methods=["GET"])
def pronoun():
    pronouns = main.get_pronoun_nominative()
    pro_table = main.get_pronoun_table()

    return render_template('pronoun.html', pronoun=pronouns, protable=pro_table)


if __name__ == '__main__':
    app.run()
