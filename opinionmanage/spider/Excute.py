from time import sleep

import requests
import json
import re
from pyquery import PyQuery as pq
from dao.OpiDao import OpiDao


def question(url1, id, url2):
    headers = {
        'Accept': "application/json, text/plain, */*",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/65.0.3325.181 Safari/537.36 "
    }
    url = url1 + id + url2
    response = requests.get(url=url, headers=headers, timeout=300)
    text = response.text
    jtext = json.loads(text)
    datalist = []
    if len(jtext['data']) == 0:
        return 0
    for data in jtext['data']:
        id = str(data.get('id'))
        answer_count = data.get('answer_count')
        data = {'id': id, 'answer_count': answer_count}
        datalist.append(data)
        pass

    return datalist


def answer(url1, id, url2, head):
    headers = {'Accept': "application/json, text/plain, */*", 'User-Agent': head}
    url = url1 + id + url2
    response = requests.get(url=url, headers=headers, timeout=300)
    jtext = json.loads(s=response.text)
    contentList = []
    if len(jtext['data']) == 0:
        return 0
    for data in jtext['data']:
        aid = str(data['id'])
        rawcontext = data['content']
        if len(rawcontext) == 0:
            return 0
        voteupcount = data.get('voteup_count')
        commentcount = data.get('comment_count')
        heat = voteupcount + commentcount * 2
        questiontext = data['question'].get('title')
        context = pq(rawcontext).text()
        qid = id
        link = "https://www.zhihu.com/question/" + qid + "/answer/" + aid
        data = {'aid': aid, 'context': context, 'voteupcount': voteupcount, 'commentcount': commentcount, 'heat': heat,
                'questiontext': questiontext, 'qid': qid, 'link': link}
        contentList.append(data)

    return contentList


item = 0
questionurl1 = "https://www.zhihu.com/api/v4/questions/"
questionurl2 = "/similar-questions?include=data%5B*%5D.answer_count%2Cauthor%2Cfollower_count&limit=5"
answerurl1 = 'https://www.zhihu.com/api/v4/questions//'
answerurl2 = '/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed' \
             '%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit' \
             '%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count' \
             '%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info' \
             '%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized' \
             '%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.settings' \
             '.table_of_content.enabled&limit=5&offset=0' \
             '&platform=desktop&sort_by=default'
questionList = [{'id': "527445211", 'answer_count': "605"}, {'id': "457368252", 'answer_count': "423"}]
user_agent_list = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
answerList = []
for i in range(100):
    if i == len(questionList):
        break
    qlist = question(questionurl1, questionList[i].get('id'), questionurl2)
    if qlist != 0:
        for qitem in qlist:
            if qitem not in questionList:
                questionList.append(qitem)
    print(i)
    j = 1
    aidlist = []
for questionitem in questionList:
    if questionitem.get('id') in aidlist:
        continue
    aidlist.append(questionitem.get('id'))
    end = int(questionitem.get('answer_count')) - int(questionitem.get('answer_count')) % 5
    for item in range(0, end, 5):
        if j == 410:
            continue
        answerurl2 = '/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed' \
                     '%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit' \
                     '%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count' \
                     '%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info' \
                     '%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship.is_authorized' \
                     '%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.settings' \
                     '.table_of_content.enabled&limit=5&offset=' \
                     + str(item) + '&platform=desktop&sort_by=default'
        alist = answer(answerurl1, questionitem.get('id'), answerurl2, head=user_agent_list[item % 18])
        if alist != 0:
            for aitem in alist:
                try:
                    opidao = OpiDao()
                    result = opidao.createcontent(aitem)
                    if result > 0:
                        print("写入成功")
                        print(j)
                        j += 1
                finally:
                    opidao.close()
