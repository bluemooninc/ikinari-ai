from PIL import Image
import glob

infile = "/home/pi/ikinari-ai/tmp.jpg"
outpath =  "/home/pi/ikinari-ai/static/img/"
files = glob.glob(outpath+'*.jpg')
outfile = outpath+'img'+'%d'%(len(files))+'.jpg'
print 'moveresize to:'+outfile
Image.open(infile).resize((480,360)).crop((80,20,400,340)).save(outfile)
