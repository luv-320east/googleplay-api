# Google play python API [![Build Status](https://travis-ci.org/NoMore201/googleplay-api.svg?branch=master)](https://travis-ci.org/NoMore201/googleplay-api)

This project contains an unofficial API for google play interactions. The code mainly
comes from [GooglePlayAPI project](https://github.com/NoMore201/googleplay-api/)
which is not maintained anymore.

# Usage
An important note about login function:
```
def login(self, email=None, password=None, gsfId=None, authSubToken=None)
```
for first time logins, you should always provide an email and password.
The module will take care of initalizing the api, uploading device information
to the Google account you supplied, and retrieving a Google Service Framework
ID (which, from now on, will be the Android ID of a device).

For the next logins you **should** save the `gsfId` and the `authSubToken`, and
provide them as parameters to the login function. If you login again with email
and password only, this is the equivalent of re-initalizing your android device
with a Google account.

# Documentation

For some documentation about the Google Play API check out the relative folder.
