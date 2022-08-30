import sys

from Excute import Excute, txtService, daoService

# limit = int(sys.argv[1])
# search_content = sys.argv[2]
execute = Excute(5)
answerDict, answercontextList, answer_id_list = execute.door()
txtService(answercontextList, answer_id_list)
daoService(answerDict)
