# coding: utf-8

import web

render = web.template.render('templates', cache=False)# 设置模板目录和模板缓存
web.template.Template.globals['static'] = '/static' # 在模板中可以使用 static 该全局对象

db = web.database(dbn='sqlite', db='D:\wwwww\ws\personInfo.db3')

# uploadpicdir = 'D:/ws/p/upload'

pictype = ['jpg','jpeg','jpe','jfif','gif','png','bmp','tif','tiff','dib']

class staticInfo:
  def __init__(self):
    self.hukou = (u'农户', u'非农户')
    self.politicalStatus = (u'党员',u'团员',u'群众')
    self.isMarry = (u'已婚',u'未婚')
    self.education = (u'博士',u'硕士',u'学士',u'专科',u'高中',u'初中',u'小学')
    self.sex = (u'男',u'女')
    self.i = 0
    self.uploadpicdir = 'D:\wwwww/ws/p/static/upload'