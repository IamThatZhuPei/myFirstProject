# from settings import render


# class scanCall:
# 	def GET(self):
# 		return render.scancall()

a_var = 'global value'
def outer():
	a_var = 'enclosed value'

	def inner():
                nonlocal a_var
		a_var = 'local value'
		print(a_var)
		
	inner()
	
outer()
