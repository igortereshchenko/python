


def clear_words(words):
    words_cleared=[]
    for word in words:
        if ',.:;!?-'.find(word[len(word)-1])>=0:
            word_cleared=word[:len(word)-1]
            if len(word_cleared)>0:
                words_cleared.append(word_cleared.lower())
        else:
            words_cleared.append(word.lower())
    
    return words_cleared


def add_statistic(statistic,word):
    if len(statistic):
        for record in statistic:
            if record[0]==word:
                record[1]+=1
                return
    statistic.append([word,1]) 
    
    
def create_statistic(words):
    statistic=[]
    
    for word in clear_words(words):
        add_statistic(statistic,word)   
    
    return statistic
    
def search_statistic_min(statistic):
    min_index=0
    min_value=statistic[min_index][1]
    
    for index in range(len(statistic)):
        if statistic[index][1]<min_value:
            min_index=index
            min_value=statistic[index][1]

    return min_value
    


def task():
    
    words=input("Enter text").split()
    
    statistic=create_statistic(words)

    min_repeat=search_statistic_min(statistic)
    

    result=[]
    
    for record in statistic:
        if record[1]==min_repeat:
            result.append(record[0])
    
    result.sort()
    print(result)
    
task()









