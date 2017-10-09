from PIL import Image
import glob

infile = "/home/pi/ikinari-ai/tmp.jpg"
outpath =  "/home/pi/ikinari-ai/static/img/"
files = glob.glob(outpath+'*.jpg')
outfile = outpath+'img'+'%d'%(len(files))+'.jpg'
print 'moveresize to:'+outfile
img = Image.open(infile).resize((640,480))
half_the_width = img.size[0] / 2
half_the_height = img.size[1] / 2
img.crop(
    (
        half_the_width - 200,
        half_the_height - 200,
        half_the_width + 200,
        half_the_height + 200
    )
).save(outfile)
