#include<iostream>
using namespace std;

int main(){
    char vocal;
    cout<<"Ingrese una vocal"<<endl;
    cin>>vocal;
    switch (vocal)
    {
    case 'a':
    case 'e':
    case 'i':
    case 'o':
    case 'u':
        cout<<vocal;
        break;
    default:
        cout<<"Error";
        break;
    }
}