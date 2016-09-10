# coding: utf-8
import time
from settings import db
from personInfo import personInfo

class workInfo:
	def __init__(self):
		self.createtime = int(time.time())
		self.workname = ''
		self.worknum = ''
		self.company = ''
		self.picture = ''
		self.aboutcompany = ''
		self.aboutwork = ''
		self.salary = ''
		self.workaddress = ''
		self.endtime = ''
		self.status = 1

	def getAllWorkInfo(self):
		result = db.query('SELECT * FROM work')
		return list(result)

	def addWorkInfo(self,work):
		result = db.query('''INSERT INTO work (createtime,workname,worknum,company,picture,aboutcompany,
			aboutwork,salary,workaddress,endtime,status) VALUES ($createtime,$workname,$worknum,$company,
			$picture,$aboutcompany,$aboutwork,$salary,$workaddress,$endtime,$status)''',
			vars=dict(createtime=work.createtime,workname=work.workname,worknum=work.worknum,company=work.company,
				picture=work.picture,aboutcompany=work.aboutcompany,aboutwork=work.aboutwork,
				salary=work.salary,workaddress=work.workaddress,endtime=work.endtime,status=work.status))
		return True

	def changeStatus(self,work):
		result = db.query('''UPDATE work SET status=$status WHERE createtime=$createtime''',
			vars=dict(status=work.status,createtime=work.createtime))
		return True

	def getWorkList(self):
		endtime = time.strftime('%Y-%m-%d',time.localtime())
		result = db.query('''SELECT * FROM work WHERE endtime >= $et AND status == 1''',
			vars=dict(et=endtime))
		return list(result)

	def getWork(self,createtime):
		result = db.query('SELECT * FROM work WHERE createtime=$ct',vars=dict(ct=createtime))
		return list(result)

