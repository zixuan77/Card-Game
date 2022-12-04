class Card:
    def __init__(self, suit, rank):
        self.suit = suit.upper()
        self.rank = rank.upper()
        self.parent = None
        self.left = None
        self.right = None
        self.count = 1
    
    def getSuit(self):
        return self.suit
    
    def setSuit(self, suit):
        self.suit = suit
        
    def getRank(self):
        return self.rank
    
    def setRank(self, rank):
        self.rank = rank
        
    def getCount(self):
        return self.count
    
    def setCount(self, count):
        self.count = count
        
    def getParent(self):
        return self.parent
    
    def setParent(self, parent):
        self.parent = parent
        
    def getLeft(self):
        return self.left
    
    def isLeft(self):
        return self.parent and self.parent.left == self
    
    def setLeft(self, left):
        self.left = left
        if left is not None:
            left.parent = self
        
    def getRight(self):
        return self.right
    
    def isRight(self):
        return self.parent and self.parent.right == self
    
    def setRight(self, right):
        self.right = right
        if right is not None:
            right.parent = self
        
    def __str__(self):
        return '{} {} | {}\n'.format(self.suit, self.rank, self.count)
    
    
    
    def __lt__(self, rhs):
        list1 = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        list2 = ['C', 'D','H', 'S']
        index1 = 0
        index2 = 0
        index3 = 0
        index4 = 0
        index1 = list1.index(self.rank.upper())
        index2 = list1.index(rhs.rank.upper())
        if index1 < index2:
            return True
        elif index1 == index2:
            index3 = list2.index(self.suit.upper())
            index4 = list2.index(rhs.suit.upper())
            return index3 < index4
        else:
            return False
        
    def __eq__(self, rhs):
        if self is not None and rhs is not None:
            return self.rank.upper() == rhs.rank.upper() and self.suit.upper() == rhs.suit.upper()
    

    def __gt__(self, rhs):
        list1 = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        list2 = ['C', 'D','H', 'S']
        index1 = 0
        index2 = 0
        index3 = 0
        index4 = 0
        index1 = list1.index(self.rank.upper())
        index2 = list1.index(rhs.rank.upper())
        if index1 > index2:
            return True
        elif index1 == index2:
            index3 = list2.index(self.suit.upper())
            index4 = list2.index(rhs.suit.upper())
            return index3 > index4
        else:
            return False
