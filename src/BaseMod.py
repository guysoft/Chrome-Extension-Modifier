#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Copyright © 2011 Guy Sheffer <guysoft@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

Created on Apr 22, 2011

@author: Guy Sheffer <guysoft@gmail.com>
'''

import os.path

class Template():
    def __init__(self,path,infoFunc):
        '''
        Init
        The path is the extention folder path,
        infoFunc is the GUI function for output information
        '''
        self.extensionId = ""
        self.path = path
        self.infofunc = infoFunc
        return
    
    '''
    This is a template Class that all patches should extend
    '''
    def patch(self):
        '''
        '''
        print "this is a test Patch"
        return
    
    def info(self,message):
        '''
        If you want to update the status use this function
        '''
        self.infofunc(message)
        
    def getExtensionPath(self):
        returnValue = os.path.join(self.path,self.extensionId)
        
        #get the only directory of this extension which is the last version
        returnValue = os.path.join(returnValue,os.listdir(returnValue)[0])
        
        return returnValue