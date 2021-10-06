'''move these 2 lines
to the first 2 lines
!/usr/bin/python
-*- coding: UTF-8 -*-'''
#links
media = "https://saturdayxiii.github.io/media"
tumblr = "https://saturdayxiii.tumblr.com/"
#all html showing up as a code block
#convert links to []() format
import os,re,io
directory = os.listdir('../../Sync/posts/html')
os.chdir('../../Sync/posts/html')

for file in directory:
    print (file)
    
    #linkback to source
    iden = file[:-5]
    source = tumblr + "post/"  + iden
    sourcelink = "<small>source: [" + source + "](" + source + ")</small>"
    
    #now edit file
    with io.open(file,'r',encoding='utf8') as open_file:
        read_file = open_file.read()
    #link posts need to be manually repaired apparently
    #print(re.search(r'href\.li/',read_file)) DONE found them all
    
    #convert time stamp to potential filename
    date = re.findall('timestamp"> (.*) <', read_file)
    date = ''.join(date)
    time = date #preserve timestamp in front matter
    date = date.split(' ')
    del date[3]
    reorder = [2,0,1]
    date = [date[i] for i in reorder]
    date = '-'.join(date)
   #reformat
    datest = ['-January-', '-1st']
    for st in datest:
        date = re.sub(st,"-01-",date)
    datest = ['-February-', '-2nd']
    for st in datest:
        date = re.sub(st,"-02-",date)
    datest = ['-March-', '-3rd']
    for st in datest:
        date = re.sub(st,"-03-",date)
    datest = ['-April-', '-4th']
    for st in datest:
        date = re.sub(st,"-04-",date)
    datest = ['-May-', '-5th']
    for st in datest:
        date = re.sub(st,"-05-",date)
    datest = ['-June-', '-6th']
    for st in datest:
        date = re.sub(st,"-06-",date)
    datest = ['-July-', '-7th']
    for st in datest:
        date = re.sub(st,"-07-",date)
    datest = ['-August-', '-8th']
    for st in datest:
        date = re.sub(st,"-06-",date)
    datest = ['-September-', '-9th']
    for st in datest:
        date = re.sub(st,"-09-",date)
    date = re.sub("-October-","-10-",date)
    date = re.sub("-November-","-11-",date)
    date = re.sub("-December-","-12-",date)
    #these have to go after month changes
    ths = ['st', 'nd', 'rd', 'th']
    for th in ths:
        date = re.sub(th,"-",date)
    date = re.sub(",","",date)
    
    # make tag list
    tags = re.findall('tag">(\w*)<', read_file)
    
    #delete header then footer
    head = re.compile ('^.*<body>\s+', flags=re.S)
    read_file = re.sub(head, "", read_file)
    foot = re.compile('\s*<div id="footer.*$', flags=re.S)
    read_file = re.sub(foot,'',read_file)
    #I think this has to happen here
    #read_file = re.sub(r'^<p>\n\s*','',read_file)

#any titles, hopefully no more than one
    h1 = re.findall(r'<h1>(.+)</h1>',read_file)
    h1 = ''.join(h1)
#get rid of empty headers, yeesh
    yeesh = ['<h1>.*</h1>','<h2></h2>']
    for eesh in yeesh:
        read_file = re.sub(eesh,'',read_file)

#identify post type and add to front matter, pics, vids, quotes, text, link, audio... maybe no chat
    post = ""
    '''
#Do these matter?  tags might have all info.
    if re.search("^<img",read_file):
        post = "art"
    if re.search("^<iframe",read_file):
        post = "tainment"
    if re.search('^<figure class="tmblr-full tmblr-embed"',read_file):
        post = "tainment"
    if re.search('body>\s*##  ##\s*<figure class="tmblr-full tmblr-embed"', read_file):
        post = "tainment"
        '''
    #lower tag case and reapply post type
    for tag in tags:
        tag = tag.lower()
        if tag == "food":
            post = "food"
        if tag == "edible":
            post = "food"
            tags.append("food")
        if tag == "music":
            post = "snd"
        if tag == "game":
            post = "tainment"
        if tag == "movie":
            post = "tainment"
        if tag == "show":
            post = "tainment"
        if tag == "art":
            post = "art"
        if tag == "photo":
            post = "art"
        if tag == "photography":
            post = "art"
            tags.append("art")
        if tag == "thoughts":
            post = "me"
            tags.append("personal")
        if tag == "personal":
            post = "me"
        if tag == "update":
            post = "me"
    tags = '"' + '", "'.join(tags)

