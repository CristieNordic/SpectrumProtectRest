import urllib3, json, sys, requests

# Version 1.0

class OcOperation(object):

    def __init__(self, protocol, address, port, instance):
        '''
        Setup your IBM Spectrum Protect Server Instance to be preconfigured.
        :param protocol:
        :param address:
        :param port:
        :param instance:
        '''
        self.baseProtocol = protocol
        self.baseAddress = address
        self.basePort = port
        self.instance = instance
        self.baseHeader = {"OC-API-Version": "1.0", "Accept": "application/json", "content-type": "text/plain"}

    def __str__(self):
        return ('{}://{}:{}/oc/api/cli/issueConfirmedCommand/{}').format(self.baseProtocol, self.baseAddress, self.basePort,self.instance)

    def testConnection(self,ocUrl,username,password, testCommand):
        self.testCmd = testCommand
        requests.packages.urllib3.disable_warnings()
        response = requests.post(ocUrl, headers=self.baseHeader, data=self.testCmd, verify=False, auth=(username, password))
        return(response)

    def runCmd(self,ocUrl, username, password, cmd):
        self.cmd = cmd
        requests.packages.urllib3.disable_warnings()
        response = requests.post(ocUrl, headers=self.baseHeader, data=self.cmd, verify=False, auth=(username, password))
        return (response)

if __name__ == '__main__':
    OcOperation('https', 'localhost', '11090', 'server1')
