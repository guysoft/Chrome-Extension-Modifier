#!/usr/bin/python
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

Created on Apr 7, 2011

@author: Guy Sheffer <guysoft@gmail.com>
'''
import wx

import gui

import TweetDeckRTL
import os
import os.path

CHROME_DEFAULT_PATH = "windows path" #windwos path
if os.name == "posix":
    CHROME_DEFAULT_PATH = "~/.config/google-chrome/Default/Extensions/" #linux path
    CHROME_DEFAULT_PATH = os.path.expanduser(CHROME_DEFAULT_PATH)
    
class framelogic(gui.MyFrame):
    '''
    All the logical operations of the GUI
    '''
    def __init__(self, *args, **kwds):
        gui.MyFrame.__init__(self, *args, **kwds)
        self.TXTInput.SetValue(CHROME_DEFAULT_PATH)
        return
    
    def CMDcommit(self,event):
        #replace here for new modules!
        a = TweetDeckRTL.TweetDeckRTL(self.getDirPath(),self.info)
        a.patch()
        return
    
    def Select_input(self,event):
        selection = wx.DirDialog(self,"Select Chrome's extension folder")
        selection.SetPath(self.getDirPath())
        if selection.ShowModal() == wx.ID_OK :
            self.TXTInput.SetValue(selection.GetPath())
        return
    def getDirPath(self):
        '''
        Get the Chrome extension folder
        '''
        return self.TXTInput.GetValue()
    
    def info(self,message):
        self.LBLStatus.SetLabel(message)

class ChromeExtensionModifier(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        app = wx.PySimpleApp()
        wx.InitAllImageHandlers()
        frame = framelogic(None, -1, "")
        
        app.SetTopWindow(frame)
        
        
        frame.Show()
        app.MainLoop()
if __name__ == '__main__':
    a = ChromeExtensionModifier()
        