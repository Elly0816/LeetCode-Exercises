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
var reverseList = function(head) {
    const items = [];
    //Navigate through the linked list and add each node value to an array
    let list = head;
    
    while (list){
        items.push(list.val);
        list = list.next;
    };
    //Reverse the array
    items.reverse();
    //Add the values to a linked list
    
    let list2 = head;
    
    for (let item of items){
        list2.val = item;
        list2 = list2.next;
    }
    
    return head;
    
};