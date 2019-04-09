#!/usr/bin/env python3
import sys

config = \
{"KBFoundation":None,
"KBCommon":["KBFoundation","KBGenericModel"],
"KBProfit":["KBFoundation","KBCommon","KBGenericModel","KBMediator"],
"KBProfile":["KBFoundation","KBCommon","KBGenericModel","KBMediator"],
"KBQuestionEngine":["KBFoundation","KBCommon","KBGenericModel"],
"KBMath":["KBFoundation","KBCommon","KBQuestionEngine","KBGenericModel","KBMediator"],
"KBEnglish":["KBFoundation","KBCommon","KBQuestionEngine","KBGenericModel","KBMediator"],
"KBOcr":["KBFoundation","KBCommon","KBQuestionEngine","KBGenericModel","KBMediator"],
"KBChinese":["KBFoundation","KBCommon","KBQuestionEngine","KBGenericModel","KBMediator"],
"KBGenericModel":["KBFoundation"],
"KBMediator":["KBFoundation","KBCommon","KBGenericModel"]}

def BuildOder(config,key):
    if not config:
        return []
    if not key or not len(key):
        return []
    queue = []
    if isinstance(key,str):
        queue.append(key)
    elif isinstance(key,list):
        queue.extend(key)
    else:
        return []
        
    tmp = []
    while len(queue):
        pop = queue.pop(0)
        tmp.append(pop)
        childs = config[pop]
        if childs and len(childs):
            queue.extend(childs) 

    sort = []
    while len(tmp):
        pop = tmp.pop()
        if not pop in sort:
            sort.append(pop)
    
    return sort

if __name__ == "__main__":
    sort = BuildOder(config,sys.argv[1:])
    print(sort)
    
sort = BuildOder(config,"KBCommon")
print(sort)
