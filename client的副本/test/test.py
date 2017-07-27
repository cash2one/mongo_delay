# _*_ coding: utf-8 _*_

import platform
print(platform.node())
climb_wall_proxies_dict = {
    'czMacBook-Pro.local':{
        'http':'http://127.0.0.1:49290', #8466
        'https':'https://127.0.0.1:49290',
    },
    'MaoMao': {
            'http':'http://127.0.0.1:8466', #8466
            'https':'https://127.0.0.1:8466',
        },
}
climb_wall_proxies = climb_wall_proxies_dict.get(
    platform.node(),
        {
            'http':'http://127.0.0.1:8466', #8466
            'https':'https://127.0.0.1:8466',
        }
    )
phproxylist = [
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '亚太地区  ',
     'baseurl': 'http://www.kn.com.my/modules/mod_syndicate/license.php', 'hl': '3ed#', 'url_encode': 'base64',
     'note': None, 'method': 'GET', 'ip': '103.50.164.54', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '美国  ',
     'baseurl': 'http://amra.ga/proxy/index.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None, 'method': 'GET',
     'ip': '107.158.239.58', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '罗马尼亚  ',
     'baseurl': 'http://www.didaxis.org/site/language/pdf_fonts/search.php', 'hl': '3ed#', 'url_encode': 'base64',
     'note': None, 'method': 'GET', 'ip': '109.199.99.74', 'wall': 0,'needtest':0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '荷兰  ',
     'baseurl': 'http://www.codehacker.nl/index.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None,
     'method': 'POST', 'ip': '109.70.1.44', 'wall': 1 ,'needtest':0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '新加坡  ',
     'baseurl': 'http://www.ipchicken.in/proxy/index.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None,
     'method': 'POST', 'ip': '111.221.46.163', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '香港 电讯盈科有限公司',
     'baseurl': 'https://www.hypernite.com/proxy/index.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None,
     'method': 'GET', 'ip': '116.49.155.70', 'wall': 0,'needtest':0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '新加坡 Digital Ocean股份有限公司数据中心',
     'baseurl': 'http://pdiperjuangan-diy.org/wp-includes/error.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None,
     'method': 'GET', 'ip': '128.199.88.81', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q',
     'address': '澳大利亚 Sugar Research Institute', 'baseurl': 'https://www.configinter.net/hide-proxy/index.php',
     'hl': '3ed#', 'url_encode': 'base64', 'note': None, 'method': 'GET', 'ip': '139.59.107.129', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '日本  ',
     'baseurl': 'http://jien.net/gim/index.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None, 'method': 'POST',
     'ip': '150.95.8.132', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '英国  ',
     'baseurl': 'http://www.pitchoo.net/zob_/index.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None,
     'method': 'GET', 'ip': '163.172.46.116', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '美国 密苏里州堪萨斯城virpus网络公司',
     'baseurl': 'http://www.proxy.gunhotnews.com/proxy/index.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None,
     'method': 'GET', 'ip': '173.0.51.131', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '美国 亚利桑那州斯科茨代尔市Go Daddy集团公司',
     'baseurl': 'http://greenpowerguy.com/blog/wp-content/themes/error.php', 'hl': '3ed#', 'url_encode': 'base64',
     'note': None, 'method': 'GET', 'ip': '173.201.196.58', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '美国 犹他州盐湖城Bluehost公司',
     'baseurl': 'http://dmburke.com/PHPProcksy/index.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None,
     'method': 'GET', 'ip': '173.254.28.144', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '美国 亚利桑那州斯科茨代尔市Go Daddy集团公司',
     'baseurl': 'http://fgks.org/proxy/index.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': '多IP,44,200,203,206', 'method': 'GET',
     'ip': '184.168.46.203', 'wall': 0,'needtest':1},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '欧洲和中东地区  ',
     'baseurl': 'https://gimmes.net/proxy/index.php', 'hl': '8#', 'url_encode': 'base64', 'note': None,
     'method': 'GET', 'ip': '185.114.157.172', 'wall': 0,'needtest':0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '立陶宛 ',
     'baseurl': 'http://charliefrancis.cf/proxy/index.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None,
     'method': 'GET', 'ip': '185.28.20.15', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '新加坡 Digital Ocean股份有限公司数据中心',
     'baseurl': 'https://frascar.uk/secret/index.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None,
     'method': 'GET', 'ip': '188.166.173.128', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '美国 ',
     'baseurl': 'https://www.fast-autolikers.com/proxy/index.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None,
     'method': 'GET', 'ip': '192.185.4.67', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '俄罗斯  ',
     'baseurl': 'http://hoponhopoff.ge/errors.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None, 'method': 'GET',
     'ip': '194.190.8.178', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '法国  ',
     'baseurl': 'http://f8ip.toile-libre.org/index.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': '不能用蓝灯',
     'method': 'POST', 'ip': '195.88.84.74', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '加拿大  ',
     'baseurl': 'https://yxorp.pandemonium.ovh/index.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None,
     'method': 'POST', 'ip': '198.245.60.86', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '加拿大  ',
     'baseurl': 'http://efintel.cl/wp-includes/error.php', 'hl': '2c0', 'url_encode': 'base64', 'note': None,
     'method': 'POST', 'ip': '198.50.180.210', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '法国 巴黎OV',
     'baseurl': 'http://www.decret-pinel.fr/wp-includes/error.php', 'hl': '3ed#', 'url_encode': 'base64',
     'note': '原始网页丢失结尾部分字符，可能造成解析错误', 'method': 'GET', 'ip': '213.251.182.111', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '匈牙利  ',
     'baseurl': 'http://totalfish.hu/errors.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None, 'method': 'GET',
     'ip': '217.20.130.216', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '法国  ',
     'baseurl': 'http://dev.chamoun.fr/proxy/index.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None,
     'method': 'GET', 'ip': '217.70.186.133', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '香港 电讯盈科有限公司',
     'baseurl': 'http://www.taiwangoodbuy.com/index.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None,
     'method': 'GET', 'ip': '223.197.160.25', 'wall': 0},
    {'strip_tail': '<!-- Yandex.Metrika counter -->', 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q',
     'address': '俄罗斯  ', 'baseurl': 'http://free.lynx.net.ru/index.php', 'hl': '3ed#', 'url_encode': 'base64',
     'note': None, 'method': 'GET', 'ip': '37.9.135.169', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '德国 OVH SAS',
     'baseurl': 'https://cajs.co.uk/proxy/index.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None,
     'method': 'GET', 'ip': '46.105.120.135', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '荷兰  ',
     'baseurl': 'http://www.flatertheek.nl/wp-includes/SimplePie/HTTP/search.php', 'hl': '3ed#', 'url_encode': 'base64',
     'note': None, 'method': 'POST', 'ip': '46.235.42.55', 'wall': 1},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '捷克  ',
     'baseurl': 'http://ubytovnaukasny.cz/errors.php', 'hl': '48', 'url_encode': 'base64', 'note': None,
     'method': 'GET', 'ip': '46.28.105.82', 'wall': 0,'needtest':0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '美国 亚利桑那州斯科茨代尔市Go Daddy集团公司',
     'baseurl': 'http://themansphere.com/wp-includes/error.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': '多IP,173,175',
     'method': 'POST', 'ip': '50.63.194.175', 'wall': 0,'needtest':1},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '美国 华盛顿州西雅图市亚马逊(Amazon)公司数据中心',
     'baseurl': 'https://symbiose-proxy.herokuapp.com/index.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None,
     'method': 'POST', 'ip': '54.170.27.88', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '北美地区  ',
     'baseurl': 'http://p.webbled.com/index.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None, 'method': 'GET',
     'ip': '66.175.239.1', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '德国  ',
     'baseurl': 'http://www.dynit.it/edit-link.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None, 'method': 'POST',
     'ip': '78.46.179.12', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '德国  ',
     'baseurl': 'http://www.weisfeltlintz.nl/wordpress_1/tmp/search.php', 'hl': '3ed#', 'url_encode': 'base64',
     'note': None, 'method': 'POST', 'ip': '78.47.90.57', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '英国  ',
     'baseurl': 'http://79.170.40.227/splashextend.co.uk/downloads/index.php', 'hl': '3ed#', 'url_encode': 'base64',
     'note': None, 'method': 'GET', 'ip': '79.170.40.227', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '英国  ',
     'baseurl': 'http://79.170.44.126/kingvisphostdemo.co.uk/downloads/vpn/index.php', 'hl': '3ed#',
     'url_encode': 'base64', 'note': None, 'method': 'POST', 'ip': '79.170.44.126', 'wall': 1},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '德国 柏林Strato公司',
     'baseurl': 'http://qartex.com/webproxy/index.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None,
     'method': 'POST', 'ip': '81.169.144.135', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '比利时  ',
     'baseurl': 'http://www.tkofschip.be/joomlasites/ankerintranet5/plugins/content/config.index.php', 'hl': '3ed#',
     'url_encode': 'base64', 'note': None, 'method': 'POST', 'ip': '81.82.233.220', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '法国 巴黎OVH SAS数据中心',
     'baseurl': 'http://p.kristof.123.fr/index.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None, 'method': 'POST',
     'ip': '91.121.167.136', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '保加利亚  ',
     'baseurl': 'http://xawos.ovh/index.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None, 'method': 'POST',
     'ip': '91.134.135.179', 'wall': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '美国 俄亥俄州哥伦布市IXwebhosting',
     'baseurl': 'http://toarabic.net/default.php', 'hl': '3ed#', 'url_encode': 'base64', 'note': None, 'method': 'GET',
     'ip': '98.130.2.33', 'wall': 0,'needtest':0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '美国 宾州费城PHL数据中心',
     'baseurl': 'http://www.proxyweb.online/index.php', 'hl': '3ed', 'url_encode': 'base64', 'note': None, 'method': 'GET',
     'ip': '162.243.50.61', 'wall': 0, 'needtest':0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '北京联通',
     'baseurl': 'http://fantaluciano.altervista.org/poste/index.php', 'hl': '3ed', 'url_encode': 'base64', 'note': None,
     'method': 'POST',
     'ip': '114.241.70.59', 'wall': 1, 'needtest': 0,'block':1},#无法访问，浏览器可以访问
     {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '捷克  ',
     'baseurl': 'http://proxy.polach.info/index.php', 'hl': '48', 'url_encode': 'base64',
     'note': None,
     'method': 'POST',
     'ip': '', 'wall': 1, 'needtest': 0,'block':1},  #无法访问
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '罗马尼亚  ',
     'baseurl': 'http://www.semneartemis.ro/errors.php', 'hl': '40', 'url_encode': None,
     'note': '使用base编码url会出错',
     'method': 'GET',
     'ip': '176.223.125.70', 'wall': 0,'needtest': 0, 'block': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '美国  ',
     'baseurl': 'https://4alltools.com/en/webproxy/index.php', 'hl': '0', 'url_encode': None,
     'note': '使用base编码url会出错',
     'method': 'GET',
     'ip': '192.254.156.235', 'wall': 0, 'needtest': 0, 'block': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '美国  ',
     'baseurl': 'https://pan.one/proxy/index.php', 'hl': '7cd', 'url_encode': None,
     'note': '不能使用base编码url会出错',
     'method': 'GET',
     'ip': '107.182.176.206', 'wall': 0,'needtest': 0, 'block': 0},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '德国  ',
     'baseurl': 'https://www.sslgate.co.uk/index.php', 'hl': '3ed', 'url_encode': 'base64',
     'note': '',
     'method': 'GET',
     'ip': '212.227.127.19', 'wall': 1, 'needtest': 0, 'block': 0,'ssl':False},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '丹麦  ',
     'baseurl': 'http://aalogic.se/error.php', 'hl': '3ed', 'url_encode': 'base64',
     'note': '',
     'method': 'GET',
     'ip': '212.97.134.13', 'wall': 0, 'needtest': 0, 'block': 0,},
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '德国  ',
     'baseurl': 'http://bypass.osiland.com/index.php', 'hl': '3ed', 'url_encode': 'base64',
     'note': '',
     'method': 'GET',
     'ip': '212.227.24.37', 'wall': 1, 'needtest': 0, 'block': 0, },
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '美国 华盛顿州西雅图市亚马逊(Amazon)公司数据中心',
     'baseurl': 'http://filterevade.com/index.php', 'hl': '3ed', 'url_encode': 'base64',
     'note': '',
     'method': 'GET',
     'ip': '54.208.158.42', 'wall': 1, 'needtest': 0, 'block': 0, },
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '美国  ',
     'baseurl': 'http://jelajah.internetmerdeka.org/index.php', 'hl': '3ed', 'url_encode': 'base64',
     'note': '',
     'method': 'GET',
     'ip': '104.37.169.89', 'wall': 1, 'needtest': 0, 'block': 0, },
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '日本  ',
     'baseurl': 'http://kochiya.rosx.net/kushi/index.php', 'hl': '3ed', 'url_encode': 'base64',
     'note': '',
     'method': 'GET',
     'ip': '27.96.40.195', 'wall': 1, 'needtest': 0, 'block': 0, },
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '法国 巴黎OVH系统公司',
     'baseurl': 'http://prox.emobilis.com/index.php', 'hl': '3ed#', 'url_encode': 'base64',
     'note': '',
     'method': 'POST',
     'ip': '213.251.182.103', 'wall': 1, 'needtest': 0, 'block': 0, },
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '加拿大 魁北克省蒙特利尔市OVH数据中心',
     'baseurl': 'http://proxy.fotserv.pl/index.php', 'hl': '3ed#', 'url_encode': 'base64',
     'note': '',
     'method': 'POST',
     'ip': '142.4.211.204', 'wall': 1, 'needtest': 1, 'block': 0, },
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '美国 犹他州盐湖城Bluehost公司',
     'baseurl': 'http://proxy.ske.ind.in/index.php', 'hl': '3ed', 'url_encode': 'base64',
     'note': '',
     'method': 'GET',
     'ip': '73.254.28.103', 'wall': 1, 'needtest': 1, 'block': 0, },
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '捷克  ',
     'baseurl': 'http://prx.afkcz.eu/prx/index.php', 'hl': '3ed', 'url_encode': 'base64',
     'note': '',
     'method': 'POST',
     'ip': '46.28.105.7', 'wall': 1, 'needtest': 1, 'block': 0, },
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '美国 纽约市DigitalOcean云公司',
     'baseurl': 'http://surfean2.kreotuweb.com/index.php', 'hl': '3ed', 'url_encode': 'base64',
     'note': '',
     'method': 'GET',
     'ip': '104.236.101.154', 'wall': 1, 'needtest': 1, 'block': 0, },
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '美国 宾夕法尼亚州切斯特县切斯特布鲁克1&1互联网公司',
     'baseurl': 'http://truthsilo.com/pox/index.php', 'hl': '3ed', 'url_encode': 'base64',
     'note': '',
     'method': 'POST',
     'ip': '74.208.180.26', 'wall': 1, 'needtest': 1, 'block': 0, },
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '美国 得克萨斯州普莱诺市Layered科技公司',
     'baseurl': 'http://vrecon.com/index.php', 'hl': '3ed', 'url_encode': 'base64',
     'note': '',
     'method': 'POST',
     'ip': '74.200.236.197', 'wall': 1, 'needtest': 1, 'block': 0, },
    {'strip_tail': None, 'strip_head': 'ocument.write("', 'p_type': 'phproxy_0', 'q': 'q', 'address': '法国 巴黎OVH',
     'baseurl': 'http://www.imzi-tours-travel.com/annuaire/index.php', 'hl': '3ed', 'url_encode': 'base64',
     'note': '尾部不完整',
     'method': 'POST',
     'ip': '13.251.182.110', 'wall': 1, 'needtest': 1, 'block': 0, },
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '新加坡 Go Daddy 有限公司新加坡数据中心',
     'baseurl': 'http://www.duckproxy.com', 'hl': '3ed', 'url_encode': 'base64',
     'note': '',
     'method': 'GET',
     'ip': '182.50.135.77', 'wall': 1, 'needtest': 1, 'block': 0, },
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '法国 巴黎OVH',
     'baseurl': 'http://www.thely.fr/proxy/index.php', 'hl': '3ed', 'url_encode': 'base64',
     'note': '',
     'method': 'POST',
     'ip': '213.251.182.110', 'wall': 1, 'needtest': 1, 'block': 0, },
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '美国  ',
     'baseurl': 'http://www.ultrabestproxy.com/index.php', 'hl': '3ed', 'url_encode': 'base64',
     'note': '',
     'method': 'GET',
     'ip': '209.126.107.97', 'wall': 1, 'needtest': 1, 'block': 0, },
     {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '美国 宾夕法尼亚州切斯特县切斯特布鲁克1&1互联网公司',
     'baseurl': 'http://www.worryfreecomputers.com/tube/index.php', 'hl': '3ed', 'url_encode': 'base64',
     'note': '',
     'method': 'GET',
     'ip': '74.208.16.73', 'wall': 1, 'needtest': 1, 'block': 0, },
    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '美国 犹他州盐湖城Bluehost公司',
     'baseurl': 'http://www.dmburke.com/PHPProcksy/index.php', 'hl': '3ed', 'url_encode': 'base64',
     'note': '',
     'method': 'GET',
     'ip': '173.254.28.144', 'wall': 0, 'needtest': 1, 'block': 0, },
]

