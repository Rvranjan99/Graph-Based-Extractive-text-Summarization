from math import cos
import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords 
from nltk.cluster.util import cosine_distance 
import numpy as np
import scipy as sp
import networkx as nx 
from nltk.tokenize import word_tokenize, sent_tokenize

def wordCount(para):
    return len(word_tokenize(para))

def sentCount(para):
    return len(sent_tokenize(para))


def read_doc(file_name):
    file=open(file_name,"r")
    filedata=file.read()
    
    article= filedata.split(".")
    #print(article)
    sentences=[]
    for sent in article:
        sentences.append(sent.replace("^a-zA-Z"," ").split(" "))
    sentences.pop()
    return sentences

def sent_similarity(sent1,sent2, stopwords=None):
    if stopwords is None:
        stopwords=[]
    sent1=[w.lower() for w in sent1]
    sent2=[w.lower() for w in sent2]
    words=list(set(sent1+sent2))

    v1=[0]*len(words)
    v2=[0]*len(words)

    for w in sent1:
        if w in stopwords:
            continue 
        v1[words.index(w)]+=1

    for w in sent2:
        if w in stopwords:
            continue 
        v2[words.index(w)]+=1 

    return 1-cosine_distance(v1,v2)

def similarity_matrix(sentences,stopwords):
    sm=np.zeros((len(sentences),len(sentences)))

    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i==j:
                continue 
            sm[i][j]=sent_similarity(sentences[i],sentences[j],stopwords)
        
    return sm 
    
def generate_summary(file_name,top_n=4):
    stop_words=stopwords.words("english")
    summarize_text=[]
    sentences=read_doc(file_name)
    #print(sentences)
    sent_similarity_matrix=similarity_matrix(sentences,stop_words)
    sent_similarity_graph=nx.from_numpy_array(sent_similarity_matrix)
    scores=nx.pagerank(sent_similarity_graph)
    ranked_sent=sorted(((scores[i],s) for i, s in enumerate(sentences)),reverse=True)
    #print(ranked_sent)
    for i in range(top_n):
        summarize_text.append(" ".join(ranked_sent[i][1]))
    return (". ".join(summarize_text))
  



    

