import time
from settings import db

class askwork:
	def __init__(self):
		self.createtime = int(time.time())
		self.worktime = ''
		self.IDcardNo = ''

	def newAskForWork(self, askwk):
		result = db.query('''INSERT INTO askforwork(createtime, worktime, IDcardNo) 
			VALUES($createtime, $worktime, $IDcardNo) ''',
			vars = dict(createtime=askwk.createtime,worktime=askwk.worktime,IDcardNo=askwk.IDcardNo))
		return True

	
