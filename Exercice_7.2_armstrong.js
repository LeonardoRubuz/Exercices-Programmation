let n= 10000;
for(let i=0; i<n; i++) {
    i= i.toString();
    let sum= 0;
    for(let j=0; j<i.length; j++) {
        sum+= Math.pow(i[j],3);
    }
    if(sum==i) {
        console.log(i);
    }
}