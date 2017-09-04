import pytest

from src.Room       import Room


def test_constructor_without_id_definition_should_raise_exception():
    objectDef = {}
    with pytest.raises(ValueError) as e_info:
        room      = Room(objectDef)
    assert 'Room definition should contain attribute id' == str(e_info.value)

def test_constructor_with_not_numeric_id_definition_should_raise_exception():
    objectDef = {
        'id' : 'invalid'
    }
    with pytest.raises(ValueError) as e_info:
        room      = Room(objectDef)
    assert 'Room identifier should be numeric' == str(e_info.value)


def test_constructor_without_name_definition_should_raise_exception():
    objectDef = {
        'id'    : 2
    }
    with pytest.raises(ValueError) as e_info:
        room      = Room(objectDef)
    assert 'Room definition should contain attribute name' == str(e_info.value)


def test_constructor_with_invalid_objects_list_should_raise_exception():
    objectDef = {
        'id'        : 1,
        'name'      : 'name',
        'objects'   : 'invalid'
    }
    with pytest.raises(ValueError) as e_info:
        room      = Room(objectDef)
    assert 'Room\'s definition of contained objects should be a list' == str(e_info.value)


def test_constructor_with_not_well_formed_objects_list_should_return_empty_room():
    objectDef = {
        'id'        : 1,
        'name'      : 'name',
        'objects'   : ['invalid']
    }
    room      = Room(objectDef)
    assert len(room.getObjects()) == 0

def test_room_with_two_adjacent_rooms_should_return_correct_number_of_ids():
    objectDef = {
        'id'        : 1,
        'name'      : 'valid',
        'north'     : 3,
        'south'     : 4,
        'objects'   : []
    }
    room      = Room(objectDef)
    assert len(room.getAvailableRooms()) == 2
    assert 4 in room.getAvailableRooms()
    assert 3 in room.getAvailableRooms()

def test_clean_room_with_two_adjacent_rooms_should_correctly_clear_pointers():
    objectDef = {
        'id'        : 1,
        'name'      : 'valid',
        'north'     : 3,
        'south'     : 4,
        'objects'   : []
    }
    room      = Room(objectDef)
    room.cleanRooms()
    assert room.hasNorthRoom() == False
    assert room.hasSouthRoom() == False

def test_get_contained_items_should_return_correct_overlapping_set():
    objectDef = {
        'id'        : 1,
        'name'      : 'valid',
        'objects'   : [
            {
                'name' : 'Knife'
            },
            {
                'name'  : 'Pillow'
            },
            {
                'name'  : 'Fork'
            }
        ]
    }
    room            = Room(objectDef)
    containedItems  = room.getContainedItems(['Fork', 'Knife'])
    assert len(containedItems) == 2
    assert 'Fork' in containedItems
    assert 'Knife' in containedItems