'''
http://103.1.172.112/archieves/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=e9#   182.50.142.233
http://62.109.25.136/index.php?q=uggc%3A%2F%2Fvc.puvanm.pbz%2Ftrgvc.nfck&hl=2fd   62.109.25.136  尾部广告
http://71.18.69.108/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#     翻墙 50.6.77.49
http://89.163.130.223/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=2ed# 89.163.130.222
http://anonymizer.in/anonymizer/  网页似乎是错的
http://arne-post.de/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  91.136.8.9
http://basit.work/index.php     翻墙  184.168.46.89
http://bbsq.us/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3eb#  149.56.203.152
http://codehacker.nl/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#   109.70.1.44
http://endo.gr/endomembers/proxy/nc/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  95.154.242.224  有人机验证，需破解
http://fitnessdepotprices.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed# 67.213.82.137
http://fuckgema.net/index.php?q=uggc%3A%2F%2Fvc.puvanm.pbz%2Ftrgvc.nfck&hl=2fd   198.71.226.39
http://fzsky.sitemix.jp/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed   内部错误
http://gxu.free.fr/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed  连接错误
http://hamedweb.persiangig.com/Anonpass.com%20-%20Free%20Anonymous%20Proxy%20Site.htm  嵌入一个链接，Anonpass.com 可用  url form
http://herosurf.net/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  91.205.174.23
http://hideip.pro.composesite.com/     有类似站点信息
http://hidemyfree.com/index.php  不跳转
http://homeschool.noip.me/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  65.175.144.121
http://ilike.ga/index.php  500错
http://iphider.org/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=36c#  192.99.4.37  域名 74.117.182.141
http://itwtf.com/index.php?q=y6qm1GtmZqLTYZWezNSTrmSaos5lyZ7XzKljlKihrw  45.33.6.150  特殊引擎，非PHProxy   This php-proxy service remains free to use. Subject to local laws.
http://khs54915.tripod.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  index.php 丢失？
http://leather-bg.com/index.php  打不开
http://matusik.net/bramka/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  176.97.143.154
http://mob.beproxy.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  184.168.27.152
http://mysyrian.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#   193.202.110.20
http://navegasinley.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ef#  178.33.112.8
http://nicetrick.info/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  149.210.154.141
http://odblokuj.115zse.frih.net/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=2ed#   144.76.111.228
http://offeng.com/ch00/Proksy/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#   勉强可以抢救   http://ip.chinaz.com/getip.aspx{ip:'74.220.207.198',address:'缇庡浗 鐘逛粬宸炵洂婀栧煄Bluehost鍏徃'}
http://panyuxin.com/proxy/index.php?q=http%3A%2F%2Fip.chinaz.com%2Fgetip.aspx&hl=481#  107.182.176.206
http://phproxy.nfriedly.com/index.php?q=http%3A%2F%2Fip.chinaz.com%2Fgetip.aspx&hl=2e1#  54.161.254.69
http://pinkpanda.comuv.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed# 153.92.0.7
http://plany.fasthosting.it/test/index.php   不能跳转
http://portal.free4viet.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=2ed#  103.9.158.194
http://pr0xi3s.ga/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed  178.32.102.34  有尾部广告
http://proxy.eglovers.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#   404
http://proxy.filipe.ch/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  88.198.41.182
http://proxy.gunhotnews.com/proxy/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=2ed 173.0.51.131
http://proxy.scorpimen.eu/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  188.116.9.91
http://proxy.twista.cz/subdom/proxy/index.php   可访问京东评论  46.28.105.24捷克
http://proxymesilly.net/
http://proxy-vault.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=7b#  198.255.10.170
http://raveandlaser.online/   402
http://rhythmusic.net/De1337/nothing/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#
http://showvision.info/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=2ed#   184.168.27.152
http://soke.za.org/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed# 104.128.238.184
http://sure.i-t.me/blow.php/zVOlWSdJ/oet_2Bcc/0_2BNhgu/jHYllBjA/0g8YkREK/b1/fnorefer  188.116.19.33
http://surfanon.net/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed# 64.85.160.49
http://theproxyfree.com    网页似乎是错的
http://trubadix.myds.me/ppp/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=2ed#   90.146.201.130
http://unafraid.epbsoft.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3cf   188.116.19.33
http://unblocked.in/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  95.154.222.196
http://unblockme.comuf.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  153.92.0.3
http://vincentgodefroy.free.fr/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed  连接错误
http://webproxy.com            glype 站点  有人机验证  {ip:'69.46.0.196',address:'美国 佛罗里达州坦帕市Hivelocity Ventures公司'}
http://worka.work/index.php?q=http%3A%2F%2Fip.chinaz.com%2Fgetip.aspx&hl=481#  184.168.27.152   抢救回来的
http://ww.297m.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  185.27.134.46
http://www.1proxy.de/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=2ed# 89.163.148.111
http://www.2proxy.de/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=2ed#  89.163.130.154
http://www.3proxy.de/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=2ed#  89.163.130.161
http://www.4proxy.de/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=2ed#  89.163.130.187
http://www.7soft.net/xx/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  138.201.197.73
http://www.blue-nil.net/pro/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#   37.187.28.130
http://www.boffjenkins.co.uk/poxy.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=1ed  90.206.218.216  页面广告多，前后都有垃圾
http://www.cliker.com/proxy/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  62.149.141.127
http://www.djezzy.ml/index.php?a=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  54.242.114.76
http://www.ekzi.com/p/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=2ed  只能从土耳其访问？
http://www.fevza.com/proxy/unblock-sites.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=2ed  94.176.239.74
http://www.giantmania.de/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=2ed#  178.254.57.13
http://www.hell-man.de/proxy/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=1fd#  82.100.220.35
http://www.infosid.com/proxy/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed# 31.220.20.28
http://www.jkworkshop.com/px12345/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  103.255.250.132
http://www.justproxy.co.uk/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=2ed#  178.79.138.160
http://www.li-cai.com.tw/webjump/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed  124.150.132.27
http://www.new-proxy.com.de/index.php   翻墙  89.163.130.236 德国
http://www.ohmymind.com/myp/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed  403
http://www.openvpnvps.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  91.216.107.189
http://www.openwebdesign.org/design/3886/phproxy/   网页似乎是错的
http://www.profitgyan.com/proxy/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#   50.28.34.116
http://www.profitgyan.com/proxy/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  50.28.34.116
http://www.proproxy.me/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  37.187.65.43
http://www.proxy4me.com/phpproxy/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D   188.116.19.33  貌似最干净
http://www.proxyaka.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed# 188.227.186.64
http://www.proxyboost.net/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=2ed#   149.210.148.6  域名 46.82.174.68
http://www.proxyghost.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#   412
http://www.proxygratuits.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#    翻墙 66.175.239.37
http://www.testesuainternet.com.br/tsi/proxy/index.php   可访问京东评论，速度貌似挺快，但不能访问查地址的页
http://www.theprofissional.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#   193.202.110.22
http://www.vigoob.com/index.php  似乎是跳转错误
http://www.vrecon.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=a#  74.200.236.197
http://www.webproxy-germany.de/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=2ed#  89.163.130.235
http://www.www2.dek-sara.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  150.107.31.52
http://www.wxfq.tk/index.php?q=moBrrgvF7Y7Dqbv4MV4K1E2r8bneRD79IfmV0ehddUjorZen&hl=5ef  54.172.21.101  编码奇特
https://carbonsecure.org/opennic-proxy/   连接错误
https://descris.ro/shell/pass/script-loader.php?q=http%3A%2F%2Fip.chinaz.com%2Fgetip.aspx&hl=2c0#   89.46.7.240  域名  176.223.124.23
https://hidefrom.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  89.221.210.144  91.205.174.23
https://phproxy.herokuapp.com/index.php?q=http%3A%2F%2Fip.chinaz.com%2Fgetip.aspx&hl=2e1#  54.161.254.69
https://px.multiscreensite.com/index.php?url=http%3A%2F%2Fip.chinaz.com%2Fgetip.aspx&hl=0#  54.175.166.83
https://quickbypass.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed  返回空白
https://wecanunblock.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  89.221.210.144
https://www.4alltools.com/en/webproxy/index.php?q=http%3A%2F%2Fip.chinaz.com%2Fgetip.aspx&hl=2e5#  192.254.156.235
https://www.best-proxy.com.de/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=2ed#  89.163.130.193  ssl
https://www.cajs.co.uk/proxy/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  46.105.120.135
https://www.fastfreewebproxy.tk/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#  204.44.85.116  要求屏蔽ADBlock
https://www.german-webproxy.de/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=2ed#  89.163.130.227  ssl 有错
https://www.iphider.org/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=36c#  192.99.4.37
https://www.justproxy.co.uk/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=2ed#    178.79.138.160
https://www.panyuxin.com/proxy/   跳转到 https://pan.one/proxy/index.php
https://www.surf100.com/   网页似乎是错的


http://soke.za.org/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#   104.128.238.184
https://proxy.wehaa-server4.com/index.php?q=aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed
'''
import requests
from proxypool.utils import get_headers
import json,base64,urllib.parse
import time,base64
from pyquery import PyQuery as pq


