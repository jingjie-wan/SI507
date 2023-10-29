#########################################
##### Name: Jingjie Wan #####
##### Uniqname: iriswan #####
#########################################
import unittest
import hw5_cards as HW5_cards

class TestCard(unittest.TestCase):

    def test_construct_Card(self):
        c1 = HW5_cards.Card(0, 2)
        c2 = HW5_cards.Card(1, 1)

        self.assertEqual(c1.suit, 0)
        self.assertEqual(c1.suit_name, "Diamonds")
        self.assertEqual(c1.rank, 2)
        self.assertEqual(c1.rank_name, "2")

        self.assertIsInstance(c1.suit, int)
        self.assertIsInstance(c1.suit_name, str)
        self.assertIsInstance(c1.rank, int)
        self.assertIsInstance(c1.rank_name, str)

        self.assertEqual(c2.suit, 1)
        self.assertEqual(c2.suit_name, "Clubs")
        self.assertEqual(c2.rank, 1)
        self.assertEqual(c2.rank_name, "Ace")
        
    def test_q1(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card with rank 12, its rank_name will be "Queen"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        test1 = HW5_cards.Card(rank = 12)
        X = test1.rank_name
        Y = 'Queen'
        self.assertEqual(X, Y)
        return X, Y
    
    def test_q2(self):
        '''
        1. fill in your test method for question 1:
        Test that if you create a card instance with suit 1, its suit_name will be "Clubs"
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        test2 = HW5_cards.Card(suit = 1)
        X = test2.suit_name
        Y = 'Clubs'
        self.assertEqual(X, Y)
        return X, Y    
    

    def test_q3(self):
        '''
        1. fill in your test method for question 3:
        Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades"

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        test3 = HW5_cards.Card(suit = 3, rank = 13)
        X = test3.__str__()
        Y = "King of Spades"
        self.assertEqual(X, Y)
        return X, Y
    
    def test_q4(self):
        '''
        1. fill in your test method for question 4:
        Test that if you create a Deck instance, it will have 52 cards in its cards instance variable
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        test4 = HW5_cards.Deck()
        X = len(test4.cards)
        Y = 52
        self.assertEqual(X, Y)
        return X, Y

    def test_q5(self):
        '''
        1. fill in your test method for question 5:
        Test that if you invoke the deal_card method on a deck, it will return a card instance.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        test5 = HW5_cards.Deck()
        X = test5.deal_card()
        Y = HW5_cards.Card
        self.assertIsInstance(X, Y)
        return X, Y
    
    def test_q6(self):
        '''
        1. fill in your test method for question 6:
        
        Test that if you invoke the deal_card method on a deck, the deck has one fewer cards in it afterwards.
        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        test6 = HW5_cards.Deck()
        Y = len(test6.cards) - 1
        test6.deal_card()
        X = len(test6.cards)
        self.assertEqual(X, Y)
        return X, Y 
    

    def test_q7(self):
        '''
        1. fill in your test method for question 7:
        Test that if you invoke the replace_card method, the deck has one more card in it afterwards. (Please note that you want to use deal_card function first to remove a card from the deck and then add the same card back in)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        test7 = HW5_cards.Deck()
        origin_number = len(test7.cards)
        add_card = test7.deal_card()
        Y = len(test7.cards) + 1
        test7.replace_card(add_card)
        X = len(test7.cards)
        self.assertEqual(X, Y)
        return origin_number, X, Y
    
    def test_q8(self):
        '''
        1. fill in your test method for question 8:
        Test that if you invoke the replace_card method with a card that is already in the deck, the deck size is not affected.(The function must silently ignore it if you try to add a card that’s already in the deck)

        
        2. remove the pass command
        
        3. uncomment the return command and 
        3b. change X, Y to the values from your assert statement
        ### please note: normally unit test methods do not have return statements. But returning will allow for unit testing of your unit test, and allow you to check your answer with the autograder.  This is optional today.

        '''
        test8 = HW5_cards.Deck()
        Y = len(test8.cards)
        add_card = HW5_cards.Card()
        test8.replace_card(add_card)
        X = len(test8.cards)
        self.assertEqual(X, Y)
        return X, Y  



if __name__=="__main__":
    unittest.main()