# IBM Spectrum Protect Restful API
Version: 1.0
Produce by Cristie Nordic AB

## About the module
This is a basic python module to easy get started with IBM Spectrum Protect Restful API though the Operation Center.

### Requriment
It writed in Python 3 and it's depending on other libraries.
 - sys
 - urllib3
 - requests

## Installation
Download the GitHub repo and import the spectrumprotect.py file to your python script.
You can use the requirment file that belongs to this script, so you easy can install the depending packages.

```
pip install -r requirment.txt
```

## Example Code
```
import spectrumprotect as sp
import json

def formatJson(output):
    r = json.loads(output.text)
    return (r)

protocol = '<PROTOCOL PROBABLY HTTPS>'
tcpaddress = '<IP OR DNS TO OC>'
tcpport = '<OC PORT, DEFAULT: 11090>'
instance = '<SP INSTANCE NAME>'
username = '<SP USERNAME>'
password = '<SP PASSWOR>'

ocInstanceUrl = sp.OcOperation(protocol,tcpaddress,tcpport,instance)

# Print Test Command that is Query Status
command = 'query status'
try:
    testCommand = ocInstanceUrl.testConnection(ocInstanceUrl, username, password, command)
    response = formatJson(testCommand)
    print(response)

expect OSError as ocerror:
    print('Ooops, something went wrong... Error: ' + ocerror)
    break

# Running my own command
print ("\nLet's run your own command now\n")
myCommand = 'query node *'
myCmd = ocInstanceUrl.runCmd(ocInstanceUrl, username, password,  myCommand)
response = formatJson(myCmd)
print (response)
```

## MIT License
Feel free to use, create your own fork, help us to develop the module.
But make sure you following the MIT license type and keep it as a open source project.

For more information about the MIT License please read the license file