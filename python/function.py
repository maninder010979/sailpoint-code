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
        for pullreq in range(len(pulljson)):
            if constant.str_display_mode == "console":
                str_title = pulljson[pullreq]['title']
                print ("*******************************************************************")
                print ("Pull Request # is...... "+str(pulljson[pullreq]['number']))
                print ("Pull Request Title..... "+pulljson[pullreq]['title'])
                print ("User Created PR........ "+pulljson[pullreq]['user']['login'])
                print ("PR URL ................"+pulljson[pullreq]['html_url'])
                print ("Diff URL .............."+pulljson[pullreq]['diff_url'])
                print ("*********************************************************************")
                print ("")
    except Exception:
        print("issue in fetchin the json")
        traceback.print_exc()
