#!/usr/bin/python3
import yaml

def readYaml(filename):
  f = open(filename)
  data = yaml.safe_load(f)
  f.close()
  return data;

