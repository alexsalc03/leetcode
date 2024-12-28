#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
num1 = None
num2 = None
result = None
class Nodo:
    def __init__(self,valore):
        self.valore = valore
        self.next = None


class Linkedlist:

    def __init__(self):
        self.head = None

    def append(self,valore):
        new_node = Nodo(valore)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current=current.next
        current.next=new_node

    def print_list(self):
        corrente = self.head
        while corrente:
            print(corrente.valore, end=" -> ")
            corrente = corrente.next
        print("None")

    def turn_to_int(self):
        numeri = []
        current = self.head
        while current:
            numeri.append(str(current.valore))
            current = current.next
        return int(''.join(numeri[::-1]))


l1=Linkedlist()
l1.append(2)
l1.append(4)
l1.append(3)

l2=Linkedlist()
l2.append(5)
l2.append(6)
l2.append(4)

print("l1:")
l1.print_list()

print("l2:")
l2.print_list()


num1 = l1.turn_to_int()
num2 = l2.turn_to_int()

result = num1+num2
print(f"[{result}]")

# explanation: I create two lists, i iterate on them in reverse way and save the numbers inside two different string
# after that , i convert the strings into integers andsum both in a new integer.