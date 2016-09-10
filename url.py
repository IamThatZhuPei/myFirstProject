# coding: utf-8

urls = (
	'/', 'index.Index',
	'/addworks', 'work.AddWorks',
	'/addwork', 'work.addWork',
	'/worklist', 'work.worklist',
	'/workdetail', 'work.workdetail',
	'/addperson', 'person.addPerson',
	'/updateperson', 'person.updatePerson',
	'/checkperson', 'person.checkPerson',

	'/scancall', 'scancall.scanCall',
	'/okmsg', 'work.okmsg',
	'/askforwork', 'work.askForWork',
	# 该行代表用户请求根目录时是去请求 index 控制器对象的 Index 方法
	)