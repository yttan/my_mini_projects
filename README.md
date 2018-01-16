# my_mini_projects
This repo contains some mini projects. Some of the sample results can be seen in the /result folder 

### List of files

* server.py     
  implemented a Python web server which can give requested HTML pages and can generate error message pages

* parse_pic_from_website    
  Pasre pictures from a Baidu Tieba website and save them in testfolder

* analyze_code_in_folder.py    
  Checks all the Python code files in a folder including subfolders and counts code lines, blank lines and annotation lines of every file.
  Write results into a txt file  
  Note:    
  1. If a line contains both annotation and code, it is counted as a code line, and annotation
  2. line number will not increment. The code takes all files into consideration, but it is correct only when the file is in Python, which means you can not use it to count a Java code etc. But a wrong result will show up in output txt if the Java(or something else) file is in the folder.  
  3. testcase in /testfolder 


* activation_key_generator_redis.py    
  Generate 20 activation keys and store them in a Redis database. Using uuid.

* activation_key_generator_mysql.py    
  Generate 20 activation keys and store them in a MySQL database. Using hashlib sha1.

* PILsample.py    
  Add a number at the top right corner of a picture. testcase in /results.

* generate_code_pic.py  
  Generate an image verificaion code. see /results/code.jpg.

* Johnsons.java    
  Read data from johnsonsGraphData.txt and run Johnson's algorithm.


