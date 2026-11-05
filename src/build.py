import hashlib,base64,pathlib
R=pathlib.Path(__file__).parent
h=lambda s:"'sha256-"+base64.b64encode(hashlib.sha256(s.encode()).digest()).decode()+"'"
lj=(R/"vendor/leaflet.js").read_text();lc=(R/"vendor/leaflet.css").read_text();ac=(R/"src/app.css").read_text();aj=(R/"src/app.js").read_text()
t=(R/"template.html").read_text()
out=t.replace("{H1}",h(lj)).replace("{H2}",h(aj)).replace("{LEAFCSS}",lc).replace("{APPCSS}",ac).replace("{LEAFJS}",lj).replace("{APPJS}",aj)
(R/"site/index.html").write_text(out);(R/"wayfarer.html").write_text(out);print("built",len(out))
