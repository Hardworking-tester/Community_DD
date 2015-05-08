#encoding:utf-8
class Person:
			# 实例化初始化的方法
			def __init__(self,name,age):
				self.name = name
				self.age = age
				print self.name
			# 有self此函数为方法
			def sayHi(self):
				print 'Hello, my name is', self.name
			# 对象消逝的时候被调用
			def __del__(self):
				print 'over'

p = Person('Swaroop',18)
		# 使用对象方法
p.sayHi()