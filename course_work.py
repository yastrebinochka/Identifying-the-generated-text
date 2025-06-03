import nltk
import nltk.corpus
from nltk.corpus import brown

from Text import Text


def cut_file(filename): #функция для укорачивания файла из Brown Corpus с 2000 слов до 1000
    with open(filename, 'r', encoding='utf-8') as f1:
        text = f1.read()
        words = text.split()
        if len(words) > 1000:
            truncated_text = ' '.join(words[:1000])
            with open(filename, 'w', encoding='utf-8') as f2:
                f2.write(truncated_text)
    return filename

#установка брауновского корпуса
nltk.download('brown')
#установка файлов из корпуса
titles = nltk.corpus.brown.fileids() #получение списка файлов
for title in titles:
    raw_corpus = brown.sents(title) #использование корпуса без тегов
    corpus = join(raw_corpus)
    with open(title+'.txt', 'w') as f:
       f.write(corpus)

#подсчет статистики для пар "корпус + нейросеть"
for i in range(1, 26):
    num = f"{i:02d}"
    file1 = cut_file(f"ca{num}.txt")
    file2 = f"ca{num}_mistral.txt"
    Brown_corpus = Text.read_txt(file1)
    Mistral = Text.read_txt(file2)
    print(Text.khmelev_statistics(Brown_corpus, Mistral))

#подсчет статистики для пар "корпус + корпус"
files = [f"ca{i:02d}.txt" for i in range(1, 26)]
pairs = []
for i in range(1, 25):
        try:
            pair = (files[i-1], files[i])
            pairs.append(pair)
            first = Text.read_txt(pair[0])
            second = Text.read_txt(pair[1])
            print(Text.khmelev_statistics(first, second))
        except IndexError:
            print(pair)
#для подсчета статистики для пар "нейросеть + нейросеть" меняются только названия файлов
#files = [f"ca{i:02d}_mistral.txt" for i in range(1, 26)]