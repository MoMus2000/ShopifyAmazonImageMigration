import pandas as pd
import requests
import wget
import os
import cv2
from PIL import Image

df = pd.read_csv("/Users/a./Downloads/product_variant (1).csv")
count =0 
output = pd.DataFrame()
api = ''
header = {"Authorization":}


output["Variant Id"] = df["id"]
output["ImageUrl"] = df["images"]
image_exceeding_200kb = []
imageID = []
imageUrl = []
failed_urls= []
for i in output["ImageUrl"]:
	imageUrl.append(i[15:-2])
for j in output["Variant Id"]:
	imageID.append(j)

final = []

for k in range(0,len(imageUrl)):
	final.append((imageUrl[k],imageID[k]))

print(len(final))

star = "*"
for im in final:
	try:
		star = star+"*"
		print(star)
		image_filename = wget.download(im[0],out ='/Users/a./Desktop/database/dataPics')
		im = Image.open(image_filename)			
		if(os.path.getsize(image_filename)>(200*1000)):
		    print("GOING INSIDE")
   			im = im.resize((400,400),Image.ANTIALIAS)
   			im.save(file,optimize=True,quality=20)
   		elif(os.path.getsize(image_filename)>=(100*1000)):
   		 	print("GOING INSODE 2")
   			# im = im.resize((400,400),Image.ANTIALIAS)
   		 	# im.save(image_filename,optimize=True,quality=70)
   		else:
   			print("GOING INSIDE 3")
   			im.save(image_filename)
		data = open(image_filename,'rb')
		files = {'image':( 'Mustafa.jpeg', data,'image/*')}
		r = requests.post(api,files=files,headers=header)
		r.raise_for_status()		
		success = open("SuccessFileDryTest3.txt","a")
		step1 = "UPDATE product_variant SET images = '{"
		step2 = " \"w400Xh400\" : \""+r.text[7:43] + "\""
		step3 = " }' WHERE id = \""+ str(im[1]) +"\";"
		txt = step1+step2+step3
		print(txt)
		success.write(txt)
		success.write("\n")
		success.close()
		

	except Exception as e:
		print(e)
		count = count+1
		f = open("ExceptionFileDryTest3.txt", "a")
		f.write("URL: "+str(im[0])+" "+str(e))
		f.write("\n")
		f.close()
		failed_urls.append(im[0])

failed = pd.DataFrame()
failed["failed"] = failed_urls
failed.to_csv("FAILEDURLSDRYTEST.csv")

		
print("DONE")
