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
        tmpconsoleprint=constant.str_console_print
        for pullreq in range(len(pulljson)):
            if constant.str_display_mode == "console":
                str_title = pulljson[pullreq]['title']
                tmpconsoleprint += "\n"+str(pulljson[pullreq]['number'])+"\t\t"+str_title[0:12]
                tmpconsoleprint += "\t"+pulljson[pullreq]['user']['login']+"\t\t"+pulljson[pullreq]['html_url']+"\t"+pulljson[pullreq]['diff_url']+"\n"
        tmpconsoleprint+=constant.str_console_footer
        print(tmpconsoleprint)   
    except Exception:
        print("issue in fetchin the json")
        traceback.print_exc()
