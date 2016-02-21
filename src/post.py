#!/usr/bin/python3
import frontmatter
import os.path
from jinja2 import Environment, FileSystemLoader
import markdown2 as md
import server

def loadPost(filename):
  if not os.path.isfile(filename):
    print("Not a valid file")
    return []
  with open(filename) as f:
    post = frontmatter.load(f)
  return post
    
def renderPost(mdFile):
    post = loadPost(mdFile)
    body = md.markdown(post.content)
    
    outFile = "index.html"
    inputFile = "input.html"

    env = Environment(loader=FileSystemLoader(''))
    template = env.get_template("input.html")

    html = template.render(post=post, body=body)
    with open (outFile, "wb") as fh:
        fh.write(bytes(html,'UTF-8'))

renderPost('test.md')
server.serveAtPort(8000)

            
                
