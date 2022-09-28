/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function(head) {
    let fast = head;
    let slow = head;
    
    if (!fast){
        return fast;
    }
    
    while (fast.next && fast.next.next){
        slow = slow.next;
        fast = fast.next.next;
        if (fast === slow){
            break;
        }
    }
    
    if(!fast.next){
        return fast.next;
    }
    
    if (!fast.next.next){
        return fast.next.next;
    }
    
    let slow2 = head;
    
    while (true){
        if (slow2 === slow){
            return slow;
        } else {
            slow = slow.next;
            slow2 = slow2.next;
        }
    }
    
};