#fix img urls, starting with tumblrs broken numbering system
    imgns = re.findall(r'<img.+\/(\d+_\d+)\.\w', read_file)
    #print ("imgns")
    #print(imgns)
    newimgns = []
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
        #read_file = re.sub(imgno, imgna, read_file) wtf i can't get 10 to stay 9 fuckit
        newimgns.append(imgna)
    #print ("newigmns")
    #print(newimgns)
    for newimg in imgns:
        #print (newimg)
        read_file = re.sub(newimg, newimgns[0], read_file)
        #print (newimgns[0])
        del newimgns[0]
    #Still can't get 10 to stay 9...just gonna resub it hardstyle
    read_file = re.sub('_00','_09',read_file)  #pls dont break things, i beg
    imgns = re.findall(r'<img.+\/(\d+_\d+)\.\w', read_file)

#tumblr isn't properly exporting these links, but they work anyway, for now:
    print( re.search('<figure class="tmblr-full" data-orig-height=".*/.*/(.*)" data', read_file))

#let's gallery-ize instead, later, nearer to frontmatter #lets table-ize groups of images
    read_file = re.sub('<img src="\.\./\.\./','<img src="https://saturdayxiii.github.io/',read_file)
    #fix video urls.
    read_file = re.sub('\s*<figure class([^>])*youtube.com.*?=([a-zA-Z0-9\-\_]+)[^>]*.*figure>','[![thumbnail](http://i3.ytimg.com/vi/\g<2>/hqdefault.jpg)](https://www.youtube.com/watch?v=\g<2>)',read_file)
    read_file = re.sub('\s*<iframe w([^>])*youtube.com/embed/([a-zA-Z0-9\-\_]+)[^>]*.*iframe>','[![thumbnail](http://i3.ytimg.com/vi/\g<2>/hqdefault.jpg)](https://www.youtube.com/watch?v=\g<2>)',read_file)
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
        read_file = re.sub('<embed src.*" type="vid.*', '', read_file)
    if not mp4:
        mp4 = ""
        
    #don't forget audio
    #this works for bandcamp. soundcloud is probably different
    snd = re.findall('<embed type="audio\/mpeg" src="(.*)">', read_file)
    if snd:
        snd = ''.join(snd)
        read_file = re.sub('<embed type="audio.*', '', read_file)
    if not snd:
        snd = ""
    #print(snd)
        
