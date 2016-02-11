#!/usr/bin/python

###
#
#            Name:  sparkle_version_check.py
#     Description:  Lists all Sparkle apps and the sparkle version 
#         Created:  2016-02-10
#   Last Modified:  2016-02-10
#         Version:  1.0
#
###
import os
import plistlib

#Set Variables
sparkle_apps = []
sparkle_version =[]

#Get list of sparkle apps
for app in os.listdir("/Applications"):
	if app.endswith(".app") and os.path.exists("/Applications/" + app + "/Contents/Frameworks/Sparkle.framework"):
		sparkle_apps.append(app)
		
		#Get Sparkle version number
		if os.path.exists("/Applications/" + app + "/Contents/Frameworks/Sparkle.framework/Resources/Info.plist"):
			pl = plistlib.readPlist("/Applications/" + app + "/Contents/Frameworks/Sparkle.framework/Resources/Info.plist")
			sparkle_version.append(pl["CFBundleShortVersionString"])
		#If sparkle version can't be found
		else:
			sparkle_version.append("UNKNOWN")
			print "Unable to find Version number for" + app
		
#output app name and sparkle version
print "APP NAME -- SPARKLE VERSION"
for app,version in zip(sparkle_apps,sparkle_version):
	print app + " -- " + version
