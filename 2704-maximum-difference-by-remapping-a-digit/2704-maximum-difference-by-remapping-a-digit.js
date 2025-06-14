/**
 * @param {number} num
 * @return {number}
 */
var minMaxDifference = function(num) {
    let strNum = num.toString();
    let maxdDigitToreplace = ''
    let minDigitToreplace = strNum[0];
    let maxStr = strNum
    for (let i = 0 ; i< strNum.length; i++) {
        if (strNum[i] !== '9') {
            maxdDigitToreplace = strNum[i];
            break; 
        }
    }
    
    if (maxdDigitToreplace !== ''){
         maxStr = strNum.replaceAll(maxdDigitToreplace, '9');
    }
   
    const maxVal = parseInt(maxStr, 10);
    const minStr = strNum.replaceAll(minDigitToreplace, '0');
    const minVal = parseInt(minStr, 10);
    console.log(maxVal, minVal)
    return maxVal - minVal;
};