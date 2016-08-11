import fractal
import bmp

pixels = fractal.mandelbrot(488, 256)

bmp.write_grayscale('mandel.bmp', pixels)