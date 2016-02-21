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
    
def renderPost(mdFile, htmlFile, htmlTemp):
    post = loadPost(mdFile)
    body = md.markdown(post.content)
    
    env = Environment(loader=FileSystemLoader(''))
    template = env.get_template(htmlTemp)

    html = template.render(post=post, body=body)
    with open (htmlFile, "wb") as fh:
        fh.write(bytes(html,'UTF-8'))

if __name__ == "__main__":
    renderPost('test.md','index.html','input.html')
    server.serveAtPort(8000)

            
                
