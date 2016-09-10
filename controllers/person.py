# coding:utf-8

from settings import render
from settings import staticInfo
from works import works
from personInfo import personInfo
import web

class addPerson:
	def GET(self):
		sInfo = staticInfo()
		work = works()
		worklist = work.getWorks()
		newPerson = personInfo()
		message = ''
		return render.addPerson(sInfo,worklist,newPerson,message)

	def POST(self):
		person = personInfo()
		message = ''
		if web.input()['perName'].strip() != '':
			person.perName = web.input()['perName'].strip()
		else:
			message += '[姓名]'
		if web.input()['IDcardNo'].strip() != '':
			person.IDcardNo = web.input()['IDcardNo'].strip()
		else:
			message += '[身份证号]'
		person.address = web.input()['address']
		if web.input()['height'].strip() != '':
			person.height = eval(web.input()['height'])
		if web.input()['phoneNo'].strip() != '':
			person.phoneNo = eval(web.input()['phoneNo'])
		else:
			message += '[电话]'
		person.eMail = web.input()['eMail']
		person.birthDay = web.input()['birthDay']
		person.birthPlace = web.input()['birthPlace']
		person.isMarry = eval(web.input()['isMarry'])
		person.education = eval(web.input()['education'])
		person.school = web.input()['school']
		person.sex = eval(web.input()['sex'])
		if web.input()['qq'].strip() != '':
			person.qq = eval(web.input()['qq'])
		person.wx = web.input()['wx']
		person.politicalStatus = eval(web.input()['politicalStatus'])
		person.hukou = web.input()['hukou']
		person.introduce = web.input()['introduce']
		# person.work = web.input()['work']
		sss = web.input(work=[])['work']
		for x in sss:
			person.work += x
			person.work += '//'

		sInfo = staticInfo()
		work = works()
		worklist = work.getWorks()

		if message != '':
			message += '必须填写~'
			return render.addPerson(sInfo,worklist,person,message)
		if person.addPerson(person) :
			return render.addPerson(sInfo,worklist,person,message)
		else :
			message += '此人信息已存在，请编辑已有信息！'
			return render.addPerson(sInfo,worklist,person,message)

class updatePerson:
	def GET(self):
		sInfo = staticInfo()
		work = works()
		worklist = work.getWorks()
		person = personInfo()
		print(web.input())
		s = web.input().i.split(',')
		person.perName = s[0]
		person.IDcardNo = s[1]
		lperson = person.getPerson(person)
		if len(lperson) > 0:
			person.phoneNo = lperson[0].phoneNo
			person.address = lperson[0].address
			person.hukou = lperson[0].hukou
			person.birthPlace = lperson[0].birthPlace
			person.height = lperson[0].height
			person.sex = lperson[0].sex
			person.birthDay = lperson[0].birthDay
			person.isMarry = lperson[0].isMarry
			person.education = lperson[0].education
			person.school = lperson[0].school
			person.politicalStatus = lperson[0].politicalStatus
			person.eMail = lperson[0].eMail
			person.wx = lperson[0].wx
			person.qq = lperson[0].qq
			person.work = lperson[0].work
			person.introduce = lperson[0].introduce
		message = ''
		return render.updatePerson(sInfo,worklist,person,message)

	def POST(self):
		person = personInfo()
		message = ''
		person.perName = web.input()['perName'].strip()
		person.IDcardNo = web.input()['IDcardNo'].strip()
		person.address = web.input()['address']
		if web.input()['height'].strip() != '':
			person.height = eval(web.input()['height'])
		if web.input()['phoneNo'].strip() != '':
			person.phoneNo = eval(web.input()['phoneNo'])
		else:
			message += '[电话]'
		person.eMail = web.input()['eMail']
		person.birthDay = web.input()['birthDay']
		person.birthPlace = web.input()['birthPlace']
		person.isMarry = eval(web.input()['isMarry'])
		person.education = eval(web.input()['education'])
		person.school = web.input()['school']
		person.sex = eval(web.input()['sex'])
		if web.input()['qq'].strip() != '':
			person.qq = eval(web.input()['qq'])
		person.wx = web.input()['wx']
		person.politicalStatus = eval(web.input()['politicalStatus'])
		person.hukou = web.input()['hukou']
		person.introduce = web.input()['introduce']
		# person.work = web.input()['work']
		sss = web.input(work=[])['work']
		for x in sss:
			person.work += x
			person.work += '//'

		sInfo = staticInfo()
		work = works()
		worklist = work.getWorks()

		if message != '':
			message += '必须填写~'
			return render.updatePerson(sInfo,worklist,person,message)
		else:
			print("@@@@@@@@@@@",person)
			person.updatePerson(person)
			return render.updatePerson(sInfo,worklist,person,message)

class checkPerson:
	def GET(self):
		newPerson = personInfo()
		message = ''
		return render.checkPerson(newPerson,message)

	def POST(self):
		person = personInfo()
		message = ''
		if web.input()['perName'].strip() != '':
			person.perName = web.input()['perName'].strip()
		else:
			message += '[姓名]'
		if web.input()['IDcardNo'].strip() != '':
			person.IDcardNo = web.input()['IDcardNo'].strip()
		else:
			message += '[身份证号]'
		if message != '':
			message += '必须填写~'
			return render.checkPerson(person,message)
		lperson = person.getPerson(person)
		if len(lperson) > 0 :
		# 	person.phoneNo = lperson[0].phoneNo
		# 	person.address = lperson[0].address
		# 	person.hukou = lperson[0].hukou
		# 	person.birthPlace = lperson[0].birthPlace
		# 	person.height = lperson[0].height
		# 	person.sex = lperson[0].sex
		# 	person.birthDay = lperson[0].birthDay
		# 	person.isMarry = lperson[0].isMarry
		# 	person.education = lperson[0].education
		# 	person.school = lperson[0].school
		# 	person.politicalStatus = lperson[0].politicalStatus
		# 	person.eMail = lperson[0].eMail
		# 	person.wx = lperson[0].wx
		# 	person.qq = lperson[0].qq
		# 	person.work = lperson[0].work
		# 	person.introduce = lperson[0].introduce

		# 	sInfo = staticInfo()
		# 	work = works()
		# 	worklist = work.getWorks()
		# 	# return render.updatePerson(sInfo,worklist,person,message)
			raise web.seeother('/updateperson?i=%(n)s,%(i)s' % {'n':person.perName, 'i':person.IDcardNo})
		else:
			# message = '此人不存在，请确认输入的信息或添加信息'
			sInfo = staticInfo()
			work = works()
			worklist = work.getWorks()
			message = ''
			return render.addPerson(sInfo,worklist,person,message)
			# return render.checkPerson(person,message)
