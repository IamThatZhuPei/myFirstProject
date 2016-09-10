# coding: utf-8

import sys
import url
import web

sys.path.append('./controllers')
sys.path.append('./models')
urls = url.urls

if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()