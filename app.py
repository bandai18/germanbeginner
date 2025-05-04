from flask import Flask, render_template, request, Response, redirect, flash
from flask_wtf.csrf import CSRFProtect, CSRFError
from markupsafe import escape
import logging
import main
import date_function as dt
import db
import re
import html
import os


app = Flask(__name__)

# Configure application
app.config.update(
    SECRET_KEY=os.environ.get('SECRET_KEY', 'dev-key-change-in-production'),
    DATABASE=os.path.join(app.instance_path, 'german.db'),
    DEBUG=os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', 't', '1')
)

# Setup logging
logging.basicConfig(
    level=logging.DEBUG if app.config['DEBUG'] else logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Initialize CSRF protection
csrf = CSRFProtect(app)

# Initialize database
db.init_app(app)


@app.route('/', methods=["GET"])
def index():

    return render_template('index.html')


@app.route('/', methods=["POST"])
def index_post():
    enter_time = sanitize_input(request.form.get('time_id', ''))
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
        response = sanitize_input(request.form.get('entered_value', ''))
        if response != "clear":
            time = main.get_time(response)
            res_rotate = main.get_rotate(response)

            return render_template('practice.html', display_value=response, time_value=time, rotates=res_rotate)

    return render_template('practice.html', display_value=display_value, rotates=rotates)


@app.route('/duration', methods=["GET", "POST"])
def duration():
    display_value = main.get_duration()
    if request.method == "POST":
        subject = sanitize_input(request.form.get('subject_id', ''))
        answer = main.get_duration_answer(subject)

        if answer is None:
            error = "Input value is not valid. Enter correct value: "
            return render_template('duration.html', display_value=display_value, error=error)
        else:
            answer_input = sanitize_input(request.form.get('duration_id', ''))
            evaluate = main.evaluate_answer(answer, answer_input)
            return render_template('duration.html', display_value=display_value, answer_value=answer_input,
                                   answer=answer, evaluate=evaluate)
    else:
        return render_template('duration.html', display_value=display_value)


@app.route('/modalverbs', methods=["GET", "POST"])
def modalverb():
    display_value = main.get_modalverb()
    pronoun = main.get_pronoun()

    if request.method == "POST" and request.form.get('clear', '') == "none":
        key = sanitize_input(request.form.get('questionkey', ''))
        modalverb = sanitize_input(request.form.get('modalverb', ''))
        entered_answer = sanitize_input(request.form.get('answer', ''))
        question_body = sanitize_input(request.form.get('questionbody', ''))
        check_answer = main.evaluate_answer(entered_answer, modalverb)

        return render_template('modalverbs.html', display_value=display_value, pronoun=pronoun,
                               questionkey=key, questionbody=question_body, answer=entered_answer, result=check_answer)
    else:
        display_question = main.get_modal_questions()

        return render_template('modalverbs.html', display_value=display_value, pronoun=pronoun,
                               modal_question=display_question)


@app.route('/perfect', methods=["GET"])
def perfect_get():
    verbs = main.get_all_verbs()

    return render_template('perfect.html', verbs=verbs)


@app.route('/perfect', methods=["POST"])
def perfect():
    verbtype = sanitize_input(request.form.get('verbtype', ''))

    if verbtype == "none":
        past_answer = sanitize_input(request.form.get('pastanswer', ''))
        perfect_answer = sanitize_input(request.form.get('perfectanswer', ''))

        past_key = sanitize_input(request.form.get('pastkey', ''))
        perfect_verb = sanitize_input(request.form.get('perfectverb', ''))
        return_verb = sanitize_input(request.form.get('verb', ''))
        result = main.evaluate_perfect(past_answer, past_key, perfect_answer, perfect_verb)
        question = main.get_verb_same_question(return_verb)
        return render_template('perfect.html', question=question, result=result)
    else:
        items = [1, 1, 1]

        if verbtype == "regwopre":
            items[1] = 0
            items[2] = 0
            explanation = 'ge --- t'
        elif verbtype == "regwzpreni":
            items[1] = 0
            explanation = '--- t'
        elif verbtype == "iregwopre":
            items[0] = 0
            items[1] = 0
            items[2] = 0
            explanation = 'ge --- en'
        elif verbtype == "iregwzpretre":
            items[0] = 0
            explanation = '(pre) ge --- en'
        elif verbtype == "iregwzpreni":
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
    date = sanitize_input(request.form.get('date', ''))
    month = sanitize_input(request.form.get('month', ''))
    year = sanitize_input(request.form.get('year', ''))
    answer = sanitize_input(request.form.get('answer', ''))

    validation = dt.validate_date_answer(date, month, answer)

    return render_template('date.html', dates=dates, month=month, year=year,
                          date=date,  answer=answer, validation=validation)


@app.route('/pronoun', methods=["GET"])
def pronoun():
    pronouns = main.get_pronoun_nominative()
    pro_table = main.get_pronoun_table()

    return render_template('pronoun.html', pronoun=pronouns, protable=pro_table)


def sanitize_input(input_string):
    """Sanitize user input to prevent XSS attacks."""
    if input_string is None:
        return ""
    # HTML escape the string
    sanitized = html.escape(input_string)
    # Only allow alphanumeric characters, spaces, and specific punctuation
    sanitized = re.sub(r'[^\w\s.,:;?!-]', '', sanitized)
    return sanitized


@app.errorhandler(CSRFError)
def handle_csrf_error(e):
    return render_template('csrf_error.html', reason=e.description), 400


if __name__ == '__main__':
    app.run()
