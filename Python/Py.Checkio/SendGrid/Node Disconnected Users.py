# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Lodgeinwh
# @file: Node Disconnected Users.py
# @time: 2019/04/23 10:21:02
# @contact: lodgeinwh@gmail.com
# @version: 1.0


def disconnected_users(net, users, source, crushes):
    all_node = set([j for i in net for j in i])
    no_crushes_net = net.copy()
    for connect in net:
        for node in crushes:
            if node in connect:
                no_crushes_net.remove(connect)
    connect_node = {source}
    for i in no_crushes_net:
        for j in no_crushes_net:
            if connect_node & set(j):
                connect_node.update(j)
    crushes_node = all_node - connect_node
    if source in crushes:
        crushes_node.add(source)
    result = 0
    for i in crushes_node:
        result += users[i]
    return result


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert disconnected_users([['A', 'B'], ['B', 'C'], ['C', 'D']], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    }, 'A', ['C']) == 70, "First"

    assert disconnected_users([['A', 'B'], ['B', 'D'], ['A', 'C'], ['C', 'D']],
                              {
                                  'A': 10,
                                  'B': 0,
                                  'C': 0,
                                  'D': 40
                              }, 'A', ['B']) == 0, "Second"

    assert disconnected_users(
        [['A', 'B'], ['A', 'C'], ['A', 'D'], ['A', 'E'], ['A', 'F']], {
            'A': 10,
            'B': 10,
            'C': 10,
            'D': 10,
            'E': 10,
            'F': 10
        }, 'C', ['A']) == 50, "Third"

    assert disconnected_users([["A", "B"], ["B", "C"], ["C", "D"]], {
        "A": 10,
        "C": 30,
        "B": 20,
        "D": 40
    }, "A", ["A"]) == 100

    print('Done. Try to check now. There are a lot of other tests')
