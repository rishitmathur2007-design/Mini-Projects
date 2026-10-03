#include<iostream>
using namespace std;
int main()
{
    int arr[10],n;
    for (int i = 0; i <10; i++)
    {
        cout<<"Enter Number:";
        cin>>arr[i];
    }
    cout<<"\nOriginal Array"<<endl;
    for (int i = 0; i < 10; i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    cout<<"\nReverse Array"<<endl;
    for (int i = 0; i <5; i++)
    {
        swap(arr[i],arr[9-i]);
    }
    for (int i = 0; i < 10; i++)
    {
        cout<<arr[i]<<" ";
    }
    
    
    
}