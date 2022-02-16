import pandas as pd
import numpy
from scipy.optimize import linear_sum_assignment

MAX_INT = 1000

"""
Parameters: df- table with columns UNIT, NAME, COUNT, CAPACITY, UNIT_NODES, ORG_NODES

Returns: matrix representing a graph of all requests, with the edges having weight (MAX_INT - people_sent)
"""
def init_weights(df):
    weights = numpy.zeros((df['UNIT'].nunique(), df['NAME'].nunique()))
    weights.fill(MAX_INT)

    for ind in df.index:  # iterates over requests to create weight matrix
        unit_node = df['UNIT_NODE'][ind]
        org_node = df['ORG_NODE'][ind]
        people = df['COUNT'][ind]  # people being sent
        weights[unit_node, org_node] -= people

    return weights

"""
Parameters: edges- list of tuples representing the edges currently in the graph
            unused- table of all rows relating to unused units
            weights- the weight matrix of the graph

Returns: a new list of edges containing any units that could have been added after the matching
"""
def add_unused_units(edges, unused, weights):
    used_units = []
    for ind in unused.index:
        unit_node = unused['UNIT_NODE'][ind]
        org_node = unused['ORG_NODE'][ind]

        if unit_node in used_units:  # if unit_node has already been used skip it
            continue

        edge = [e for e in edges if e[1] == org_node][0]  # gets the edge used in the matching
        people_sent = MAX_INT - weights[edge[0]][edge[1]]  # people sent in the matching
        people_to_send = unused['COUNT'][ind]  # people that can be sent by the current unit
        capacity = unused["CAPACITY"][ind]
        if people_to_send < capacity - people_sent:  # checks if the people can be sent in addition to the ones already sent
            weights[edge[0]][edge[1]] -= people_to_send  # updates the weights
            edges += [(unit_node, org_node)]  # adds new edge to the graph
            used_units += [unit_node]

    return edges


"""
Description: takes two lists of requests from organizations and from units and pairs them using a weighted maximal matching algorithm. Weights are based on both priority and number of people provided

Parameters: org_req - table with columns NAME, CAPACITY
            unit_req - table with UNIT, COUNT, NAME, DATE
            notice that NAME is the same in both tables

Returns: list of pairs (org_req_id, unit_req_id)

Notes: assumes count < capacity for any given request
"""


def Matching_Algorithm(org_req, unit_req):
    full_df = unit_req.merge(org_req, on='NAME')
    unit_nodes = {full_df['UNIT'].unique()[i]: i for i in
                  range(0, full_df['UNIT'].nunique())}  # matches units to nodes
    org_nodes = {full_df['NAME'].unique()[i]: i for i in
                  range(0, full_df['NAME'].nunique())}  # matches orgs to nodes

    full_df['ORG_NODE'] = full_df['NAME'].apply(lambda x: org_nodes[x])
    full_df['UNIT_NODE'] = full_df['UNIT'].apply(lambda x: unit_nodes[x])
    # print(full_df)

    weights = init_weights(full_df)
    # print(weights)

    m = linear_sum_assignment(weights)  # returns two arrays, one of units and one of orgs

    unused_units = [n for n in full_df['UNIT_NODE'] if n not in m[0]]  # list of unused unit nodes
    edges = [(e[0], e[1]) for e in zip(m[0], m[1]) if weights[e[0]][e[1]] != MAX_INT]  # removes all edges equal to MAX_INT
    unused = full_df[full_df['UNIT_NODE'].isin(unused_units)]  # gets all rows with unused units
    # print(edges)
    edges = add_unused_units(edges, unused, weights)  # checks if more units can be added and adds them
    # print(edges)

    ret = []
    for e in edges:
        row = full_df.loc[(full_df['UNIT_NODE'] == e[0]) & (full_df['ORG_NODE'] == e[1])].squeeze()  # gets row relevant to current edge
        dic = row.to_dict()
        dic.pop('UNIT_NODE')
        dic.pop('ORG_NODE')
        dic.pop('CAPACITY')
        ret += [dic]

    print(ret)




def test():
    org_req = pd.DataFrame(data={'NAME': [1, 2, 3, 4, 5, 6], 'CAPACITY': [20, 40, 100, 50, 70, 30]})
    unit_req = pd.DataFrame(data={'UNIT': [1, 2, 3, 4, 1, 5, 3, 4, 6, 7], 'NAME': [1, 2, 3, 5, 5, 6, 5, 1, 4, 6], 'COUNT': [4, 4, 3, 2, 4, 4, 3, 7, 5, 6]})
    Matching_Algorithm(org_req, unit_req)


if __name__ == "__main__":
    test()
