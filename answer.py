import pandas as pd
import requests
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import words
from textblob import TextBlob

input_file = pd.read_excel('Input.xlsx')

for index, row in input_file.iterrows():
    url = row['URL']
    url_id = row['URL_ID']
    
    response = requests.get(url)
    
    if response.status_code == 200:
    
        soup = BeautifulSoup(response.text, 'html.parser')
        
        article_title = soup.find('title').text
        article_text = soup.find('article').text  
      
        with open(f'{url_id}.txt', 'w', encoding='utf-8') as file:
            file.write(article_title + '\n')
            file.write(article_text)
    else:
        print(f"Failed to retrieve data from {url}")  


nltk.download('punkt')
nltk.download('words')


file_list = ["URL_ID1.txt", "URL_ID2.txt", ...]


results = []

for filename in file_list:
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    
    results.append([positive_score, negative_score, polarity_score, subjectivity_score,
                    avg_sentence_length, percentage_complex_words, fog_index,
                    avg_words_per_sentence, complex_word_count, word_count,
                    syllable_per_word, personal_pronouns, avg_word_length])


output_df = pd.DataFrame(results, columns=["URL_ID", "POSITIVE SCORE", "NEGATIVE SCORE", "POLARITY SCORE", "SUBJECTIVITY SCORE",
                                           "AVG SENTENCE LENGTH", "PERCENTAGE OF COMPLEX WORDS", "FOG INDEX",
                                           "AVG NUMBER OF WORDS PER SENTENCE", "COMPLEX WORD COUNT", "WORD COUNT",
                                           "SYLLABLE PER WORD", "PERSONAL PRONOUNS", "AVG WORD LENGTH"])


output_df.to_excel('Output Data Structure.xlsx', index=False)

      

