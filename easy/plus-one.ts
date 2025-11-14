// https://leetcode.com/problems/plus-one/ 
function plusOne(digits: number[]): number[] {
    // Start a loop from right to left looking for the first non-9 value you run to
    var idx = digits.length - 1;

    while(idx >= 0){
        // If you find the first non-9 value, increment it by 1 and return the array
        // Your business ends here
        if(digits[idx] < 9){
            digits[idx] += 1;
            return digits;
        }

        // Otherwise, it means you ran into a 9, convert it into zero and resume your loop
        digits[idx] = 0
        idx -= 1;
    }

    // If you reach the end of the loop and you havent returned anything
    // then it means you ran into a 999, 9999 situation, 
    // which were then converted to 0s, i.e 000 and 0000 respectively, 
    // therefore all you have to do here is prepend 1 at the beginning of the array
    // and return the whole array post mutation

    // I'm sure there's a better way to do this in TS
    var res = [1];

    for(var i = 0; i < digits.length; i+=1){
        res.push(0);
    }

    return res;
};
