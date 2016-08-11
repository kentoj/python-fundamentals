import fractal
import bmp


def main():
    pixels = fractal.mandelbrot(488, 256)

    bmp.write_grayscale('mandel.bmp', pixels)


if __name__ == '__main__':
    main()
