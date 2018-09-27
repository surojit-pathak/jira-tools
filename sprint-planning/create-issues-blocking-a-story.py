import getpass
import json
from jira import JIRA
import netrc
from pprint import pprint
import sys



def jira_connect():
    secrets = netrc.netrc()
    username,account,password = secrets.authenticators('devel-jira')  
    password = getpass.getpass('Password:')
    jira = JIRA(options={'server': account}, basic_auth=(username, password))
    return jira

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        data = json.load(f)
        # pprint(data)
    
    jira = jira_connect()
    for issue in data['issues']:
        issue_dict = {
            'summary': issue['summary'],
            'description': issue['description'],
            'labels': [data['label']],
            'project': data['project'],
            'issuetype': { 
                 'name': 'Task'
            },
            'customfield_10006': data['epic']
        }
        try:
            new_issue = jira.create_issue(fields=issue_dict)
            jira.create_issue_link('Blocks', new_issue, jira.issue(data['story']))
            
            issue = jira.issue(new_issue['key'])
            print issue['key'], issue.fields.issuelinks
        except:
            print Exception
        

