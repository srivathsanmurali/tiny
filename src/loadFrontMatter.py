#!/usr/bin/python3
import frontmatter
import os.path
def loadPost(filename):
  if not os.path.isfile(filename):
    print("Not a valid file")
    return []
  with open(filename) as f:
    post = frontmatter.load(f)
  return post

post = loadPost("test.md")
print(post['Title'])
print(post['Author'])
print(post['Discription'])
print(post.content) 
