class BST_Node:
    def __init__(self, value) -> None:
        self.__value = value
        self.__left = None
        self.__right = None

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def set_left(self, node):
        self.__left = node

    def get_left(self):
        return self.__left

    def set_right(self, node):
        self.__right = node

    def get_right(self):
        return self.__right

    def __eq__(self, __o) -> bool:
        return self.__value.word == __o.get_value().word

class BST:
    def __init__(self) -> None:
        self.__root = None

    def set_root(self, node):
        self.__root = node

    def get_root(self):
        return self.__root

    def insert_node(self, value):
        if not self.__root:
            self.__root = BST_Node(value)
        else:
            self._insert_recursive(self.__root, value)

    def _insert_recursive(self, node: BST_Node, value):
        if value.word < node.get_value().word:
            if node.get_left() is None:
                node.set_left(BST_Node(value))
            else:
                self._insert_recursive(node.get_left(), value)
        elif value.word > node.get_value().word:
            if node.get_right() is None:
                node.set_right(BST_Node(value))
            else:
                self._insert_recursive(node.get_right(), value)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.get_left())
            print(root.get_value())
            self.inorder_traversal(root.get_right())

    def write_file(self, root, f):
        if root:
            self.inorder_traversal(root.get_left())
            p = root.get_value().meanings.get_first_node()
            while p is not None:
                mean = p.get_value()
                line = f'{root.get_value().word} / {mean.get_speech()} / {mean.get_definition()} / {mean.get_example()}\n'
                f.write(line)
                p = p.get_next_node()

            self.inorder_traversal(root.get_right())

    def search_node(self, value):
        p = self.__root
        
        while p is not None:
            if value < p.get_value().word:
                p = p.get_left()
            elif value > p.get_value().word:
                p = p.get_right()
            else:
                return p.get_value()
        return None

    def min_value_node(self, node):
        current = node
        while current.get_left() is not None:
            current = current.get_left()
        return current

    def remove_node(self, key):
        parent = None
        current = self.__root
        while current is not None and current.get_value().word != key:
            parent = current
            if key < current.get_value().word:
                current = current.get_left()
            else:
                current = current.get_right()

        if current is None:
            return self.__root  # Key not found in tree

        if current.get_left() is None or current.get_right() is None:
            new_current = current.get_left() if current.get_left() else current.get_right()

            if parent is None:
                return new_current

            if current == parent.get_left():
                parent.set_left(new_current)
            else:
                parent.set_right(new_current)
        else:
            min_node = self.min_value_node(current.get_right())
            min_value = min_node.get_value()
            self.__root = self.remove_node(min_node.get_value().word)
            current.set_value(min_value)

class Meaning:
    def __init__(self, speech, definition, example) -> None:
        self.__speech = speech
        self.__definition = definition
        self.__example = example

    def get_speech(self):
        return self.__speech

    def get_definition(self):
        return self.__definition

    def get_example(self):
        return self.__example

    def __str__(self) -> str:
        return f'  + {self.__speech} {self.__definition} {self.__example}\n'

    def __eq__(self, __o) -> bool:
        return self.__definition.lower() == __o.get_definition().lower()

class Link_List_Node:
    def __init__(self, value) -> None:
        self.__value = value
        self.__next = None

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value

    def set_next_node(self, node):
        self.__next = node

    def get_next_node(self):
        return self.__next


class Link_List_Meanings:
    def __init__(self) -> None:
        self.__first_node = None

    def set_first_node(self, node: Link_List_Node):
        self.__first_node = node

    def get_first_node(self):
        return self.__first_node

    def insert_node(self, value):
        temp = Link_List_Node(value)
        if self.__first_node is None:
            self.__first_node = temp
            return
        p = self.__first_node
        while p.get_next_node() is not None:
            p = p.get_next_node()
        p.set_next_node(temp)


