import gethtml
import articletext

url ="http://english.jagran.com/uttar-pradesh-suspense-on-priyanka-gandhis-role-for-uttar-pradesh-assembly-polls-85069"
#web_text = gethtml.getHtmlText(url)
#print articletext.getArticleText(web_text)
article = articletext.getArticle(url)
for w in articletext.getKeywords(article):
	print w