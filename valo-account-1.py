import pyautogui as pt

un = ("input your username here")
pwd = ("input your password here")

# 1. find valorant icon
icon = None
while icon is None:
    icon = pt.locateOnScreen("valo_icon.png", confidence = 0.5)

x1, y1 = pt.locateCenterOnScreen("valo_icon.png")
pt.doubleClick(x1, y1)

# 2. find sign in text
sign_in = None
while sign_in is None:
    sign_in = pt.locateOnScreen("valo_sign_in.png", confidence = 0.9)
x2, y2 = pt.locateCenterOnScreen("valo_sign_in.png")
pt.click(x2, y2)

# 3. find username text field
username = None
while username is None:
    username = pt.locateOnScreen("valo_username.png", confidence = 0.7)

x3, y3 = pt.locateCenterOnScreen("valo_username.png")

# 4. click username text field, then type username
pt.click(x3, y3)
pt.typewrite(un)

# 5. find password text field
password = None
while password is None:
    password = pt.locateOnScreen("valo_password.png", confidence = 0.7)

x4, y4 = pt.locateCenterOnScreen("valo_password.png")

# 6. click password text field, then type password
pt.click(x4, y4)
pt.typewrite(pwd)

# 7. click enter
enter = None
while enter is None:
    enter = pt.locateOnScreen("valo_enter.png", confidence = 0.9)

x5, y5 = pt.locateCenterOnScreen("valo_enter.png")
pt.click(x5, y5)