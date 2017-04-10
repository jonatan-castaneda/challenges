def changeWord(char, begin_word, index):
    begin_word = list(begin_word)
    begin_word[index] = char
    return ''.join(begin_word)

def priorityWord(begin_word, priority_words):
    if(len(priority_words) > 0):
        begin_word = list(begin_word)
        priority = list()
        for word in priority_words:
            x = 0
            i = 0
            for char in word:
                if char == begin_word[i]:
                    x += 1
                    i += 1
            priority.append(x)
        priority.sort()
        return priority_words[len(priority) - 1]
    if(len(priority_words) == 1):
        return priority_words.pop()
    else:
        return ''.join(begin_word)
    
    

if __name__ == '__main__':
    
#    begin_word = input("Enter the begin word: ")
#    end_word = input("Enter the end word: ")
#    word_list = input("Enter the list of the words accepted separated with coma: ")
#    word_list = word_list.split(',')
#    print(word_list)

    begin_word = 'hit'
    end_word = 'cog'
    word_list = ['hot', 'dot', 'dog','lot', 'log', 'cog']
    priority_words = list()
    for word in word_list:
        x = 0
        while x < len(word):
            changed_word = changeWord(word[x], begin_word, x)
            
            if changed_word in word_list:
                if(changed_word != begin_word):
                    priority_words.append(changed_word)
                    #print("->" + changed_word)
                    #begin_word = changed_word
            x += 1
        #print(priority_words)
        begin_word = priorityWord(begin_word, priority_words)
        priority_words = list()
        print("->" + begin_word)
