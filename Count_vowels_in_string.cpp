#include<iostream>
#include <string>
using namespace std;
void vowels(string text)
{
    
    string vow="aeiou",VOW="AEIOU";
    char arr[5]={' ',' ',' ',' ',' '};
    int l=text.length(),k=0;
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < l; j++)
        {
            if (text[j]==vow[i]||text[j]==VOW[i])
            {
                k++;
                arr[i]=VOW[i];
            }
        } 
    }
    cout<<"Total Vowels:"<<k<<endl;
    for (int i = 0; i < 5; i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}
int main()
{
    string text;
    cout<<"Enter Text:";
    cin>>text;
    vowels(text);
}