var num1=3563;

var result=findreverse(num1);
console.log(result);
function findreverse()
{
    var rev=0;
var rem=0;
while(num1>0)
{
rem=num1%10;
rev=rev*10+rem;
num1=parseInt(num1/10);
}
return rev;
}