import time
import torch
import tqdm
from importlib import import_module
from torch import nn
from tqdm import tqdm
import torch.utils.data as Data

from models.my_rnn_attention import RNN
from utils import build_dataset

model_path = './my_model_dict/epoch_17_loss_1.0007380723953248_acc_tensor(0.5675, device=\'cuda_0\')_param.pt'
output_path='./ZhiHuAnswers/data/output.txt'
device=torch.device('cpu')
def tag(model,dataset):
    labels = []
    for batch_x in tqdm(dataset):
        batch_x=batch_x[0].to(device)
        output=model(batch_x)
        predict=torch.max(output.data,1)[1]
        labels+=predict.tolist()
    print(labels)
    return labels


if __name__ == '__main__':
    batch_size = 16
    vocab_size, embedding_dim, hidden_size, num_classes, num_layers = 18000, 256, 128, 3, 1
    dataset = 'ZhiHuAnswers'
    start_time = time.time()
    x = import_module('models.' + 'bert')
    config = x.Config(dataset)
    print("Loading data...")

    untagged_data ,texts= build_dataset(config, mode='utilize')
    train_data = Data.TensorDataset(torch.tensor(untagged_data))
    train_loader = Data.DataLoader(
        dataset=train_data,
        batch_size=batch_size,
        num_workers=2
    )
    model = RNN(vocab_size, embedding_dim, hidden_size, num_classes, num_layers)
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    labels=tag(model,train_loader)
    with open(output_path,'w',encoding='UTF-8') as f:
        for text,label in zip(texts,labels):
            text=text.strip('\n').strip('\t')
            sentence=text+'\t'+str(label)+'\n'
            f.write(sentence)

