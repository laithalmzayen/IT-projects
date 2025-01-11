from Cooking import cooking
from flask import Flask, jsonify, request, abort, render_template
from experta import *

expert_engine = cooking()
app = Flask(__name__)

@app.route('/ask_question', methods=['POST'])
def ask_question():
    try:
        data = request.get_json()
        question = data.get('question', '')
        # Display the question in the console (for illustration purposes)
        expert_engine.running = False
        return jsonify({'question':question})
    except Exception:
        abort(400,'Error')
    # Simulate processing the question and getting an answer

@app.route('/get_suggestion',methods=['POST'])
def print_results():
    try:
        data = request.get_json()
        suggestion = data['suggestion']
    except Exception as e:
        abort(400, 'Error')
    final_suggestion = suggestion
    return jsonify({'suggestion':final_suggestion})
    return render_template('get_suggestion.html',suggestion = final_suggestion)

@app.route('/')
def hello():
    return render_template('ask_question.html',question="Hello")

@app.route('/start_engine')
def start():
    if not expert_engine.started:
        expert_engine.reset()
        expert_engine.started = True
    try:
        expert_engine.run()
        response_string = str(expert_engine.current_question)
        question = response_string.replace("answers: ","")
        answers = response_string.split("answers:")[1].split(",")
        for i in range(len(answers)):
            answers[i] = str(answers[i])
    except Exception:
        abort(400,'Error')
    # return jsonify({'Sucess':200,
    #                'Data':{
    #                    'question':question,
    #                    'answers':answers
    #                }})
    if expert_engine.end:
        final_resuls = expert_engine.suggestion
        expert_engine.current_question = ""
        expert_engine.started = False
        expert_engine.fact_name = ""
        expert_engine.end = False
        expert_engine.suggestion = ""
        return jsonify({'suggestion':final_resuls})
        # return render_template("get_suggestion.html",suggestion = expert_engine.suggestion)
    return jsonify({'question':question,'answers':answers})
    # return render_template("ask_question.html",question=question)


@app.route('/reset_engine',methods=['GET'])
def reset():
    expert_engine.reset()
    return jsonify({'sucess':200})

@app.route('/answer',methods=['POST'])
def answer():
    # data = request.get_data()
    # answer = str(data).split("user_answer")[1].replace("=","").replace("'","").replace("+"," ")
    try:
        data = request.get_json()
        answer = str(data['user_answer']).replace("=","").replace("'","").replace("+"," ")
        if expert_engine.fact_name == 'n':
            expert_engine.declare(Fact(n=str(answer)))
        elif expert_engine.fact_name == 'g':
            expert_engine.declare(Fact(g=str(answer)))
        elif expert_engine.fact_name == 'l':
            expert_engine.declare(Fact(l=str(answer)))
        elif expert_engine.fact_name == 'k':
            expert_engine.declare(Fact(k=str(answer)))
        elif expert_engine.fact_name == 'f':
            expert_engine.declare(Fact(f=str(answer)))
        elif expert_engine.fact_name == 'j':
            expert_engine.declare(Fact(j=str(answer)))
        expert_engine.running = True
        return start()
    except Exception:
        abort(400,'Error')

if __name__ == '__main__':
    app.debug = False
    app.run(host = '127.0.0.1',port=5000)