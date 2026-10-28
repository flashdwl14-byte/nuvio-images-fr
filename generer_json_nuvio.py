#!/usr/bin/env python3
"""Usage: python3 generer_json_nuvio.py NOM_UTILISATEUR NOM_DEPOT [BRANCHE]"""
import json,sys,pathlib,urllib.parse
if len(sys.argv)<3:
 print("Usage : python3 generer_json_nuvio.py UTILISATEUR DEPOT [BRANCHE]");sys.exit(1)
user,repo=sys.argv[1:3];branch=sys.argv[3] if len(sys.argv)>3 else 'main'
base=pathlib.Path(__file__).resolve().parent
original=json.loads((base/'nuvio-original.json').read_text(encoding='utf-8'))
correspondances=json.loads((base/'correspondances.json').read_text(encoding='utf-8'))
by_id={f['id']:f for c in original for f in c.get('folders',[])}
for item in correspondances:
 folder=by_id[item['id_dossier']]
 assert folder.get('coverImageUrl')==item['ancienne_url'],item['id_dossier']
 folder['coverImageUrl']='https://raw.githubusercontent.com/'+urllib.parse.quote(user,safe='')+'/'+urllib.parse.quote(repo,safe='')+'/'+urllib.parse.quote(branch,safe='')+'/'+item['fichier_github']
out=base/'nuvio-collections-profile-6-francais-images-FR.json'
out.write_text(json.dumps(original,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('JSON créé :',out,'| Couvertures modifiées :',len(correspondances))
