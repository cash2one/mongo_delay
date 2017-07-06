
module_name = '.'.join(('hello','hello1','test'))
m1 = __import__(module_name)  # 找到了脚本所在的目录
print (m1)
script = getattr(m1, 'hello1')  # 根据类型找到脚本
cls = getattr(script, 'test')
print (cls)
cls = getattr(cls, 'test')()  # 根据类型找到脚本中的类，实例话
print (script)