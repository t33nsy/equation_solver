#include <bits/stdc++.h>
using namespace std;
double omega = 7, t = 4;

/// @brief Function f = sqrt(l(l-1))+ln(sqrt(l)+sqrt(l-1))-sqrt(2)*omega*t,
/// where l is lambda
/// @param lambda - lambda
/// @return function value
double f(double lambda) {
    if (lambda <= 1) return INFINITY;
    return sqrt(lambda * (lambda - 1)) + log(sqrt(lambda) + sqrt(lambda - 1)) -
           sqrt(2) * omega * t;
}

/// @brief Derivative of the function f(x)
/// @param lambda - lambda
/// @param f - function
/// @return derivative value in the point lambda
double df(double lambda, double (*f)(double) = f) {
    double eps = 1e-10;
    return ((2.0 * lambda - 1.0) / sqrt((lambda - 1.0) * lambda) +
            1.0 / (sqrt(lambda - 1.0) * sqrt(lambda))) /
           2.0;
    // return (f(lambda + eps) - f(lambda - eps)) / (2 * eps);
}

/// @brief bisection method to find zero of the function f(x)
/// @param l - left border
/// @param r - right border
/// @param eps - epsilon, default 1e-15
/// @param f - function, default f(x)
/// @return root of the function
double bisection(double l, double r, double eps = 1e-15,
                 double (*f)(double) = f) {
    cout << "Bisection method, starting with [" << l << "," << r << "]" << endl;
    while (fabs(r - l) / 2 > eps) {
        cout << "Iteration [" << l << "," << r << "]" << endl;
        double m = l + (r - l) / 2;
        double fm = f(m);
        if (fabs(fm) < eps)
            return m;
        else if (fm * f(l) < 0)
            r = m;
        else
            l = m;
    }
    return (l + r) / 2;
}

/// @brief newton's method to find zero of the function f(x)
/// @param x0 - starting point
/// @param eps - epsilon, default 1e-15
/// @param f - function, default f(x)
/// @param df - derivative of the function, default df(x, f)
/// @return root of the function
double newton(double x0, double eps = 1e-15, double (*f)(double) = f,
              double (*df)(double, double (*f)(double)) = df) {
    cout << "Newton's method, starting with " << x0 << endl;
    double fx = f(x0);
    double dfx = df(x0, f);
    if (dfx == 0) cout << "derivative = " << dfx << endl;
    double x1 = x0 - fx / dfx;
    while (fabs(x1 - x0) >= eps) {
        cout << "Iteration " << x0 << " " << x1 << endl;
        x0 = x1;
        fx = f(x0);
        dfx = df(x0, f);
        x1 = x0 - fx / dfx;
        if (fabs(fx) < eps) return x0;
    }
    return x1;
}

int main() {
    cin >> omega >> t;
    double l = 1.01, r = 10;
    // find initial borders
    while (f(l) * f(r) >= 0) {
        ++r;
        if (l > 2) --l;
    }
    double lambda_bi = bisection(l, r);
    double lambda_new = newton((r - l) / 2);
    cout << "Lambda in bisection = " << fixed << setprecision(15) << lambda_bi
         << endl;
    cout << "Lambda in newthon = " << fixed << setprecision(15) << lambda_new
         << endl;
    cout << "|lambda_bisection-lambda_newton|= " << fabs(lambda_bi - lambda_new)
         << endl;
    return 0;
}