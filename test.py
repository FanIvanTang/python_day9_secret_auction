from main import max_bidding


def test_case_1_max_bidding():

    assert max_bidding({"ivan": 23.0, "amy": 19, "john": 12}) == ("ivan", 23.0)
