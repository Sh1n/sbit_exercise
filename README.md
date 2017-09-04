### Developed using TDD technique
If you wish to run the tests use the following command:

```
python -m pytest tests
```

Make sure you have the right dependences, ottherwise in you python environment fire the following command:

```
pip install -r requirements.pip
```


### Docker Usage
Build the provided image by firing the following command:
```
docker build -t sbit .
```

Play one of the two maps by doing so:
```
docker run sbit python main.py maze_1.json <starting Room Id> <item 1> <item 2> ...
docker run sbit python main.py maze_2.json <starting Room Id> <item 1> <item 2> ...
```

If you wish to provide an external maze configuration fire the following command:
```
docker run -v <absolute path to file>:/usr/src/app/<new filename> sbit python main.py <new filename> <starting Room Id> <item 1> <item 2> ...
```


