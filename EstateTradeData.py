#encoding = utf-8

####################################
#								   #
# 		Date: 2016-11-18		   #
#	  	  By BoyceHong             #
#	  							   #
####################################

import re
import urllib.request
import linecache
from plib import _Getch
from plib import switch

def getHtml(url):
	html = urllib.request.urlopen(url, timeout = 10).read()
	#html = html.decode('UTF-8')
	if html == 'null':
		print('Get html fail!')
	return html

def getDate(SrcStr):
	reg = r'<span id="ctl00_TitleContent_lbl_date">(.+)</span>'
	dateRe = re.compile(reg)
	dateList = re.findall(dateRe, SrcStr)
	#date = dateList.split("'")[1]
	date = ('').join(dateList)
	return date

def getInfo(SrcStr):
	reg = r'\d+'
	dataList = re.findall(reg, SrcStr)
	#data = ('').join(dataList)
	return dataList

Date = "2016-11-15"
Number = [0] * 14
Area = [0] * 14

htmlPath = r"C:\Users\boyce_hong\Desktop\python\html.log"
dataPath = r"C:\Users\boyce_hong\Desktop\python\EstateTradeData.log"
targetUrl = 'http://www.szfcweb.com/szfcweb/(S(mxdc4tn5ia1xl145ucqevd55))/DataSerach/XSFWINFO.aspx'

print('\nPress Ctrl + C to exit.\n')

f = open(dataPath, "w+", encoding = 'utf-8')
while True:
	try:
		html = getHtml(targetUrl)

		htmlf = open(htmlPath, "wb+")
		htmlf.write(html)
		htmlf.close()

		linecache.updatecache(htmlPath)

		addLine = 0
		lineString = linecache.getline(htmlPath,11)
		pList = getInfo(lineString)
		if(pList == '<div>'):
			addLine = 2
		else:
			addLine = 0

		lineString = linecache.getline(htmlPath,18+addLine)
		DateTemp = getDate(lineString)
		if(Date != DateTemp):
			Date = 	DateTemp
			print('\n成交房屋信息: ' + Date + '\n')
			f.write('\n成交房屋信息: ' + Date + '\n')

		#姑苏
		lineString = linecache.getline(htmlPath,91+addLine)
		pList = getInfo(lineString)
		if(Number[0] != int(pList[1]) or Area[0] != float(pList[2]+'.'+pList[3])):
			Number[0] = int(pList[1])
			Area[0] = float(pList[2]+'.'+pList[3])
			print('GuSu Area: '+ str(Number[0]) + '\t' + str(Area[0]))
			f.write('姑苏区: ' + str(Number[0]) + '\t' + str(Area[0]) + '\n')	
			lineString = linecache.getline(htmlPath,93+addLine)
			pList = getInfo(lineString)
			Number[1] = int(pList[0])
			Area[1] = float(pList[1]+'.'+pList[2])
			print('其中住宅: ' + str(Number[1]) + '\t' + str(Area[1]) + '\n')
			f.write('其中住宅: ' + str(Number[1]) + '\t' + str(Area[1]) + '\n')

		#吴中
		lineString = linecache.getline(htmlPath,95+addLine)
		pList = getInfo(lineString)
		if(Number[2] != int(pList[1]) or Area[2] != float(pList[2]+'.'+pList[3])):
			Number[2] = int(pList[1])
			Area[2] = float(pList[2]+'.'+pList[3])
			print('WuZhong Area : '+ str(Number[2]) + '\t' + str(Area[2]))
			f.write('吴中区: ' + str(Number[2]) + '\t' + str(Area[2]) + '\n')	
			lineString = linecache.getline(htmlPath,97+addLine)
			pList = getInfo(lineString)
			Number[3] = int(pList[0])
			Area[3] = float(pList[1]+'.'+pList[2])
			print('其中住宅: ' + str(Number[3]) + '\t' + str(Area[3]) + '\n')
			f.write('其中住宅: ' + str(Number[3]) + '\t' + str(Area[3]) + '\n')

		linecache.clearcache()
		pass
	except KeyboardInterrupt:
		print('\nGood Bye!\n')
		f.close()
		break
		pass



#print(getInfo(html))



