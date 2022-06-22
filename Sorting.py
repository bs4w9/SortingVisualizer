#code for the UI was based on tutorial from: https://www.youtube.com/watch?v=XGlRX34KvJ8
from tkinter import *
from tkinter import ttk
import random
import time

root = Tk()
root.title("Sorting Visualization")
root.maxsize(900,600)
root.config(bg='black')

#vars
selected_alg = StringVar()

data = []

def drawData():
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data)+1)
    offset = 10
    spacing = 10
    
    normalizedData = [i / max(data) for i in data]
    
    
    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill='#3CD39F')
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))
        

def Generate():
    data.clear()
    print("Alg Selected: " + selected_alg.get())
    try:
        minVal = int(minEntry.get())
    except:
        minVal = 1
    
    try:    
        maxVal = int(maxEntry.get())
    except:
        maxVal = 10
    try:    
        size = int(sizeEntry.get())
    except:
        size = 10
        
    if minVal > maxVal : minVal , maxVal = maxVal, minVal    
    if minVal < 0 : minVal = 1
    if maxVal > 100 : maxVal = 100
    if size > 30 or size < 3: size = 20

    

    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))
    
    drawData()
    
def bubbleSort():
    
    indexing_length = len(data) - 1
    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if data[i] > data[i+1]: 
                sorted = False
                data[i], data[i+1] = data[i+1], data[i]
                
                updateData()
                
    
def mergeSort():
    
    leftList = data[:len(data)//2]
    rightList = data[len(data)//2:]
    
    #updateData()
    
def Sort():
    if algMenu.get() == "Bubble Sort": bubbleSort()
    if algMenu.get() == "Merge Sort": mergeSort()
    
def updateData():
    drawData()
    canvas.update()
    time.sleep(0.02)
        

frame = Frame(root, width=600, height=200, bg='grey')
frame.grid (row=0, column=0, padx=10, pady=5)


canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1, column=0, padx=10, pady=5)

#UI
#Row 0
Label(frame, text='Algorithm: ', bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(frame, textvariable=selected_alg, values=["Bubble Sort", "Merge Sort"])
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

Button(frame, text="Generate", command=Generate, bg='#3CD39F').grid(row=0, column=2, padx=5, pady=5)
Button(frame, text="Sort", command=Sort, bg='#3CD39F').grid(row=0, column=3, padx=5, pady=5)

#Row 1
Label(frame, text='Size: ', bg='grey').grid(row=1, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Entry(frame)
sizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

Label(frame, text='Min Value: ', bg='grey').grid(row=1, column=2, padx=5, pady=5, sticky=W)
minEntry = Entry(frame)
minEntry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

Label(frame, text='Max Value: ', bg='grey').grid(row=1, column=4, padx=5, pady=5, sticky=W)
maxEntry = Entry(frame)
maxEntry.grid(row=1, column=5, padx=5, pady=5, sticky=W)





root.mainloop()