import socket

def getIp(domain):
    def __getIp(domain):
        try:
            return  socket.getaddrinfo(domain,'http')[0][4][0]
        except Exception as e:
            return '0'
    ip =  __getIp(domain)
    count = 0
    while ip == '0':
        if __getIp('www.baidu.com') == '0':
            time.sleep(1)
            count += 1
        else:
            ip =  __getIp(domain)
            break

        if count > 180:
            ip = '0'
            break


    return ip



def gethost(url):
    return  urllib.parse.urlparse(url).netloc
def getscheme(url):
    return  urllib.parse.urlparse(url).scheme
def getpath(url):
    return  urllib.parse.urlparse(url).path

def getbaseurl(url):
    return getscheme(url) +'://' + gethost(url) + getpath(url)

def getmethod(pq_form):

    method = pq_form.attr.method
    action = pq_form.attr.action
    inputs = pq_form('input')

    payload = {}
    postreq = {}

    for input in inputs.items():
        name = input.attr.name
        p_type = input.attr.type
        if p_type == 'text':
            payload[name] = '__inputbox__'
            postreq['input'] = name
            #ToDo 如果有多个输入框，这里会有问题
        elif p_type == 'checkbox':
            payload[name] = 'on' if input.attr.checked == 'checked' else ''
        elif p_type == 'hidden':
            payload[name] = input.attr.value
        elif p_type == 'submit' and name != None:
            if postreq.get('submit',None) == None:
                postreq['submit'] = {}
            postreq['submit'][name] = input.attr.value
            #payload[name] = input.attr.value   #多按钮情况下有用

    #print(payload,action,method)

    postreq['payload'] = payload
    postreq['action'] = action
    postreq['method'] = method

    #print(postreq)
    return postreq

