import requests
from xmljson import badgerfish as bf
from xml.etree.ElementTree import fromstring

def topiczoom(text):
    def remove_namespaces(e) :
        for elem in e.getiterator():
            if not hasattr(elem.tag, 'find'): continue  # (1)
            i = elem.tag.find('}')
            if i >= 0:
                elem.tag = elem.tag[i+1:]
        return(e)

    params = (
        ('lang', 'de'),
    )

    data=text

    response = requests.post('http://twittopic.topiczoom.de/quickindex.xml', params=params, data=data)

    feedjson=bf.data(remove_namespaces(fromstring(response.text)))

    topiczoom_list=feedjson["Envelope"]["Body"]["TZTopicSet"]["TZTopic"]
    
    topiczoom_list = sorted(topiczoom_list, reverse=True, key=lambda x: x["@weight"])

    return (topiczoom_list)

