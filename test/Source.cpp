#include <fstream>
#include <iostream>
using namespace std;

const int MYCONST;

namespace Foo {
    namespace Bar {
    }
}
namespace egorka {
}

void somEEEfunction(int a, void *b) { return; }

double anotherfunction()
{
    int a = 0;
    int b = a;
    return (double)b;
}

SomeClass::Constructor() : aaaaaaaa(aaaaaaaa), aaaaaaaa(aaaaaaaa), aaaaaaaa(aaaaaaaaaaaaaaaaaaaaaaaaa) { return 0; }

class myclass
{
  public:
    int x;

    myclass();
}

int main()
{
    int n;
    int i = 0;
    int j = 0;
    cout << "\n Vvedite rezmernost matrici";
    cin >> n;
    int **matrEca;
    matr = new int *[n];
    if(matr[i] = NULL) {
        cout << "Nesozdandinamicheskiymassiv";
        return 0;
    }
    for(int i = 0; i < n; i++) {
        matr[i] = new int[n];
        if(matr[i] = NULL) {
            cout << "Ne sozdan dinamicheskiy massiv";
            return 0;
        }
    }
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cout << "vvedite massiv";
            cin >> matr[i][j];
        }
    }
    int *har;
    har = new int[n];
    for(i = 0; i < n; i++) {
        har[i] = 0;
        for(j = 0; j < n; j++) {
            if((matr[i][j] % 2 == 0) && (matr[i][j] > 0)) {
                har[i] += matr[i][j];
            }
        }
    }
    int *rab;
    int min;
    for(i = 0; i < n; i++) {
        min = har[i];
        for(j = i; j < n; j++)
            if(min > har[i]) {
                min = har[i];
                i = j;
            }
        har[j] = har[i];
        har[i] = min;
        rab = matr[i];
        matr[i] = matr[j];
        matr[j] = rab;
    }
    for(i = 0; i < n; i++) {
        for(j = 0; j < n; j++) {
            cout << "matrica:" << matr[i][j];
        }
    }

    switch(var) {
    case 0:
    case 1:
    case 2: {
        dosomething();
        break;
    }
    case 4: {
        do_something_else();
        break;
    }
    default: {
    /*...*/}
    }

    x = *p;
    p = &x;
    x = r.y;
    x = r->y y = x + z--;
    y = x == 0 ? 1 : 0;

    return 0;
}