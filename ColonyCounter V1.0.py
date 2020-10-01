from tkinter import *
from matplotlib import pyplot as plt
from skimage import data
from skimage.feature import blob_dog, blob_log, blob_doh
from math import sqrt
from skimage.color import rgb2gray
import glob
from skimage.io import imread

#Image processing function
def ip(path):
    example_file = glob.glob(path)[0]
    im = imread(example_file, as_grey=True)
    #plt.imshow(im)
    #plt.show()
    blobs_log = blob_log(im, max_sigma=30, num_sigma=10, threshold=.1)
    # Compute radii in the 3rd column.
    blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
    numrows = len(blobs_log)
    return numrows
    fig, ax = plt.subplots(1, 1)
    #plt.imshow(im)
    for blob in blobs_log:
        y, x, r = blob
        c = plt.Circle((x, y), r+5, color='lime', linewidth=2, fill=False)
        ax.add_patch(c)

#GUI function for submit button
def retrieve_input():
    filename=entry_1.get()
    out="No of colonies: "+str(ip(filename))
    label_2 = Label(root, text=out,width=20,font=("bold", 10))
    label_2.place(x=220,y=180)

#GUI function for Clear button
def clear():
    v.set("")

#GUI function for Exit button
def ext():
    root.destroy()

#GUI builder
root = Tk()
v=StringVar()
root.geometry('500x500')
root.title("Colony Counter")

label_0 = Label(root, text="Colony Counter",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="Enter Filename: ",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root, textvariable=v)
entry_1.place(x=240,y=130)

cnt=Button(root, text='Count',width=20,bg='brown',fg='white',command=retrieve_input).place(x=180,y=250)

clr=Button(root, text='Clear',width=20,bg='brown',fg='white',command=clear).place(x=180,y=300)

ext=Button(root, text='Exit',width=20,bg='brown',fg='white',command=ext).place(x=180,y=350)

root.mainloop()






















