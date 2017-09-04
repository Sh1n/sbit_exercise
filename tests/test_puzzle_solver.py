import pytest
import collections

from src.PuzzleSolver               import PuzzleSolver
from src.InvalidMazeConfigException import InvalidMazeConfigException

def test_puzzle_solver_with_maze_not_as_array_should_raise_correct_exception():
    maze = 'invalid maze config'
    with pytest.raises(InvalidMazeConfigException) as e_info:
        pz = PuzzleSolver()
        pz.solvePuzzle(maze, None, [])
    assert 'Maze config should be a sequence containing the property "rooms"' == str(e_info.value)

def test_puzzle_solver_with_maze_as_faulty_string_should_raise_correct_exception():
    maze = 'invalid maze config but containing the word rooms'
    with pytest.raises(InvalidMazeConfigException) as e_info:
        pz = PuzzleSolver()
        pz.solvePuzzle(maze, None, [])
    assert 'Maze config should be a sequence containing the property "rooms"' == str(e_info.value)


def test_puzzle_solver_with_maze_as_number_should_raise_correct_exception():
    maze = 1
    with pytest.raises(InvalidMazeConfigException) as e_info:
        pz = PuzzleSolver()
        pz.solvePuzzle(maze, None, [])
    assert 'Maze config should be a sequence containing the property "rooms"' == str(e_info.value)

def test_puzzle_solver_with_maze_with_room_without_id_should_raise_correct_exception():
    maze = {
        "rooms" : [
            {
                "name": "without id"
            }
        ]
    }
    with pytest.raises(InvalidMazeConfigException) as e_info:
        pz = PuzzleSolver()
        pz.solvePuzzle(maze, 1, [])
    assert 'Maze\' rooms should contain the id property' == str(e_info.value)

def test_puzzle_solver_with_maze_with_room_without_name_should_raise_correct_exception():
    maze = {
        "rooms" : [
            {
                "id": "without name"
            }
        ]
    }
    with pytest.raises(InvalidMazeConfigException) as e_info:
        pz = PuzzleSolver()
        pz.solvePuzzle(maze, 1, [])
    assert 'Maze\' rooms should contain the name property' == str(e_info.value)

def test_puzzle_solver_with_invalid_starting_room_raise_correct_exception(validMazeInstanceOne):
    with pytest.raises(ValueError) as e_info:
        pz = PuzzleSolver()
        pz.solvePuzzle(validMazeInstanceOne, None, [])
    assert 'Starting point should be a numeric identifier' == str(e_info.value)


def test_puzzle_solver_with_not_existing_starting_room_raise_correct_exception(validMazeInstanceOne):
    with pytest.raises(ValueError) as e_info:
        pz = PuzzleSolver()
        pz.solvePuzzle(validMazeInstanceOne, -1, [])
    assert 'Starting point should exists in the maze configuration' == str(e_info.value)

def test_puzzle_solver_with_items_to_get_not_as_array_should_raise_exception(validMazeInstanceOne):
    items = "not an array"
    with pytest.raises(ValueError) as e_info:
        pz = PuzzleSolver()
        pz.solvePuzzle(validMazeInstanceOne, 2, items)
    assert 'Items to gather should be an array' == str(e_info.value)

def test_puzzle_solver_with_empty_items_to_gather_should_reply_with_empty_route(validMazeInstanceOne):
    pz      = PuzzleSolver()
    route   = pz.solvePuzzle(validMazeInstanceOne, 2, [])
    assert isinstance(route, collections.Iterable) == True
    assert len(route) == 0

def test_puzzle_solver_with_should_get_item_from_room_and_return_room_itself(validMazeInstanceOne):
    pz              = PuzzleSolver()
    route           = pz.solvePuzzle(validMazeInstanceOne, 3, ['Knife'])
    assert isinstance(route, collections.Iterable) == True
    assert len(route) == 1
    for node in route:
        assert len(node) == 3

def test_puzzle_solver_with_one_item_per_adjacent_rooms_should_take_both_into_route(twoRoomsMaze):
    pz              = PuzzleSolver()
    route           = pz.solvePuzzle(twoRoomsMaze, 1, ['Knife', 'Cup'])
    assert isinstance(route, collections.Iterable) == True
    assert len(route) == 2
    for node in route:
        assert len(node) == 3

def test_puzzle_solver_should_pass_first_maze_instance(validMazeInstanceOne):
    pz              = PuzzleSolver()
    route           = pz.solvePuzzle(validMazeInstanceOne, 2, ['Knife', 'Potted Plant'])
    assert isinstance(route, collections.Iterable) == True
    assert len(route) == 6
    for node in route:
        assert len(node) == 3
