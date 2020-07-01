# AUTHOR = 4TH4RV
# DATE = 6/24/2020
# NAME = Basic Login and Sign up

import tkinter as tk
from tkinter import *


def createWindow():  # CREATE WINDOW
    # mainWindow
    global root

    # GlobalVar MethodWindow
    global signupwindow
    global loginwindow
    global mainmenu

    # GlobalVar SignUp
    global userinput
    global emailinput
    global passwordinput
    global password
    global username
    global email
    global signupbutton

    # GlobalVarLogin
    global loginUsername
    global loginUsernameInput
    global loginPassword
    global loginPasswordInput
    global loginButton

    # GlobalVar Status
    global usernameNotA
    global accountcreated
    global accnotfound
    global wrongdata

    # GlobalVar LoggedIn
    global accountName
    global passwordName
    global logOut

    # Main root window innit
    root = Tk()
    root.title = "SignupLogin"
    root.geometry("200x200")
    # Choose Method Window
    signupwindow = tk.Button(root, text="Sign Up", command=showsignup)
    loginwindow = tk.Button(root, text="Log in", command=showlogin)
    mainmenu = tk.Button(root, text="Back", command=open_mainmenu)
    signupwindow.pack()
    loginwindow.pack()

    # Sign up
    username = tk.Label(root, text="Username")
    userinput = tk.Entry(root)
    email = tk.Label(root, text="Enter your email address")
    emailinput = tk.Entry(root)
    password = tk.Label(root, text="Choose password")
    passwordinput = tk.Entry(root, show="*")
    signupbutton = tk.Button(root, text="SignUp", command=createAccount)

    # Login window
    loginUsername = tk.Label(root, text="Username")
    loginUsernameInput = tk.Entry(root)
    loginPassword = tk.Label(root, text="Password")
    loginPasswordInput = tk.Entry(root, show="*")
    loginButton = tk.Button(root, text="Log in", command=loginAccount)

    # LoggedInStuff
    accountName = tk.Label(root, text="Account name:")
    passwordName = tk.Label(root, text="Password:")
    logOut = tk.Button(root, text="Log Out")

    # Status
    usernameNotA = tk.Label(root, text="Username not available")
    accountcreated = tk.Label(root, text="Account created successfully")
    wrongdata = tk.Label(root, text="Wrong username or password")
    accnotfound = tk.Label(root, text="Account doesn't exists")

    root.mainloop()  # Main window Loop


def showsignup():  # Show sign up gui
    # Sign Up
    hidelogin()
    signupwindow.pack_forget()
    loginwindow.pack_forget()
    username.pack()
    userinput.pack()
    email.pack()
    emailinput.pack()
    password.pack()
    passwordinput.pack()
    signupbutton.pack()
    mainmenu.pack(side="left")


def hidesignup():  # hide sign up gui
    # Sign Up
    signupwindow.pack_forget()
    loginwindow.pack_forget()
    username.pack_forget()
    userinput.pack_forget()
    email.pack_forget()
    emailinput.pack_forget()
    password.pack_forget()
    passwordinput.pack_forget()
    signupbutton.pack_forget()
    mainmenu.pack_forget()
    usernameNotA.pack_forget()
    accountcreated.pack_forget()
    wrongdata.pack_forget()
    accnotfound.pack_forget()
    return


def showlogin():  # Show login gui
    # Log in
    hidesignup()
    signupwindow.pack_forget()
    loginwindow.pack_forget()
    loginUsername.pack()
    loginUsernameInput.pack()
    loginPassword.pack()
    loginPasswordInput.pack()
    loginButton.pack()
    mainmenu.pack(side="left")


def hidelogin():  # hide login gui
    # Log in
    signupwindow.pack_forget()
    loginwindow.pack_forget()
    loginUsername.pack_forget()
    loginUsernameInput.pack_forget()
    loginPassword.pack_forget()
    loginPasswordInput.pack_forget()
    loginButton.pack_forget()
    mainmenu.pack_forget()
    accountcreated.pack_forget()
    wrongdata.pack_forget()
    accnotfound.pack_forget()
    return


def showLoggedIn(userA, passB):  # show the screen when a user is logged in
    hidelogin()
    accountName.pack()
    passwordName.pack()
    accountName.config(text="Username: " + userA)
    passwordName.config(text="Password: " + passB)
    logOut.pack(side="bottom")
    logOut.config(command=logoutacc)


def open_mainmenu():  # hides login or sign up screen and opens up the main menu for choosing method
    hidelogin()
    hidesignup()
    signupwindow.pack()
    loginwindow.pack()


def check_if_string_in_file(file_name, string_to_search):  # checks if a username or password is in the main database
    with open(file_name, 'r') as read_obj:
        lineC = 0
        for line in read_obj:
            lineC += 1
            if string_to_search in line:
                return lineC
    return None


def checkUsername(usernameA):  # checks username in database
    f = open("LoginInfo", mode='r')
    checkusernameString = check_if_string_in_file("LoginInfo", usernameA)
    if checkusernameString:
        foundString = f.readlines()[checkusernameString - 1].split(";")[0].split(":")[1]
        if foundString == usernameA:
            f.close()
            return True
        else:
            f.close()
            return False


def checkUserInfo(usernameA, passwordB):  # Checks the userinfo like password or username
    getLine = check_if_string_in_file("LoginInfo", usernameA)
    f = open("LoginInfo", mode='r')
    if getLine:
        userinfo = f.readlines()[getLine - 1].split(";")
        if passwordB == userinfo[2].split(":")[1]:
            return True
        else:
            return False
    else:
        return None
    f.close()


def createAccount():  # creates an account in the database file
    USERNAME = userinput.get()
    EMAIL = emailinput.get()
    PASSWORD = passwordinput.get()
    f = open("LoginInfo", mode='a')
    try:
        checkingusername = checkUsername(USERNAME)
        if not checkingusername:
            usernameNotA.pack_forget()
            f = open("LoginInfo", mode='a')
            f.write("\nUsername:" + USERNAME + ";Email:" + EMAIL + ";Password:" + PASSWORD)
            accountcreated.pack()
        else:
            accountcreated.pack_forget()
            usernameNotA.pack()
    finally:
        f.close()


def loginAccount():  # login account button function
    USERNAME = loginUsernameInput.get()
    PASSWORD = loginPasswordInput.get()

    checkdata = checkUserInfo(USERNAME, PASSWORD)
    if checkdata:
        accnotfound.pack_forget()
        wrongdata.pack_forget()
        showLoggedIn(USERNAME, PASSWORD)

    elif not checkdata:
        accnotfound.pack_forget()
        wrongdata.pack()
    elif checkdata is None:
        wrongdata.pack_forget()
        accnotfound.pack()


def logoutacc():  # function for loggin out
    accountName.pack_forget()
    passwordName.pack_forget()
    accountName.config(text="Username: ")
    passwordName.config(text="Password: ")
    logOut.pack_forget()
    open_mainmenu()


createWindow()  # call the main function
