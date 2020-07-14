import re
import random
import requests
from proxy_provider import get_proxy_dict,generate_session_id
from time import sleep
from multiprocessing.dummy import Pool as ThreadPool
from threading import Timer, Event


REFERERS_LIST = []
with open('referers.txt','r') as f:
    REFERERS_LIST = [line.strip() for line in f.read().split("\n")]
    
UA_LIST = []
with open('ua.txt','r') as f:
    UA_LIST = [line.strip() for line in f.read().split("\n")]
    

TOTAL_VIDEO_COUNTS = 0

def test(i):
    print(f"Current iteration: {i}")
    # Make first request
    session_id = generate_session_id()
    proxydict = get_proxy_dict(session_id)


    session = requests.Session()

    VIDEO_URL = 'https://www.pornhub.com/view_video.php?viewkey=ph5f0cc6468692e'
    UA = random.choice(UA_LIST)
    REFERER = random.choice(REFERERS_LIST)
    video_loaded_response = session.get(
        VIDEO_URL,
        proxies= proxydict,
        headers={
            'referer':REFERER,
            'user-agent':UA
        }
    )
    if video_loaded_response.status_code != 200:
        print('Something went wrong!')


    """data-video-id="332754762">"""

    VIDEO_ID = str(re.findall('(?<=data-video-id=").+?(?=")',video_loaded_response.text)[0])
    # Wait 8 seconds...
    print ('Sleeping 8 seconds')
    sleep(7)
    # Parse video add
    register_video_count_url = str(re.findall('(?<=vcServerUrl":").+?(?=")',video_loaded_response.text)[0]).replace('\\','')
        
                                                                                
    final_response = session.get(
        f"https://www.pornhub.com{register_video_count_url}",
        headers={
            'referer':VIDEO_URL,
            'host':'www.pornhub.com',
            'origin':'https://www.pornhub.com',
            'user-agent':UA
        },
        proxies=proxydict
    )
    if final_response.text.strip() == 'ok':
        TOTAL_VIDEO_COUNTS = TOTAL_VIDEO_COUNTS+1
        print('Video count registered. Total = '+str(TOTAL_VIDEO_COUNTS))
    

    LIKE_URL = register_video_count_url = str(re.findall('(?<=submitVote":").+?(?=")',video_loaded_response.text)[0]).replace('\\','')
    # Put a like aswell
    like_delay = random.randint(10,40)
    print('Placing like')
    
    sleep(like_delay)
    session.post(
        f"https://www.pornhub.com{LIKE_URL}",
        headers={
            'referer':VIDEO_URL,
            'host':'www.pornhub.com',
            'origin':'https://www.pornhub.com',
            'user-agent':UA
        },  
        proxies=proxydict
    )


rng = range(0,999999)



with  ThreadPool(34) as pool:
    pool.map(test,rng)

