class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            temp = self.top.data
            self.top = self.top.next
            return temp


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 0. 빈 리스트 예외 처리
        if not head:
            return None

        # 1. 스택에 모든 노드 넣기 (기존 코드 유지)
        stack = Stack()
        current = head
        while current:
            stack.push(current)
            if current.next == None:
                break
            else:
                current = current.next

        # 2. 첫 번째로 꺼낸 노드가 뒤집힌 리스트의 새로운 시작점(ListNode)이 됩니다.
        new_head = stack.pop()
        current = new_head

        # 3. 스택이 빌 때까지 꺼내면서 뒤로 연결(.next)해줍니다.
        while not stack.is_empty():
            current.next = stack.pop()  # 다음 노드 연결
            current = current.next  # 포인터 이동

        # 4. 원래 첫 번째였던 노드(현재 마지막 노드)의 next를 None으로 끊어줍니다. (무한 루프 방지)
        current.next = None

        # 5. 뒤집힌 리스트의 head(ListNode)를 반환합니다.
        return new_head



            
            

        
        
            
            
       
        
        
        
            