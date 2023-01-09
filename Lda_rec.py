import jieba
import pandas as pd
import numpy as np
from gensim.models import  ldamodel
from gensim import corpora,models,similarities
import gensim


class LdaRec:

    def __init__(self,cotent:list) -> None:
        
        self.content = content
        self.contents_clean = []
        self.lda = None

    def test_text(self,content:str):

        self.lda = ldamodel.LdaModel.load('mymodel.model')
        self.content = [content]

        #分词
        content_S = []
        for line in self.content:
            current_segment = [w for w in jieba.cut(line) if len(w)>1]
            if len(current_segment) > 1 and current_segment != '\r\t':
                content_S.append(current_segment)
        #分词结果转为DataFrame
        df_content = pd.DataFrame({'content_S':content_S})

        contents = df_content.content_S.values.tolist()

        dictionary = corpora.Dictionary(contents)

        word = [w for w in jieba.cut(content)]

        bow = dictionary.doc2bow(word)
        print(self.lda.get_document_topics(bow))


    # 训练
    def train(self,num_topics=2,random_state=3):

        dictionary = corpora.Dictionary(self.contents_clean)
        corpus = [dictionary.doc2bow(sentence) for sentence in self.contents_clean]
        self.lda = gensim.models.ldamodel.LdaModel(corpus=corpus,id2word=dictionary,num_topics=num_topics,random_state=random_state)

        for e, values in enumerate(self.lda.inference(corpus)[0]):
            print(self.content[e])
            for ee, value in enumerate(values):
                print('\t分类%d推断值%.2f' % (ee, value))


    # 过滤停用词
    def drop_stopwords(self,contents,stopwords):
        contents_clean = []
        for line in contents:
            line_clean = []
            for word in line:
                if word in stopwords:
                    continue
                line_clean.append(word)
            contents_clean.append(line_clean)
        return contents_clean

    def cut_word(self) -> list:
        #分词
        content_S = []
        for line in self.content:
            current_segment = [w for w in jieba.cut(line) if len(w)>1]
            if len(current_segment) > 1 and current_segment != '\r\t':
                content_S.append(current_segment)

        #分词结果转为DataFrame
        df_content = pd.DataFrame({'content_S':content_S})

        # 停用词列表
        stopwords = pd.read_table('stop_words.txt',names = ['stopword'],quoting = 3)

        contents = df_content.content_S.values.tolist()
        stopwords = stopwords.stopword.values.tolist()

        self.contents_clean = self.drop_stopwords(contents,stopwords)


if __name__ == '__main__':
    
    title1="乾坤大挪移,如何将同步阻塞(sync)三方库包转换为异步非阻塞(async)模式？Python3.10实现。"
    title2="Generator(生成器),入门初基,Coroutine(原生协程),登峰造极,Python3.10并发异步编程async底层实现"
    title3="周而复始,往复循环,递归、尾递归算法与无限极层级结构的探究和使用(Golang1.18)"
    title4="彩虹女神跃长空,Go语言进阶之Go语言高性能Web框架Iris项目实战-JWT和中间件(Middleware)的使用EP07"
    content = [title1,title2, title3,title4]

    lr = LdaRec(content)

    lr.cut_word()

    lr.train()

    lr.lda.save('mymodel.model')

    lr.test_text("巧如范金,精比琢玉,一分钟高效打造精美详实的Go语言技术简历(Golang1.18)")

    
