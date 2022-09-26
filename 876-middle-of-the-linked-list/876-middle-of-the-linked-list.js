/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var middleNode = function(head) {
    let listLength = 0;
    let find = 0;
    let start1 = head;
    while (start1){
        listLength++;
        start1 = start1.next;
    }
    
    if (listLength/2 === Math.trunc(listLength/2)){
        find = (listLength/2)+1;
    } else {
        find = (listLength/2) +0.5;
    }
    
    let start2 = head;
    for (let i=0; i<find-1; i++){
        start2 = start2.next;
    }
    
    return start2;
};