#!/usr/bin/python3

# browzers

browzer = ["firefox","chrome","brave", "internet explorer", "vivida",]

for x in browzer:
   print(x)
print("-----------")
browzer2 = {   
    "mozilla" : "firefox",
    "google"  : "chrome",
    "??" : "brave",
    "??"  : "vivida",
    "microsoft" : "internet explorer",
    "apple" : "safari",
}

for x in browzer2:
    print(x)
    
    
print("-----------")


for key,val in browzer2.items():
    print(key, "=>", val)
