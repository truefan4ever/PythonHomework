import unittest
import math
from .pycalc import testing
from .reverse_polish_notation import transformation
from .splitting import string_splitting


class TestPyCalc(unittest.TestCase):
    def test_errors(self):
        self.assertRaises(ValueError, testing, '')
        self.assertRaises(ValueError, testing, '1+')
        self.assertRaises(ValueError, testing, 'pow(2,3,4)')
        self.assertRaises(ValueError, testing, '((2*3)+4')
        self.assertRaises(ValueError, testing, 'factorial(1,2)')
        self.assertRaises(ValueError, testing, 'pow(1)')
        self.assertRaises(ValueError, testing, '2 > = 1')
        self.assertRaises(ValueError, testing, 'fraps(-4)')
        self.assertRaises(ValueError, testing, '1 123')
        self.assertRaises(ValueError, testing, '1>=')
        self.assertRaises(ValueError, testing, '<2')
        self.assertRaises(ValueError, testing, '==')

    def test_splitting(self):
        self.assertEqual(string_splitting("1+1"), [1.0, '+', 1.0])
        self.assertEqual(string_splitting("cos(-sin(pi))"),
                         ['cos', '(', 'neg', 'sin', '(',
                          3.141592653589793, ')', ')'])
        self.assertEqual(string_splitting("pow(-2,sqrt(pow(2,2)))"),
                         ['pow', '(', -2.0, ',', 'sqrt', '(',
                          'pow', '(', 2.0, ',', 2.0, ')', ')', ')'])
        self.assertEqual(string_splitting("3^2>=factorial(3)"),
                         [3.0, '^', 2.0, '>=', 'factorial', '(', 3.0, ')'])
        self.assertEqual(string_splitting("1+-+-+-+-1"), [1.0, '+', 1.0])
        self.assertEqual(string_splitting("+----+-1"), [-1.0])
        self.assertEqual(string_splitting("+-+--+-1"), [1.0])
        self.assertEqual(string_splitting("abs(-4)"), ['abs', '(', -4.0, ')'])
        self.assertEqual(string_splitting("abs(+4)"), ['abs', '(', 4.0, ')'])
        self.assertEqual(string_splitting("cos(+sin(pi))"),
                         ['cos', '(', 'sin', '(',
                          3.141592653589793, ')', ')'])

    def test_rev_pol_not(self):
        self.assertEqual(transformation([1.0, '+', 1.0]), [1.0, 1.0, '+'])
        self.assertEqual(transformation(['cos', '(', 'neg', 'sin', '(',
                                         3.141592653589793, ')', ')']),
                         [3.141592653589793, 'sin', 'neg', 'cos'])
        self.assertEqual(transformation(['pow', '(', -2.0, ',', 'sqrt',
                                         '(', 'pow', '(', 2.0, ',', 2.0,
                                         ')', ')', ')']),
                         [-2.0, 2.0, 2.0, 'pow', 'sqrt', 'pow'])
        self.assertEqual(transformation([3.0, '^', 2.0, '>=',
                                         'factorial', '(', 3.0, ')']),
                         [3.0, 2.0, '^', 3.0, 'factorial', '>='])
        self.assertEqual(transformation([1.0, '+', 1.0]), [1.0, 1.0, '+'])
        self.assertEqual(transformation(['abs', '(', -4.0, ')']),
                         [-4.0, 'abs'])
        self.assertEqual(transformation(['cos', '(', 'sin', '(',
                                         3.141592653589793, ')', ')']),
                         [3.141592653589793, 'sin', 'cos'])

    def test_arithmetic(self):
        self.assertEqual(testing("1+1"), 1 + 1)
        self.assertEqual(testing("2^-3"), 2**-3)
        self.assertEqual(testing("2*-3"), 2 * -3)
        self.assertEqual(testing("1+-+-+-+-1"), 1 + -+-+-+-1)
        self.assertEqual(testing("1+-----+-1"), 1 + -----+-1)
        self.assertEqual(testing("+-----+-1"), +-----+-1)
        self.assertEqual(testing("+-+--+-1"), +-+--+-1)
        self.assertEqual(testing("2-3*5/10+1.5"), 2 - 3 * 5 / 10 + 1.5)
        self.assertEqual(testing("(6+10-4)/(1+1*2)+1"),
                         (6 + 10 - 4) / (1 + 1 * 2) + 1)
        self.assertEqual(testing("1+2*(3+4/2-(1+2))*2+1"),
                         1 + 2 * (3 + 4 / 2 - (1 + 2)) * 2 + 1)
        self.assertEqual(testing("11+(3+4*6+6*1)*2/3"),
                         11 + (3 + 4 * 6 + 6 * 1) * 2 / 3)
        self.assertEqual(testing("5//2"), 5 // 2)
        self.assertEqual(testing("5%3"), 5 % 3)
        self.assertEqual(testing("2^3"), 2 ** 3)
        self.assertEqual(testing("abs(3-10)"), abs(3 - 10))
        self.assertEqual(testing("round(5/2)"), round(5 / 2))
        self.assertEqual(testing("round(1.16,1)"), round(1.16, 1))
        self.assertEqual(testing("(3+4*2)^2"), (3 + 4 * 2) ** 2)
        self.assertEqual(testing("1.1+1.1"), 1.1 + 1.1)
        self.assertEqual(testing("10/3"), 10 / 3)
        self.assertEqual(testing("1-5"), 1 - 5)
        self.assertEqual(testing("666"), 666)
        self.assertEqual(testing("-4"), -4)
        self.assertEqual(testing("abs((3-4*5)+2)"), abs((3 - 4 * 5) + 2))
        self.assertEqual(testing("2+abs((3-4*5)+2)"), 2 + abs((3 - 4 * 5) + 2))
        self.assertEqual(testing("1+round(10.5)"), 1 + round(10.5))
        self.assertEqual(testing("pi*2"), math.pi * 2)
        self.assertEqual(testing("1+sqrt(4)"), 1 + math.sqrt(4))
        self.assertEqual(testing("cos(pi*sqrt(4))"),
                         math.cos(math.pi * math.sqrt(4)))
        self.assertEqual(testing("sin(pi/6)"), math.sin(math.pi / 6))
        self.assertEqual(testing("tan(pi/4)"), math.tan(math.pi / 4))
        self.assertEqual(testing("e"), math.e)
        self.assertEqual(testing("tau*2"), math.tau * 2)
        self.assertEqual(testing("(100)"), (100))
        self.assertEqual(testing("inf"), math.inf)
        self.assertEqual(testing("2+hypot(3,sqrt(16))"),
                         2 + math.hypot(3, math.sqrt(16)))
        self.assertEqual(testing("180+degrees(pi)"),
                         180 + math.degrees(math.pi))
        self.assertEqual(testing("pi+radians(360)"),
                         math.pi + math.radians(360))
        self.assertEqual(testing("exp(2)"), math.exp(2))
        self.assertEqual(testing("e^2"), math.e ** 2)
        self.assertEqual(testing("1+pow(2,3)"), 1 + math.pow(2, 3))
        self.assertEqual(testing("1+log(27,3)"), 1 + math.log(27, 3))
        self.assertEqual(testing("1+log2(128)"), 1 + math.log2(128))
        self.assertEqual(testing("3*log10(1000)"), 3 * math.log10(1000))
        self.assertEqual(testing("log1p(1)"), math.log1p(1))
        self.assertEqual(testing("expm1(2)"), math.expm1(2))
        self.assertEqual(testing("atan2(1,1)"), math.atan2(1, 1))
        self.assertEqual(testing("acosh(1)"), math.acosh(1))
        self.assertEqual(testing("asinh(1)"), math.asinh(1))
        self.assertEqual(testing("atanh(-0.5)"), math.atanh(-0.5))
        self.assertEqual(testing("sinh(1)"), math.sinh(1))
        self.assertEqual(testing("cosh(1)"), math.cosh(1))
        self.assertEqual(testing("tanh(1)"), math.tanh(1))
        self.assertEqual(testing("erf(-1)"), math.erf(-1))
        self.assertEqual(testing("erfc(-1)"), math.erfc(-1))
        self.assertEqual(testing("gamma(inf)"), math.gamma(math.inf))
        self.assertEqual(testing("ceil(-1.1)"), math.ceil(-1.1))
        self.assertEqual(testing("copysign(2,-1)"), math.copysign(2, -1))
        self.assertEqual(testing("pow(-3,3)"), math.pow(-3, 3))
        self.assertEqual(testing("fabs(-4)"), math.fabs(-4))
        self.assertEqual(testing("floor(4.1)"), math.floor(4.1))
        self.assertEqual(testing("fmod(-5,-3)"), math.fmod(-5, -3))
        self.assertEqual(testing("frexp(1)"), math.frexp(1))
        self.assertEqual(testing("isfinite(nan)"), math.isfinite(math.nan))
        self.assertEqual(testing("isinf(1)"), math.isinf(1))
        self.assertEqual(testing("isnan(1)"), math.isnan(1))
        self.assertEqual(testing("modf(1.3)"), math.modf(1.3))
        self.assertEqual(testing("trunc(1.1)"), math.trunc(1.1))
        self.assertEqual(testing("2+fsum(1,11,11,1,1)"),
                         2 + math.fsum([1, 11, 11, 1, 1]))
        self.assertEqual(testing("6-(-13)"), 6 - (-13))
        self.assertEqual(testing("pow(2,pow(3,4))"),
                         math.pow(2, math.pow(3, 4)))
        self.assertEqual(testing("3^2^3"), 3**2**3)
        self.assertEqual(testing("(3^2)^3"), (3**2)**3)
        self.assertEqual(testing("pow(.1,.2)"), math.pow(.1, .2))
        self.assertEqual(testing("pow(.1,-.2)"), math.pow(.1, -.2))

    def test_comparison(self):
        self.assertFalse(testing("-2>1"))
        self.assertTrue(testing("pi!=e"))
        self.assertTrue(testing("sin(pi/sqrt(4))==log(e)"))
        self.assertFalse(testing("fsum(1,2,3)>6"))
        self.assertTrue(testing("1+9*4/3+1!=1+9*4/3+2"))
        self.assertTrue(testing("2+(3*4-4)<=22+((3+2)*4)"))
        self.assertFalse(testing("-1>0"))
        self.assertTrue(testing("1+pow(2,3)>=hypot(3,4)"))
        self.assertTrue(testing("pow(2,sqrt(2^4))==round(abs(-16.328053))"))
        self.assertFalse(testing("factorial(4)<log(32,2)"))
        self.assertTrue(testing("1==1"))
        self.assertTrue(testing("1+1>=factorial(2)"))
        self.assertFalse(testing("2^3==pow(2,4)"))
        self.assertTrue(testing("0!=1"))
        self.assertTrue(testing("log10(1000)>=3"))
        self.assertFalse(testing("pi/2>e"))


if __name__ == '__main__':
    unittest.main()
