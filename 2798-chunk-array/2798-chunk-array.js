/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let count = 0;
    let chunkedArray = [];
    while(count<arr.length){
        let subArray = [];
        for(let i=count;i<count+size && i<arr.length;i++){
            subArray.push(arr[i]);
        }
        count = count + size
        chunkedArray.push(subArray);
    }
    return chunkedArray;
    
};
