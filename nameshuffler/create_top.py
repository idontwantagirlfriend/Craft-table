"""Applies to any text in parsed list. Calculate the top_num most frequent lemma."""

def create_top(parsed_lst,top_num):
        temp_dict={}
        for i in parsed_lst:
                if (i in temp_dict)==False:
                        temp_dict[i]=0
                else:
                        temp_dict[i]+=1
        temp_lst=[]
        stpwd={"的","有","和","了","与","为","在","上","等","而","以","如","之","只",\
                                 "是","都","即","后","中","同","从","及","也","对","到"}
        for i in temp_dict:
                if i in stpwd:
                        pass
                else:
                        temp_lst.append([i,temp_dict[i]])
        temp_lst=sorted(temp_lst,key=lambda x:x[1],reverse=True)
        for i in range(top_num):
                print("{0}: {1}".format(temp_lst[i][0],temp_lst[i][1]))
        print("Calculation terminated.")
