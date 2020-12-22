def deco(anything):
    """Nodes are marked by random functions (here print()), functions involving \
input parameter (here the function "anything"), and the input function \
"anything" itself.  
"""
	type(anything)
	anything	print("another print")
	print("report start.")
	def wrapper(self,*arg,**kwarg):
		print(type(wrapper))
		print("point 1: wrapper initiated")
		anything(self,*arg,**kwarg)
		print("input func executed, about to end wrapper.")
	return wrapper
	print("wrapper ends")
	type(anything)
	anything
	print("report2 started")
	def wrapper2(self,*arg,**kwarg):
		print(type(wrapper))
		print("point 2: wrapper initiated")
		anything(self,*arg,**kwarg)
		print("input2 func executed, about to end wrapper2.")
	return wrapper2
	print("wrappers ends")
	type(anything)
	anything
@deco
def func(another):
	print("the function has been initiated")
	print("function for {}".format(another))
	print("the function has been terminated.")
# It returns :
#
# "
# another print
# report start.
# "
#
# Which indicates that by calling "@deco" and defining the input function, we 
# are evoking the deco(anything) itself, until the wrapper function
# "wrapper(self, *arg, **kwarg")". After wrapper(self, *arg, **kwarg) has been
# defined, the parent function "deco(anything)" is halted.

func("parameter1")
# It returns :
#
# "
#<class 'function'>
# point 1: wrapper initiated
# the function has been initiated
# function for parameter1
# the function has been terminated.
# input func executed, about to end wrapper.
# "
#
# which means that deco(anything) is run until the first wrapper (and only
# the first wrapper) has been executed (at "return wrapper"). After that,
# deco(anything) is halted, and any function after the return of the first
# wrapper is omitted..

def deco(anything):
	type(anything)
	anything
	print("another print")
	print("report2 started")
	def wrapper2(self,*arg,**kwarg):
		print(type(wrapper2))
		print("point 2: wrapper initiated")
		anything(self,*arg,**kwarg)
		print("input2 func executed, about to end wrapper2.")
	return wrapper2
	print("wrapper2 ends")
	type(anything)
	anything
	print("report start.")
	def wrapper(self,*arg,**kwarg):
		print(type(wrapper))
		print("point 1: wrapper initiated")
		anything(self,*arg,**kwarg)
		print("input func executed, about to end wrapper.")
	return wrapper
	print("wrapper ends")
	type(anything)
	anything
@deco
def func(another):
	print("the function has been initiated")
	print("function for {}".format(another))
	print("the function has been terminated.")
# It returns :
#
# "
# another print
# report2 started
# "

func("parameter1")
# It returns :
#
# "
# <class 'function'>
# point 2: wrapper initiated
# The function has been initiated
# function for parameter1
# the function has been terminated.
# input2 func executed, about to end wrapper2.
# "
# which proves that "wrapper" the name is not necessary for the
# function that actually runs as a wrapper. Here the wrapper for
# func(another) is the function wrapper2.

def deco(anything):
	type(anything)
	anything
	print("another print")
	print("report2 started")
	def wrapper2(*arg,**kwarg):
		print(type(wrapper2))
		print("point 2: wrapper initiated")
		anything(*arg,**kwarg)
		print("input2 func executed, about to end wrapper2.")
	return wrapper2
	print("wrapper2 ends")
	type(anything)
	anything
	print("report start.")
	def wrapper(*arg,**kwarg):
		print(type(wrapper))
		print("point 1: wrapper initiated")
		anything(*arg,**kwarg)
		print("input func executed, about to end wrapper.")
	return wrapper
	print("wrapper ends")
	type(anything)
	anything
@deco
def func(another):
	print("the function has been initiated")
	print("function for {}".format(another))
	print("the function has been terminated.")
# It returns :
#
# "
# another print
# report2 started
# "

func("parameter23")
# It returns :
#
# "
# <class 'function'>
# point 2: wrapper initiated
# The function has been initiated
# function for parameter23
# the function has been terminated.
# input2 func executed, about to end wrapper2.
# "
#
# Why the self parameter in wrapper2 did not break the function?
