class Node{
    int data;
    Node left,right;
    public Node(int val){
        data = val;
        left = right = null;
    }
}

class BinaryTree{
    Node root;
    BinaryTree(int key){
        root = new Node(key);

    }

    BinaryTree(){
        root = null;
    }

    public static void main(String[] args){
        BinaryTree tree = new BinaryTree();
        tree.root = new Node(1);
        tree.root.left = new Node(2);
    }
}