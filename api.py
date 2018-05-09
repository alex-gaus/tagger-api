import hug
from topiczoom import topiczoom

@hug.post("/api",output=hug.output_format.json)
def post_here(body):
    text=body["text"].encode('utf-8')
    print(text)
    topiczoom_list=topiczoom(text)
    print(topiczoom_list)
    response = {"annotations":[]}
    for item in topiczoom_list:
        response["annotations"].append({"title":item["@txt"]})
    return(response)
        