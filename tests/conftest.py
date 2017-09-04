import pytest

@pytest.fixture
def validMazeInstanceOne():
    return {
        "rooms": [
            { 
                "id": 1,
                "name": "Hallway", 
                "north": 2, 
                "objects": [] 
            },
            { 
                "id": 2, 
                "name": "Dining Room", 
                "south": 1, 
                "west": 3, 
                "east": 4,
                "objects": []
            },
            { 
                "id"    : 3,
                "name"  : "Kitchen",
                "east"  : 2, 
                "objects": [ { "name": "Knife" } ]
            },
            { 
                "id": 4,
                "name": "Sun Room",
                "west":2, 
                "objects": [ { "name": "Potted Plant" } ] 
            }
        ]
    }


@pytest.fixture
def twoRoomsMaze():
    return {
        "rooms": [
            { 
                "id": 1,
                "name": "Hallway", 
                "north": 2, 
                "objects": [
                    { 'name': 'Knife'}
                ] 
            },
            { 
                "id": 2, 
                "name": "Dining Room", 
                "south": 1, 
                "west": 3, 
                "east": 4,
                "objects": [
                    { 'name': 'Cup' },
                    { 'name': 'Plate'}, 
                    { 'name': 'A copy of The Hitchhiker\'s Guide to the Galaxy'}
                ]
            }
        ]
    }