def getformstr(text):
    forms = ''
    while True:
        pos = text.find('<form')

        if pos == -1:
            break
        posend = text[pos:].find('</form>')+len('</form>')
        if posend == -1:
            break
        #print(pos,posend)
        forms += text[pos:posend]
        #print(forms)
        text = text[posend:]
        #print(text)
    #print('aaaa',forms)
    return forms

def updateproxy(proxy,encode,mode = 'GET',headers = None,reqdata={},ssl=1,well=0,title='',hl='3ed#'):

    proxies = climb_wall_proxies if well == 1 else 0
    headers = headers or  {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        #'Host':'www.ip-adress.com',
        #'Cookie':'flags=3ed',
        #'origin':url,
        'Referer':getbaseurl(proxy.get('baseurl')),
        #':authority':url.replace('http://','').replace('https://',''),
        #':method':'POST',
        #':path':'/index.php',
        #':scheme':'https'
    }
    wellstr = '翻墙' if well == 1 else ''
    sslstr = '忽略SSL校验错误' if ssl == 0 else ''

    checkip = 'http://ip.chinaz.com/getip.aspx'
    #checkip = 'https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv3306&productId=4250886&score=0&sortType=6&page=2&pageSize=10&isShadowSku=0&fold=1'
    baseurl = proxy.get('baseurl')

    #rint(baseurl,reqdata)

    t = time.time()
    conn = requests.session()
    try:
        if mode == 'FORM':  #使用网页的对话框参数
            action = reqdata.get('action', getpath(baseurl))
            if action == None:
                action = getpath(baseurl)
                reqdata['action'] = action
            q = reqdata.get('input', 'q')
            posturl = gethost(baseurl) + '/' + action
            posturl = getscheme(baseurl) + '://' + posturl.replace(r'//', r'/')

            print(posturl)

            payload = reqdata.get('payload')
            payload[q] = checkip

            req = conn.post(url = posturl ,proxies=proxies,data=payload,headers=headers,verify=getSSL(ssl),timeout=20)
        else:  #'GET
            # ToDo Get方式下需编码payload里面的参数
            if encode == 1:
                url = urllib.parse.quote_from_bytes(base64.b64encode(checkip.encode('utf8')))
            else:
                url = urllib.parse.quote_from_bytes(checkip.encode('utf8'))
            #使用Get方式时，不同的站点差别较大，需要用不同的脚本解决，这里暂时只支持PHProxy
            geturl = r'{}?{}={}&hl={}'.format(baseurl, 'q', url, hl)
            req = requests.get(url = geturl,proxies=proxies,headers=headers,verify=getSSL(ssl),timeout=10)

        if req.status_code != 200:
            print(req.status_code)
        text = req.text
        print(req.url)
        #print(text)
        #sslagree
        if 'sslagree' in text:
            '''
                        <html>
            <head>
                <title>Security Warning</title>
                <style type="text/css">
            html, body {
                background: #0b1933;
                text-align: center;
            }
            body {
                font: 80% Tahoma;
            }
            #wrapper {
                margin: 100px auto;
                width: 500px;
                text-align: left;
                background: #fff;
                padding: 10px;
               border: 5px solid #ccc;
            }
            form {
               text-align: center;
            }
                </style>
               <base href="http://gameproxy.org/">
            </head>
            <body>
                <div id="wrapper">
                    <h1>Warning!</h1>
                    <p>The site you are attempting to browse is on a secure connection. This proxy is not on a secure connection.</p>
                  <p>The target site may send sensitive data, which may be intercepted when the proxy sends it back to you.</p>
                  <form action="includes/process.php" method="get">
                     <input type="hidden" name="action" value="sslagree">
                        <input type="submit" value="Continue anyway...">
                     <input type="button" value="Return to index" onclick="window.location='.';">
                    </form>
                  <p><b>Note:</b> this warning will not appear again.</p>
                </div>
            </body>
            </html>
            '''
            print('-----------',text)
            print('sslagree')

            #req = conn.get(baseurl + 'includes/process.php',proxies=proxies,params=ppp,headers=headers,verify=getSSL(ssl))
            req = conn.get(url = posturl,proxies=proxies,params={'action:sslagree'},headers=headers,verify=getSSL(ssl),timeout=20)

            text = req.text
            #print(text)
    except Exception as e:
        print(e)
        return 0

    if "{ip:'" in text:
        def getstr(text,start,end):
            pos = int(text.find(start) + len(start))
            posend = int(text[pos:].find(end))+pos
            return text[pos:posend]


        print(title, req.url,wellstr,sslstr)
        et = time.time() - t
        print('        ',et, mode, len(text), text[:100].replace('\n', '').replace('\r', ''))
        ip = getstr(text,"{ip:'","',address:'" )
        address = getstr(text,"',address:'","'}")
        #print('        ',ip,address)
        '''
            {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '德国  ',
             'baseurl': 'http://www.weisfeltlintz.nl/wordpress_1/tmp/search.php', 'hl': '3ed#',
              'url_encode': 'base64',
             'note': None, 'method': 'POST', 'ip': '78.47.90.57', 'wall': 0},
        '''
        if len(address) < 2 :address = '网页可能有错误'
        if len(ip) > 7 and len(address) > 2:
            ipset = proxy.get('mutil_ip',None)
            if ipset == None:
                proxy['mutil_ip'] = {}
                ipset = proxy.get('mutil_ip', None)
            ipset[ip] = address

            #print(ip, '---', address)
            strip_head = ''
            head_s = 0
            head_e = text.find("{ip:'" + ip)
            if head_e - head_s > 20:
                strip_head = text[head_e - 20:head_e]

            tail_s = text.rfind(ip + "',address:'" + address + "'}") + len(ip + "',address:'" + address + "'}")
            tail_e = len(text)
            #print('s=', tail_s, 'e=', tail_e)
            if tail_e - tail_s > 10:
                pos = tail_s + 10
                while pos < (((tail_e - 1) - tail_s) / 2 + tail_s + 1):
                    p = text[tail_s + 5:].find(text[tail_s:pos])
                    #print('aaaa', p)
                    if text[tail_s + 5:].find(text[tail_s:pos]) == -1:
                        break
                    pos += 1
                tail_e = pos

            strip_tail = text[tail_s:tail_e]
            proxy['strip_head'] = strip_head
            proxy['strip_tail'] = strip_tail
        else:
            return 0

        #print('aaaaaa',proxy.get('delay', 10000))
        if et < proxy.get('delay',10000):
            print('        更新proxy',proxy['p_type'])

            proxy['delay'] = et
            proxy['method'] = mode
            if mode == 'GET':
                proxy['req']['GET'] = {}
                proxy['req']['GET']['url_encode'] = 'base64' if encode == 1 else None
                proxy['req']['GET']['hl'] = hl
                proxy['p_type'] = 'phproxy_0'
            else:
                proxy['req']['FORM'] = reqdata
                payload = reqdata.get('payload', {})

                #print(text)
                if "ginf={url:" in text:
                    proxy['p_type'] = 'Glype'

                if 'ctl00$plhMainBar$txtUrl' == proxy['req']['FORM']['input'] :
                    proxy['p_type'] = 'ASPProxy'

                if proxy['p_type'] == 'unknow':
                    phproxykeys =  """
                    hl[strip_title]  hl[session_cookies] hl[show_images]
                    hl[base64_encode] hl[accept_cookies] hl[show_referer]
                    hl[strip_meta] hl[remove_scripts]  hl[rotate13] hl[include_form]
                    """
                    for key in payload.keys():
                        if payload[key] in phproxykeys:
                            proxy['p_type'] = 'phproxy_0'
                            break

                if proxy['p_type'] == 'unknow':
                    if reqdata['input'] == 'url':
                        proxy['p_type'] = 'php-proxy'

                if proxy['p_type'] == 'unknow':
                    proxy['p_type'] = 'ohter'


            proxy['updatetime'] = time.time()

        return 1
    return 0

