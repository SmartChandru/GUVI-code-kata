#include<stdio.h>
  
int main(){
int n,k=0,i;
char a[100000],b[100000];
scanf("%s%s%d", a,b,&n);
for(i=0;a[i]!='\0';i++){
if(a[i]!=b[i]){
k++;
}
}
if(k==n) printf("yes");
else printf("no");
return 0;
}
