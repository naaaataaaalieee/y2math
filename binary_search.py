import tkinter as tk

window = tk.Tk()
window.title("Binary search")

frame = tk.Frame(window)
frame.grid()

def display_arr (arr, row_, mid_index=-1):
    for i in range (len(arr)):
        if i == len(arr)//2:
            tk.Label(frame, text=str(arr[i]), fg="yellow", bg="black").grid(row=row_, column=i+4)
        else:
            tk.Label(frame, text=str(arr[i]), fg="white", bg="black").grid(row=row_, column=i+4)

def visualbin ():
    global frame
    frame.destroy()

    arr = array.get().split(",")
    target = target_.get()

    arr = [int(x) for x in arr]
    arr.sort()

    target = int(target)

    curr_row = 10
    lower_bound = 0
    upper_bound = len(arr)-1

    frame = tk.Frame(window)
    frame.grid(row=curr_row)

    display_arr(arr, curr_row+1)
    curr_row += 1

    found = False

    while lower_bound <= upper_bound:
        mid = (lower_bound+upper_bound)//2
        tk.Label(frame, text="Mid: "+str(arr[mid]), fg="yellow", bg="black").grid(row=curr_row, column=1)
        display_arr(arr[lower_bound:upper_bound+1], curr_row, mid)

        if arr[mid] == target:
            tk.Label(frame, text="Found!").grid(row=curr_row+2, column=1)
            found = True
            break
        elif arr[mid] > target:
            upper_bound = mid-1
        else:
            lower_bound = mid+1
        curr_row += 2

    if not found:
        tk.Label(frame, text="Not found!").grid(row=curr_row+2, column=1)


tk.Label(window, text="Visualizing binary search", fg="white",
         bg="black").grid(row=1)

array = tk.StringVar()
array.set("1,2,3")

target_ = tk.StringVar()
target_.set("0")

tk.Label(window, text="Enter the array (separated by commas): ").grid(row=2)
tk.Entry(window, textvariable=array).grid(row=2, column=1)

tk.Label(window, text="Enter the target: ").grid(row=3)
tk.Entry(window, textvariable=target_).grid(row=3, column=1)

tk.Button(window, text="Confirm entry",command=visualbin).grid(row=4)
