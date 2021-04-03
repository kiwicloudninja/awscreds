# awscreds

This is a python based app.

There is a Linux executable in the dist/ folder

The app updates your ~/.aws/credentials file with a credential copied to the clipboard from the AWS Single Sign-On console.

It assumes the clipboard contents will be in the following format:
[AWSAccNum_IAMRoleName]
aws_access_key_id=XXXXXXXXXXXXX
aws_secret_access_key=XXXXXXXXXXXXXXXXXX
aws_session_token=XXXXXXXXXXXXXXXXXXXXXX

It only checks that aws_access_key_id exists as a key. It doesn't validate the other keys or any of the values.

It assumes that a ~/.aws/ folder exists.

If you have an existing credentials file, the app will check whether the new credential values match and only update if they differ.

The code uses:
https://docs.python.org/3/library/configparser.html
https://pypi.python.org/pypi/pyperclip
