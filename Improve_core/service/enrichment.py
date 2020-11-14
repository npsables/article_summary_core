from gensim.models import Word2Vec
import numpy as np
import gensim.models.keyedvectors as word2vec
from pyvi import ViTokenizer
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
import nltk
import const
nltk.download('punkt')

def enrichment(args, constant_code):
    # Choose model
    model = select_model(constant_code)
    print(args)
    res = []
    count = 0
    try:
        for a in args:
            arg = a.replace(" ", "_")
            keys = model.wv.most_similar(arg)
    except:
        return " ".join(args)
    #Chọn 4 related keywords để search
    while count<4:
        if "_" in keys[count][0]:
            res = res + [keys[count][0]]
        count=count + 1
    
    final_args = '"' + args[0] + '" ' + ' '.join(res)
    print("Seach args: ", final_args)
    return final_args.replace("_", " ")

def old_enrichment(args):
    model = Word2Vec.load('./model/word2vec_Politic.model')
    for a in args:
        arg = a.replace(" ", "_")
        keys = model.wv.most_similar(arg)
    count= 0
    res = []
    while count<4:
        if "_" in keys[count][0]:
            res = res + [keys[count][0]]
        count=count + 1
    final_args = '"' + args[0] + '" ' + ' '.join(res)
    print("Seach args: ", final_args)
    return final_args.replace("_", " ")

def select_model(code):
    model = {
        const.CHINH_TRI     : Word2Vec.load('./model/word2vec_Politic.model'),
        const.CONG_NGHE     : Word2Vec.load('./model/word2vec_Technology.model'),
        const.COVID_19      : Word2Vec.load('./model/word2vec_Covid19.model'),
        const.DIEN_ANH      : Word2Vec.load('./model/word2vec_Film.model'),
        const.GIAI_TRI      : Word2Vec.load('./model/word2vec_Entertainment.model'),
        const.GIAO_DUC      : Word2Vec.load('./model/word2vec_Education.model'),
        const.KINH_TE       : Word2Vec.load('./model/word2vec_Economy.model'),
        const.PHAP_LUAT     : Word2Vec.load('./model/word2vec_Law.model'),
        const.THE_THAO      : Word2Vec.load('./model/word2vec_Sport.model'),
    }[code]
    return model
    
def knn_model(sentences):
    sentences = nltk.sent_tokenize(sentences)

    model=Word2Vec.load('./model/word2vec_Covid19.model')
    vocab = model.wv.vocab
    X = []
    for sentence in sentences:
        sentence_tokenized = ViTokenizer.tokenize(sentence)
        words = sentence_tokenized.split(" ")
        sentence_vec = np.zeros((100))
        for word in words:
            if word in vocab:
                sentence_vec+=model.wv[word]
        X.append(sentence_vec)
    n_clusters = 3
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans = kmeans.fit(X)
    avg = []
    for j in range(n_clusters):
        idx = np.where(kmeans.labels_ == j)[0]
        avg.append(np.mean(idx))
    closest, _ = pairwise_distances_argmin_min(kmeans.cluster_centers_, X)
    ordering = sorted(range(n_clusters), key=lambda k: avg[k])
    summary = ' '.join([sentences[closest[idx]] for idx in ordering])
    return summary