def parse_ip_address(result):
    s1 = None  # 去掉前面的
    s2 = None  # 去掉后面的
    if '<!-- Yandex.Metrika counter -->' in ip:
        s2 = '<!-- Yandex.Metrika counter -->'

    if s1 != None:
        ip = ip.split(s1)[1]

    if s2 != None:
        ip = ip[:ip.rfind(s2)]
    # print(ip)
    ip = ip.replace('ip:\'', '"ip":"').replace("',address:'", '","address":"').replace('\'', '"')
    note = None
    if '"}' not in ip:
        ip = ip + '"}'
        note = '原始网页丢失结尾部分字符，可能造成解析错误'
    # print(ip)



def getSSL(ssl):
    return True if ssl == 1 else False

def getform(url,ssl=1):

    url = url.strip()
    print(url)
    req,ssl,well = sniffhost(url)

    if isinstance(req,int):
        return 0

    res = {}
    res['baseurl'] = getbaseurl(url)
    res['p_type'] = 'unknow'
    res['strip_head'] = None
    res['strip_tail'] = None
    res['note'] = []
    res['method'] = 'form'
    res['req'] = {'FORM':{},'GET':{}}
    #res['q'] = 'q'
    if ssl == 0: #正常参数为True，校验ssl，有些网站证书错误，必须关闭这个参数。也可考虑全都关闭
        res['req']['ssl'] = getSSL(ssl) # False
    res['req']['wall'] = well  # 是否需要翻墙，为1需要
    if well == 1:print('需要防火墙')
    content = req.content[10:]
    #print(content)
    if b'<form ' in content and  b'form>' in content:
        doc = pq(content[content.find(b'<form'):])
        forms = doc('form')
    elif b'<FORM ' in content and  b'FORM>' in content:
        # print('aaa')
        doc = pq(content[content.find(b'<FORM'):])
        forms = doc('form')
    else:
        return 0

    #print('aaaa',forms)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        #'Host':'www.ip-adress.com',
        #'Cookie':'flags=3ed',
        'origin':url,
        'Referer':url,
        #':authority':url.replace('http://','').replace('https://',''),
        #':method':'POST',
        #':path':'/index.php',
        #':scheme':'https'
    }

    for form in forms.items():
        formreq = getmethod(form)
        #print(formreq)

        if formreq.get('method',None ) == None:
            continue

        headers['Referer'] = res.get('baseurl')
        ok = 0
        method = formreq.get('method','post').lower()

        submits = formreq.get('submit',{})
        if submits != {}:  #多按钮
            print('发现多按钮---------------')
            for key in submits.keys():
                formreq['payload'][key] = submits[key]
                ok += updateproxy(proxy=res, mode='FORM', title='1. default link'
                              , ssl=ssl, well=well, reqdata=formreq, encode=0, hl='3ed#')
                if ok > 0:
                    break
                else:
                    formreq['payload'].pop(key)

        else:
            ok += updateproxy(proxy=res,mode='FORM',title='1. default link'
                              ,ssl=ssl,well=well,reqdata=formreq,encode=0,hl='3ed#')

        if res['p_type'] == 'Glype':
            print(res)
            return res


    ok += updateproxy(proxy=res,title='2. get no base64'
                      ,ssl=ssl,well=well,reqdata=formreq,encode=0,hl='2c0#')
    ok += updateproxy(proxy=res,title='3. get base64'
                      ,ssl=ssl,well=well,reqdata=formreq,encode=1,hl='3ed#')

    if ok > 0:
        print(res)
        return res




