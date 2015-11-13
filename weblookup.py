import requests
import urllib
from bs4 import BeautifulSoup

def stripRelevantLinks(myStr):
	resList = myStr.split('class="g"')
	htmlDict = {}
	for i in xrange(1,len(resList)):
		print "\t",resList[i]
		first = 0
		print "\n\n"
		for el in resList[i].split('href'):
			print "\t\t",el
			first += 1
			if first == 1:
				continue
			divString = el.split('"')[1]
			print "\t\t",divString
			if len(divString.split("http")) > 1 and len(divString.split("http")[1].split(".html")) > 1:
				htmlString = "http" + divString.split("http")[1].split(".html")[0] + ".html"
				print "\t\t\t", htmlString
				if htmlString not in htmlDict:
					htmlDict[htmlString] = 1
			elif len(divString.split("http")) > 1 and len(divString.split("http")[1].split("&amp")) > 1:
				htmlString = "http" + divString.split("http")[1].split("&amp")[0]
				print "\t\t\t", htmlString
				if htmlString not in htmlDict:
					htmlDict[htmlString] = 1
		print "\n\n\n\n\n\n"
	print "\n\n\n\n\n"
	for ele in htmlDict:
		print "\t\t\t",ele

	return htmlDict
def get_result():
	contentText = ""
	minDate = ['9','10','2011']
	maxDate = ['9','21','2011']
	#search = "Trump"
	#searchString = ""
	#searchString += "https://www.google.com/search?cf=all&hl=en&pz=1&ned=us&tbm=nws&gl=us&as_q=" + search + "&as_occt=any&as_drrb=b&as_mindate=" + minDate[0] + "%2F" + minDate[1] + "%2F" + minDate[2] + "&as_maxdate=" + maxDate[0] + "%2F" + maxDate[1] + "%2F" + maxDate[2] + "&tbs=cdr%3A1%2Ccd_min%3A" + minDate[0] + "%2F" + minDate[1] + "%2F" + minDate[2] + "%2Ccd_max%3A" + maxDate[0] + "%2F" + maxDate[1] + "%2F" + maxDate[2] + "&authuser=0"
	s = "plane"
	sarr = s.split()
	string = ""
	for i in xrange(0, len(sarr)):
		string += sarr[i]
		if i != len(sarr) - 1:
			string += "+"

	searchStrings = []
	pageOne = "https://www.google.com/search?q=" + string + "&hl=en&gl=us&authuser=0&source=lnt&tbs=cdr%3A1%2Ccd_min%3A" + minDate[0] + "%2F" + minDate[1] + "%2F" + minDate[2] + "%2Ccd_max%3A" + maxDate[0] + "%2F" + maxDate[1] + "%2F" + maxDate[2] + "&tbm=nws"
	searchStrings.append(pageOne)
	start = 0
	while start < 40:
		start += 10
		nextPage = "https://www.google.com/search?q=" + string + "&hl=en&gl=us&authuser=0&source=lnt&tbs=cdr%3A1%2Ccd_min%3A" + minDate[0] + "%2F" + minDate[1] + "%2F" + minDate[2] + "%2Ccd_max%3A" + maxDate[0] + "%2F" + maxDate[1] + "%2F" + maxDate[2] + "&tbm=nws#q=" + string + "&hl=en&gl=us&authuser=0&tbs=cdr:1,cd_min:" + minDate[0] + "/" + minDate[1] + "/" + minDate[2] + ",cd_max:" + maxDate[0] + "/" + maxDate[1] + "/" + maxDate[2] + "&tbm=nws&start=" + str(start)
		searchStrings.append(nextPage)
	rawText = ""
	urlDict = {}
	print searchStrings
	for s in searchStrings:
		print s
		r = requests.get(s)
		print r
		contentText += r.content + "\n\n\n\n\n\nHERE\n\n\n\n\n\n"
		for el in stripRelevantLinks(r.content).keys():
			if el not in urlDict:
				urlDict[el] = 1
			else:
				urlDict[el] += 1
	for el in urlDict.keys():
		try:
			html = urllib.urlopen(el).read()
			soup = BeautifulSoup(html)
			# kill all script and style elements
			for script in soup(["script", "style"]):
				script.extract()    # rip it out
			#rawText += el + "\n\n\n\n"
			temp = soup.get_text()
			for element in temp.split('\n'):
				if element.split() > 200:
					rawText += element + "\n"
			#rawText += "\n\n\n\n\n\n\nBREAK_BETWEEN_TWO_PAGES\n\n\n\n\n\n\n"
			rawText += "\n"
		except Exception:
			sa = 1
		print el
	#return rawText
	return rawText
f = open("newsout.txt",'w')
f.write(get_result().encode('utf8'))
