from flask import Blueprint,request,jsonify,make_response,session,render_template,g,redirect,url_for
from .forms import QuestionForm,AnswerForm
from models import QuestionModel,AnswerModel
from exts import db
from decorators import login_required



bp = Blueprint('qa', __name__, url_prefix="/")

@bp.route('/')
def index():
    # return "Hello World"
    questions = QuestionModel.query.order_by(QuestionModel.create_time.desc()).all()
    return render_template('index.html',questions=questions)
@bp.route('/qa/public',methods=['GET','POST'])
@login_required
def public_question():
    if request.method == 'GET':
        return render_template('public_question.html')
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title,content=content,author_id=g.user.id)
            db.session.add(question)
            db.session.commit()
            return redirect("/")
            # return jsonify(form.data)
        else:
            # return jsonify(form.errors)
            print(form.errors)
            return redirect(url_for('qa.public_question'))

@bp.route('/qa/detail/<int:qa_id>')
def detail(qa_id):
    question = QuestionModel.query.get(qa_id)
    print(question.author.username)
    if question:
        return render_template('detail.html',question=question)
    else:
        return redirect("/")
    return render_template('detail.html',question=question)

@bp.route('answer/public',methods=['POST'])
@login_required
def public_answer():
    form = AnswerForm(request.form)

    # print("问题id："+form.question_id.data)
    if form.validate():
        content = form.content.data
        question_id = form.question_id.data
        print('--------------')
        print("问题id：" + str(form.question_id.data))
        print('--------------')
        answer = AnswerModel(content=content,question_id=question_id,author_id=g.user.id)
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('qa.detail',qa_id=question_id))
    else:
        # print('--------------')
        # print("问题id：" + form.question_id.data)
        # print('--------------')
        print(form.errors)
        return redirect(url_for('qa.detail',qa_id=request.form.get('question_id')))

@bp.route('/search')
def search():
    q = request.args.get('q')
    questions = QuestionModel.query.filter(QuestionModel.title.contains(q)).all()
    return render_template('index.html',questions=questions)