#!/usr/bin/python3
import os
import sys 

import yamlread as yr
import post
import server

def main():
  print("Tiny Static Site Generator")
  if not os.path.isfile('config.yaml'):
    print ("Config.yaml Not found exiting")
    sys.exit(0);

  # config data from the yaml. basic 
  # meta data and directory strucuture
  # global config data
  configData = yr.readYaml('config.yaml')

  ## check if all the directories are presents
  if not os.path.exists(configData['content']):
    print ("content dir does not exist")
    sys.exit(0);
  
  if not os.path.exists(configData['layouts']):
    print ("layouts dir does not exist")
    sys.exit(0)

  #if output dir doesnt exist, it is created
  if not os.path.exists(configData['output']):
    print ("Creating build dir")
    os.makedirs(configData['output'])

  walkContents(configData['content'], configData)
  os.chdir(configData['output'])
  server.serveAtPort(8000)

def walkContents(folderLoc, configData):
  #print ([ name for name in os.listdir(folderLoc) if os.path.isdir(os.path.join(folderLoc, name)) ])
  print("Folder ", os.path.relpath(folderLoc, configData['content']) )
  # chking if the build folder exists
  # if else create it
  if not os.path.samefile(folderLoc, configData['content']):
    outputfolder = os.path.join(configData['output'], 
      os.path.relpath(folderLoc, configData['content']))
  else:
    outputfolder = configData['output']

  if not os.path.exists(outputfolder):
    os.makedirs(outputfolder)

  # walks the directory and renders the html files
  # need to make sure the files that rendered are md
  for name in os.listdir(folderLoc):
    if not os.path.isdir(os.path.join(folderLoc,name)):
      print (name)
      inputMd = os.path.join(folderLoc,name)
      htmlfile = os.path.splitext(name)[0] + '.html'
      outputHtml = outputfolder + '/' +  htmlfile
      template = os.path.join(configData['layouts'],'input.html')
      post.renderPost(inputMd, outputHtml,template)

  for name in os.listdir(folderLoc):
    if os.path.isdir(os.path.join(folderLoc,name)):#
      walkContents(os.path.join(folderLoc,name), configData)


if __name__ == "__main__":
  main()

