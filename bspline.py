import numpy as np


class BSpline:

    def __init__(self, controls, degree=3):
        self._controls = None
        self._n = None
        self.controls = controls

        self._nodal = None
        self._k = None

        self.k = degree

    @property
    def controls(self):
        return self._controls

    @controls.setter
    def controls(self, value):
        self._controls = [np.array(p).transpose() for p in value]
        self._n = len(self._controls)

    @property
    def n(self):
        return self._n

    @property
    def k(self):
        return self._k

    @k.setter
    def k(self, value):
        self._k = value
        self._nodal = [i for i in range(self.n + self.k)]

    def close(self):
        for i, v in enumerate(self._nodal):
            if i < self.k:
                self._nodal[i] = 0
            elif i <= self.n:
                self._nodal[i] -= self.k - 1
            else:
                self._nodal[i] = self._nodal[self.n]

    def __shift(self, u):
        i = self.k
        dec = 0
        while u > self._nodal[i]:
            i += 1
            dec += 1
        return dec

    def __initial(self, dec):
        return [self.controls[dec + i] for i in range(self.k)]

    def compute(self, u):
        dec = self.__shift(u)
        f = self.__initial(dec)
        k = self.k
        j = 0
        while k > 0:
            for i in range(k - 1):
                a = self._nodal[dec + i + j + 1]
                b = self._nodal[dec + i + j + k]
                f[i] = ((b - u) / (b - a)) * f[i] + ((u - a) / (b - a)) * f[i + 1]
            j += 1
            k -= 1
        return f[0]

    def compute_range(self, step=0.01):
        return [self.compute(u) for u in np.arange(self._nodal[self.k - 1], self._nodal[self.n], step)]
