function fact(n) {
    let sum1=1, sum2=1;
    for(let i=2; i<=n; i+=2) {
        sum1*=i;
    }
    for(let i=1; i<=n; i+=2) {
        sum2*=i;
    }
    console.log(sum1);
    console.log(sum2);
}
fact(100);