from Card import Card
from PlayerHand import PlayerHand

def test_card():
    card1 = Card("C", "A")
    

    assert card1.getSuit() == "C"
    assert card1.getRank() == "A"
    assert card1.getParent() == None
    assert card1.getCount() == 1
    assert str(card1) == "C A | 1\n"

    card2 = Card("C", "A")
    assert (card1 == card2) == True
    card3 = Card("S", "10")
    assert (card1 < card3) == True
    assert (card3 < card2) == False
    
    card1.setSuit("S")
    card1.setRank("J")
    card3.setParent(card1)
    card1.setLeft(card3)
    assert card1.getSuit() == "S"
    assert card1.getRank() == "J"
    assert card3.getParent() == card1
    assert card1.getLeft() == card3

    assert (card1 > card3) == True
    


def test_playhandconstruct():
    ph1 = PlayerHand()
    assert ph1.root == None
    assert ph1.size == 0



def test_playhandinsertroot():
    ph1 = PlayerHand()
    ph1.put("D", "A")
    assert ph1.root.getSuit() == "D"
    assert ph1.root.getRank() == "A"
    assert ph1.root.getLeft() == None
    assert ph1.root.getRight() == None
    assert ph1.root.getParent() == None
    assert ph1.root.getCount() == 1
    ph1.put("D", "A")
    assert ph1.root.getCount() == 2

 

def test_playhandsetnodes():
    ph1 = PlayerHand()
    ph1.put("D", "A")
    assert ph1.root.getSuit() == "D"
    assert ph1.root.getRank() == "A"
    assert ph1.root.getLeft() == None
    assert ph1.root.getRight() == None
    assert ph1.root.getParent() == None
    assert ph1.root.getCount() == 1

    ph1.root.setSuit("S")
    ph1.root.setRank("2")
    assert ph1.root.getSuit() == "S"
    assert ph1.root.getRank() == "2"



def test_playhandinsertnodes():
    ph1 = PlayerHand()
    ph1.put("D", "A")
    ph1.put("D", "5")
    ph1.put("S", "A")
    ph1.put("C", "A")


    assert ph1.root.suit == "D"
    assert ph1.root.rank == "A"
    assert ph1.root.left.suit == "C"
    assert ph1.root.left.rank == "A"
    assert ph1.root.right.suit == "D"
    assert ph1.root.right.rank == "5"
    assert ph1.root.right.left.suit == "S"
    assert ph1.root.right.left.rank == "A"
    assert ph1.root.getCount() == 1

  

def test_getmin():
    ph1 = PlayerHand()
    ph1.put("D", "A")
    ph1.put("D", "5")
    ph1.put("S", "A")
    ph1.put("C", "A")
    assert ph1.getMin().getSuit() == "C"
    assert ph1.getMin().getRank() == "A"

test_getmin()

def test_get():
    ph1 = PlayerHand()
    assert ph1.get("S","5") == None
    ph1 = PlayerHand()
    ph1.put("D", "A")
    ph1.put("D", "5")
    ph1.put("S", "A")
    ph1.put("C", "A")

    assert ph1.get("D", "A").getSuit() == "D"
    assert ph1.get("D", "A").getRank() == "A"



def test_delete():
    ph1 = PlayerHand()
    assert ph1.get("S","5") == None
    ph1 = PlayerHand()
    ph1.put("D", "A")
    ph1.put("D", "5")
    ph1.put("S", "A")
    ph1.put("C", "A")
    ph1.put("D", "A")
    ph1.get("D", "A").getCount() == 2

    assert ph1.get("S", "A").getSuit() == "S"
    assert ph1.get("S", "A").getRank() == "A"
    assert ph1.get("D", "A").getSuit() == "D"
    assert ph1.get("D", "A").getRank() == "A"
    assert ph1.get("C", "A").getSuit() == "C"
    assert ph1.get("C", "A").getRank() == "A"
    assert ph1.get("D", "5").getSuit() == "D"
    assert ph1.get("D", "5").getRank() == "5"

    ph1.delete("D", "A") == True
    ph1.delete("S", "A") == True
    ph1.delete("C", "A") == True
    ph1.delete("D", "A") == True
    ph1.delete("H", "2") == False



def test_inorder():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')
    assert hand.inOrder() == "D A | 1\nS 2 | 1\nH 7 | 1\nC Q | 1\nC K | 1\nS K | 2\n"


def test_preorder():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')
    assert hand.preOrder() =="D A | 1\nS K | 2\nS 2 | 1\nC Q | 1\nH 7 | 1\nC K | 1\n"
    hand.delete("C","Q")
    assert hand.preOrder() =="D A | 1\nS K | 2\nS 2 | 1\nC K | 1\nH 7 | 1\n"


def test_getsuccessor():
    hand = PlayerHand()
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')

    hand.getSuccessor("D", "A") == Card("S", "2")
    hand.getSuccessor("C", "K") == None
    hand.getSuccessor("H", "3") == None


def test_gettotal():
    hand = PlayerHand()
    assert hand.getTotalCards() == 0
    hand.put('D', 'A')
    hand.put('S', 'K')
    hand.put('S', '2')

    assert hand.getTotalCards() == 3
    hand.put('C', 'Q')
    hand.put('H', '7')
    hand.put('S', 'K')
    hand.put('C', 'K')

    assert hand.getTotalCards() == 7

