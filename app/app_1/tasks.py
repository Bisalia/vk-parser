from urllib import request
from bs4 import BeautifulSoup
import lxml
import time

def count_words(url):
    print(f'Counting words at {url}')

    start= time.time()

    r = request.urlopen(url)

    soup = BeautifulSoup(r.read().decode(), lxml)

    paragraphs = " ".join([div.text for div in soup.find_all("div")])

    word_count = dict()

    for i in paragraphs.split():
        if not i in word_count:
            word_count[i] = 1
        else:
            word_count[i] += 1
    end = time.time()

    time_elapsed = end - start

    print(word_count)
    print(f'Total Words: {len(word_count)}')
    print(f'Time elapsed: {time_elapsed}')

    return len(word_count)

