# coding:utf-8
import time
from settings import db


class personInfo:

	def __init__(self):
		self.IDcardNo = ''
		self.perName = ''
		self.address = ''
		self.phoneNo = ''
		self.height = ''
		self.eMail = ''
		self.birthDay = ''
		self.birthPlace = ''
		self.isMarry = 0
		self.education = 0
		self.school = ''
		self.sex = 1
		self.qq = ''
		self.wx = ''
		self.politicalStatus = ''
		self.hukou = ''
		self.createTime = ''
		self.updateTime = ''
		self.power = '0'
		self.enable = ''
		self.work = ''
		self.introduce = ''

	def getPerson(self, person):
		result = db.query('SELECT * FROM PerInfo WHERE perName=$n and IDcardNo=$id',
		 vars=dict(n=person.perName, id=person.IDcardNo))
		return list(result)

	def addPerson(self, person):
		if len(self.getPerson(person)) > 0 :
			return False
		else :
			createtime = int(time.time())
			result = db.insert('PerInfo',IDcardNo=person.IDcardNo,
				perName=person.perName,address=person.address,
				phoneNo=person.phoneNo,height=person.height,
				eMail=person.eMail,birthDay=person.birthDay,
				birthPlace=person.birthPlace,isMarry=person.isMarry,
				education=person.education,school=person.school,
				sex=person.sex,qq=person.qq,wx=person.wx,
				politicalStatus=person.politicalStatus,hukou=person.hukou,
				createTime=createtime,updateTime=createtime,
				power='0',enable='',work=person.work,introduce=person.introduce)

			return True
	
	def updatePerson(self, person):
		print('@@@@@@@@@@@@@@@@@@@@update@@@@@@@@@@@@@@@@@@@@@@@')
		upt = int(time.time())
		result = db.query('''UPDATE PerInfo SET 
			address=$address,phoneNo=$phoneNo,height=$height,eMail=$eMail,
			birthDay=$birthDay,birthPlace=$birthPlace,isMarry=$isMarry,
			education=$education,school=$school,sex=$sex,qq=$qq,wx=$wx,
			politicalStatus=$politicalStatus,hukou=$hukou,updateTime=$updateTime,
			work=$work,introduce=$introduce WHERE perName=$perName AND IDcardNo=$IDcardNo''',
			vars=dict(perName=person.perName, IDcardNo=person.IDcardNo, 
				address=person.address, phoneNo=person.phoneNo, height=person.height, 
				eMail=person.eMail, birthDay=person.birthDay, birthPlace=person.birthPlace, 
				isMarry=person.isMarry, education=person.education, school=person.school, 
				sex=person.sex, qq=person.qq, wx=person.wx, politicalStatus=person.politicalStatus, 
				hukou=person.hukou, updateTime=upt, work=person.work, introduce=person.introduce))

	def getAll(self):
		persons = db.select('PerInfo')
		# TODO
		return persons




	

