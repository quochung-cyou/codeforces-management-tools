#include<iostream>
#include<math.h>
 
using namespace std;
long long tree[10000];
int main(){
    long long n;
    cin >> n;
    long long result;
   tree[1] = 1;
   tree[2] = 4;
    for(int i = 3; i < n + 1; i++){
       tree[i] = (4*tree[i - 1] - tree[i - 2])%1000000007;
    }
    result =tree[n];
    cout << result;
}