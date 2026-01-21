#include<iostream>
#include<vector>
using namespace std;
int linearsearch(vector<int>&arr,int n,int ele){
    for(int i=0;i<n;i++){
        if(ele==arr[i]){
            return i;
        }
    }
    return -1;
}
int main(){

    int i,n;
    int ele;
    vector<int>arr;
    cout<<"enter the number of element in the array:";
    cin>>n;
    for(int i=0;i<n;i++){
    
        cin>>ele;
        arr.push_back(ele);
    }
    cout<<"enter the element to be searched:";
    cin>>ele;
    int index=linearsearch(arr,n,ele);
    if(index==-1){
        cout<<"element not found in array";

    }
    else{
        cout<<"element is found at index:"<<index;
    }
    return 0;
}
