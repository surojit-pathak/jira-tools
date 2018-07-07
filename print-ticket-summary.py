import netrc
import getpass
from jira import JIRA

def jira_connect():
    secrets = netrc.netrc()
    username,account,password = secrets.authenticators('devel-jira')  
    password = getpass.getpass('Password:')
    jira = JIRA(options={'server': account}, basic_auth=(username, password))
    return jira

if __name__ == '__main__':
    jira = jira_connect()
    while 1:
        ticket = raw_input('Enter the ticket in question: ')
        try:
            issue = jira.issue(ticket)
            print issue.fields.summary
        except:
            print Exception
        

