from tkinter import*
from compress_module import compress,decompress
from tkinter import filedialog
root = Tk()
root.title('Sintrosoft\'s Compression/Decompression Engine')
root.resizable(width=False, height=False)
canvas=Canvas(root,width=700,height=600)
canvas.pack()

#making fuction
def open_file():
    filename = filedialog.askopenfilename(initialdir='/', title="Select file to compress")
    return filename

def compression(i, o):
    compress(i, o)

def decompression(i,o):
    decompress(i,o)


#making main label
main_label=Label(root,text= "File Compressor/Decompressor",fg = "blue",font=("arial",30))
canvas.create_window(350,50,window=main_label)

#making button
button=Button(root, text="Compress", command = lambda : compression(open_file(),output_entry.get()),font=("arial",15),fg = "green")
canvas.create_window(350,250,window=button)

#making compress output file name
label= Label(root,text="Enter the name of the output file(.txt format):",font=("arial",20),fg = "green")
canvas.create_window(350,150,window=label)
output_entry= Entry(root,width=30)
canvas.create_window(350,200,window=output_entry)

#making output file name decompress
label= Label(root,text="Enter the name of the decompressed file(.txt format):",font=("arial",20),fg = "green")
canvas.create_window(350,400,window=label)
decom_entry= Entry(root,width=30)
canvas.create_window(350,450,window=decom_entry)

#making decompress button
button=Button(root, text="Decompress",font=("arial",15),fg = "green",command= lambda : decompression(open_file(),decom_entry.get()))
canvas.create_window(350,500,window=button)





root.mainloop()