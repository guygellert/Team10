import pandas as pd

"""
Description: takes two lists of requests from organizations and from units and pairs them using a weighted maximal matching algorithm. Weights are based on both priority and number of people provided

Parameters: org_req - table with columns ID, NUM_PEOPLE
            unit_req - table with UNIT_ID, ORG_ID, NUM_PEOPLE, PRIORITY (ranking from 1 to 5 where 5 is lowest)

Returns: list of pairs (org_req_id, unit_req_id)

"""


def Matching_Algorithm(org_req, unit_req):
    print(org_req)
    print(unit_req)
    # weights = {id:(6 - priority) for id in unit_req}


def test():
    org_req = pd.DataFrame(data={'ID': [1, 2, 3, 4], 'NUM_PEOPLE': [7, 8, 4, 3]})
    unit_req = pd.DataFrame(data={'UNIT_ID': [1, 2, 3, 4, 1, 2, 3, 4], 'ORG_ID': [1, 2, 3, 4, 4, 3, 2, 1], 'NUM_PEOPLE': [4, 4, 3, 2, 4, 4, 3, 2], 'PRIORITY': [1, 1, 1, 1, 2, 2, 2, 2]})
    Matching_Algorithm(org_req, unit_req)


if __name__ == "__main__":
    test()
