import sys
import os
from bs4 import BeautifulSoup

WRITE_DIRECTORY = '_posts'

counter = 30

def parse_child(child):
    title = child.find('h3').next
    title = title.strip()
    #print('Title is "%s"' % title)

    try:
        link_attributes = child.find('a').attrs
        #print('Attributes are {}'.format(link_attributes))
    except AttributeError:
        link_attributes = None
        #print("No link attributes")

    try:
        image_attributes = child.find('img').attrs
        #print("Image attrs are {}".format(image_attributes))
    except AttributeError:
        image_attributes = None
        #print("No images")

    content = child.find('div', {'class': 'col-md-8'})
    #print("Content is {}".format(content))

    make_post_file(title, link_attributes, image_attributes, content)
    

def make_post_file(title, link_attrs, img_attrs, content):
    global counter
    
    file_title = "-".join(title.lower().split())
    filename = "2015-12-{}-{}.md".format(counter, file_title)
    filepath = os.path.join(WRITE_DIRECTORY, filename)
    counter -= 1

    header_string = make_header(title, link_attrs, img_attrs)

    content_string = make_content(content)
    
    with open(filepath, "w") as f:
        f.write(header_string)
        f.write(content_string)


def make_header(title, link_attrs, img_attrs):
    header = ['---\n']
    
    if title:
        header.append("title: {}\n".format(title))
    if link_attrs:
        header.append("image-link: {}\n".format(link_attrs['href']))
    if img_attrs:
        header.append("image-source: {}\n".format(img_attrs['src']))

        try:
            header.append("image-alt: {}\n".format(img_attrs['alt']))
        except KeyError:
            image_alt = None

        try:
            header.append("image-height: {}\n".format(img_attrs['height']))
        except KeyError:
            image_height = None

        try:
            header.append("image-width: {}\n".format(img_attrs['width']))
        except KeyError:
            image_width = None

    header.append("---\n")

    return "".join(header)


def make_content(content):
    title = content.find('h3').next
    title = title.strip()

    content_strings = []

    content_strings.append("<h3>{}</h3>\n".format(title))
    
    for index, item in enumerate(content.children):
        if index == 2:
            content_strings.append("<p>{}</p>\n".format(item.encode('utf8').strip()))

    content_strings.append("{}\n".format(content.find('a')))

    return "".join(content_strings)


def main():
    with open("old_index.md", "r") as f:
        soup = BeautifulSoup(f, 'html.parser')
        for child in soup.children:
            if len(child) < 3:
                continue
            else:
                parse_child(child)

if __name__ == "__main__":
    main()
