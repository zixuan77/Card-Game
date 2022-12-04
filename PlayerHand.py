from Card import Card

class PlayerHand:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def getTotalCards(self):
        return self.size
    
    def getMin(self):
        current = self.root
        while current is not None and current.getLeft() is not None:
            current = current.left
        return current

    def _getMin(self, root):
        current = root
        while current is not None and current.getLeft() is not None:
            current = current.left
        return current

    def get(self, suit, rank):
        if self.root:
            res = self._get(suit, rank, self.root)
            if res:
                return res
            else:
                return None
        else:
            return None
        

    def _get(self, suit, rank, currentnode):
        card = Card(suit, rank)
        if not currentnode:
            return None
        elif card == currentnode:
            return currentnode
        elif card < currentnode:
            return self._get(suit, rank, currentnode.left)
        else:
            return self._get(suit, rank, currentnode.right)      


    def getSuccessor(self, suit, rank):
        current = self.get(suit, rank)
        if current is None:
            return current
        right = current.getRight()
        if right is not None:
            temp = right.getLeft()
            while temp is not None:
                right = temp
                temp = right.getLeft()

        parent = None
        tmpParent = current
        while tmpParent is not None and not tmpParent > current:
            tmpParent = tmpParent.getParent()
        if tmpParent is not None and tmpParent > current:
            parent = tmpParent
        if right is None:
            return parent
        if parent is None:
            return right
        if right < parent:
            return right
        else:
            return parent


    def put(self, suit, rank):
        self.size += 1
        if self.root:
            self._put(suit, rank, self.root)
        else:
            cardTmp = Card(suit, rank)
            self.root = cardTmp

    def _put(self, suit, rank, currentNode):
        cardTmp = Card(suit, rank)
        if cardTmp < currentNode:
            if currentNode.getLeft():
                self._put(suit, rank, currentNode.getLeft())
            else:
                currentNode.setLeft(cardTmp)
        elif cardTmp == currentNode:
            currentNode.setCount(currentNode.getCount()+1)
        else:
            if currentNode.getRight():
                self._put(suit, rank, currentNode.getRight())
            else:
                currentNode.setRight(cardTmp)


    def delete(self, suit, rank):
        current = self.get(suit, rank)
        if current is None:
            return False
        self.size -= 1
        if current.getCount() > 1:
            current.setCount(current.getCount()-1)
            return True
        self._delete(self.root, suit, rank)
        return True


    def _delete(self, root, suit, rank):
        cardTmp = Card(suit, rank)
        if root is None:
            return
        if cardTmp < root:
            self._delete(root.getLeft(), suit, rank)
        elif cardTmp > root:
            self._delete(root.getRight(), suit, rank)
        else:
            if root.getLeft() and root.getRight():
                temp  = self._getMin(root.getRight())
                root.suit = temp.suit
                root.rank = temp.rank
                root.count = temp.count
                if temp.isLeft():
                    temp.getParent().setLeft(temp.getRight())
                elif temp.isRight():
                    temp.getParent().setRight(temp.getRight())
            elif not root.getRight():
                if root.isLeft():
                    root.getParent().setLeft(root.getLeft())
                elif root.isRight():
                    root.getParent().setRight(root.getLeft())
                else:
                    self.root = root.getLeft()
                    if self.root is not None:
                        self.root.setParent(None)
            elif not root.getLeft():
                if root.isLeft():
                    root.getParent().setLeft(root.getRight())
                elif root.isRight():
                    root.getParent().setRight(root.getRight())
                else:
                    self.root = root.getRight()
                    if self.root is not None:
                        self.root.setParent(None)




    def isEmpty(self):
        return self.root is None

    def inOrder(self):
        ret = self._inOrder(self.root)
        output = ''
        for item in ret:
            output +=str(item)
        return output

    def _inOrder(self, node):
        ret = []
        if node is not None:
            ret += self._inOrder(node.getLeft())
            ret += [node]
            ret += self._inOrder(node.getRight())
        return ret

    def preOrder(self):
        ret = self._preOrder(self.root)
        output = ''
        for item in ret:
            output += str(item)
        return output

    def _preOrder(self, node):
        ret = []
        if node is not None:
            ret += [node]
            ret += self._preOrder(node.getLeft())
            ret += self._preOrder(node.getRight())
        return ret
