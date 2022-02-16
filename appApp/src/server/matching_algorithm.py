import pandas as pd
import numpy
from scipy.optimize import linear_sum_assignment

"""
Description: takes two lists of requests from organizations and from units and pairs them using a weighted maximal matching algorithm. Weights are based on both priority and number of people provided

Parameters: org_req - table with columns ID, NUM_PEOPLE
            unit_req - table with UNIT, ORG_REQ_ID, NUM_PEOPLE

Returns: list of pairs (org_req_id, unit_req_id)

"""


def Matching_Algorithm(org_req, unit_req):
    print(org_req)
    print(unit_req)
    org_nodes = {org_req['ID'][org_req.index[i]]: i for i in range(0, len(org_req.index))}
    unit_nodes = {unit_req['UNIT'].unique()[i]: i for i in range(0, unit_req['UNIT'].nunique())}

    weights = numpy.zeros((unit_req['UNIT'].nunique(), len(org_req.index)))
    weights.fill(1000)
    print(weights)
    for ind in unit_req.index:
        unit_node = unit_nodes[unit_req['UNIT'][ind]]
        org_node = org_nodes[unit_req['ORG_REQ'][ind]]
        people = unit_req['NUM_PEOPLE'][ind]
        weights[unit_node, org_node] = weights[unit_node, org_node] - people

    M = linear_sum_assignment(weights)
    print(M)
    print(weights)



def test():
    org_req = pd.DataFrame(data={'ID': [1, 2, 3, 4], 'NUM_PEOPLE': [7, 8, 4, 3]})
    unit_req = pd.DataFrame(data={'UNIT': [1, 2, 3, 4, 1, 5, 3, 4], 'ORG_REQ': [1, 2, 3, 4, 4, 3, 2, 1], 'NUM_PEOPLE': [4, 4, 3, 2, 4, 4, 3, 7]})
    Matching_Algorithm(org_req, unit_req)


if __name__ == "__main__":
    test()
