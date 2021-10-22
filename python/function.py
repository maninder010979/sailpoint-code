import constant
import requests
import traceback
import json

def getapi():
    try:
        requesturl=constant.git_pull_requst_repo+constant.pull_request_type
        response = requests.get(requesturl)
        pullreqjson = response.json()
        return pullreqjson
    except Exception:
        print("issue in fetchin the json")
        traceback.print_exc()

def parsejson(pulljson):
    try:
        print ("")
        print("From Mail...."+constant.str_from_email)
        print("To Mail......"+constant.str_to_email)
        print("Subject......"+constant.str_mail_subject)
        print("")
        print(constant.str_mail_body)
        for pullreq in range(len(pulljson)):
            if constant.str_display_mode == "console":
                str_title = pulljson[pullreq]['title']
                
                print (" * Pull Request # is...... "+str(pulljson[pullreq]['number']))
                print ("   Pull Request Title..... "+pulljson[pullreq]['title'])
                print ("   User Created PR........ "+pulljson[pullreq]['user']['login'])
                print ("   Pull Request state.... "+pulljson[pullreq]['state'])
                print ("   PR URL ................"+pulljson[pullreq]['html_url'])
                print ("   Diff URL .............."+pulljson[pullreq]['diff_url'])
                
                print ("")
    except Exception:
        print("issue in fetchin the json")
        traceback.print_exc()
