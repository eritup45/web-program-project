# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, Response
from Crawler_PTT_Beauty import crawler
from Crawler_search_name import s_crawler
import os

# crawler()
# app = Flask(__name__)
app = Flask(__name__, static_url_path='')

# 加載靜態網頁
@app.route('/test')
def test():
    return app.send_static_file('home.html')

# Home
@app.route('/', methods=['GET'])
def index():
    search_name = request.args.get('search_name',' ',type = str)    # get info from form
    print("search_name is", search_name, '.')
    PAGE = 10    # How many pages in PTT beauty
    result = {} # dictionary contains the search_name
    s_crawler(search_name, PAGE, result)
    return render_template('home.html', result = result)

# 今日美女
@app.route('/today_beauty')
def today_beauty():
    path = crawler()
    return render_template("today_beauty.html", path = path)

# 使用方法
@app.route('/how2use')
def how2use():
    return render_template('how2use.html')

# self introduce    
@app.route('/about')    #define in ./templates/includes
def about():
    return render_template('/self_intro/self_intro.html')

@app.route('/self_intro/self_intro_ch')
def self_intro_ch():
    return render_template('/self_intro/self_intro_ch.html')
    
@app.route('/self_intro/self_intro_eng')
def self_intro_eng():
    return render_template('/self_intro/self_intro_eng.html')

@app.route('/self_intro/edu_ch')
def edu_ch():
    return render_template('/self_intro/edu_ch.html')

@app.route('/self_intro/edu_eng')
def edu_eng():
    return render_template('/self_intro/edu_eng.html')
# self introduce

# @app.route('/articles')
# def articles():
#     return render_template('articles.html', articles = Articles)
#     #pass in articles

if __name__ == "__main__":
    app.run(debug=True)
