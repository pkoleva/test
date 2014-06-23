import org.sikuli.basics.SikuliXforJython
from sikuli import *
import unittest
from subprocess import call
import string


from Lib import ImageLibrary
from Lib import Common
from Common import *


addApp=False
addUser=False
addGroup=False

class EndToEndScenarios(unittest.TestCase):
    def test000_OpenStore(self):
               #open browser and load AppManager
        print("opening browser")
        addrBarresult=Common.OpenBrowser(ImageLibrary.common.browserName,ImageLibrary.common.addressBar,10)
        if(addrBarresult!=None):
#Navigate to URL
            print("Browser is opened, navigating to url")
            Common.typeInField(ImageLibrary.common.addressBar,ImageLibrary.common.baseURL)
            type(Key.ENTER)
            loggedInResult=Common.defineState(ImageLibrary.common.loginBtn,ImageLibrary.common.profilePicture,20)
        else:
            print("Browser not loaded")
            assert(1==0)
#Maximize browser and set zoom to 100%
        type("0", Key.CTRL)
        type(Key.UP,Key.WIN)
#         type("0", Key.META)
#         type("L",Key.META)
#LogIn
#         loggedInResult=Common.isUserLoggedIn()
        print(loggedInResult)
        if (loggedInResult==1):
            print("Try to log in")
            Common.LogIn(ImageLibrary.common.username,ImageLibrary.common.password)
            print("Successful log in " + repr(waitToLoad(ImageLibrary.common.profilePicture,10)))     
        elif(loggedInResult==2):
            print("User is already logged in")
        else:
            print("We are not on the correct page")
            assert(1==0)
#OpenStore
        print("Is Open AppManager button on the screen " + repr(exists(ImageLibrary.common.openAppManagerBtn)))
        print("Is Store opened " + repr(exists(ImageLibrary.common.appManagerTitle)))
        storeOpenedResult=Common.defineState(ImageLibrary.common.openAppManagerBtn,ImageLibrary.common.appManagerTitle,20)
        print(storeOpenedResult)
        if (storeOpenedResult==1):
            print("Opening AppManager")
            click(ImageLibrary.common.openAppManagerBtn)
            waitVanish(ImageLibrary.common.openAppManagerBtn)  
        elif(storeOpenedResult==2):
            print("AppManager is already opened")
        else:
            print("We are not on the correct page")
            assert(1==0)
#Accept EULA
        print("Is EULA on the screen " + repr(exists(ImageLibrary.common.acceptBtn)))
        print("Is getting started view on the screen " + repr(exists(ImageLibrary.common.getStartedBtn)))
        print("Is main view on the screen " + repr(exists(ImageLibrary.apps.addNewAppBtn)))
        eulaOnScreen=Common.defineState(ImageLibrary.common.acceptBtn,ImageLibrary.common.getStartedBtn,20)
        print(eulaOnScreen)
        if (eulaOnScreen==1):
            print("Accepting EULA")
            click(ImageLibrary.common.acceptBtn)
            waitVanish(ImageLibrary.common.acceptBtn)  
        elif(eulaOnScreen==2):
            print("Skip getting started")
            click(ImageLibrary.common.getStartedBtn)
            waitVanish(ImageLibrary.common.getStartedBtn)
            print("Passed the video")
            resgetAddAppBtn=waitToLoad(ImageLibrary.common.addAppBtn,10)
            print("Add App button image found on the screen " + repr(resgetAddAppBtn))
            if(exists(ImageLibrary.common.addAppBtn)):
                click(ImageLibrary.common.addAppBtn)
                waitVanish(ImageLibrary.common.addAppBtn)
                print("Clicked Add an App button")
            else:
                print("Either the store is opened or it is not created")
        else:
            if(exists(ImageLibrary.apps.addNewAppBtn)):
                print("Main view opened")
            else:
                print("We are not on the correct page")
                assert(1==0)
    def test001_OpenStore_InviteUser_CreateGroup_UploadApp(self):
        global addApp,addUser,addGroup
        if (not exists(ImageLibrary.common.appManagerTitle)):
            self.test000_OpenStore()
#Check if the AppManager is opened
        print("Is AppManager opened " + repr(exists(ImageLibrary.common.appManagerTitle)))
        print("App manager loaded after waiting" + repr(waitToLoad(ImageLibrary.common.appManagerTitle,10)))
#Invite a user
#Navigate to users view
        print("User menu found on the screen" + repr(waitToLoad(ImageLibrary.common.usersMenuItem,5)))
        click(ImageLibrary.common.usersMenuItem)
        print("Found users title " + repr(waitToLoad(ImageLibrary.users.usersTitle,5)))
#Inviting user
        print("Found invite User button " + repr(waitToLoad(ImageLibrary.users.inviteUserBtn,5)))
        inviteUser(ImageLibrary.users.userToInvite)
        resInvitedUserMsg=waitToLoad(ImageLibrary.common.actionDoneMessage,10)
