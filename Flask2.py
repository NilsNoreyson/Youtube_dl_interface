# -*- coding: utf-8 -*-
"""
Created on Tue May 13 14:28:23 2014

@author: peterb
"""


from flask import Flask,jsonify,request, make_response
import os
import subprocess, shlex


topPath=os.path.dirname(os.path.realpath(__file__))


app = Flask(__name__, static_url_path='')

outPath = '/media/music/rip/Youtube/%(title)s.%(ext)s'





@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/set_number',methods=['POST'])
def set_number():
    youUrl=request.form['youtube_url']
    print youUrl
    youtube_dl = "/usr/bin/youtube-dl %s -o %s -f bestaudio" %(youUrl, outPath)


    arg_ls = shlex.split(youtube_dl)
    download_youtube=subprocess.Popen(arg_ls)

    return app.send_static_file('index.html')

if __name__ == '__main__':
    #app.run(host='0.0.0.0',port=443,ssl_context=context,debug=True)
    app.run(host='0.0.0.0',port=8080,debug=True)
