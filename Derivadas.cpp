#include <iostream>
#include <iomanip>
#include <cmath>

using namespace std;

double Forward(double (*f)(double), double x, double deltaX, int derivada) {
    if (derivada == 1) {
        return (f(x + deltaX) - f(x)) / deltaX;
    }
    return  (Forward(f, x + deltaX, deltaX, derivada - 1) - Forward(f, x, deltaX, derivada - 1)) / deltaX;
}

double Center(double (*f)(double), double x, double deltaX, int derivada) {
    if (derivada == 1) {
        return (f(x + deltaX) - f(x - deltaX)) / (2 * deltaX);
    }
    return (Center(f, x + deltaX, deltaX, derivada - 1) - Center(f, x - deltaX, deltaX, derivada - 1)) / (2 * deltaX);
}

double Backward(double (*f)(double), double x, double deltaX, int derivada) {
    if (derivada == 1) {
        return (f(x) - f(x - deltaX)) / deltaX;
    }
    return (Backward(f, x, deltaX, derivada - 1) - Backward(f, x - deltaX, deltaX, derivada - 1)) / deltaX;
}

double f1(double x) {
    return (exp(-4*x) * cos(x));
}


int main()
{

    int opcao;
    int grau_derivacao;
    double x;
    double delta_x;

    cout << "Digite o valor de x: ";
    cin >> x;

    cout << "Digite o valor de delta_x: ";
    cin >> delta_x;

    while (true) {
        cout << "Digite o grau da derivacao: ";
        cin >> grau_derivacao;
        if (grau_derivacao > 0)
            break;
        else
            cout << "Entrada invalida. O grau da derivacao deve ser positivo." << endl;
    }   

    double fw = Forward(&f1, x, delta_x, grau_derivacao);
    double bw = Backward(&f1, x, delta_x, grau_derivacao);
    double ce = Center(&f1, x, delta_x, grau_derivacao);
    cout << endl;
    cout << "Derivada de grau " << grau_derivacao << endl;
    cout << "Filosofia Forward: " << fw << endl;
    cout << "Filosofia Backward: " << bw << endl;
    cout << "Filosofia Central: " << ce << endl;
}
