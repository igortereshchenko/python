def is_letter(letter):
    pattern='qwertyuiopasdfghjklzxcvbnm'
    if  pattern.find(letter.lower())!=-1:
        return True
        
    return False


def get_word(prompt):
    
    not_correct_data=True
    while not_correct_data:


        
        word=input('Enter '+prompt+':')
        
        not_correct_data=False
        
        if len(word)>0:
            not_correct_data=False
        else:
            not_correct_data=True            
            continue
        
        if word[0]!=word[0].upper():
            not_correct_data=True            
            continue
        
        
        for letter in word:
            if (not is_letter(letter)):
                not_correct_data=True
                break
        
        
    
    return word


    
    
print(get_word('Surname'))
