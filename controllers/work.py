# coding: utf-8
from settings import render
from settings import staticInfo
from settings import pictype
from askforwork import askwork
from works import works
from workInfo import workInfo
from personInfo import personInfo
import web

class AddWorks:
	def GET(self):
		return render.addworks('new')

	def POST(self):
		work = works()
		# print(web.input()['work'])
		if web.input()['work'].strip() == '':
			return render.addworks('null')
		else:
			work.work = web.input()['work']
			if work.addWorks(work) :
				print('aaaa')
				return render.addworks('new')
			else :
				print('bbbb')
				return render.addworks('exist')


class addWork:
	def GET(self):
		sInfo = staticInfo()
		work = works()
		worklist = work.getWorks()
		wkInfo = workInfo()
		message = ''
		return render.addwork(sInfo,worklist,wkInfo,message)

	def POST(self):
		sInfo = staticInfo()
		work = works()
		worklist = work.getWorks()
		wkInfo = workInfo()
		message = ''

		# print('$$$$$$$$$',web.input(workradio='1')['workradio'])

		p = web.input(picture={})
		print(',,,,,,,,,', p.picture.filename)
		if p.picture.filename != '':
			filepath = p.picture.filename.replace('\\','/')
			filename = filepath.split('/')[-1]
			print(filename.split('.')[-1].lower())
			if filename.split('.')[-1].lower() not in pictype:
				message += '[公司图片]格式不正确！'

		if web.input(workradio='1') == '1':
			message += '[工作岗位]'
		else:
			wkInfo.workname = web.input(workradio='1')['workradio']
		if web.input()['worknum'] == '':
			message += '[招聘人数]'
		else:
			wkInfo.worknum = eval(web.input()['worknum'])
		if web.input()['company'].strip() == '':
			message += '[公司名称]'
		else:
			wkInfo.company = web.input()['company'].strip()
		if web.input()['salary'] == '':
			message += '[岗位薪资]'
		else:
			wkInfo.salary = eval(web.input()['salary'])
		if web.input()['workaddress'].strip() == '':
			message += '[工作地点]'
		else:
			wkInfo.workaddress = web.input()['workaddress']
		if web.input()['endtime'].strip() == '':
			message += '[截止时间]'
		else:
			wkInfo.endtime = web.input()['endtime'].strip()
		if web.input()['aboutcompany'].strip() == '':
			message += '[公司简介]'
		else:
			wkInfo.aboutcompany = web.input()['aboutcompany'].strip()
		if web.input()['aboutwork'].strip() == '':
			message += '[岗位简介]'
		else:
			wkInfo.aboutwork = web.input()['aboutwork'].strip()

		if message == '':
			
			fout = open(sInfo.uploadpicdir + '/' + filename, 'wb')
			fout.write(p.picture.file.read())
			fout.close()

			wkInfo.picture = filename

			result = wkInfo.addWorkInfo(wkInfo)
			render.addwork(sInfo,worklist,wkInfo,message)
		else:
			message += '必须填写！'
			return render.addwork(sInfo,worklist,wkInfo,message)

class worklist:
	def GET(self):
		work = workInfo()
		wl = work.getWorkList()
		worklist = []
		for w in wl:
			work = workInfo()
			work.createtime = w['createtime']
			print(',,,,,,,,,,,,,,,,',w.createtime, work.createtime)
			work.workname = w['workname']
			work.worknum = w['worknum']
			work.company = w['company']
			work.workaddress = w['workaddress']
			worklist.append(work)

		return render.worklist(worklist)

class workdetail:
	def GET(self):
		sInfo = staticInfo()
		createtime = web.input()['createtime']
		work = workInfo()
		detail = work.getWork(createtime)
		print('...........',detail)
		work.createtime = detail[0].createtime
		work.workname = detail[0].workname
		work.worknum = detail[0].worknum
		work.company = detail[0].company
		work.picture = detail[0].picture
		work.aboutcompany = detail[0].aboutcompany
		work.aboutwork = detail[0].aboutwork
		work.salary = detail[0].salary
		work.workaddress = detail[0].workaddress
		work.endtime = detail[0].endtime

		return render.workdetail(sInfo,work)

class askForWork:
	def GET(self):
		person = personInfo()
		message = ''
		afw = askwork()
		afw.worktime = int(web.input()['worktime'].strip())
		print(afw.worktime)
		return render.askForWork(person,message)

	def POST(self):
		afw = askwork()
		person = personInfo()
		message = ''
		if web.input()['worktime'].strip() != '':
			afw.worktime = int(web.input()['worktime'].strip())
		else:
			message += '[worktime is null!]'
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
			return render.askForWork(person,message)
		lperson = person.getPerson(person)
		if len(lperson) > 0 :
			afw.IDcardNo = person.IDcardNo
			afw.newAskForWork(afw)
			return render.okmsg()
		else:
			message = '此人不存在，请确认输入的信息或添加个人信息'
			return render.askForWork(person,message)


class okmsg:
	def GET(self):
		return render.okmsg()

