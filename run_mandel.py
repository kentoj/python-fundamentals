import fractal
import bmp


def main():
    pixels = fractal.mandelbrot(448, 256)

    bmp.write_grayscale('mandel.bmp', pixels)


if __name__ == '__main__':
    main()
