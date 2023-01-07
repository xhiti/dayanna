class Complex:
    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        isInstance = isinstance(other, Complex)

        if not isInstance:
            return NotImplemented
        else:
            if other.real == self.real and other.imaginary == self.imaginary:
                return True
            return False

    def __repr__(self):
        real = self.real
        imag = self.imaginary

        return f'{"Complex(real=" + str(real) + ", imaginary=" + str(imag) + ")"}'

    def __str__(self):
        sign = ""

        if self.imaginary >= 0:
            sign = "+"
        elif self.imaginary < 0:
            self.imaginary = -1 * self.imaginary
            sign = "-"

        return f'{str(self.real) + " " + sign + " " + str(self.imaginary) + "i"}'

    def __abs__(self):
        a = self.real
        b = self.imaginary

        return float(((a ** 2) + (b ** 2)) ** (1/2))

    def __add__(self, other):
        if type(other) is int:
            return TypeError("TypeError: unsupported operand type(s) for +: 'Complex' and 'int'")

        isInstance = isinstance(other, Complex)
        newComplex = Complex(0, 0)

        if not isInstance:
            return NotImplemented
        else:
            newComplex.real = self.real + other.real
            newComplex.imaginary = self.imaginary + other.imaginary
            return newComplex

    def __iadd__(self, other):
        isInstance = isinstance(other, Complex)

        if not isInstance:
            return NotImplemented
        else:
            self.real = self.real + other.real
            self.imaginary = self.imaginary + other.imaginary
            return self

    @staticmethod
    def add_all(comp, *comps):
        isInstance = isinstance(comp, Complex)
        if not isInstance:
            return NotImplemented
        else:
            newComplex = Complex(0, 0)
            newComplex.real += comp.real
            newComplex.imaginary += comp.imaginary
            for comp in comps:
                if isinstance(comp , Complex):
                    newComplex.real += comp.real
                    newComplex.imaginary += comp.imaginary
                else:
                    return NotImplemented

            return newComplex


c1 = Complex(-1, -2)
c2 = Complex(2, 4)
c3 = Complex(1, 2)


# print("C1 equal to C3, Sum of C1 and C2: ", Complex.__eq__(c1, c3), Complex.__eq__(Complex.__add__(c1, c2), c3))
# print("Complex Number Format: ", Complex.__repr__(c1))
# print("Complex Number 1: ", Complex.__str__(c1))
# print("Abolute Value of C1: ", Complex.__abs__(c1))
# print("Sum of C1 and C2: ", Complex.__add__(c1, c2))
# print("Sum of C1 and C3: ", Complex.__iadd__(c1, c3))
# print("Format of C1: ", Complex.__str__(c1))
# print("Sum of all Complex Numbers: ", Complex.add_all(c2, c2, c3))
# try:
#     print("Summ of c1 with 1: ", Complex.__add__(c1, 1))
# except TypeError as e:
#     print(f"{type(e).__name__}: {e}")