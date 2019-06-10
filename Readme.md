# A simple python mail script
Note, most of this script is taken from the [google api guide](https://developers.google.com/docs/api/quickstart/python).

## Installation
`pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`.

Also make sure to authorize the script with the google api for the account / organization you want to use it with. 

## Usage
Start by calling the main method i.e. `quickstart.main()` to setup authentication etc. 

### Sending a message
To send a message first make sure that you have called the main method as stated above. 
Then simply call the `quickstart.send_message()` method with the following parameters:
* `sender`: The email address you wish to send from, you will have to acquired an authentication token for this specific mail address.
* `to`: The receiving mail address.
* `subject`: The subject of the mail.
* `message_text`: The actual text contents of the mail.

### Example usage
```python
quickstart.main()
quickstart.send_message("somemail@gmail.com", "some.guy@hotmail.com", "Party invitation", "Hi Some Guy! \n\n ...")
```
