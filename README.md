# AAP
Android apk analysis web platform by django  
Location: http://aap.seeleit.com/  
Better browsing performance with desktop browsers  

***

AAP is an Android apk static analysis web platform. Here you can upload your apk file to check out its static security info. Also, we collect over 10000 apk samples from Android markets and present the statistics of all the apks.  

Except for the web part, in /analysis we provide a local scanner to work with a crawler. The scanner can monitor your path and automatically analyze the new added apks to sync the data to database. If you have a apk crawler, you can use the scanner to monitor the crawler path to sync the new apk's info dynamically.  

Our scanner module is based on [androguard](https://github.com/androguard/androguard) which implements permission, ad sdk and obfuscation analysis.  

## How to use

1. scanner part  
	We provide two watchers for both win and linux under /analysis, you can simplely run the watcher to monitor you crawler's path.  
	
2. web part  

	1. Change the database settings in settings.py.

	2. Then 
		```
		python manage.py makemigrations
		python manage.py migrate
		```
	3. We also provide the database of apk info we have collected under /database, you can import the .sql to your own database.
	4. For deployment, you can check [here](https://github.com/HevLfreis/server) for some infomation. Hope it helps.


> If you have any problem, please contact hevlhayt@foxmail.com (ﾉﾟ▽ﾟ)ﾉ








