from dao.BaseDao import BaseDao


class OpiDao(BaseDao):
    def createJobData(self, sql, params):
        result = self.execute(sql, params)
        self.commit()
        return result
        pass

    def createcontent(self, data={}):
        sql = "insert into opinions (aid,context,voteupcount,commentcount,heat,questiontext,qid,link) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        params = [data.get('aid'),data.get('context'), data.get('voteupcount'), data.get('commentcount'),data.get('heat'), data.get('questiontext'),data.get('qid'),data.get('link')]
        result = self.execute(sql, params)
        self.commit()
        return result
        pass
