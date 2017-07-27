class test:
    def hello(self):
        module_name = '.'.join(('hello', 'kk','fun'))
        m1 = __import__(module_name)  # 找到了脚本所在的目录

        script = getattr(m1, 'kk')  # 根据类型找到脚本
        script = getattr(script, 'fun')  # 根据类型找到脚本
        cls = getattr(script, 'hel')()  # 根据类型找到脚本中的类，实例话
        cls.test()