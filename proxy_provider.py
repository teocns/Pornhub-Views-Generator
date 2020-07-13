### This application is engineered to be using Residential Proxy Pool. You may need to change this file accordingly to your Proxy provider API
### We are hereby implementing Oxylabs    |    https://docs.oxylabs.io/residential/index.html#getting-started
import requests
import hashlib




def generate_session_id():
    hashlib.md5("time.time()".encode('utf-8')).hexdigest()
# To get random IP pool we can use curl -x tr-pr.oxylabs.io:30000 -U "customer-USERNAME:PASSWORD" https://ipinfo.io
# Since we are not passing any credential, IP must be whitelisted for the requesting machine.
import urllib3
import json
class Proxy:
    def __init__(self,host,port):
        self.host = host
        self.port = port
    
def get_proxy_dict(sessId = ''):
    sessId = f"-sessid-{sessId}" if sessId else ''
    
    
    username = 'rarthuraxton'
    password = 'la69qhnjdR'
    
    entry = ('http://customer-%s%s:%s@pr.oxylabs.io:7777' %
        (username, sessId, password))
    return {
        'http': entry,
        'https': entry,
    }
 