import os
from urllib import urlopen
import grequests
import nltk
from bs4 import BeautifulSoup
import redis
from rq import Worker, Queue, Connection
from gevent import monkey; monkey.patch_all()
from gevent.pool import Pool


def count_and_save_words(url):
	#r = grequests.get(url)
	p = Pool(1)
	p.map(requests.get, url)
	
	return {'a' : 'r'}



listen = ['default']

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

conn = redis.from_url(redis_url)

if __name__ == '__main__':
	with Connection(conn):
		worker = Worker(map(Queue, listen))
		worker.work()