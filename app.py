import os
from flask import Flask, render_template
from rq import Queue
from rq.job import Job
from worker import conn
from models import *
import nltk
import grequests
import requests

app = Flask(__name__)
#app.config.from_object(os.environ['APP_SETTINGS'])

q = Queue(connection=conn)



def count_and_save_words(url):
	errors = []
	print "!@!@!@!@"
	try:
		r = requests.get(url)
	except Exception as err:

		errors.append(
			err + "s"
		)
	return {"error" : errors}

job = q.enqueue_call(
		func=count_and_save_words, args=("http://aaronlandy.com",), result_ttl=5000
	)

@app.route('/', methods=['GET', 'POST'])
def index():
	results = {}
	if request.method == "POST":
		url = request.form['url']
		if 'http://' not in url[:7]:
			url = 'http://' + url
		
		print job.get_id()
	return render_template('index.html', results=results)

@app.route("/results/<job_key>", methods=['GET'])
def get_results(job_key):

    job = Job.fetch(job_key, connection=conn)

    if job.is_finished:
        return str(job.result), 200
    else:
        return "Nay!", 202



