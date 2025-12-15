class Node:
    def __init__(self):
        self.next = None

    @staticmethod
    def create_chain(dangling_size, loop_size):
        """
        Создает цепь с dangling частью и циклом
        dangling_size - размер нецикличной части
        loop_size - размер цикла
        """
        # Создаем начальный узел
        start = Node()
        current = start

        # Создаем dangling часть
        for _ in range(dangling_size - 1):
            current.next = Node()
            current = current.next

        # Запоминаем начало цикла
        loop_start = Node()
        current.next = loop_start
        current = loop_start

        # Создаем остальную часть цикла
        for _ in range(loop_size - 1):
            current.next = Node()
            current = current.next

        # Замыкаем цикл
        current.next = loop_start

        return start

node = Node.create_chain(3904, 1087)


def loop_size(node):
    """
    алгоритм Флойда

    беговая дорожка
    2 бегуна стартуют из разных точек
    один бежит в 2 раза быстрее другого
    на круговой дорожке быстрый обязательно догонит медленного

    :param node:
    :return:
    """
    turtle  = node.next
    rabbit = node.next.next

    while turtle != rabbit:
        turtle= turtle.next
        rabbit = rabbit.next.next

    accumulate = 1
    current = turtle.next
    while current != turtle:
        accumulate += 1
        current = current.next

    return accumulate


print(loop_size(node))