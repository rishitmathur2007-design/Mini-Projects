#include<iostream>
using namespace std;
int main()
{   
    int n,amt=0,wit=0;
    while(n!=4)
    {cout<<"\n1-Check Balance"<<endl;
    cout<<"2-Deposit Amount"<<endl;
    cout<<"3-Withdraw Amount"<<endl;
    cout<<"4-Exit"<<endl;
    cout<<"\nEnter your choice:";
    cin>>n;
    switch (n)
    {
    case 1:
        cout<<"Balance:"<<amt<<endl;
        break;
    case 2:
        cout<<"Enter Amount to Deposit:"<<endl;
        cin>>wit;   
        amt+=wit;
        cout<<"Successfully Deposited"<<endl;
        break;
    case 3:
        cout<<"Enter Amount to Withdraw:"<<endl;
        cin>>wit;   
        if (amt>=wit)
        {
            amt-=wit;
            cout<<"Successfully Withdraw"<<endl;
        }
        else
        {
            cout<<"Insufficient Balance"<<endl;
        }
        break;
    case 4:
        cout<<"Bye"<<endl;
        break;
    default:
        cout<<"Enter Valid Number"<<endl;
        break;
    }}
}