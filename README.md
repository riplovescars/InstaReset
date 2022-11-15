# InstaReset - _Forgot Instagram Password_ using Python !

<br>

## What is this?
This script was made to send a Instagram reset password request using Python **without asking for reCAPTCHA** as Instagram does if we used a browser, It supports username and email methods.

## How it works ?
This script works by using a faked mobile user agent like `Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440)` and send a POST request to `https://i.instagram.com/api/v1/accounts/send_password_reset/` _with a random generated CSRF token of 32 chars_ in the request data.

## Features
- Faster ⚡
- No reCAPTCHA 🤖
- Nice looking CLI 🎨
- Works on mobile 📱

## Requirements
_in case you want to run the script quickly without the requirments and python just run the `main.exe` file_
<br>
_which was converted using [PyInstaller](https://pyinstaller.org/en/stable/), [click here to install](https://www.github.com/Kh4lidMD/InstaReset/raw/main/main.exe/)_
- [Python 3 or higher](https://www.python.org/downloads/)
- [Requests](https://pypi.org/project/requests/) module `pip install requests`
- [Colorama](https://pypi.org/project/colorama/) module `pip install colorama`

## Changelog

**v1.1**
- Auto detect target's method (email/username)
- More clean code
- Fixed bug in email method

**v1.0**
- Initial release

## Module version
Coming soon...

<br><hr>

_Liked the script? Leave a star ⭐ to show your support!_
