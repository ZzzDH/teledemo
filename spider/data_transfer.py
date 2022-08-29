from tqdm import tqdm
import numpy as np

# path='./ZhiHuAnswers/data/train.txt'
# with open(path, 'r', encoding='UTF-8') as f:
#     a={'1':0,'2':0,'0':0}
#     for line in tqdm(f):
#         lin = line.strip()
#         if not lin:
#             continue
#         content, label = lin.split('\t')
#         a[label]=a[label]+1
#
#     print(a)
output_path = './ZhiHuAnswers/data/output.txt'
raw_path = './ZhiHuAnswers/data/raw.txt'


def answer_match():
    sentences_with_id = []
    aid_list = []
    index_list = []
    labels = []
    with open(raw_path, 'r', encoding='UTF-8') as f:
        for line in f:
            lin = line.strip()
            if lin in ['\n', '\r\n'] or lin == "":
                continue
            temp = lin.split('||')
            if len(temp) == 2:
                if temp[1] in ['\n', '\r\n', '\t', '\t\n'] or temp[1] == "":
                    continue
            sentences_with_id.append(lin)
    with open(output_path, 'r', encoding='UTF-8') as f:
        for line in f:
            lin = line.strip()
            label = lin.split('\t')[1]
            labels.append(int(label))
    t_idx = []
    aid = 0
    for i, sentence in enumerate(sentences_with_id):
        content = sentence.split('||')
        if len(content) == 2:
            if i != 0:
                aid_list.append(aid)
                index_list.append(t_idx)
                t_idx = []
            aid = content[0]
        t_idx.append(i)
    aid_list.append(aid)
    index_list.append(t_idx)
    labels = np.array(labels)
    label_slices = []
    for idx in index_list:
        label_slices.append(labels[idx])
    label_slices = np.array(label_slices, dtype=object)
    out = []
    aaa=[]
    for id, label in zip(aid_list, label_slices):
        l = np.argmax(np.bincount(label))
        aaa.append(l)
        out.append([id, l])
    bb=np.array(aaa)

    return out


if __name__ == '__main__':
    b=np.array(answer_match())

