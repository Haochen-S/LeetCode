# Done
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        list_a = []
        list_b = []
        while (l1 != None):
            list_a.append(l1.val)
            l1 = l1.next
            
        while (l2 != None):
            list_b.append(l2.val)
            l2 = l2.next

        num1 = 0
        num2 = 0
        
        i = len(list_a) - 1
        while (i >= 0):
            if (i == 0):
                num1 += list_a[i]
            else:
                num1 += list_a[i] * (10 ** i)
            i -= 1
        
        i = len(list_b) - 1
        while (i >= 0):
            if (i == 0):
                num2 += list_b[i]
            else:
                num2 += list_b[i] * (10 ** i)
            i -= 1
        
        total = num1 + num2
        total_list_node = ListNode()

        while (total >= 10):
            ge_wei_shu = total % 10
            if (total_list_node.next == None):
                total_list_node.val = ge_wei_shu
                total_list_node.next = ListNode()

            else:
                curr = total_list_node.next
                while (curr.next != None):
                    curr = curr.next
                curr.val = ge_wei_shu
                curr.next = ListNode()

                
            total = (total - ge_wei_shu) / 10

        curr = total_list_node
        while (curr.next != None):
            curr = curr.next
        curr.val = total

        return total_list_node
# Done
