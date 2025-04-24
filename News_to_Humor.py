from flask import Flask,request,jsonify,json,Response
import requests
import os
from groq import Groq

app = Flask(__name__)

@app.route('/')
def home():
    return "Please Enter Your Queries in Url"

@app.route('/<string:keyword>')
def fetch_news(keyword):
    try:
        os.environ['GROQ_API_KEY'] = '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'        
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + os.getenv('GROQ_API_KEY', ''),
        }
        key = 'c5175958ce7244458fba294f6ff591a5'
        url= f'https://newsapi.org/v2/everything?q={keyword}&language=en&apiKey={key}'
        response = requests.get(url=url)
        if response.status_code == 200:
            data = response.json()
            list_articles = []
            maxloop = 5
            for values in data['articles'][:maxloop]:
                dic_articles = {}
                title = values['title']
                content = values['content']
                dic_articles['Title']= title
                dic_articles['Original News']= content
                json_data = {
                'model': 'llama-3.3-70b-versatile',
                'messages': [
                {
                'role': 'user',
                'content': f'News content is {content} please convert this in a humorous with emoji and very small line',
                },
                ],
                }

                response = requests.post('https://api.groq.com/openai/v1/chat/completions', headers=headers, json=json_data)
                if response.status_code != 200:
                    return "Too Many Requests Please Wait And Try Again"
                if response.status_code == 200:
                    data_res = response.json()
                    status = {}
                    dic_articles['Humorous News'] = data_res['choices'][0]['message']['content']
                    status['Status'] = "Success"
                    list_articles.append(status)
                    list_articles.append(dic_articles)


            return Response(json.dumps(list_articles, ensure_ascii=False, indent=4), mimetype="application/json")
            
    except Exception as e:
        return "Something is Wrong"
app.run(port=5000,debug=True)

