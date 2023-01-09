# Lda-Gensim-Recommended-System-Python310

## 安装

```
pip3 install jieba
pip3 install gensim
```

## 运行

```
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
```
