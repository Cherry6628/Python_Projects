def draw_image(
        filename,
        path_loc="",
        pen_color="white",
        outline_color='white',
        bg_color="black",
        thickness=12,
        canvas_h=500,
        canvas_w=500,
        save_h=None,
        save_w=None,
        pen_motion_type="<B1-Motion>",
        image_mode='RGB'
):
    if (save_h is None) and (save_w is None):
        save_h, save_w = canvas_h, canvas_w
    import tkinter as tk
    from PIL import Image, ImageDraw

    def save_image(canvas, pathway, filename):
        # Get the canvas dimensions
        canvas_height = save_h
        canvas_width = save_w
        """canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()"""

        # Create a new image with the same dimensions as the canvas
        img = Image.new(image_mode, (canvas_width, canvas_height), bg_color)

        # Create a drawing context
        draw = ImageDraw.Draw(img)

        # Get a list of all items on the canvas
        items = canvas.find_all()

        for item in items:
            # Get the coordinates of the item
            coords = canvas.coords(item)

            # Draw a white circle at the item's coordinates
            draw.ellipse([coords[0], coords[1], coords[2], coords[3]], fill=pen_color)
        # Define the path where you want to save the image
        path = f"{pathway+filename}.png"

        # Save the image
        img.save(path, 'PNG')
        return path

    def draw(event):
        x1, y1 = (event.x - thickness), (event.y - thickness)
        x2, y2 = (event.x + thickness), (event.y + thickness)
        canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline=outline_color, width=thickness)

    root = tk.Tk()
    canvas = tk.Canvas(root, width=canvas_w, height=canvas_h, bg=bg_color)
    canvas.pack()

    canvas.bind(pen_motion_type, draw)

    def on_closing():
        name = filename
        path_ = path_loc
        try:
            if name != "":
                path = save_image(canvas, path_, name)
                print(f"Image saved at {path}")
            else:
                print("Your Image wasn't saved ! ")
        except FileNotFoundError as e:
            print(FileNotFoundError.__name__, f": {e}")
        except PermissionError as e:
            print(PermissionError.__name__, f": {e}")
        except IsADirectoryError as e:
            print(IsADirectoryError.__name__, f": {e}")
        except Exception as e:
            print("An unexpected error occurred :", e)
        finally:
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()


#####################  Custom_Variables  #####################
pathway = ""
for i in range(int(input("Total Number of Images >> "))):
    image_name = input("Image Name without Extension >> ")
    if image_name == "":
        image_name = f"image{i:05}"
    draw_image(path_loc=pathway, filename=image_name)
##############################################################
