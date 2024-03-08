from PIL import Image

# temp_pixels = [
#     [(54, 54, 54), (232, 23, 93), (71, 71, 71), (168, 167, 167)],
#     [(204, 82, 122), (54, 54, 54), (168, 167, 167), (232, 23, 93)],
#     [(71, 71, 71), (168, 167, 167), (54, 54, 54), (204, 82, 122)],
#     [(168, 167, 167), (204, 82, 122), (232, 23, 93), (54, 54, 54)],
#     [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0)]
# ]


def image_from_pixels(pixels_list, image_loc, image_name_without_extension):
    if len(image_loc) != 0:
        if image_loc[-1] != "/":
            image_loc += "/"
    # Define image dimensions (width and height)
    width = len(pixels_list[0])
    height = len(pixels_list)

    # Create a new image with RGB mode
    new_image = Image.new("RGB", (width, height))

    # Set pixel values for each row
    for y in range(height):
        for x in range(width):
            new_image.putpixel((x, y), pixels_list[y][x])

    # Save the image to a file (e.g., 'new_image.png')
    new_image.save(image_loc+image_name_without_extension+".png")


def pixels_from_image(image_loc, image_name):
    if len(image_loc) != 0:
        if image_loc[-1] != "/":
            image_loc += "/"
    image = Image.open(image_loc + image_name)
    # Get the dimensions of the image
    width, height = image.size

    # Initialize an empty list to store rows
    rows = []

    # Iterate through each row (height) of the image
    for y in range(height):
        row = []  # Initialize an empty row
        for x in range(width):
            # Get the RGB values for the pixel at (x, y)
            pixel = image.getpixel((x, y))
            row.append(pixel)  # Append the pixel to the row
        rows.append(row)  # Append the row to the list of rows

    return rows
