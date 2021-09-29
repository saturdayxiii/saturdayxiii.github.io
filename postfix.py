'''move these 2 lines
to the first 2 lines
!/usr/bin/python
-*- coding: UTF-8 -*-'''
#once this works, I have no plans to clean it up.
#media folder location
media = "https://saturdayxiii.github.io/media"
#all html showing up as a code block
#convert links to []() format
import os,re,io
directory = os.listdir('../../Sync/posts/_posts')
os.chdir('../../Sync/posts/_posts')

for file in directory:
    print (file)
    #open_file = open(file,'r')#easy way, but
    with io.open(file,'r',encoding='utf8') as open_file:
        read_file = open_file.read()
    read_file = re.sub('type: img', 'type: art', read_file)
    read_file = re.sub('type: vid', 'type: tainment', read_file)
    read_file = re.sub('type: lnk', 'type: me', read_file)
    read_file = re.sub('type: health', 'type: me', read_file)
    read_file = re.sub('type: personal', 'type: me', read_file)
    with io.open(file,'w', encoding='utf8') as write_file:
        write_file.write(read_file)
    #break


