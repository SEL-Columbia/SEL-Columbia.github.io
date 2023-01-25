#!/usr/bin/python

import os
import re

PATH_TO_IMAGES_FOLDER = '../assets/uploads/'
PATH_TO_TEAM_POSTS = '../team/_posts/'

def replace_photo_path(path):
    pass
    

def change_team_photo_paths():
    pattern = re.compile('\/assets\/images\/([\w]+.(jpg|png))\n')
    for root, directory, files in os.walk(PATH_TO_TEAM_POSTS):
        for post in files:
            with open(root + post, 'r') as f:
                data = f.readlines()
                m = pattern.search(data[2])
                if m:
                    new_path = 'photo: /assets/uploads/team/' + m.group(1) + '\n'
                    print(new_path)
                    data[2] = new_path
                    
                    '''
            with open(root + post, 'w') as f:
                f.writelines(data)
                '''
if __name__ == '__main__':
    change_team_photo_paths()




