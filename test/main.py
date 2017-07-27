module_name = '.'.join(('hello','run'))
m1 = __import__(module_name)  # 找到了脚本所在的目录

script = getattr(m1, 'run')  # 根据类型找到脚本

cls = getattr(script, 'test')()  # 根据类型找到脚本中的类，实例话
cls.hello()