# pythonsamples
This repo contains some Python sample code.

### List of files

* PILsample.py    
Add a number in the top right corner of a picture.

* analyze_code_in_folder.py    
Check all the Python code files in a folder and its subfolders.
Count code lines, blank lines and annotation lines of every file.
Write results into a txt file
Note:
This code takes all files into consideration, but it is correct only when the file
is in Python code, which means you can not use it to count a Java code etc. But a wrong result will
show up in output txt if the Java(or something else) file is in the folder.
If a line contains both annotation and code, it is counted as a code line, and annotation
line number will not increment.

* activation_key_generator_redis.py    
Generate 20 activation keys and store them in a Redis database. Using uuid.

* activation_key_generator_mysql.py    
Generate 20 activation keys and store them in a MySQL database. Using hashlib sha1.
