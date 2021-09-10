'''move these 2 lines
to the first 2 lines
!/usr/bin/python
-*- coding: UTF-8 -*-'''
#once this works, I have no plans to clean it up.
#media folder location
media = "https://saturdayxiii.github.com/media"
#all html showing up as a code block
#convert links to []() format
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
    #post needs to be manually repaired because its a link?
    #print(re.search(r'href\.li/',read_file)) DONE found them all
    #convert time stamp to potential filename
    date = re.findall('timestamp"> (.*) <', read_file)
    #convert to string
    date = ''.join(date)
    time = date #preserve timestamp in front matter
    date = date.split(' ')
    del date[3]
        #to do: make day always 2 digits pls
    singledays = ['1','2','3','4','5','6','7','8','9']
    #for days in singledays: if date[1] = days err... replace spot [1] with... "0" and "days"... but how to do that with array and strings?
    #for days in singledays: resub ^days$, 0days, date[2]? or something?
    
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
    read_file = re.sub("<h2>","### ",read_file)
    read_file = re.sub("</h2>"," ###",read_file)
    read_file = re.sub("<h1>","## ",read_file)
    read_file = re.sub("</h1>"," ##",read_file)
    #identify post type and add to front matter, pics, vids, quotes, text, link, audio... maybe no chat
    #more post types decided in tagging section
    post = ""
    if re.search("body>\s*<img",read_file):
        post = "img"
    if re.search("body>\s*<iframe",read_file):
        post = "vid"
    if re.search('body>\s*<figure class="tmblr-full tmblr-embed"',read_file):
        post = "vid"
    if re.search('body>\s*##  ##\s*<figure class="tmblr-full tmblr-embed"', read_file):
        post = "vid"
    if re.search('body>\s*##  ##\s*<p class="npf_link"', read_file):
        post = "lnk"
    #fix img urls, starting with tumblrs broken numbering system
    imgns = re.findall(r'<img.+\/(\d+_\d+)\.\w', read_file)
    for imgn in imgns:
        #split & math last number into imgnn then join
        imgno = imgn
        imgnss = imgn.split("_")
        imgnn = int(imgnss[1])
        imgnn = imgnn-1
        imgnn = str(imgnn)
        imgna = imgnss[0]
        imgna = str(imgna)
        imgna = imgna + "_" + imgnn
        read_file = re.sub(imgno, imgna, read_file)
    #first get filname
    #images = re.findall('<img src="../../(.+)"', read_file)
    #this shouldn't be necessary... try fixing html first. done.
    #tumblr isn't properly exporting these links, but they work anyway, for now:
    print( re.search('<figure class="tmblr-full" data-orig-height=".*/.*/(.*)" data', read_file))
    #lets table-ize groups of images
    threeimg = re.compile(r'\s*(<img.*?>)\s*?</p>\s*?<p>\s*?(<img.*?>)\s*?</p>\s*?<p>\s*?(<img.*?>)\s*?</p>\s*', flags=re.S)
    twoimg = re.compile(r'\s*(<img.*?>)\s*?</p>\s*?<p>\s*?(<img.*?>)\s*?</p>\s*', flags=re.S)
    oneimg = re.compile(r'\s*?<p>\s*?\n\s*?(<img.*?>)\s*?\n\s*?</p>\s*')
    read_file = re.sub(threeimg,'| \g<1> | \g<2> | \g<3> |\n',read_file)
    read_file = re.sub(twoimg,'| \g<1> | \g<2> |  |\n',read_file)
    read_file = re.sub(oneimg,'\n|  | \g<1> |  |\n', read_file)
    read_file = re.sub('<img src="\.\./\.\./','<img src="https://saturdayxiii.github.io/',read_file)
    #fix video urls.  
    read_file = re.sub('<figure class([^>])*youtube.com.*?=([a-zA-Z0-9\-\_]+)[^>]*','[![thumbnail](http://i3.ytimg.com/vi/\g<2>/hqdefault.jpg)](https://www.youtube.com/watch?v=\g<2>)',read_file)
    read_file = re.sub('<iframe w([^>])*youtube.com/embed/([a-zA-Z0-9\-\_]+)[^>]*','[![thumbnail](http://i3.ytimg.com/vi/\g<2>/hqdefault.jpg)](https://www.youtube.com/watch?v=\g<2>)',read_file)
    tubes = re.findall("http://i3\.ytimg\.com/vi/([a-zA-Z0-9\-\_]+)/hqdefault.jpg\)", read_file)
    for tube in tubes:
        yturl = "[![thumbnail](http://i3.ytimg.com/vi/" + tube + "/hqdefault.jpg)](https://www.youtube.com/watch?v=" + tube + ")"
        yturld = yturl + ">" + yturl + ">"
        read_file = re.sub(rf"{re.escape(yturld)}", yturl, read_file)
    #playlists are probably different, watchout
    #here's for embedded vids, but it won't work if more than one in post
    mp4 = re.findall('<embed src="\.\.\/\.\.\/media(.*)" type="vid.*', read_file)
    if mp4:
        mp4 = ''.join(mp4)
        mp4 = media + mp4
    if not mp4:
        mp4 = ""
    #replace chars
    regex = re.compile('&rsquo;')
    read_file = regex.sub('\'', read_file)
    read_file = re.sub("\xe2\x80\x99","'",read_file)
    read_file = re.sub("\xc2\xa0","",read_file)
    read_file = re.sub("&ldquo;",'"',read_file)#adding these quotes replacements
    read_file = re.sub("&rdquo;",'"',read_file)#suddenly added / to quotes... what...  non-ascii is visible when "print"-ed.
    #get title - do after text corrections, but before html remove
    titlelong = re.findall('<p>(\w.{0,25}).*?<', read_file)
    titlelong.append('')
    titleless = titlelong[0]
    title = ''.join(titleless)
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_=~`'''
    no_punc = ""
    for char in title:
        if char not in punc:
            no_punc = no_punc + char
    no_punc = re.sub('[^\u0000-\u00af]',' ',no_punc)
    no_punc = re.sub('p$','',no_punc)
    no_punc = re.sub('p $','',no_punc)
    no_punc = re.sub('http','',no_punc)
    no_punc = re.sub('href','',no_punc)
    date += no_punc
    date = re.sub(" ","-",date)
    if no_punc == '':
        no_punc = "NT"
    #print (no_punc)
    print (date)
    #date is now title I guess
    #make a summary WAIT!  We don't need it no more
    '''
    summ2 = re.findall('<p>(\w.{0,150}).*?</', read_file)#why doesn't non greedy modifier do anything???
    summ2.append('')
    summ1 = summ2[0]
    summ1 = ''.join(summ1)
    summ = ""
    for char in summ1:
        if char not in punc:
            summ = summ + char
    '''
    # make tag list and generate frontmatter
    tags = re.findall('tag">(\w*)<', read_file)
    #lower tag case and reapply post type
    for tag in tags:
        tag = tag.lower()
        if tag == "food":
            post = "food"
        if tag == "music":
            post = "audio"
        if tag == "game":
            post = "game"
        if tag == "movie":
            post = "vid"
        if tag == "show":
            post = "vid"
        if tag == "art":
            post = "img"
    tags = '"' + '", "'.join(tags)
    #delete html bits
    #head = re.match('^.*<body>\s+',read_file, re.DOTALL) #another random break, tho I'm surprised this line worked at all
    #read_file = re.sub(head.group(0),"",read_file)
    head = re.compile ('^.*<body>\s+', flags=re.S)
    read_file = re.sub(head, "", read_file)
    #foot = re.match('^.*(<div id="footer">.*$)',read_file, re.DOTALL)
    #print (foot)
    #read_file = re.sub(foot.group(1),"",read_file) #suddenly stopped working?
    replacefoot = re.compile('<div id="footer">[^\.]*$', flags=re.S)
    read_file = re.sub(replacefoot,'',read_file)
    newlines = ["<p></p>", "<p>", "</p>", "\n\s*\n", "\n\n\n", "\n\n"]
    for new in newlines:
        read_file = re.sub(new, '\n', read_file)
    erases = ['<div>', '</div>', '##  ##', '          ', '</figure>', '</iframe>', '</embed>']
    for erase in erases:
        read_file = re.sub(erase, '', read_file)
    codebit = re.compile('<div class=".*?">')
    read_file = re.sub(codebit, '', read_file)
    #find and flag instagram posts
    #print(re.search('instagram.com', read_file)) DONE WITH THAT
# add images to front matter
# ---
#<img src = *jpg gif png
# or [![thumbnail](http://i3.ytimg.com/vi/kpTdG4PkwXA/hqdefault.jpg)](https://www.youtube.com/watch?v=kpTdG4PkwXA)>
#but don't touch | <img... or \n | <img
    #print(re.search('^\|', read_file))
    #print(re.search('^\n\|', read_file)) #this doesn't necessarily mean it's only finding the first instance...
    #read_file = re.sub('^\n\|','howmanydoesthisdo',read_file) IT ONLY DID THE FIRST ONE YAY
    image = ""
    link = ""
    oimgs = re.findall('^<img src="(.*)?"', read_file)
    ntub = re.findall('^.*\)\]\(?(http.*)?\)', read_file)
    if not ntub:
        ntub = oimgs
    if not oimgs:
        oimgs = re.findall('^\[\!\[thumbnail\]\((http.*)?\)\]', read_file)
    if oimgs:
        image = ''.join(oimgs)
        link = ''.join(ntub)
        read_file = re.sub('^.*\n', '', read_file)
    
    #add front matter
    fmatt = "---\nlayout: post\ntitle: " + no_punc +"\ntype: " + post + "\ntimestamp: " + time + "\nvideo: " + mp4 + "\nimage: " + image + "\nlink: " + link + "\ntags: [" + tags + '"]\ncomments: true\n---'
    read_file = fmatt + "\n" + read_file + "\n" + source
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

