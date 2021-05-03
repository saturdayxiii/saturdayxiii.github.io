'''move these 2 lines
to the first 2 lines
!/usr/bin/python
-*- coding: UTF-8 -*-'''
#all html showing up as a code block
#convert links to []() format
#youtube vids and media vids exist and need fixing
#group img thumbnails are probably different
import os,re,io
directory = os.listdir('../../Sync/posts/html')
os.chdir('../../Sync/posts/html')

for file in directory:
    print (file)
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
        #to do: make day always 2 digits pls
    reorder = [2,0,1]
    date = [date[i] for i in reorder]
    date = ''.join(date)
    #reformat
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
    #these have to go after month changes
    date = re.sub("th","-",date)
    date = re.sub("st","-",date)
    date = re.sub("nd","-",date)
    date = re.sub("rd","-",date)
    date = re.sub(",","",date)
    #shift h tags
    read_file = re.sub("<h2>","###",read_file)
    read_file = re.sub("</h2>","###",read_file)
    read_file = re.sub("<h1>","##",read_file)
    read_file = re.sub("</h1>","##",read_file)
    #fix img urls
    #first get filname
    #images = re.findall('<img src="../../(.+)"', read_file)
    #this shouldn't be necessary... try fixing html first
    #
    read_file = re.sub('<img src="\.\./\.\./','<img src="https://saturdayxiii.github.io/',read_file)
    #gifs are different, see kvass post
    #fix video urls.  Do they need it? Yes.
    #read_file = re.sub('<iframe.*v=', 'embed/', read_file)
    #?feature=oembed&amp;enablejsapi=1&amp;origin=http://safe.txmblr.com&amp;wmode=opaque"
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
    no_punc = re.sub('[^\u0000-\u00af]',' ',no_punc)
    no_punc = re.sub(" ","-",no_punc)
    date += no_punc
    #date is now title I guess
    #make a summary
    summ1 = re.findall('<p>(\w.{0,150}).*?</', read_file)#why doesn't non greedy modifier do anything???
    summ1 = ''.join(summ1)
    summ = ""
    for char in summ1:
        if char not in punc:
            summ = summ + char
    #print date
    #print summ
    # make tag list and generate frontmatter
    tags = re.findall('tag">(\w*)<', read_file)
    tags = '"' + '", "'.join(tags)
    #delete html bits
    head = re.match('^.*<body>\s+',read_file, re.DOTALL)
    read_file = re.sub(head.group(0),"",read_file)
    foot = re.match('^.*(<div id="footer">.*$)',read_file, re.DOTALL)
    read_file = re.sub(foot.group(1),"",read_file)
    newlines = ["<p></p>", "<p>", "</p>"]
    for new in newlines:
        read_file = re.sub(new, '\n', read_file)
    erases = ['<div>', '</div>', '####'] # '####' needs to be before html for html to work, we'll add it later.
    for erase in erases:
        read_file = re.sub(erase, '', read_file)
    codebit = re.compile('<div class=".*">')
    read_file = re.sub(codebit, '', read_file)
    #add front matter
    fmatt = "---\ntype: " + post + "\ntimestamp: " + time + "\ntags: [" + tags + '"]\n---\n'
    read_file = fmatt + "####\n" + read_file + "\n" + source
    #tumblrs better without titles and summaries?
    #"\ntitle: " + no_punc +
    #"\nsummary: " + summ + 
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

