# Problem Link : https://leetcode.com/problems/perfect-squares/


int numSquares(int n){
    if (ceil(sqrt(n)) == floor(sqrt(n)))
        return 1;
    int num = n;
    while (num % 4 == 0)
        num /= 4;
    if (num % 8 == 7)
        return 4;
    for(int i; i * i <= n; i++) {
        num = n - (i * i);
        if (ceil(sqrt(num)) == floor(sqrt(num)))
            return 2;
    }
    return 3;

}