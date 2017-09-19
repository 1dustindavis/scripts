#!/usr/bin/python

#
# This script iterates through ldap and displays users where the uid and email do not match.
#

import ldap

# Define global variables
ldap_server = 'ldaps://ldap.example.com:636'
ldap_ou = 'ou=people,dc=example,dc=com'
ldap_filter = '(&(objectClass=person)(!(ou:dn:=ExcludedOU)))'
domain = '@example.com'

mismatch = {}
missing = []

# Setup ldap connection and define the search
l = ldap.initialize(ldap_server)
search = l.search_s(ldap_ou,ldap.SCOPE_SUBTREE,ldap_filter, attrlist=['uid','mail'])

#
# https://www.python-ldap.org/doc/html/ldap.html#ldap.LDAPObject.search_s
# "Each result tuple is of the form (dn, attrs), where dn is a string containing the DN (distinguished name) of the entry,
# and attrs is a dictionary containing the attributes associated with the entry. The keys of attrs are strings, and the associated values are lists of strings.""
#

# Loop through the ldap results.
for dn,entry in search:
	if entry.items()[0][0] == 'mail':

		# The actual data is stored as a string, in a list, in a dictionary, in a tuple.
		mail = entry.items()[0][1].pop()
		uid = entry.items()[1][1].pop()


		# If mail and uid don't match, add them to a dict called 'mismatch'
		if mail != (uid + domain):
			mismatch[uid] = mail

	else:
		# If mail is missing, add them to a list called 'missing'
		missing.append(dn)

# Display results in an overly complicated ascii table
print ""
print "-"*50
print "%+33s" % "UID/Mail Mismatch"
print "-"*50
print "%-25s%-25s" % ("UID", "MAIL")
print "-"*50
for user in sorted(mismatch):
	print "%-25s%-25s" % (user, mismatch[user])
print "-"*50
print ""
print ""
print "-"*50
print "%+33s" % "Mail Value Missing"
print "-"*50
for user in sorted(missing):
	print "%-25s" % (user)
print "-"*50
print ""
