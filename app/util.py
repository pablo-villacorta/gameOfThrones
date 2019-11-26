import re
from app.models import Character

def createLinks(content):
    print("creating links...")
    matches = re.findall("@\w+", content)
    print(str(len(matches))+" matches")
    ret = content
    print(matches)
    for m in matches:
        try:
            ch = Character.objects.get(slug=m[1:])
            html = tooltipHTML()
            html = html.replace("#name", ch.name)
            html = html.replace("#house", ch.house.name)
            html = html.replace("#imageURL", ch.image)
            ret = ret.replace(m, '<a href="/lore/character/'+str(ch.pk)+'/" data-toggle="tooltip" data-html="true" title="'+html+'">'+m+'</a>', 1)
            #ret.replace(m, 'damn')
            print(ret)
        except Character.DoesNotExist:
            print("nothing")
            continue
    return ret

def tooltipHTML():
    return """  <div class='tooltip-content'>
                    <h3>#name</h3>
                    <h4>#house</h4>
                    <img src='#imageURL' width='100'/>
                </div>"""