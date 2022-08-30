from dao.BaseDao import BaseDao


class OpiDao(BaseDao):

    def createcontent(self,aid,data={}):

        sql = "insert into opinions (aid,context,feature,voteupcount,commentcount,heat,keyword,questiontext,qid,link) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        params = [aid,data.get('context'),data.get('feature'), data.get('voteupcount'), data.get('commentcount'),data.get('heat'),data.get('keyword'),data.get('questiontext'),data.get('qid'),data.get('link')]

        result = self.execute(sql, params)
        self.commit()
        return result
        pass

    def updatetag(self,data={}):
        sql = "update opinions set feature = %s where aid= %s"
        params = [data['feature'],data['aid']]
        result = self.execute(sql,params)
        self.commit()
        return result
        pass

    def updatekeyword(self,data={}):
        sql = "update opinions set feature = %s where aid= %s"
        params = [data['keyword'], data['aid']]
        result = self.execute(sql, params)
        self.commit()
        return result
        pass
