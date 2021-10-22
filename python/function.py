import constant
import requests
import traceback
import json

def getapi():
    try:
        requesturl=constant.git_pull_requst_repo+constant.pull_request_type
        print (requesturl)
        response = requests.get(requesturl)
        pullreqjson = response.json()
        return pullreqjson
    except Exception:
        print("issue in fetchin the json")
        traceback.print_exc()

def parsejson(pulljson):
    try:
        jsonstr =pulljson
        for pullreq in range(len(jsonstr)):
            
            print(pullreq['state'])
    except Exception:
        print("issue in fetchin the json")
        traceback.print_exc()