# add images to front matter
    image = ""
    link = ""
    oimgs = re.findall('<img src="(.*?)"', read_file)
    read_file = re.sub('<img src=.*?/>','',read_file) #hmm. maybe messy
    #read_file = re.sub('/>','',read_file) #not bad, if that's it
    ntub = re.findall('^.*\)\]\(?(http.*)?\)', read_file)#that's markdown links... only youtube thumbnails use it at this point.
    if not ntub:
        ntub = oimgs
    if not oimgs:
        oimgs = re.findall('^\[\!\[thumbnail\]\((http.*)?\)\]', read_file)
    if len(oimgs) == 1:
        image = ''.join(oimgs)
        link = ''.join(ntub)
        read_file = re.sub('^.*\n', '', read_file)
    gallery = 'gallery:'
    #cont directly in frontmatter
    
    #convert regular links to markdown
    read_file = re.sub (r'<a href="(.*?)".*?>(.+?)</a>','[\g<2>](\g<1>)',read_file)
    #read_file = re.sub('\s*<iframe w([^>])*youtube.com/embed/([a-zA-Z0-9\-\_]+)[^>]*.*iframe>','[![thumbnail](http://i3.ytimg.com/vi/\g<2>/hqdefault.jpg)](https://www.youtube.com/watch?v=\g<2>)',read_file)
    
    #correct chars
    regex = re.compile(r'&rsquo;')
    read_file = regex.sub('\'', read_file)
    read_file = re.sub(r"&lsquo;","'",read_file)
    read_file = re.sub("\xe2\x80\x99","'",read_file)
    read_file = re.sub("&ldquo;",'"',read_file)#adding these quotes replacements
    read_file = re.sub("&rdquo;",'"',read_file)#suddenly added / to quotes... what...  non-ascii is visible when "print"-ed.
    read_file = re.sub("&gt;",">",read_file)
    #replace chars
    read_file = re.sub(r'<i>','*',read_file) #italics
    read_file = re.sub(r'</i>','*',read_file)
    read_file = re.sub(r'<b>','**',read_file) #bolds
    read_file = re.sub(r'</b>','**',read_file)
    #shift h tags
    read_file = re.sub("<h2>(.+)</h2>","### \g<1> ###\n",read_file)
    #read_file = re.sub("</h2>"," ###",read_file)
    read_file = re.sub("<h1>(.+)</h1>","## \g<1> ##\n",read_file)
    
    read_file = re.sub('^(<p>(.|\n)*?)(\w{2,})','\g<3>',read_file)
    cleanup = ['\s*<div class="caption"><p>','\s*<div class="caption">','\s*class="caption"><p>','^div','<figure.*?</figure>','<h2></h2>','</p>\s*?</div>','\xc2\xa0']
    for up in cleanup:
        read_file = re.sub(up,'',read_file)
    dnewlines = ['</p>\s*<p>','</p>;\s*<p>','\n\n\n']
    for dewl in dnewlines:
        read_file = re.sub(dewl,'\n\n',read_file)
    newlines = ['<br/>','\s*</p>']
    for ewl in newlines:
        read_file = re.sub(ewl,'\n',read_file)
    andyet = ['\s*<p>\s*']
    for yet in andyet:
        read_file = re.sub(yet,'',read_file)

    #find and flag instagram posts
    #print(re.search('instagram.com', read_file)) DONE WITH THAT
        
    #get title
    if not h1:
        h1 = re.findall('^(.{1,200})', read_file)#why doesn't non greedy modifier do anything???
        h1 = ''.join(h1)
        h1 = re.sub('\]\(.*\)','',h1)
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_=~`'''
    no_punc = ""
    for char in h1:
        if char not in punc:
            no_punc = no_punc + char
    no_punc = re.sub('[^\u0000-\u00af]',' ',no_punc)
    noneofthis = ['p\s*$', 'http','href','thumbnail']
    for this in noneofthis:
        no_punc = re.sub('this','',no_punc)
    no_punc = (no_punc[:30])
    orthis = ['p\s+$','\s+\w$']
    for this in orthis:
        no_punc = re.sub(this,'',no_punc)
    if no_punc == '':
        no_punc = "NT"
    date += no_punc
    date = re.sub('\s+','-',date)
    #date = re.sub(" ","-",date)
    print (date)
    #date is now title I guess
    
    #make a summary WAIT!  We don't need it no more
    '''summ2 = re.findall('(.{1,145})', read_file)#why doesn't non greedy modifier do anything???
    summ2 = ''.join(summ2)
    summ2 = re.sub('(\[.*\])','',summ2)
    summ2 = re.sub('(http.*?)<','',summ2)
    summ2 = re.sub('(<.*?>)',' ',summ2)
    summsubs = ['\xa0','-&gt','||   |  |','|   |  |','|   |','|     ','    ','##','|']
    for subs in summsubs:
        summ2 = re.sub(subs,'',summ2)
    summ = (summ2[:137] + '...') if len(summ2) > 140 else summ2
    print (summ)'''
    
    #add front matter
    fmatt = '---\nlayout: post\ntitle: "' + no_punc + '"\ntype: ' + post + '\ntimestamp: ' + time + '\naudio: ' + snd + '\nvideo: ' + mp4 + '\nimage: ' + image + '\nlink: ' + link
    if len(oimgs) >1:
        image = oimgs[0]
        link = oimgs[0]
        del oimgs[0]
        fmatt = "---\nlayout: post\ntitle: " + no_punc + "\ntype: " + post + "\ntimestamp: " + time + "\naudio: " + snd + "\nvideo: " + mp4 + "\nimage: " + image + "\nlink: " + link
        for i in oimgs:
            gallery = gallery + '\n  - title: \n    gimage: ' + i + '\n    url: ' + i
        fmatt = fmatt + "\n" + gallery
    fmatt = fmatt + "\ntags: [" + tags + '"]\ncomments: true\n---'
    #print (fmatt)
    read_file = fmatt + "\n" + read_file + "\n" + sourcelink
    print (read_file)
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

    with io.open(date,'w', encoding='utf8') as write_file:
        write_file.write(read_file)
    #break

