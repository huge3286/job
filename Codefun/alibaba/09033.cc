#include<bits/stdc++.h>
using namespace std;
#define int long long 
#define pb push_back 
#define MAXN 120000
int s[120000];
int Parent[MAXN];


map<int,int> mp;

void init(int n){
    for(int i=0;i<n;i++){
        Parent[i]=i;        
    }
}

// 并查集
int find(int x){
    if(Parent[x]==x)
        return x;
    else{
            Parent[x]=find(Parent[x]);   
            return Parent[x];
    }
}
void merge(int i,int j){
    Parent[find(j)] = find(i);
}

signed main() {
	int n;
	cin>>n;
	for(int i=1;i<=n;i++){
		cin>>s[i];
	}
	init(MAXN);
	int ans=0;
	for(int i=0;i<n-1;i++)
	{
		int lin,lin1;
		cin>>lin>>lin1;
		if(s[lin]==s[lin1])
		merge(lin,lin1);
	}
	for(int i=1;i<=n;i++){
		mp[find(i)]++;
	}
	int p=0;
	for(auto i : mp){
		if(s[i.first]==3){
			ans+=(i.second)*(i.second-1)/2*3;
		}
		else{
			ans+=(i.second)*(i.second-1)/2*5;
		}
		p+=15*(n-i.second)*(i.second);
	}
	cout<<ans+p/2<<endl; 
	return 0;
}