def sniffhost(url , headers=None , ssl=None , well=None,count=5):

    def getSSL(ssl):
        return True if ssl == 1 else False

    headers = headers or {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        #'Host':'www.ip-adress.com',
        #'origin':url,
        #'Referer':url
    }

    well = 1
    ssl = 0
    ssl = 1 if ssl == None else ssl
    well = 0 if well == None else well

    req = 0
    try:
        req = requests.get(url,headers=headers , proxies = climb_wall_proxies if well == 1 else {} , verify=getSSL(ssl),timeout=10)

        if req.status_code != 200:
            print('访问错误',req.status_code)
        #print(req.text,ssl,well)
        return req,ssl,well
    except Exception as e:
        if count <=0 :
            return req,ssl,well
        print(e)
        if 'certificate verify failed' in str(e):
            ssl = 0
        if 'No route to host' in str(e) or 'Failed to establish a new connection' in str(e) or 'ConnectionResetError' in str(e):
            well = 1
        return sniffhost(url,headers=headers,ssl=ssl,well=well,count=count-1)




class PHProxy(object):
    def __init__(self):
        pass

    @staticmethod
    def makeproxy(url):
        '''
        从一个url中自动生成一个PHProxy代理对象
        使用getform自动尝试各种可能性，需要正确配置蓝灯，windows下翻墙探测可能不准确
        :param url:
        :return: 代理对象
        '''

    @staticmethod
    def findproxyjson(self,proxy):
        plink = proxy.split('?')[0]
        for p in phproxylist:
            if p['baseurl'] == plink:
                return p
        #new  自动测试
        print('new proxy ',proxy)
        return None

    @staticmethod
    def strip(text,phproxy):
        s1 = phproxy.get('strip_head',None)
        s2 = phproxy.get('strip_tail',None)
        if s1 != None:
            text = text.split(s1)[1]

        if s2 != None:
            text = text[:text.rfind(s2)]

        return text

    @staticmethod
    def _fetch_get(url,phproxy,headers,proxies):
        baseurl = phproxy.get('baseurl')
        q = phproxy.get('q', 'q')
        hl = phproxy.get('hl', '3ed#')
        url_encode = phproxy.get('url_encode', 'base64')

        if url_encode == 'base64':
            url = urllib.parse.quote_from_bytes(base64.b64encode(url.encode('utf8')))
        requrl = r'{}?{}={}&hl={}'.format(baseurl, q, url, hl)
        # print(requrl)
        # requrl = baseurl + '?q=' + 'aHR0cDovL2lwLmNoaW5hei5jb20vZ2V0aXAuYXNweA%3D%3D&hl=3ed#'
        print(requrl)
        sslverify = phproxy.get('ssl',True)
        if proxies != None:
            r = requests.get(requrl, headers=headers, proxies=proxies,verify=sslverify,timeout=10)
        else:
            r = requests.get(requrl, headers=headers,verify=sslverify,timeout=10)
        text = PHProxy.strip(r.text, phproxy)

        return r.status_code, text

    @staticmethod
    def _fetch_post(url,phproxy,headers,proxies):
        baseurl = phproxy.get('baseurl')
        q = phproxy.get('q', 'q')

        payload = {
            q:url,
            'hl[include_form]':'off',
            'hl[remove_scripts]':'off',
            'hl[accept_cookies]':'off',
            'hl[show_images]':'off',
            'hl[show_referer]':'off',
            'hl[rotate13]':'off',
            'hl[base64_encode]':'on',
            'hl[strip_meta]':'off',
            'hl[strip_title]':'off',
            'hl[session_cookies]':'off',
        }
        sslverify = phproxy.get('ssl',True)
        if proxies != None:
            r = requests.post(baseurl, data = payload,headers=headers, proxies=proxies,verify=sslverify,timeout=10)
        else:
            r = requests.post(baseurl, data = payload, headers=headers,verify=sslverify,timeout=10)
        text = PHProxy.strip(r.text, phproxy)

        return r.status_code, text

    @staticmethod
    def fetch(url,phproxy,headers=get_headers(),proxies = None,method=None):
        if isinstance(phproxy,str):
            if '{' in phproxy and '}' in phproxy:  #json
                try:
                    phproxy = json.loads(phproxy)
                except Exception as e:
                    print(e)
                    raise ValueError(e)
            else:  # 查找json
                phproxy = PHProxy.findproxyjson(phproxy)

        baseurl = phproxy.get('baseurl','http://123.456')
        headers['Referer'] = baseurl
        headers['Host'] = gethost(baseurl)
        headers['Origin'] = getscheme(baseurl) + '://' + headers['Host']

        #if 'www.sslgate.co.uk' in phproxy.get('baseurl'):
        #    headers['Host'] = 'letangel.com'

        if proxies == None and phproxy.get('wall') == 1:
            proxies = climb_wall_proxies

        if method == None:
            method = phproxy.get('method','GET')
        try:
            if method == 'GET':
                return PHProxy._fetch_get(url,phproxy,headers,proxies)
            elif method == 'POST':
                return PHProxy._fetch_post(url,phproxy,headers,proxies)
            else:
                raise ValueError('错误模式')
        except Exception as e:
            print(e)
            return 0,'无内容'

    @staticmethod
    def testproxylist(plist=phproxylist,needtest=1):
        ipset = set()
        print('列表长度={}'.format(len(plist)))

        def getstr(s, begin, end):
            pos = s.find('being') + len(begin)
            posend = s[pos:].find(end)
            return s[pos:posend]

        for p in plist:
            if p.get('needtest', 0) == needtest:
                code = 0
                content = '无内容'
                if p.get('needtest', 0) != 3:
                    try:
                        chekip = 'http://ip.chinaz.com/getip.aspx'
                        t = time.time()
                        code, content = PHProxy.fetch(chekip, p, method='GET')
                        t1 = time.time()
                        code2, content2 = PHProxy.fetch(chekip, p, method='POST')
                        t2 = time.time()
                    except Exception as e:
                        print(e)
                    finally:
                        print(p)
                        if isinstance(content, bytes):
                            print(t1 - t, code, content.decode('utf8'))
                        else:
                            print(t1 - t, code, content)
                        if isinstance(content2, bytes):
                            print(t2 - t1, code2, content2.decode('utf8'))
                        else:
                            print(t2 - t1, code2, content2)

                        ip1 = getstr(content, "{ip:'", "'address")
                        ip2 = getstr(content2, "{ip:'", "'address")
                        ip3 = p.get('ip')

                        if ip1 in ipset or ip2 in ipset or ip3 in ipset:
                            print('ip重复', p)
                        if len(ip1) > 7:
                            ipset.add(ip1)
                        if len(ip1) > 7:
                            ipset.add(ip2)
                        if len(ip1) > 7:
                            ipset.add(ip3)


