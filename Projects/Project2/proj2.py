#
# Name: Jingjie Wan
# Uniqname: iriswan
#

from Proj2_tree import printTree

#
# The following two trees are useful for testing.
#
smallTree = \
    ("Is it bigger than a breadbox?",
        ("an elephant", None, None),
        ("a mouse", None, None))
mediumTree = \
    ("Is it bigger than a breadbox?",
        ("Is it gray?",
            ("an elephant", None, None),
            ("a tiger", None, None)),
        ("a mouse", None, None))

def main():
    """DOCSTRING!"""
    # Write the "main" function for 20 Questions here.  Although
    # main() is traditionally placed at the top of a file, it is the
    # last function you will write.
    print('Welcome to 20 Questions!')
    #if load file
    ifload = input('Would you like to load a tree from a file?')
    if ifload == 'yes':
        filename = input("What's the name of the file?")
        treeFile = open(filename, "r")
        tree = loadTree(treeFile)
        treeFile.close()
    elif ifload == 'no':
        tree = smallTree
    #playgame
    newTree = play(tree)
    #if play again
    while (input('Would you like to play again?') == 'yes'):
        newTree = play(newTree)
    #if save file
    ifsave = input("Would you like to save this tree for later?")
    if ifsave == 'yes':
        filename = input("Please enter a file name:")
        treeFile = open(filename, "w")
        saveTree(newTree, treeFile)
        treeFile.close()
        print('Thank you! The file has been saved.')
    print('Bye!')
    
        


def simplePlay(tree):
    """DOCSTRING!"""
    if tree[1] == None and tree[2] == None:
        answer = input('Is the object ' + tree[0] + '?')
        if answer == 'yes':
            return True
        elif answer == 'no':
            return False
    else:
        answer = input(tree[0])
        if answer == 'yes':
            return simplePlay(tree[1])
        elif answer == 'no':
            return simplePlay(tree[2])
            
def play(tree):
    """DOCSTRING!"""
    if tree[1] == None and tree[2] == None:
        answer = input('Is it ' + tree[0] + '?')
        if answer == 'yes':
            print("I got it!")
            return tree
        elif answer == 'no':
            name = input('Drats! What was it?')
            question = input("What's a question that distinguishes between "+ name +" and "+ tree[0] + "?")
            position = int(input("And what's the answer for " + name + "?") != 'yes') #'yes':0, 'no': 1
            if position == 0:
                newtree = (question, (name, None, None), tree)
            elif position == 1:
                newtree = (question, tree, (name, None, None))
            return newtree
    else:
        answer = input(tree[0])
        if answer == 'yes':
            return (tree[0], play(tree[1]), tree[2])
        elif answer == 'no':
            return (tree[0], tree[1], play(tree[2]))
def saveTree(tree, treeFile):
    text, left, right = tree
    if left is None and right is None:
        print('Leaf', file = treeFile)
        print(text, file = treeFile)
    else:
        print('Internal node', file = treeFile)
        print(text, file = treeFile)
        saveTree(left, treeFile)
        saveTree(right, treeFile)
        
def loadTree(treeFile):
    while True:
        line = treeFile.readline().strip()
        if line == '': break
        if line == 'Leaf':
            name = treeFile.readline().strip()
            return (name, None, None)
        elif line == 'Internal node':
            name = treeFile.readline().strip()
            return (name, loadTree(treeFile), loadTree(treeFile))
#
# The following two-line "magic sequence" must be the last thing in
# your file.  After you write the main() function, this line it will
# cause the program to automatically play 20 Questions when you run
# it.
#
if __name__ == '__main__':
    main()