class Entry:
    def __init__(self, word):
        self.word = word
        self.meanings = Link_List_Meanings()

    def add_meaning(self, part_of_speech, definition, example):
        mean = Meaning(part_of_speech, definition, example)
        self.meanings.insert_node(mean)

    def __str__(self):
        output = f"{self.word}:\n"
        p = self.meanings.get_first_node()
        while p is not None:
            mean = p.get_value()
            output += f'\t+{mean.get_speech()} {mean.get_definition()} {mean.get_example()}\n'
            p = p.get_next_node()
        return output 


class Dictionary:
    def __init__(self):
        self.entries = dict()
        for i in range(26):
            self.entries[chr(ord('a') + i)] = BST()

    def add_entry(self, entry: Entry):
        word = entry.word
        tree = self.entries.get(word[0])
        if tree:
            check_duplicated_word = tree.search_node(word)
            if check_duplicated_word is None:
                tree.insert_node(entry)
                self.entries[word[0]] = tree
                return True
            else:
                p = check_duplicated_word.meanings.get_first_node()
                while p is not None:
                    if p.get_value() == entry.meanings.get_first_node().get_value():
                        print(f"Entry '{word}' was available!")
                        return False
                    p = p.get_next_node()
                check_duplicated_word.meanings.insert_node(entry.meanings.get_first_node().get_value())
                return True

    def remove_entry(self, word):
        tree = self.entries.get(word[0])
        if tree:
            root = tree.remove_node(word)
            tree.set_root(root)
            return True
        return False

    def lookup_entry(self, word):
        tree = self.entries.get(word[0])
        if tree:
            res = tree.search_node(word)
            return res
        return None

    def save_dictionary(self, file):
        with open(file, 'w', encoding='utf-8') as f:
            for k in self.entries:
                value = self.entries[k]
                value.write_file(value.get_root(), f)

    def load_dictionary(self, file):
        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                # loại bỏ ký tự \ufeff ở đầu file khi sử dụng mã hóa utf-8 dùng để xác định thứ tự byte
                if line.startswith('\ufeff'):
                    line = line.lstrip('\ufeff')
                # chia dữ liệu thành 1 mảng được ngăn cách bởi /
                line = line.strip().split(' / ')
                # khởi tạo mục từ
                tu = Entry(line[0].lower())
                # add meaning
                tu.add_meaning(line[1].lower(), line[2].lower(), line[3])
                # Bắt đầu thêm từ vào từ điển
                self.add_entry(tu)

def main():
    file = 'D:/n21dcdt024_bam.txt'
    dictionary = Dictionary()
    try:
        dictionary.load_dictionary(file)
    except Exception as ex:
        print('Processing load file was error.')
        return
    
    while True:
        print("\nMenu:")
        print("1. Add a new entry to the dictionary: ")
        print("2. Remove a dictionary entry: ")
        print("3. Look up an entry: ")
        print("4. Save dictionary to file")
        print("5. Load dictionary from file")
        print("6. Exit")

        choice = input("Enter your choice (1 - 6): ")

        if choice == "1":
            word = input("Enter the word: ").lower()
            part_of_speech = input("Enter the part_of_speech: ").lower()
            definition = input("Enter the definition: ").lower()
            example = input("Enter the example: ")
            entry = Entry(word)
            entry.add_meaning(part_of_speech, definition, example)
            if dictionary.add_entry(entry):
                print(f"Entry '{word}' added successfully!'")
            else: 
                print(f"Entry '{word}' added fail!'")

        elif choice == "2":
            word = input("Enter the word to remove: ")
            word = word.lower()
            if dictionary.remove_entry(word):
                print(f"Entry '{word}' removed successfully.")
            else:
                print(f"Entry '{word}' removed fail!")

        elif choice == "3":
            word = input("Enter the word to lookup: ")
            entry = dictionary.lookup_entry(word)
            if entry:
                print(entry)
            else:
                print(f'Entry {word} was not found in dictionary.')

        elif choice == "4":
            dictionary.save_dictionary(file)
            print(f"Dictionary saved to '{file}'.")

        elif choice == "5":
            dictionary.load_dictionary(file)
            print(f"Dictionary loaded from '{file}'.")

        elif choice == "6":
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == '__main__':
    main()
