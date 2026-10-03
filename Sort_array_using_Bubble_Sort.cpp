#include<iostream>
#include <vector>
using namespace std;
void bubble_sort(vector <int> &arr)
{
    int l=arr.size();

    for (int i = 0; i <l; i++)
    {
        for (int j = 0; j <l-i-1; j++)
        {
            if (arr[j]>arr[j+1])
            {
                swap(arr[j],arr[j+1]);
            }
        }
    }
}
int main()
{
    int n;
    vector <int> arr;
    cout<<"Enter '0' to stop"<<endl;
    while (true)
    {
        cout<<"ENTER NUMBER:";
        cin>>n;
        if (n!=0)
        {
            arr.push_back(n);
        }
        else
        {
            break;
        }
    }
    bubble_sort(arr);
    for (int i = 0; i < arr.size(); i++)
    {
        cout<<arr[i]<<" ";
    }
    
}