def test():
    global t_count
    while True:
        lock_read.acquire()
        t_count += 1
        print('读文件', t_count)
        line = inFile.readline().strip()
        lock_read.release()
        if len(line) == 0: break

        url = line.split(' ')[0].strip()
        host = gethost(line)

        if url[0] != 'h':
            continue

        baseurl = ''
        if len(url) > 5:
            baseurl = getbaseurl(url)
        if len(baseurl) < 5:
            continue
        try:
            ip = getIp(host)
            print('-----------------------------------------------------------------')
            print(line, ip)
            proxy = getform(baseurl)
            if proxy.get('p_type', 'unknow') != 'unknow':
                s = proxy.get('baseurl') + '    |' + str(proxy.get('mutil_ip')) + '     |' + str(proxy) + '\n'
                lock_write.acquire()
                print(s)
                with open('phproxy-list-2017-7-13.txt', 'a', encoding='utf8') as outFile:
                    outFile.write(s)
                lock_write.release()

        except Exception as e:
            print('error', baseurl)
            print(e)
            continue

if __name__ == "__main__":

    import threading

    inFile = open('crawl_listproxysites_com.txt', 'r',encoding='utf8')
    lock_read = threading.Lock()
    lock_write = threading.Lock()
    t_count = 0

    all_thread = []
    for i in range(50):
        t = threading.Thread(target=test)
        all_thread.append(t)
        t.start()

    for t in all_thread:
        t.join()

    inFile.close()
    exit()

    #'http://phx.unblock-me.org/direct/aHR0cHM6Ly93d3cuamQuY29tLw-- '     #正确的地址，如何去掉尾部？
    # http://zigproxy.com/ 尾部丢失1个字节，可修复
    # http://www.imzi-tours-travel.com/annuaire/
    #https://www.ninjaproxy.ninja/browse.php/WwDRC_2Bp8ZB26yvBWOlc_3D/b29/fnorefer/
    #getform('http://uberstudyguide.com')
    #getform('http://62.109.25.136/index.php')
    #getform('http://proxy.proxysite.win/')  #very fast  glype
    #getform('https://www.best-proxy.com.de/index.php')     # phproxy  #ssl 错误  页面容易解析错
    #getform('http://itwtf.com/index.php')    #php-proxy  引擎
    #getform('http://proxy.tian-le.net/phpproxy.php')   #疑似php-proxy
    #getform('http://anonymizer.in/anonymizer/')
    #getform('http://anonymouse.org/anonwww_de.html')   #特殊类型
    #getform('http://hidebox.ru/index.php')

    #getform('http://qc.stop-block.com/direct/aHR0cHM6Ly93d3cuamQuY29tLw--')
    #getform('https://viewpro.info/')
    #getform('http://superproxy.top/index.php')
    #getform('http://anonymousonline.gq/')
    #getform('http://zigproxy.com/')
    #getform('http://gvirabi.com/')
    #http://www.radiocarb.com/p/index.php5
    #http://proxyanonymity.gq/
    #http://lackmoney.cf/
    #http://home.iitk.ac.in/~ravikira/glype-1.4.10/index.php
    # http://instantunblock.com/facebook-proxy/
    #http://www.samstevenm.net/prox/index.php
    #getform('http://morestep.ml')
    #http://www.exiost.com/
    #http://checkday.gq
    #http://gamemarket.ml/
    #http://learnfirst.ga
    #exit(0)


    plist = [    {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q', 'address': '北京联通',
     'baseurl': 'http://fantaluciano.altervista.org/poste/index.php', 'hl': '3ed', 'url_encode': 'base64', 'note': None,
     'method': 'POST',
     'ip': '114.241.70.59', 'wall': 1, 'needtest': 0,'block':1},
     {'strip_tail': None, 'strip_head': None, 'p_type': 'phproxy_0', 'q': 'q',
      'address': '美国 犹他州盐湖城Bluehost公司',
      'baseurl': 'http://www.dmburke.com/PHPProcksy/index.php', 'hl': '3ed', 'url_encode': 'base64',
      'note': '',
      'method': 'POST',
      'ip': '173.254.28.144', 'wall': 0, 'needtest': 1, 'block': 0,},

    ]

    print(gethost('http://fantaluciano.altervista.org/poste/index.php'))
    print(getscheme('http://fantaluciano.altervista.org/poste/index.php'))
    print(getpath('http://fantaluciano.altervista.org/poste/index.php'))
    #PHProxy.testproxylist(plist,needtest=1)

    lines = []
    with open('crawl_listproxysites_com.txt','r',encoding='utf8') as f:
        lines = f.readlines()

    proxyhosts = []

    i=0
    for p in phproxylist:
        proxyhosts.append(gethost(p.get('baseurl')))

    def geturlbyhost(host):
        for pp in phproxylist:
            baseurl = pp.get('baseurl')
            if gethost(baseurl) == host:
                return baseurl

    for line in lines:
        line = line[:-1]
        url = line.split(' ')[0]
        host = gethost(line)

        if host in proxyhosts:
            print('已在列表存在|',line,geturlbyhost(host))
            #continue

        #print(line)
        baseurl = ''
        if len(url) > 5:
            baseurl = url.split('?')[0]
            if url[0] != 'h':
                continue

        if len(baseurl) < 5:
            continue

        domain = gethost(baseurl)
        try:

            ip = getIp(domain)

            print('-----------------------------------------------------------------')
            print(line, ip)
            proxy = getform(baseurl)

            if proxy.get('p_type','unknow') != 'unknow':
                with open('phproxy-list-2017-7-12-crawl_listproxysites_com.txt','a',encoding='utf8') as f:
                    s = proxy.get('baseurl') + '    |' + str(proxy.get('mutil_ip')) + '     |' + str(proxy) + '\n'
                    f.write(s)


            # get_ip_info(ip)
        except Exception as e:
            print('error', baseurl)
            print(e)
            continue

        continue

        if i>2:
            break

        i = i+1

