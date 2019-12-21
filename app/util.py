import re
from app.models import Character

def createLinks(content, positionInThread):
    print("creating links...")
    matches = re.findall("@\w+", content)
    print(str(len(matches))+" matches")
    ret = content
    n = 0
    for m in matches:
        try:
            ch = Character.objects.get(slug=m[1:])
            html = tooltipHTML()
            id = str(positionInThread*100000+n*200)
            html = html.replace("#id", id)
            ret = ret.replace(m, '<a charId="'+str(ch.pk)+'" class="character-slug-ref area" id="character-slug-'+id+'" href="/lore/character/'+str(ch.pk)+'/">'+m+html+'</a>', 1)
            print(ret)
            n = n+1 
        except Character.DoesNotExist:
            continue
    return ret

def tooltipHTML():
    return """  <div class='fixed slug-popup' id='slug-popup-#id'></div>"""