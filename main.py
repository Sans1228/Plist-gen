#Copyright CaspD3V All Rights reserved.
#This script can generate plists for cydia alternatives.
#Dont steal this code and say its yours because that will make you a skid..

print("--------------------------")
print("")
print("Welcome!")
print("Lets generate some plists.")
print(
    "Copyright CaspD3V All Rights reserved, script was not made by repl owner,  few changes have been made."
)
print("--------------------------")
plistName = (input(".plist Name: "))
ipaLink = (input(".ipa Link: "))
bundleId = (input("Bundle ID: "))
appName = (input("App Name: "))

print("")
print("Creating Plist..")

print("Done.")

print("--------------------------")
print("Plist:")
print(
    '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd …">\n<plist version="1.0">\n<dict>\n<key>items</key>\n<array>\n<dict>\n<key>assets</key>\n<array>\n<dict>\n<key>kind</key>\n<string>software-package</string>\n<key>url</key>\n<string>'
    + ipaLink +
    '</string>\n</dict>\n<dict>\n<key>kind</key>\n<string>display-image</string>\n<key>url</key>\n<string>https://app.eonhub.co/img/icon.png</string>\n</dict>\n<dict>\n<key>kind</key>\n<string>full-size-image</string>\n<key>url</key>\n<string>https://app.eonhub.co/img/icon.png</string>\n</dict>\n</array>\n<key>metadata</key>\n<dict>\n<key>bundle-identifier</key>\n<string>'
    + bundleId +
    '</string>\n<key>bundle-version</key>\n<string>1</string>\n<key>kind</key>\n<string>software</string>\n<key>title</key>\n<string>'
    + appName + '</string>\n</dict>\n</dict>\n</array>\n</dict>\n</plist>')
