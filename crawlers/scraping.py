from bs4 import BeautifulSoup
import requests

REDDIT_URL = 'https://old.reddit.com/r/'
SCORE_FILTER = 5000

class Reddit:
    def __init__(self, subreddit, title, score, link, comments, datetime):
        self.subreddit = subreddit
        self.title = title
        self.score = score
        self.link = link
        self.comments = comments
        self.datetime = datetime   

def check_exists(soup):
    error = soup.find('p', {'id': 'noresults', 'class': 'error'})
    if error == None:
        return True
    else:
        return False

def request_content(word):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
    response = requests.get(f'{REDDIT_URL}{word}', headers=headers).text
    return BeautifulSoup(response, 'html.parser')

def get_threads(args):
    words = [x for x in args.split(';') if x] #check if is an empty string
    results = []
    for word in words:
        soup = request_content(word)

        if check_exists(soup):
            subreddit = soup.find('span', {'class': 'redditname'}).text
            content = soup.find_all('div', {'data-subreddit': subreddit})

            threads = []
            for thread in content:
                try: #exception to pass any character unless integer
                    score = int(thread.find('div', {'class': 'score unvoted'})['title'])
                    if score >= SCORE_FILTER:
                        title = thread.find('a', {'class': 'title'}).text
                        comments = thread.find('a', {'class': 'comments'})['href']
                        link = thread.find('a', {'class': 'title'})['href']
                        datetime = thread.find('time', {'class': 'live-timestamp'})['datetime']
                        r = Reddit(subreddit, title, score, link, comments, datetime)
                        threads.append(r)
                except:
                    pass
            results.append(threads)
        else:
            results.append({'subreddit': word, 'msg': "doesn't exists"})

    return results