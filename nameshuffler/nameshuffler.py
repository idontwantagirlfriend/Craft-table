# encoding="utf-8"
# Version: Python 3.9.0
# Date of creation: 12/23/2020

from nltk.tokenize import word_tokenize as nltk_tokenize
from random import randint as rand
from copy import deepcopy
from jieba import lcut as jieba_tokenize

class nameshuffler:
    """
    A name shuffler can generate from a text pool (str format) a random name of a given length.
    The default corpus is from a book about syntax, while you can load a custom corpus.
    Currently only supports Chinese and languages in latin alphabets. You may however give a few more attempts on other languages.
    """
              
    def __init__(self, corpus="D:\Le F\Desktop\Grammatical Theory.txt", lang="alpha"):
        temp_lst=[]
        if lang=="alpha":            
            _scrap=(".", ",", "?", "!","d","{","}","(",")","[","]","'",'"',"\/","|","\\","=","$","0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        elif lang=="zh":
            _scrap=("。","，","！","？","…","•","”","“","（","）","—","、","；","：","＼",",",".","?", "!","d","{","}","(",")","[","]","'",'"',"\/","|","\\","=","$","0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
        else:
            raise ValueError("Invalid language parameter. Must be between \"zh\" and \"latin\"")
        #标点符号列表，你不会考虑带有标点符号的名字吧？
        
        with open(corpus, encoding="utf-8") as text:
            for line in text:
                if lang=="non-zh":
                    temp_lst.extend(nltk_tokenize(line))
                elif lang=="zh":
                    temp_lst.extend(jieba_tokenize(line))
        temp_set=set(temp_lst)

        temp_lst.clear()

        masked=deepcopy(temp_set)
        #如果对temp_set（一个set）的遍历正在进行，但set的长度改变，这个遍历会无法继续：
        #RuntimeError: Set changed size during iteration
        #所以设定了temp_set提供遍历来源，masked作为工事对象，在masked被改变时，不会影响temp_set
        #的长度，遍历可以继续。
        
        for i in temp_set:
            if isinstance(i,str):
                if i.startswith("_"):
                    masked.remove(i)
                else:
                    for j in _scrap:
                        if j in i:
                            masked.remove(i)
                            break
                            
        #当temp_set中的词汇i因为包含_scrap中的字符已经被移除，而对_scrap的穷举“for j in _scrap”仍然没有
        #结束时，如果i在之后对_scrap的遍历中再次被判定为要移除，则会发出temp_set.remove(i)，对
        #temp_set移除一个本来就不存在于其中的元素，所以报错：
        #    KeyError: [i]
        #这里通过remove后立刻break中断遍历，解决了这个问题。当然也可以：
        #Optiion 1: 通过在内部for加入
        #    if i in temp_set:
        #        <remove operation>
        #    else:
        #        break
        #Option 2: 在内部for加入
        #    if j in i:
        #         try: temp_set.remove(i)
        #         except KeyError:
        #             pass
                    
        for i in masked:
              temp_lst.append(i)
              
        self.corpus=corpus
        self.pool=temp_lst
        self.lang=lang
        #成为class内部的全局变量，这样就可以在接下来继续使用参数

    def shuffle(self, leng=2):
        #从已经建立的pool中抽取元素。允许重复。
        size=len(self.pool)
        counter1=0
        shufflename=[]
        
        while counter1<leng:
            key=self.pool[rand(0,size-1)]
            if isinstance(key,str):
                if self.lang=="alpha":
                    key=key.lower()
                    key=key.capitalize()
                else:
                    pass
            shufflename.append(key)
            counter1+=1
            
        if self.lang=="alpha":
            return " ".join(shufflename)
        else:
            return "".join(shufflename)

    def special(self, a, lengt):
        #根据特定的字符，定制名字。
        #直到名字被产生之前，shuffle将会一直进行下去。
        b=self.shuffle(leng=lengt)
        while (a in b)==False:
            b=self.shuffle(leng=lengt)
        return b
    
