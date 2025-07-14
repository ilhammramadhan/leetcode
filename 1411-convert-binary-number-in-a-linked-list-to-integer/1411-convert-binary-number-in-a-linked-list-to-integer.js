/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {number}
 */
var getDecimalValue = function(head) {
     // 1. Initialize our result to 0.
    let decimalValue = 0;
    
    // 2. Start at the beginning of the list.
    let currentNode = head;

    // 3. Loop until we've fallen off the end of the list.
    while (currentNode !== null) {
        // This is the core logic. It's a common way to process binary numbers.
        // It's equivalent to: decimalValue = (decimalValue * 2) + currentNode.val;
        decimalValue = (decimalValue << 1) | currentNode.val;
        // 4. Move to the next node in the list.
        currentNode = currentNode.next;
    }
    
    // 5. Return the final calculated value.
    return decimalValue;
};