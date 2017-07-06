#服务器第一次运行该脚本时，执行该脚本，下载脚本依赖的第三方库

import os
import setting

print ('Starting....')
for moudel in setting.INSTALL_MOUDEL:
    os.system('%s %s' % ('pip3 install', moudel)) #安装依赖模块
print ('End......')