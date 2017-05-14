#!/usr/bin/python

###
#
#            Name:  sparkle_version_check.py
#     Description:  Lists all Sparkle apps and the sparkle version 
#         Created:  2016-02-10
#   Last Modified:  2017-05-13
#         Version:  1.1
#
###
from os import listdir, path
from plistlib import readPlist

app_path = "/Applications/"
sparkle_plist = "/Contents/Frameworks/Sparkle.framework/Resources/Info.plist"
sparkle_path = "/Contents/Frameworks/Sparkle.framework"
sparkle_apps = {}

#Get list of sparkle apps
for app in listdir(app_path):
	if app.endswith(".app") and path.exists(app_path + app + sparkle_path):
		
		#Get Sparkle version number
		if path.exists(app_path + app + sparkle_plist):
			pl = readPlist(app_path + app + sparkle_plist)
			#Add app and version to sparkle_apps dictionary
			sparkle_apps[app] = pl["CFBundleShortVersionString"]
		#If sparkle version can't be found
		else:
			sparkle_apps[app] = "UNKNOWN"
			
#output app name and sparkle version
print "-"*50
print "%-25s%-25s" % ("APPLICATION", "SPARKLE VERSION")
print "-"*50
for app in sorted(sparkle_apps):
	print "%-25s%-25s" % (app, sparkle_apps[app])
print "-"*50