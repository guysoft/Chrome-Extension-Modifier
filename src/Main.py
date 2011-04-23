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
import sys

CHROME_DEFAULT_PATH = "" #No Path
if os.name == "posix":
    CHROME_DEFAULT_PATH = "~/.config/google-chrome/Default/Extensions/" #linux path
    CHROME_DEFAULT_PATH = os.path.expanduser(CHROME_DEFAULT_PATH)
else: #windows path
    try:
        import windowsutils
        applicationData = windowsutils.getApplicationData()
        CHROME_DEFAULT_PATH = os.path.join(applicationData,"Google\Chrome\User Data\Default\Extensions")
    except:
        print "This is not a posix, nor is it windowsXP, not sure what OS this is"

    
class framelogic(gui.MyFrame):
    '''
    All the logical operations of the GUI
    '''
    def __init__(self, *args, **kwds):
        gui.MyFrame.__init__(self, *args, **kwds)
        logoPath = os.path.join(self.getRunPath(),"Chromium_11_Logo.png")
        self.bitmap_1.SetBitmap(wx.Bitmap(logoPath,wx.BITMAP_TYPE_ANY))
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
        
    def getRunPath(self):
        '''
        Get the path of where we are running
        '''
        print 'sys.argv[0] =', sys.argv[0]      # script name   (for testing)
        print 'os.getcwd() =', os.getcwd()      # where we are  (for testing)
        
        return os.path.dirname(sys.argv[0])

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
        
