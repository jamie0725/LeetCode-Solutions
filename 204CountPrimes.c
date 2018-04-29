/*
 * Count the number of prime numbers less than a non-negative number, n.
 */ 

int countPrimes(int n) {  
    if(n<2)return 0;  
    int *prime=(int *)malloc(n*sizeof(int));  
    for(int i=0;i<n;i++)  
        prime[i]=1;  
    prime[0]=prime[1]=0;  
    int k=0;  
    int j;  
    for(int i=2;i*i<n;i++){  
      if(prime[i]!=1)continue;//是素数？  
    for(j=i*i;j<n;j+=i)//小于n?,小于的话将该素数的平方及其平方后+该素数的定位合数  
        prime[j]=0;  
    }  
    for(j=0;j<n;j++)  
        if(prime[j]==1)k++;  
return k;  
}  
