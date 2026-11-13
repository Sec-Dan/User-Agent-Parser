from flask import Flask, Response, request, render_template
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

@app.route('/robots.txt')
def robots_txt():
    return Response("User-agent: *\nAllow: /\nSitemap: https://agent.dansec.red/sitemap.xml\n", mimetype='text/plain')

@app.route('/sitemap.xml')
def sitemap_xml():
    return Response('<?xml version="1.0" encoding="UTF-8"?>\n'
                    '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                    '<url><loc>https://agent.dansec.red/</loc></url></urlset>\n', mimetype='application/xml')

if __name__ == '__main__':
    app.run(debug=True)
