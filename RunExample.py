import spectrumprotect as sp
import json

def formatJson(output):
    r = json.loads(output.text)
    return (r)

protocol = 'https'
tcpaddress = '10.0.0.1'
tcpport = '11090'
instance = 'SERVER1'
username = 'username'
password = 'myPassword'

ocInstanceUrl = sp.OcOperation(protocol,tcpaddress,tcpport,instance)

# Print Test Command that is Query Status
command = 'query status'
try:
    response = ocInstanceUrl.testConnection(ocInstanceUrl, username, password, command)
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