#Invitation result
        if (resInvitedUserMsg== False):
            addUser=False
            print("user not invited")
        else:
            addUser=True
            print("user is invited")
#navigate to apps
        print("Is AppManager opened " + repr(exists(ImageLibrary.common.appManagerTitle)))
        click(ImageLibrary.common.appManagerTitle)
        waitToLoad(ImageLibrary.apps.addNewAppBtn,10)
#Add app
        print("Is the 'Add new app' button on the screen " + repr(exists(ImageLibrary.apps.addNewAppBtn)))
        if not(exists(ImageLibrary.apps.addNewAppBtn)):
            print("Add new app button is not on the screen,entering url to apps " + repr(ImageLibrary.apps.urlApps))
            typeInField(ImageLibrary.common.addressBar,ImageLibrary.apps.urlApps)
        else:
            print("Add new app button is found")
        click(ImageLibrary.apps.addNewAppBtn)
        waitToLoad(ImageLibrary.apps.addNewAppTitle,2)
        n=10
        while ((not exists(ImageLibrary.apps.okRsult)) and n>0):
            n -= 1
            if(addAnAppPackage(ImageLibrary.common.appToUploadAndroidValid)==None):
                print("Upload unsuccessful")
                if (deleteAnAppPackage()==1):
                    print("Deleted package")
                    waitToLoad(ImageLibrary.apps.packageField,2)
                else:
                    print("Refresh page")
                    type("r",KEY_CTRL)
                    waitToLoad(ImageLibrary.apps.packageField,10)
            else:
                break
        print ("Tried to upload an app " + repr(10-n) + " times")
        if (exists(ImageLibrary.apps.okRsult)!= None):
#             verifyFieldContent()
#Filling in the description
#if it is visible, if not, scroll down to it  
            click(Pattern(ImageLibrary.apps.addNewAppTitle).targetOffset(200,0))
            while(not(exists(ImageLibrary.apps.descriptionTitle))):
                type(Key.DOWN)
            typeInField(Pattern(ImageLibrary.apps.descriptionTitle).targetOffset(0,50),"slhaslkhda")
#Filling in distribution
#if it is not on the screen scroll down
            click(Pattern(ImageLibrary.apps.descriptionTitle).targetOffset(200,0))
            while(not(exists(ImageLibrary.apps.addAppBtn))):
                type(Key.DOWN)
            click(ImageLibrary.apps.addAppBtn)
#Verify result of adding app   
            resAddApp=waitToLoad(ImageLibrary.common.actionDoneMessage,10)
            if (resAddApp==True):
                print("App added")
                addApp= True
                waitToLoad(ImageLibrary.apps.addNewAppBtn,5)
            else:
                addApp= False
                res=exists(ImageLibrary.common.errorMessage)
                print("App not added. Error occured " + repr(res))
#Navigate to groups
        print("Is AppManager opened " + repr(exists(ImageLibrary.common.appManagerTitle)))
        click(ImageLibrary.common.appManagerTitle)
        waitToLoad(ImageLibrary.groups.groupsMenuItem,5)
        click(ImageLibrary.groups.groupsMenuItem)
        print("Is add group btn on the screen " + repr(exists(ImageLibrary.groups.addNewGroupBtn)))    
#Add new group
        waitToLoad(ImageLibrary.groups.addNewGroupBtn,10)
        click(ImageLibrary.groups.addNewGroupBtn)
        print("Opened add group view " + repr(waitToLoad(ImageLibrary.groups.addGroupTitle,10)))
        typeInField(ImageLibrary.groups.groupNameField,"New Group")
#Select members of the group
        a=find(ImageLibrary.groups.findUsersField).below(100)
        typeInField(ImageLibrary.groups.findUsersField,"Delete")
        b=a.find(ImageLibrary.common.checkbox)
        click(b)
#Select apps in groups
        a=find(ImageLibrary.groups.findAppsField).below(100)
        typeInField(ImageLibrary.groups.findAppsField,"Barcode")
        b=a.find(ImageLibrary.common.checkbox)
        click(b)
        click(ImageLibrary.groups.addGroupBtn)
        resAddApp=waitToLoad(ImageLibrary.common.actionDoneMessage,10)
        if (resAddApp==True):
            addGroup=True
            print("Group added")
            waitToLoad(ImageLibrary.groups.addNewGroupBtn,5)
        else:
            addGroup=False
            res=exists(ImageLibrary.common.errorMessage)
            print("Group not added. Error occured " + repr(res))
        print("Overall result added user " + repr(addUser) + ", added app " + repr(addApp) + ", added group " + repr(addGroup))
        assert((addUser==True) and (addApp==True) and (addGroup==True))
