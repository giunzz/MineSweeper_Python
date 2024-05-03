# MineSweeper_Python


## Overview 
![alt text](/report_imp/image.png)

## Stuctures for gameplay
<pre>
├── main.py # file chính build game
└── Scripts
    ├── board.py # tạo bảng mìn
    ├── game.py  # quản lý gameplay
    ├── piece.py # xử lý thao tác từng phần tử của bảng
    └── Solver.py # chuyển động di chuyển chuột của user
    └── States.py # state win , lose, option , menu
    └── bnt.py # UI for create a button 
└── music
└── images
</pre>

## Requirements
```bash
python -m pip install pygame
python -m pip install requirements.txt
```
## run code
```
python -m main.py
```

## Boards

| scheme       | rows   | cols   | mines   |      |
| ------------ | ------ | ------ | ------- |------|
| Basic        | 4    | 4     | <= 50% * 16    |Choose
| Normal | 9   | 9   | 20      |<= 50% * 81|
| Hard      | 19    | 19    | <= 50 % (19*19)     | Choose


## Features

- Cấu trúc tổ chức file : run file `main.py` để hiển thị màn hình 
    - File `board.py` : khởi tạo bảnng chơi, check game win
    - File `game.py` : code UI (picture, music, stage etc)
    - file `piece.py`: các thông số thay đổi khi chơi game
    - file `solver.py`: di chuyển chuột



## Material
- [Python/Pygame Minesweeper Tutorial](https://www.youtube.com/watch?v=ABGtsAlXw7c) 
- [Pygame Tutorial for Beginners](https://www.youtube.com/watch?v=FfWpgLFMI7w)
- [5 Tips To Organize Python Code](https://www.youtube.com/watch?v=e9yMYdnSlUA&t=184s)
- [HOW TO MAKE A MENU SCREEN IN PYGAME!](https://www.youtube.com/watch?v=GMBqjxcKogA&t=81s)

- [Converting Python Project (Multiple Files) to Executable (.exe) Format](https://www.youtube.com/watch?v=wp2pNVUl3lc&t=234s)
