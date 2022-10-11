def check_relation(net, *first, **second):
    friends = []
    friends_friends = []
    for name in first:
        friend = []
        for i in net:
            if name in i:
                for j in i:
                    if j != name:
                        friend.append(j)
        friends.append(friend)
        friend_friend = []
        for name in friend:
            for i in net:
                if name in i:
                    for j in i:
                        if j != name:
                            friend_friend.append(j)
        friends_friends.append(friend_friend)

    return any(x in friends[0] for x in friends[1]) or any(x in friends_friends[0] for x in friends_friends[1])


if __name__ == '__main__':
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша")
    )

    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True
