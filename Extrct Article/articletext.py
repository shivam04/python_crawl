from bs4 import BeautifulSoup
import gethtml

def getArticleText(web_text):
	articletext = ""
	soup = BeautifulSoup(web_text)
	for tag in soup.findAll('p'):
		articletext += tag.contents[0]
	return articletext

def getArticle(url):
	htmltext = gethtml.getHtmlText(url)
	return getArticleText(htmltext)

def getKeywords(articletext):
	common = open('common.txt').read().split('\n')
	word_dict = {}
	word_list = articletext.lower().split()
	for word in word_list:
		if word not in common and word.isalnum():
			if word not in word_dict:
				word_dict[word] = 1
			if word in word_dict:
				word_dict[word] += 1
	top_words = sorted(word_dict.items(),key=lambda(k,v):(v,k),reverse=True)[0:25]
	top25 = []
	for w in top_words:
		top25.append(w[0])
	return top25