#Delete created items
    def test002_DeleteCreatedItems(self):
        global addApp,addUser,addGroup
        if (not exists(ImageLibrary.common.appManagerTitle)):
            self.test000_OpenStore()
        print("Is AppManager opened " + repr(exists(ImageLibrary.common.appManagerTitle)))
        print("Added app successfully " + repr(addApp) + ", added user successfully " + repr(addUser) + 
              ", added group successfully " + repr(addGroup))
        if(addApp==True):
            print("Deleting app")
#Navigating to apps
            print("Is AppManager opened " + repr(exists(ImageLibrary.common.appManagerTitle)))
            click(ImageLibrary.common.appManagerTitle)
            waitToLoad(ImageLibrary.common.findField,10)
#Deleting app
            typeInField(ImageLibrary.common.findField,"Accelerometer")
            click(ImageLibrary.common.checkbox)
            click(ImageLibrary.common.deleteBtn)
            waitToLoad(ImageLibrary.common.deletePopUpBtn,5)
            click(ImageLibrary.common.deletePopUpBtn)
#Verify result of deleting app   
            resDelApp=waitToLoad(ImageLibrary.common.actionDoneMessage,10)
            if (resDelApp==True):
                delApp=True
                print("App deleted")
            else:
                delApp=False
                res=exists(ImageLibrary.common.errorMessage)
                print("App not deleted. Error occured " + repr(res))
        else:
            delApp=False
            print("No need to delete an app")

        if(addUser==True):
            print("Deleting user")
#Navigating to users
            print("User menu found on the screen" + repr(waitToLoad(ImageLibrary.common.usersMenuItem,5)))
            click(ImageLibrary.common.usersMenuItem)
            waitToLoad(ImageLibrary.common.findField,5)
#Deleting user
            typeInField(ImageLibrary.common.findField,"Tam")
            click(ImageLibrary.common.checkbox)
            click(ImageLibrary.common.deleteBtn)
            waitToLoad(ImageLibrary.common.deletePopUpBtn,5)
            click(ImageLibrary.common.deletePopUpBtn)
#Verify result of deleting user 
            resDelUser=waitToLoad(ImageLibrary.common.actionDoneMessage,10)
            if (resDelUser==True):
                delUser=True
                print("User deleted")
            else:
                delUser=False
                res=exists(ImageLibrary.common.errorMessage)
                print("User not deleted. Error occured " + repr(res))
        else:
            delUser=False
            print("No need to delete a user")
        if(addGroup==True):
            print("Deleting group")
#Navigate to groups
            print("User menu found on the screen" + repr(waitToLoad(ImageLibrary.groups.groupsMenuItem,5)))        
            click(ImageLibrary.groups.groupsMenuItem)
            waitToLoad(ImageLibrary.common.findField,10) 
#Add new group
            typeInField(ImageLibrary.common.findField,"New")
            click(ImageLibrary.common.checkbox)
            click(ImageLibrary.common.deleteBtn)
            waitToLoad(ImageLibrary.common.deletePopUpBtn,5)
            click(ImageLibrary.common.deletePopUpBtn)
#Verify result of deleting user 
            resDelGroup=waitToLoad(ImageLibrary.common.actionDoneMessage,10)
            if (resDelGroup==True):
                delGroup=True
                print("Group deleted")
            else:
                delGroup=False
                res=exists(ImageLibrary.common.errorMessage)
                print("Group not deleted. Error occured " + repr(res))
        else:
            delGroup=False
            print("No need to delete a group")
        assert((addApp==delApp) and (addUser==delUser) and (addGroup==delGroup))
    def test003_PublishAppAndManageGroups(self):
        if (not exists(ImageLibrary.common.appManagerTitle)):
            self.test000_OpenStore()
#Navigate to groups
        print("Is AppManager opened " + repr(exists(ImageLibrary.common.appManagerTitle)))
        click(ImageLibrary.common.appManagerTitle)
        waitToLoad(ImageLibrary.groups.groupsMenuItem,5)
        click(ImageLibrary.groups.groupsMenuItem)
        print("Is add group btn on the screen " + repr(exists(ImageLibrary.groups.addNewGroupBtn)))
#Find group and select it for editing
        typeInField(ImageLibrary.groups.findGroupSearchbox, "Def")
        click(ImageLibrary.common.checkbox)
        wait(ImageLibrary.common.editBtn,2)
        click(ImageLibrary.common.editBtn)
#Edit group
        waitVanish(ImageLibrary.common.editBtn)
        typeInField(ImageLibrary.groups.findUsersField,"Delete")
        click(ImageLibrary.groups.memberCheckbox)
#Select all apps to be visible to the user      
        a=find(ImageLibrary.groups.findAppsField).below(100)
        b=a.find(ImageLibrary.common.checkbox)
        click(b)
        click(ImageLibrary.groups.saveChangesBtn)
        waitToLoad(ImageLibrary.common.actionDoneMessage,5)
        waitToLoad(ImageLibrary.groups.addNewGroupBtn,5)
#Publish app
    def test999_Tests(self):
        #try parts of tests here
        assert(1==1)