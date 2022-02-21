from mlproject.distance import haversine

def test_distance_is_positive():

    assert haversine(48.865070, 2.380009,52.49579, 13.43461) > 0
