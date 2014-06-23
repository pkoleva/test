import org.sikuli.basics.SikuliXforJython
from sikuli import *

class common:
    browser="C:\Program Files (x86)\\Internet Explorer\\iexplore.exe"
    browserName="iexplore"
    baseURL="https://testtap.telerik.com"
    addressBar="CMN_IE_addressBar.png"
    

#btns
    loginBtn="CMN_loginBtn.png"
    openAppManagerBtn="CMN_openAppManagerBtn.png"
    acceptBtn="CMN_acceptBtn.png"
    getStartedBtn="CMN_getStartedBtn.png"
    addAppBtn="CMN_addAppBtn.png"
    radioBtn_empty="CMN_radioBtn_empty.png"
    usersMenuItem="US_usersMenuItem.png"
    checkbox="CMN_checkbox.png"
    editBtn=Pattern("CMN_editBtn.png").similar(0.99)
#fields
    browserOpenedView=""
    profilePicture=Pattern("CMN_profilePicture.png").similar(0.99)
    telerikPlatformLogin="CMN_telerikPlatformLogin_text.png"
    telerikLogin="CMN_telerikLogin_text.png"
    workspacesView="CMN_workspaces_text.png"
    appManagerTitle="CMN_appManager_text.png"
    validationErrorField="CMN_validationErrorField.png"
    errorMessage="CMN_errorMessage.png"
    actionDoneMessage=Pattern("CMN_actionDoneMessage.png").similar(0.99)
    deleteBtn="CMN_deleteBtn.png"
    deletePopUpBtn="CMN_deletePopUpBtn.png"
    findField="CMN_findField.png"
#data
    username="pavlina.koleva@telerik.local"
    password="enoone"
    userToInvite="someUser@telerik.com"
    appToUploadiOSValid=""
    appToUploadiOSInvalid=""
    appToUploadiOSCyrilic=""
    appToUploadAndroidValid="R:\TAM\QA\StoreContent\Calendar.apk"
    appToUploadAndroidInvalid=""
    appToUploadAndroidCyrilic=""
    
class apps:
    urlApps=""
#btns
    addNewAppBtn="AP_addNewAppBtn.png"
    browseForFileBtn="AP_browseForFileBtn.png"
    addAppBtn="AP_addAppBtn.png"  
    
#fields
    addNewAppTitle="AP_addNewAppTitle.png"  
    packageField="AP_packageField.png"
    appsTitle="AP_appsTitle.png"
    fileNameField="AP_fileNameField.png"
    extractingMetadata="App_extractingMetadata_text.png"
    okRsult="AP_okRsult.png"
    trashbinBtn="AP_trashbinBtn.png"
    descriptionTitle="AP_descriptionTitle.png"
    distributionTitle="AP_distributionTitle.png"

class users:
    usersTitle="US_usersTitle.png"
    userToInvite="tamtestuser@abv.bg"
#btns
    inviteUserBtn="US_inviteUserBtn.png"
    sendInvitationBtn="US_sendInvitationBtn.png"
#fields
    inviteUserTitle="US_inviteUserTitle.png"
    userInvitedMessage="US_userInvitedMessage.png"


class groups:
#btns
    groupsMenuItem="GR_groupsMenuItem.png"
    addNewGroupBtn="GR_addNewGroupBtn.png"
    addGroupBtn="GR_addGroupBtn.png"
    saveChangesBtn="GR_saveChangesBtn.png"
#fields
    addGroupTitle="GR_addGroupTitle.png"
    findUsersField="GR_findUsersField.png"
    groupNameField="GR_groupNameField.png"
    memberCheckbox="GR_memberCheckbox.png"
    findAppsField="GR_findAppsField.png"
    findGroupSearchbox="GR_findGroupSearchbox.png"