def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
    # I also added some extra unwanted words 
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", \
    "on","not", "for","in", "other","now", "new"]
    
    # LEARNER CODE START HERE
    file_contents = file_contents.lower().split()
    word_dictionay = {}
    
    # Check is this word is alpha
    words_check_alpha = []
    for word in file_contents:
        if word.isalpha():
            words_check_alpha.append(word)
    
    # remove unwanted words 
    words_check_unwanted_words = []
    for word in words_check_alpha:
        if word not in uninteresting_words:
            words_check_unwanted_words.append(word)
    
    #print(words_check_unwanted_words)
    
    # create a dictionary and check the word frequencies 
    word_dictionay = {}
    for word in words_check_unwanted_words:
        if word not in word_dictionay:
            word_dictionay[word] = 0
        word_dictionay[word] += 1
            
    #print(words_check_alpha)
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_dictionay)
    return cloud.to_array()
