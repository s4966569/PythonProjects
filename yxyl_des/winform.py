from tkinter import *
import base64, pyDes

root = Tk()
# topFrame = Frame(root)
# topFrame.pack()


inputContent = Text(root,height=15)
inputContent.pack()

resultContent = Text(root,height=15)
resultContent.pack();


def decrypt():
    resultContent.delete("1.0", END)
    encrypt_data = inputContent.get("1.0", END)
    base64_data = base64.b64decode(encrypt_data)
    des_key = pyDes.des("ws3edaw4", pyDes.ECB, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
    decrypt_data = des_key.decrypt(base64_data, padmode=pyDes.PAD_PKCS5)
    resultContent.insert(END, decrypt_data.decode('utf8'))
    # print("hell world")

def copy():
    text = resultContent.get("1.0", END)
    root.clipboard_clear()
    root.clipboard_append(text)


button1 = Button(root, text="开始解密", fg="red", command=decrypt)
button1.pack()

button2 = Button(root, text="复制结果", fg="green", command=copy)
button2.pack()

root.mainloop()



