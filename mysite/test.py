#!/usr/bin/env python
# coding: utf-8

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
 
def main():
    from blog.models import Blog
    f = open('oldblog.txt')
     
    BlogList = []
    for line in f:
        parts = line.split('****')
        BlogList.append(Blog(title=parts[0], content=parts[1]))
     
    f.close()
         
    # BlogList = [Blog(title=line.split('****')[0], content=line.split('****')[1]) for line in f]
     
    Blog.objects.bulk_create(BlogList)
 
if __name__ == "__main__":
    main()
    print('Done!')
