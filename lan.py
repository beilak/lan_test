class Lan:
    # Class for Lan
    # Created as a Tree

    def __init__(self, node_id: str, parent=None):
        '''
        :param node_id: Id for Node
        :param parent: Parent (last Node)
        '''
        self.__node_id = node_id
        self.__parent = parent
        self.__items = []

    def get_parent(self):
        return self.__parent

    def get_items(self):
        return self.__items

    def add_item(self, node_id):
        '''
        :param node_id: Item Id
        :return: create Node
        '''
        item_node = Lan(node_id, self)
        self.__items.append(item_node)
        return item_node

    def get_node_id(self):
        return self.__node_id

    def get_root(self):
        '''
        Go back to first(root) level
        :return: first node
        '''
        result = None
        parent = self
        # Loop until find node without Parent
        while True:
            if parent.get_parent() is None:
                result = parent
                break
            else:
                parent = parent.get_parent()
        return result

    def get_node(self, node_id):
        '''
        Get Node in items (deep only 1 level)
        :param node_id: id which looking for
        :return: None - if can't find or object which we found
        '''
        result = None
        for item in self.get_items():
            if item.get_node_id() == node_id:
                result = item
                break
        return result

    def get_item_count(self):
        return len(self.__items)


def count_sub_lan(lan: Lan, curr_level=0):
    '''
    Calculate how many sub-lan(lan) we have
    :param lan:
    :param curr_level: optional; current level
    :return: count
    '''

    # Calculate items only for second level
    # (exmpale:
    # 192.168.1.10,
    # 192.168.2.10
    # 168 is second level. Level stored 2 items

    if curr_level == 2:
        result = lan.get_item_count()
    else:
        result = 0
    curr_level += 1
    for item in lan.get_items():
        result += count_sub_lan(item, curr_level)
    return result


def main(file_name="input.txt"):
    '''
    :param file_name: file name with IP
    :return: count of sub-lan (or lan)
    '''

    curr_node = Lan("root")

    with open(file_name) as file_in:
        for file_line in file_in:
            # Create a map of Network
            curr_node = curr_node.get_root()
            line_items = file_line.split('.')
            if len(line_items) == 0:
                continue
            for item in line_items:
                node = curr_node.get_node(item)
                if node is None:
                    node = curr_node.add_item(item)
                curr_node = node

    # Calculate sub-lan(lan)
    curr_node = curr_node.get_root()
    result = int(count_sub_lan(curr_node))
    return result


if __name__ == '__main__':
    print(main())