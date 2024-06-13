from flask import Flask, request, render_template
import user_agents

app = Flask(__name__)

@app.route('/')
def home():
    user_agent = request.headers.get('User-Agent')
    parsed_user_agent = user_agents.parse(user_agent)
    return render_template('index.html', user_agent=user_agent, parsed_user_agent=parsed_user_agent)

@app.route('/parse', methods=['POST'])
def parse():
    user_agent = request.form.get('user_agent')
    parsed_user_agent = user_agents.parse(user_agent)
    return render_template('index.html', user_agent=user_agent, parsed_user_agent=parsed_user_agent, from_form=True)

if __name__ == '__main__':
    app.run(debug=True)
