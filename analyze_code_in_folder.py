"""Check all the Python code files in a folder and its subfolders.
Count code lines, blank lines and annotation lines of every file.
Write results into a txt file
Note:
This code takes all files into consideration, but it is correct only when the file
is in Python code, which means you can not use it to count a Java code etc. But a wrong result will
show up in output txt if the Java(or something else) file is in the folder.
If a line contains both annotation and code, it is counted as a code line, and annotation
line number will not increment.
Code in Python3
"""
import os
import sys
global annotation_flag
annotation_flag = False

walk_dir = sys.argv[1]
print ("walk_dir = "+walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

def blank_row(s):
    s = s.strip("\n\r\t")
    if len(s) == 0:
        return True
    else:
        return False
def annotation_row(s):
    s = s.strip("\n\r\t")
    slist = s.split()
    global annotation_flag
    if annotation_flag == False:
        if slist[0].startswith('#'):
            return True
        elif slist[0].startswith('\"\"\"'):
            annotation_flag = True
            return True
        else:
            return False
    else:
        if slist[-1].endswith('\"\"\"'):
            annotation_flag= False
            return True
        else:
            return True

for root, subdirs, files in os.walk(walk_dir):
    print('--\nroot = ' + root)
    result_file_path = os.path.join(root, 'analyze_result.txt')
    print('result_file_path = ' + result_file_path)
    with open(result_file_path, 'wb') as result_file:
        for subdir in subdirs:
            print('\t- subdirectory ' + subdir)
        for filename in files:
            blank=0
            code=0
            annotation=0
            file_path = os.path.join(root, filename)
            print('\t- file %s (file path: %s)' % (filename, file_path))
            with open(file_path) as f :
                for line in f:

                    if blank_row(line) == True:
                        blank = blank+1
                    elif annotation_row(line) == True:
                        annotation = annotation+1
                    else:
                        code = code+1
            result_file.write(('The file %s contains:\n' % filename).encode('utf-8'))
            result_file.write(('%s blank lines\n' % blank).encode('utf-8'))
            result_file.write(('%s annotation lines\n' % annotation).encode('utf-8'))
            result_file.write(('%s code lines\n' % code).encode('utf-8'))
            result_file.write(b'\n')
            f.close()
    result_file.close()
