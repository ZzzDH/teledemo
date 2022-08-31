import requests
import json

from jieba.analyse import extract_tags
from pyquery import PyQuery as pq
from dao.OpiDao import OpiDao
from config import user_agent_list, questionList, questionurl1, questionurl2, answerurl1
from analyse import analysis

split_path = r'/ZhiHuAnswers/data/split_raw.txt'
non_split_path = r'/ZhiHuAnswers/data/raw.txt'


def get_keyword(data):
    for keyword, weight in extract_tags(data, withWeight=True, topK=1):
        return keyword


def question(url1, qid, url2):
    headers = {
        'Accept': "application/json, text/plain, */*",
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/65.0.3325.181 Safari/537.36 "
    }
    url = url1 + qid + url2
    response = requests.get(url=url, headers=headers, timeout=300)
    text = response.text
    jtext = json.loads(text)
    datalist = []
    if len(jtext['data']) == 0:
        return 0
    for data in jtext['data']:
        Id = str(data.get('id'))
        answer_count = data.get('answer_count')
        data = {'id': Id, 'answer_count': answer_count}
        datalist.append(data)
        pass

    return datalist


def answer(url1, qid, url2, head):
    headers = {'Accept': "application/json, text/plain, */*", 'User-Agent': head}
    url = url1 + qid + url2
    response = requests.get(url=url, headers=headers, timeout=300)
    jtext = json.loads(s=response.text)
    contentdict = {}
    if len(jtext['data']) == 0:
        return 0
    for data in jtext['data']:
        aid = str(data['id'])
        rawcontext = data['content']
        if len(rawcontext) == 0:
            break
        context = pq(rawcontext).text()
        if context == '':
            break
        voteupcount = data.get('voteup_count')
        commentcount = data.get('comment_count')
        heat = voteupcount + commentcount * 2
        questiontext = data['question'].get('title')

        keyword = get_keyword(context)
        link = "https://www.zhihu.com/question/" + qid + "/answer/" + aid
        data = {'context': context, 'voteupcount': voteupcount, 'commentcount': commentcount,
                'heat': heat, 'keyword': keyword,
                'questiontext': questiontext, 'qid': qid, 'link': link}
        contentdict[aid] = data

    return contentdict


def daoService(anwserDict):
    a=analysis()
    j = 0
    for aid in anwserDict.keys():
        anwserDict[aid]['keyword'] = get_keyword(anwserDict[aid]['context'])
        anwserDict[aid]['feature'] = str(a.get(aid))
        opidao = OpiDao()
        try:
            result = opidao.createcontent(aid, anwserDict[aid])
            if result > 0:
                #if j % 50 == 0:
                print("写入成功")
                print(j)
                j += 1
        except Exception as e:
            print(e)
            return 0
        finally:
            opidao.close()
    return 1


def txtService(answercontextList, answer_id_list):
    with open(split_path, 'w+', encoding='utf-8') as f:
        for (context, aid) in zip(answercontextList, answer_id_list):
            f.write(context + "\t\n")

    with open(non_split_path, 'w+', encoding='utf-8') as f:
        for (context, aid) in zip(answercontextList, answer_id_list):
            con = aid + '||' + context
            f.write(con + "\t\n")
    print("写入txt完成")


class Excute(object):
    def __init__(self, limit):
        self.limit = limit

    def door(self):
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
        answerDict = {}
        answercontextList = []
        answer_id_list = []
        for questionitem in questionList:
            end = int(questionitem.get('answer_count')) - int(questionitem.get('answer_count')) % 5
            for item in range(0, end, 5):
                if j == 410:
                    continue
                answerurl2 = '/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info' \
                             '%2Cis_collapsed' \
                             '%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by' \
                             '%2Csuggest_edit' \
                             '%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count' \
                             '%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info' \
                             '%2Crelevant_info' \
                             '%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Crelationship' \
                             '.is_authorized' \
                             '%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.settings' \
                             '.table_of_content.enabled&limit=5&offset=' \
                             + str(item) + '&platform=desktop&sort_by=default'
                adict = answer(answerurl1, questionitem.get('id'), answerurl2, head=user_agent_list[item % 18])
                if adict != 0:
                    for aid in adict.keys():
                        if aid in answer_id_list:
                            continue
                        answerDict[aid] = adict[aid]
                        answercontextList.append(answerDict[aid]['context'])
                        answer_id_list.append(aid)
                        if j > self.limit-1:
                            return answerDict,answercontextList, answer_id_list
                        j += 1
                        print(j)



if __name__ == '__main__':
    execute = Excute(1000)
    answerDict,answercontextList, answer_id_list=execute.door()
    txtService(answercontextList, answer_id_list)
    daoService(answerDict)
