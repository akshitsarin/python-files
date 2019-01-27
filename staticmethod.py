class A ():
	def __init__(self):
		print "Hello"
	@staticmethod 
	def stat():
		print "I am static"
if __name__ == "__main__":
	A.stat()
	obj = A()
	obj.stat()
