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


def walkContents(folderLoc, configData):
  #print ([ name for name in os.listdir(folderLoc) if os.path.isdir(os.path.join(folderLoc, name)) ])
  print("Folder ", os.path.relpath(folderLoc, configData['content']) )
  # chking if the build folder exists
  # if else create it
  #if not os.path.exist(

  # walks the directory and renders the html files
  for name in os.listdir(folderLoc):
    if not os.path.isdir(os.path.join(folderLoc,name)):
      print (name)

  for name in os.listdir(folderLoc):
    if os.path.isdir(os.path.join(folderLoc,name)):#
      walkContents(os.path.join(folderLoc,name), configData)


if __name__ == "__main__":
  main()
