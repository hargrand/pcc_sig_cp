"""mandel.py - Generates a mandelbrot image and saves it to a PNG file"""

from math import fmod
import time
from PIL import Image


def mandel(c: complex, max_iters: int) -> int:
    """
    Determine whether the value c is in the Mandelbrot set

    Args:
        c (complex): The value to check
        max_iters (int): The maximum number of iterations to perform

    Return:
        int: The number of iterations performed
    """
    z = 0.0j
    ctr = 0
    while (z * z.conjugate()).real < 4 and ctr < max_iters:
        z = z * z + c
        ctr += 1
    return ctr


def generate_grid(
    view_center: complex, view_height: float, image_width: int, image_height: int
) -> list[list[complex]]:
    """
    Generate a grid of the complex values to check for inclusion in the mandelbrot set

    Args:
        view_center (complex): The center of the view
        view_height (float): The height of the view
        image_width (int): The width of the image
        image_height (int): The height of the image

    Return:
        list[list[complex]]: The grid of complex values
    """
    scale = image_width / image_height
    view_width = view_height * scale
    left = view_center.real - view_width / 2
    top = view_center.imag + view_height / 2
    delta = view_width / image_width

    grid = [
        [(left + col * delta) + (top - row * delta) * 1j for col in range(image_width)]
        for row in range(image_height)
    ]

    return grid


def generate_data(grid: list[list[complex]], max_iters: int) -> list[list[int]]:
    """
    Generate the data for the image
    Args:
        grid (list[list[complex]]): The grid of complex values
        max_iters (int): The maximum number of iterations to perform

    Return:
        list[list[int]]: The data for the image
    """
    data = [[mandel(c, max_iters) for c in row] for row in grid]
    return data


def generate_colormap(length: int) -> list[int]:
    """
    Generate a colormap of a given length using the HSV color space.

    Args:
        length (int): The number of colors to generate. The last color will be black.

    Returns:
        list[int]: A list of RGB color tuples.
    """
    colormap = []
    for i in range(length):
        red = i / length
        green = fmod(i * 4 / length, 1)
        blue = fmod(i * 16 / length, 1)
        color = int(red * 256) + int(green * 256 * 256) + int(blue * 256 * 256 * 256)
        colormap.append(color)

    colormap.append(0)

    return colormap


def write_image(
    image_width: int,
    image_height: int,
    data: list[list[int]],
    filename: str,
    colormap: list[int] | None = None,
):
    """
    Write the image data to a PNG file
    Args:
        image_width (int): Width of the image to write
        image_height (int): Height of the image to write
        data (list[list[int]]): The data for the image
        filename (str): The name of the file to write to
        colormap (list[int] | None): A list of RGB tuples to color the image.
            If None, a grayscale image is created.
    """
    flat_data = [item for row in data for item in row]
    colordata = [colormap[value] for value in flat_data] if colormap else flat_data
    image_mode = "RGB" if colormap else "L"

    image = Image.new(image_mode, (image_width, image_height))
    image.putdata(colordata)
    image.save(filename)


def main():
    """Main function"""
    view_center = 0j
    view_height = 4
    image_width = 2048
    image_height = 1080
    max_iters = 1024

    print("Generating grid...")
    start = time.time()
    grid = generate_grid(view_center, view_height, image_width, image_height)
    duration = time.time() - start
    print(f"Grid generated in {duration} seconds")

    print("Generating data...")
    start = time.time()
    data = generate_data(grid, max_iters)
    duration = time.time() - start
    print(f"Data generated in {duration} seconds")

    print("Generating colormap...")
    start = time.time()
    colormap = generate_colormap(max_iters)
    duration = time.time() - start
    print(f"Colormap generated in {duration} seconds")

    print("Writing image...")
    start = time.time()
    write_image(image_width, image_height, data, "mandelbrot_color.png", colormap)
    duration = time.time() - start
    print(f"Image written in {duration} seconds")


if __name__ == "__main__":
    main()
