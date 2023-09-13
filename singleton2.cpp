#include <iostream>
using namespace std;

class LavarropasSingleton
{
public:
    // Método para obtener la única instancia del Singleton
    static LavarropasSingleton *GetInstance()
    {
        // Static garantiza que haya solo una instancia en toda la vida del programa
        static LavarropasSingleton instance;
        cout << "La Instancia es: " << &instance << endl;
        return &instance;
    }

    // Variables miembro públicas
    int a, b, c;

private:
    // Constructor privado para evitar instancias fuera de la clase
    LavarropasSingleton() : a(0), b(0), c(0)
    {
        cout << "Instancia Singleton creada." << endl;
    }

    // Destructor privado para evitar la destrucción accidental
    ~LavarropasSingleton()
    {
        cout << "Instancia Singleton destruida." << endl;
    }
};

int main()
{
    // Obtener la instancia del Singleton
    LavarropasSingleton *lavado1 = LavarropasSingleton::GetInstance();
    LavarropasSingleton *lavado2 = LavarropasSingleton::GetInstance();

    // Modificar variables miembro del Singleton
    lavado1->a = 1;
    lavado2->b = 2;

    // Imprimir valores de las variables miembro
    cout << "Pedro ha reservado la Lavadora: " << lavado1->a << " para el martes 19/09 a las 12:00" << endl;
    cout << "Maria ha reservado la Lavadora: " << lavado2->b << " para el lunes 23/10 a las 08:45" << endl;

    return 0;
}
