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
TWEETDECK_ID  = "hbdpomandigafcibbmofojjchbcdagbl"
import BaseMod
import os.path
import shutil
import sys

class TweetDeckRTL(BaseMod.Template):
    '''
    This is the module that patches TweetDeckRTL to support RTL alignment
    '''
    def __init__(self,path,infoFunc):
        BaseMod.Template.__init__(self,path,infoFunc)
        self.extensionId = TWEETDECK_ID
        return

    def patch(self):
        LINE_TO_ADD = '<script src="../scripts/rtl.js"></script>\n'
            
        try:
            #this is where we patch the script line
            fileToPatch =  os.path.join(self.getExtensionPath(),"templates","default.html")
            
            print fileToPatch
            lastLine = file(fileToPatch, "r").readlines()[-1]
            
            if lastLine != LINE_TO_ADD and lastLine == "</html>\n":
                self.info("Patching TweetDeck")
                f = open(fileToPatch, 'a')
                f.write(LINE_TO_ADD)
                f.close()
                
                rtlScriptPath = os.path.join(self.getRunPath(),"rtl.js")
                
                rtlScriptDest = os.path.join(self.getExtensionPath(),"scripts")
                shutil.copy(rtlScriptPath,rtlScriptDest)
                self.info("TweetDeck patched successfully")
            else:
                self.info("Not patching TweetDeck,\nperhaps its already patched?")
        except:
            self.info("Error while attempting to patch, Have you selected the Chrome extension folder?")
        return
    
    def getRunPath(self):
        '''
        Get the path of where we are running
        '''
        print 'sys.argv[0] =', sys.argv[0]      # script name   (for testing)
        print 'os.getcwd() =', os.getcwd()      # where we are  (for testing)
        
        return os.path.dirname(sys.argv[0])