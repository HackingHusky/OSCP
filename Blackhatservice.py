# install: "pip install pywin32 wmi pyinstaller" first

import os
import servicemanager
import shutil
import subprocess
import sys

import win32event
import win32service
import win32serviceutil

SRCDIR = 'C:\\User\\"localuser"\\"folderpath"' # subject to change, remove qoutes 
TGTDIR = 'C:\\Windows\\TEMP' 

class BHServerSvc(win32serviceutil.ServiceFramework):
    _svc_name_ = "BlackHatService"
    _svc_display_name = "Nelson: HA-HA!"
    _svc_description_ = ("Windows esculation: Executes VBScripts" + "What could possibly go wrong!")
    
def_init_(self,args):
    self.vbs = os.path.join(TGTDIR, 'bhservice_task.vbs')
    salf.timeout = 1000 * 60 
    
    win32serviceutil.ServiceFramework._init_(self, args)
    self.hWaitStop = win32eventCreateEvent(None, 0, 0, None)
    
def SvCStop(self):
    self.ReportServiceStatus(win32serivce.SERVICE_STOP_PENDING)
    win32event.SetEvent(self.hWaitStop)
    
def SvcDoRun(self):
    self.ReportServiceStatus(win32serivce.SERVICE_RUNNING)
    self.main()
    
    def main(self):
        while True:
            ret_code = win32event.WaitForSingleObject(
            self.hWaitStop, self.timeout)
            if ret_code == win32event.WAIT_OBJECT_O:
                servicemanager.LogInfoMessage("Service is stopping")
                break
            
            src = os.path.join(SRCDIR, 'bhservice_task.vbs')
            shutil.copy(src, self.vbs)
            subprocess.call("cscript.exe %s" % self.vbs, shell=False)
            os.unlink(self.vbs)
            
    if_name_ == '_main_':
        if len(sys.argv) == 1:
            servicemanager.Initialize()
            servicemanager.PrepareToHostSingle(BHServerSvc)
            servicemanager.StartServiceCtrDispatcher()
            
        else:
            win32serviceutil.HandleCommandLine(BHServerSvc)
            
            
            
            
# place this in the path you want to use
# then create the service in the folder path you want to use: pyinstaller -F --hiddenimport win32timezone bhservice.pyinstaller
# then install: bhservice.exe install
# then run: bhservice.exe startswith


#this will run every minute until you stop but do the stop command

# stop command: bhservice.exe stop