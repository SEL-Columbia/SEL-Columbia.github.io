from bs4 import BeautifulSoup
from datetime import datetime

#make soup with publications file
soup = BeautifulSoup(open('test2.md'), 'html.parser')
#create array with each "row-fluid" div as a separate item
rf = soup.findAll(attrs={"class":"row-fluid"},recursive=True)

#create datetime object
today = datetime.today()
today_string = today.strftime('%Y-%m-%d')

#count of untitled posts
count_untitle = 0

#go through every element in list rf to make new post file
for div in rf:
    #print type(div)
    if(div.strong):
        title = str(div.strong)
        title = title[8:-9]
    else:
        count_untitle += 1
        title = "Untitled"+ str(count_untitle)

    #get title of the post
    post_title = title.replace(' ','-')


    #get link of publication
    #url = None
    if(div.a):
        a_tag = div.a.extract()
        #for a in soup.find_all('a',href=True):
        #    link = a['href']
        link = a_tag['href']
    #get the description of content
    description = None
    x = div.findAll(attrs={"class":"pubdescription"})
    if (x):
        #print ('here is the description')
        description = x[0].getText()
        #print description + '\n'

    # make a file for the post (YYYY-MM-DD-title.md)
    file_name = today_string + "-" + post_title + ".md"
    f = open(file_name,"w")

    # format YAML front matter
    # title, layout, images
    f.write('---\n')
    f.write('title: \''+title+'\'\n')
    f.write('layout: post\n')
    f.write('image: '+str(div.a)+'\n')
    f.write('link: "'+ link +'"\n')
    f.write('---\n')
    # TO DO- insert main text, link (or find a better place to put it)
    if(description!=None):
        try:
            description = description.encode("utf-8")
        except UnicodeError:
            description = unicode(description,"utf")
        else:
            pass
        f.write(str(description) + ' \n')
    f.close()
