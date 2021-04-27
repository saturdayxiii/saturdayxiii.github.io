'''move these 2 lines
to the first 2 lines
!/usr/bin/python
 -*- coding: UTF-8 -*-'''
import os,re,io
directory = os.listdir('html')
os.chdir('html')

for file in directory:
	print file
	#linkback to source
	iden = file[:-5]
	source = "<small>source: https://saturdayxiii.tumblr.com/post/" + iden + "</small>"
	#now edit file
	#open_file = open(file,'r')#easy way, but
	with io.open(file,'r',encoding='utf8') as open_file:
		read_file = open_file.read()
	#convert time stamp to potential filename
	date = re.findall('timestamp"> (.*) <', read_file)
	#convert to string
	date = ''.join(date)
	time = date #preserve timestamp in front matter
	date = date.split(' ')
	del date[3]
	reorder = [2,0,1]
	date = [date[i] for i in reorder]
	date = ''.join(date)
	#reformat
	date = re.sub("th","-",date)
	date = re.sub("st","-",date)
	date = re.sub("nd","-",date)
	date = re.sub("rd","-",date)
	date = re.sub(",","",date)
	date = re.sub("January","-01-",date)
	date = re.sub("February","-02-",date)
	date = re.sub("March","-03-",date)
	date = re.sub("April","-04-",date)
	date = re.sub("May","-05-",date)
	date = re.sub("June","-06-",date)
	date = re.sub("July","-07-",date)
	date = re.sub("August","-08-",date)
	date = re.sub("September","-09-",date)
	date = re.sub("October","-10-",date)
	date = re.sub("November","-11-",date)
	date = re.sub("December","-12-",date)
	#shift h tags
	read_file = re.sub("<h2>","<h3>",read_file)
	read_file = re.sub("</h2>","</h3>",read_file)
	read_file = re.sub("<h1>","<h2>",read_file)
	read_file = re.sub("</h1>","</h2>",read_file)
	#fix img urls
	#temp fix to new directory, bah
	read_file = re.sub('<img src="../../','<img src="../',read_file)
	#fix video urls.  Do they need it?
	#identify post type and add to front matter, pics, vids, quotes, text, link, audio... maybe no chat
	post = "post"
	if re.search("body>\s*<img",read_file):
		post = "img"
	if re.search("body>\s*<iframe",read_file):
		post = "vid"
	#replace chars
	regex = re.compile('&rsquo;')
	read_file = regex.sub('\'', read_file)
	read_file = re.sub("\xe2\x80\x99","'",read_file)
	read_file = re.sub("\xc2\xa0","",read_file)
	read_file = re.sub("&ldquo;",'"',read_file)#adding these quotes replacements
	read_file = re.sub("&rdquo;",'"',read_file)#suddenly added / to quotes... what...  non-ascii is visible when "print"-ed.
	#get title - do after text corrections, but before html remove
	title = re.findall('<p>(\w.{0,25}).*<', read_file)
	title = ''.join(title)
	punc = '''!()-[]{};:'"\,<>./?@#$%^&*_=~`'''
	no_punc = ""
	for char in title:
		if char not in punc:
			no_punc = no_punc + char
	no_punc = re.sub('[^\u0000-\u007f]',' ',no_punc)
	no_punc = re.sub(" ","-",no_punc)
	date += no_punc
	#date is now title I guess
	#make a summary
	summ = re.findall('<p>(\w.{0,150}).*?</', read_file)#why doesn't non greedy modifier do anything???
	summ = ''.join(summ)
	#print date
	#print summ
	# make tag list and generate frontmatter
	tags = re.findall('tag">(\w*)<', read_file)
	tags = '"' + '", "'.join(tags)
	#delete html but preserve <h> and <p>?
	#how?
	#remove footer/head is easy I guess.
	head = re.match('^.*<body>',read_file, re.DOTALL)
	read_file = re.sub(head.group(0),"",read_file)
	foot = re.match('^.*(<div id="footer">.*$)',read_file, re.DOTALL)
	read_file = re.sub(foot.group(1),"",read_file)
	#add front matter
	fmatt = "---\ntype: " + post + "\ntitle: " + no_punc + "\ntimestamp: " + time + "\nsummary: " + summ + "\ntags: [" + tags + '"]\n---\n'
	read_file = fmatt + read_file + "\n" + source
	#
	'''#new file, new ext
	name, ext = file.split('.')
	nfile = '{}.{}'.format(name, 'md') '''
	#no need, just append .md
	md = '.md'
	date += md
	#write_file = open(date,'w')
	#write_file.write(read_file)
	#encoding? do this for "open_file" too
	with io.open(date,'w', encoding='utf8') as write_file:
		write_file.write(read_file)
	#break
