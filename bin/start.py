#!/usr/bin/env python
#coding:utf-8

import os
os.sys.path.insert(0,os.getcwd())
import pydash

if __name__ == '__main__':
    from pprint import pprint
    options={}
    options['port']=80
    options['project_path']=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    options['static_path'] = options['project_path']+'/static'
    options['template_path'] = options['project_path']+'/jade'
    pprint(options)
    
    pydash.start_server(options)