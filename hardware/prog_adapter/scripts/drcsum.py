import json,collections,sys
d=json.load(open(sys.argv[1]))
for k in ('violations','unconnected_items','schematic_parity'):
    v=d.get(k,[]); print(k,len(v), dict(collections.Counter((x['severity'],x['type']) for x in v)))
for x in d['violations']+d.get('schematic_parity',[])+d['unconnected_items']:
    if x['severity']=='error' or (len(sys.argv)>2):
        print(x['severity'],x['type'],x['description'][:60],'|',' ; '.join(i['description'][:55]+'@'+str((round(i['pos']['x'],2),round(i['pos']['y'],2))) for i in x['items']))
