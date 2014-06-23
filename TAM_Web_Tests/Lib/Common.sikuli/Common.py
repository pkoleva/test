import org.sikuli.basics.SikuliXforJython
from sikuli import *
import string

from Lib import ImageLibrary


def OpenBrowser(browserName, addressBar, time):
    print("opening browser")
    os.system("start " + browserName + " /q")
    addrBarresult= waitToLoad(addressBar, time)
    print addrBarresult
    return addrBarresult

#Receives 2 parameters - image and counter and returns exists(image) result
#Waits for "counter"* 2 seconds for the "image" to exist on the screen and returns if the "image" is found on the screen
def LogIn(username, password):
    typeInField(Pattern(ImageLibrary.common.loginBtn).targetOffset(0,-180),username)
    typeInField(Pattern(ImageLibrary.common.loginBtn).targetOffset(0,-100),password)
    click(ImageLibrary.common.loginBtn)

def isUserLoggedIn():
    a=exists(ImageLibrary.common.loginBtn)
    b=exists(ImageLibrary.common.profilePicture)
    if((a==None)and (b!=None)):
        print("user is logged in")
        return "1"
    elif((a!=None)and (b==None)):
        print("log in page")
        return "0"
    else:
        print("We're not on the login page and the user is not logged")
        return "-1"

def waitToLoad(image, counter):
    n=counter
    a= False
    while (n!=0):
        if(exists(image)):
            print("Found image" + repr(image))
            a=True
            break
        else:
            wait(2)
        n -=1
    print("Waited for " + repr((counter-n)*2) + " seconds")
    return a

#When loading a page and you are not sure which of two images will be found there
#for example is the user logged in, or not
#takes 2 images and time to wait
#returns 1 if img 1 is found, 2 for img2 and 0 if none can be found
def defineState(image1,image2,counter):
    n=counter
    while((not exists(image1))and (n!=0)):
        if(exists(image2)):
            print("Found image" + repr(image2))
            return 2
        else:
            wait(2)
        n-=1
    if (exists(image1)):
        print("Found image" + repr(image1))
        return 1
    else:
        print("Not on expected page")
        return 0

def typeInField(field,string):
    click(field)
    type(string)

#Searches for a certain image in a field with specified width, height, x and y offset and returns if the image is found
def verifyFieldContent(field,x,y,h,w, image):
    a=field.below(y).right(x).width(w).height(h)
    res=a.find(image)
    return res

#########APP Methods
#Finds the button "Browse for file" below the text "App package" and searches for the nameOfPackage
def addAnAppPackage(nameOfPackage):
    packField=find(ImageLibrary.apps.packageField).below(200)
    browseBtn=packField.find(ImageLibrary.apps.browseForFileBtn)
    click(browseBtn)
    waitToLoad(ImageLibrary.apps.fileNameField,2)
    typeInField(Pattern(ImageLibrary.apps.fileNameField).targetOffset(50,0),nameOfPackage)
    type(Key.ENTER)
    waitToLoad(ImageLibrary.apps.extractingMetadata,2)
    a = waitToLoad(ImageLibrary.apps.okRsult,10)
    print ("File uploaded " + repr(a))
    return a

#Returns if a package was deleted, or there was no package to delete
def deleteAnAppPackage():
    hover(Pattern(ImageLibrary.apps.addNewAppTitle).targetOffset(0,100))
    if(exists(ImageLibrary.apps.trashbinBtn)):
        click(ImageLibrary.apps.trashbinBtn)
        print("deleted app package")
        return 1
    else:
        print("no package to delete")
        return 0

#Fill in Distribution
def fillInDistribution(column, x, y):
    #check if there is a radio btn here
    click(Pattern(column).targetOffset(x,y))
        

###################USERS Methods
def inviteUser(userToInvite):
    click(ImageLibrary.users.inviteUserBtn)
    waitToLoad(ImageLibrary.users.inviteUserTitle,5)
    typeInField(Pattern(ImageLibrary.users.inviteUserTitle).targetOffset(0,70),userToInvite)
    click(ImageLibrary.users.sendInvitationBtn)


