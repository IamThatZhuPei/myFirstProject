# coding:utf-8

import time
from settings import db

class works:
	def __init__(self):
		self.work = ''

	def getWorks(self):
		works = db.select('Works')
		print("works is:", works)		
		return list(works)

	def addWorks(self, aWork):
		if self.isIn(aWork) :
			return False
		else :
			createtime = int(time.time())
			addworkResult = db.insert('Works', work=aWork.work, createtime=createtime)
			print(addworkResult)
			return True


	def isIn(self, aWork):
		# result = db.select('Works', work = aWork.work)
		result = db.where('Works', work = aWork.work)
		# print("RRRR")
		
		if len(list(result)) > 0 :
			return True
			# 数据库中存在此工作
		else :
			return False

