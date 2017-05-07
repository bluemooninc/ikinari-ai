import subprocess
import os
import glob

def execute_unix(inputcommand):
   p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()
   return output

dirname = '/home/pi/ikinari-ai/static/img/*.jpg.txt'
img_path = max(glob.iglob(dirname), key=os.path.getctime)

f = open(img_path)
a = f.read() 
f.close()

# speak aloud
c = 'sudo espeak -ven+f3 -k5 -s110 --punct=".,;?" "%s" 2>>/dev/null' % a #speak aloud

execute_unix(c) 
