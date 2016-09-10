# coding: utf-8
from settings import render

class Index:
	def GET(self):
		return render.index()