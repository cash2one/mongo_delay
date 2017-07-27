def backproxy(self, tbobj, proxyip, retdict):  # retdict字典要求有三个字段:'host','result','resTime','deviceInfo'('id','type')
    if (proxyip is None) or (proxyip.get('_id') is None):
        return
    host = retdict.get('host', 'https://www.jd.com')
    if isinstance(host, str):
        hoststr = host[host.find(':') + 3:].replace('.', '_').replace('/', '__')
    else:
        print(host, "不是字符串类型")
        return
    ret = retdict.get('result', False)
    resTime = retdict.get('resTime')
    if ret == False:
        tscore = -10
    elif (resTime is None) or (isinstance(resTime, float) == False):
        tscore = 1
    elif resTime <= 1.0:
        tscore = 10
    elif resTime <= 2.0:
        tscore = 9
    elif resTime <= 3.0:
        tscore = 8
    elif resTime <= 4.0:
        tscore = 7
    elif resTime <= 5.0:
        tscore = 6
    elif resTime <= 6.0:
        tscore = 5
    elif resTime <= 7.0:
        tscore = 4
    elif resTime <= 8.0:
        tscore = 3
    elif resTime <= 9.0:
        tscore = 2
    elif resTime <= 10.0:
        tscore = 1
    else:
        tscore = 0
    if ret == True:  # 访问成功
        susscore = 1
    else:  # 访问不成功
        susscore = 0

    tempstr1 = 'ipInfo.score.' + hoststr + '.' + 'score'
    tempstr2 = 'ipInfo.score.' + hoststr + '.' + 'usecount'
    tempstr3 = 'ipInfo.score.' + hoststr + '.' + 'suscount'

    tbobj.find_and_modify(query={'_id': proxyip.get('_id')},
                          update={'$inc': {'ipInfo.count': -1, tempstr1: tscore, tempstr2: 1, tempstr3: susscore}},
                          new=True)

    if proxyip and proxyip.get('ipInfo') and proxyip.get('ipInfo').get('count') < 5 and proxyip.get('ipInfo').get(
            'count') > -5 and proxyip.get('ipInfo').get('status') == 4:
        tbobj.find_and_modify(query={'_id': proxyip.get('_id')}, update={'$set': {'ipInfo.status': 1}})
    if proxyip and proxyip.get('ipInfo') and (
            proxyip.get('ipInfo').get('count') < -5 or proxyip.get('ipInfo').get('count') > 5) and proxyip.get(
            'ipInfo').get('status') == 1:
        tbobj.find_and_modify(query={'_id': proxyip.get('_id')}, update={'$set': {'ipInfo.status': 4}})
    # 记录使用记录
    mydvInfo = retdict.get('deviceInfo')
    if mydvInfo:
        devdata = {'device':  # 使用情况#设备
                       {'id': mydvInfo.get('id', socket.getfqdn(socket.gethostname())),  # 设备名
                        'info': {  # 待定,辅助id确定使用机器的唯一性,若为已知机器可通过id确定唯一性,则此字段可为空
                            'type': mydvInfo.get('type', 'pc'),  # 设备类型(pc/moble)
                        }},
                   'time': time.localtime(time.time()),  # 使用记录时间
                   'interval': 5 * 60,  # 使用间隔
                   }
        tbobj.find_and_modify(query={'_id': proxyip.get('_id')}, update={'$push': {'ipInfo.use': devdata}})