# SmallProjs
This repository contains some small projects. Some of the sample results can be seen in the /result folder

### Projects and Descriptions  

<table>
  <tr>
    <td>File</td>
    <td>Description</td>
  </tr>
  <tr>
    <td>server.py</td>
    <td>a Python web server which can give requested HTML pages and can generate error message pages</td>
  </tr>
  <tr>
    <td>parse_pic_from_website.py</td>
    <td>Pasre pictures from a Baidu Tieba website and save them in /testfolder</td>
  </tr>
  <tr>
    <td>analyze_code_in_folder.py</td>
    <td>
    Checks all the Python code files in a folder including subfolders and counts code lines, blank lines and annotation lines of every file.
    Write results into a .txt file  
    Note:    
    1. If a line contains both annotation and code, it is counted as a code line, and annotation
    2. line number will not increment. The code takes all files into consideration, but it is correct only when the file is in Python, which means you can not use it to count a Java code etc. But a wrong result will show up in output txt if the Java(or something else) file is in the folder.  
    3. testcase in /testfolder
    </td>
    </tr>
    <tr><td>activation_key_generator_redis.py<td><td>Generate 20 activation keys and store them in a Redis database. Using uuid.<td></tr>
    <tr><td>activation_key_generator_mysql.py<td><td>Generate 20 activation keys and store them in a MySQL database. Using hashlib sha1.<td></tr>
    <tr><td>PILsample.py<td><td>Add a number at the top right corner of a picture. testcase in /results.<td></tr>
    <tr><td>generate_code_pic.py<td><td>Generate an image verificaion code. see /results/code.jpg.<td></tr>
    <tr><td>Johnsons.java<td><td>Read data from johnsonsGraphData.txt and run Johnson's algorithm.<td></tr>

</table>
