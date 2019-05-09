import tkinter as tk
from tkinter import filedialog
import os
from huffman import Huffman


class Application:
    def __init__(self, master=None):

        self.width_screen = master.winfo_width()
        self.height_screen = master.winfo_height()

        self.container1 = tk.Frame(master)
        self.container1.pack()
        self.label_title = tk.Label(self.container1, text="Winrar FLEX")
        self.label_title["font"] = ("Verdana", "40", "bold")
        self.label_title.pack()

        self.container2 = tk.Frame(master)
        self.container2.pack(fill=tk.X)
        self.encode_button = tk.Button(
            self.container2, text="Compactar/Descompactar")
        self.encode_button["command"] = self.browserFile
        self.encode_button.pack(pady="30")

        self.container3 = tk.Frame(master)
        self.container3.pack(fill=tk.X)
        self.label_log = tk.Label(self.container3, text="Logs: ")
        self.label_log["font"] = ("Verdana", "10", "bold")
        self.label_log.pack(side=tk.LEFT, padx="20")

        self.container4 = tk.Frame(
            master, background="white", width=self.width_screen - 20, height=200)
        self.container4.pack()
        self.log = tk.Label(self.container4, background="white", justify=tk.LEFT)
        self.log["font"] = ("Heveltica", "14", "bold")
        self.log.pack(side=tk.TOP, padx="30", pady="10", anchor=tk.NW)
        self.resume = tk.Label(self.container4, background="white",justify=tk.LEFT)
        self.resume["font"] = ("Heveltica", "12")
        self.resume.pack(side=tk.LEFT, padx="30", pady="5", anchor=tk.NW)

        self.container4.pack_propagate(False)

    def browserFile(self):
        filename = filedialog.askopenfilename(
            initialdir=".", title="Selecione a o arquivo", filetypes=(("text files", ".txt"),))

        file = open(filename, "r")

        first_line = file.readline()

        if first_line[:2] == "*(":

            word_dencode = ''

            for line in file:
                word_dencode += line

            dencode = Huffman(word=word_dencode, trim=eval(
                first_line[1:]), dencode=0)

            file_dencode = open(os.path.basename(file.name)[
                                0: -4]+"_dencoded.txt", "w+")
            file_dencode.write(dencode.word_decode)
            
            self.log["text"] = "Descompactação realizada com sucesso!!\n" + \
                                "Verifique o resultado na pasta raiz do projeto."
            self.resume["text"] = ""

        else:
            file.seek(0)

            word_for_encode = ''

            for line in file:
                word_for_encode += line

            encodefy = Huffman(word=word_for_encode)

            file_encode = open(os.path.basename(file.name)[
                0: -4] + "_encoded.txt", "w+")

            file_encode.write("*" + str(encodefy.trim) + "\n")
            file_encode.write(str(encodefy.word_encode))

            self.log["text"] = "Compressão realizada com sucesso!!\n" + \
                                "Verifique o resultado na pasta raiz do projeto."
            self.resume["text"] = "Tamanho antigo do arquivo: " + \
                str(len(encodefy.word)*8) + " bits \n" + "Tamanho atual do arquivo: " + \
                str(len(encodefy.word_encode)) + " bits"

        file.close()


if __name__ == "__main__":

    root = tk.Tk()
    root.title("Winrar FLEX")
    root.geometry("800x400+500+300")
    root.update()
    Application(root)
    root.mainloop()
