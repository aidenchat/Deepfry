from PIL import Image, ImageEnhance
import random
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo 

#img_path = "J:\Python_Projects\Images"
filename = ''

def deepfry(contrast, brightness, noise, qual, img_path):
    real_contrast = contrast + 1
    real_brightness = brightness + 1
    if noise <= 0:
        real_noise = 0
    else: real_noise = 2/noise
    real_quality = round(((10-qual) * 8) + 1)
    print('Real quality: ', real_quality)

    #for file in os.listdir(img_path):
        #if file.endswith(".jpg"):
            #filepath = os.path.join(img_path, file)
            #print(filepath)
    img = Image.open(img_path)
    out_name = img_path.strip(".jpg") + "_df_" + str(contrast) + "_" +  str(brightness) + "_" + str(noise) + "_" + str(qual) + ".jpg"
    img = ImageEnhance.Contrast(img).enhance(real_contrast)
    img = ImageEnhance.Brightness(img).enhance(real_brightness)
    
    if real_noise > 0:
        for i in range( round(img.size[0]*img.size[1]*real_noise) ):
            img.putpixel(
                (random.randint(0, img.size[0]-1), random.randint(0, img.size[1]-1)),
                (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            )

    img.save(out_name, format="JPEG", quality=real_quality)
    print("deepfried {} as {}".format(img_path, out_name))
    img.close()

def run():
    while True:
        try:
            contrast_coeff = float(input("Input contrast intensity (0-10): "))
            brightness_coeff = float(input("Input brightness intensity (0-10): "))
            noise_coeff = float(input("Input noise intensity (0-10): "))
            jpeg_quality = float(input("Input the intensity of degradation of the photo (0-10): "))
            deepfry(contrast_coeff, brightness_coeff, noise_coeff, jpeg_quality)
            break
        except Exception as e:
            print(e)
            break

def app():
    window = tk.Tk()
    greeting = tk.Label(
        text="Welcome!\nSelect photo and deepfry it.\n.jpg file accepted.",
        height=5,
        width=20
        )
    greeting.pack()

    open_button = tk.Button(
        window,
        text='Open a File',
        command=select_file
    )
    open_button.pack(expand=True)
    df_button = tk.Button(
        window,
        text='Deepfry It!',
        command=pre_deepfry
    )
    df_button.pack(expand=True)

    window.mainloop()


def select_file():
    filetypes = (
        ('JPEG image', '*.jpg'),
        ('All files', '*.*')
    )

    global filename 
    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes).replace('/', '\\')

    if filename != '': 
        showinfo(
            title='Selected File',
            message=filename
        )

def pre_deepfry():
    if filename != '': 
        deepfry(5, 5, 5, 5, filename) 
    else:
        showinfo(
            title='Error!',
            message='No file selected!'
        )
    


def main():
    app()

if __name__ == "__main__":
    #new comment 13:54 - push to main attempt 
    main()