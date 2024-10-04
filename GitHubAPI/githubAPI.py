import requests
import argparse


#Fuction to parse the argument from CIL
def parseArguments():
    parser = argparse.ArgumentParser(description='GitHub Activity Program')
    parser.add_argument('UserID', nargs=1,help='User Id with no spaces')
    parser.add_argument('EventQuantity', nargs='?',default=0,help='Quantity of events to show')
    args = parser.parse_args()
    return args.UserID[0],int(args.EventQuantity)

#Connect to GitHub API and request the User activity
def getActivity(user):    
    url = f"https://api.github.com/users/{user}/events"
    response = requests.request("GET", url)
    if response.ok:        
        return response.json()
    else:
        print('Request error. UserdID not Found')

#Select the number of required events
def selectEvent(quantity,activity):
    reduce = activity[0:quantity]
    return reduce

#Fuction to parse the GitHub Event and print the result
def parseActivity (apiRequest):
    print('-'*30 + '\n\tOutput:' + '\n' + '-'*30)
    for event in apiRequest:
        if event['type'] == 'CommitCommentEvent':
            print(f'- "{event['actor']['login']}" created Commit Event')
        elif event['type'] == 'CreateEvent':
            print(f'- "{event['actor']['login']}" created a {event['payload']['ref_type']} with the comment: "{event['payload']['description']}"')
        elif event['type'] == 'DeleteEvent':
            print(f'- "{event['actor']['login']}" delete a {event['payload']['ref_type']} with the name: "{event['payload']['ref']}"')
        elif event['type'] == 'ForkEvent':
            print(f'- "{event['actor']['login']}" forked the repository "{event['payload']['forkee']}"')
        elif event['type'] == 'IssueCommentEvent':
            print(f'- "{event['actor']['login']}" {event['payload']['action']} a comment. Issue: "{event['payload']['issue']['title']}"')
        elif event['type'] == 'IssuesEvent':
            print(f'- "{event['actor']['login']}" {event['payload']['action']} the issue "{event['payload']['issue']['title']}"')
        elif event['type'] == 'PublicEvent':
            print(f'- "{event['actor']['login']}" {event['payload']['action']} the issue "{event['payload']['issue']['title']}"')
        elif event['type'] == 'PullRequestEvent':
            print(f'- "{event['actor']['login']}" {event['payload']['action']} the PullRequesst "{event['payload']['number']}"')
        elif event['type'] == 'PullRequestReviewEvent':
            print(f'- "{event['actor']['login']}" review the PullRequesst. Commit ID: "{event['payload']['review']['commit_id']}"')                    
        elif event['type'] == 'PushEvent':
            print(f'- "{event['actor']['login']}" pushed: {event['payload']['size']} commit')                            
        else:
            print(event['type'])
    
#Main fuction
def main ():
    user,quantity = parseArguments()

    activity = getActivity(user)
    if quantity>0:
        activity = selectEvent(quantity,activity)
    parseActivity (activity)

if __name__ == '__main__':
    main()