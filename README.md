LÖVE HTML5/Web Assembly
============

[(Russian README)](readme_RU.md)

Emscripten port of LÖVE framework version 12.0 for distribution your games on the web.
- https://github.com/love2d/love/tree/main

Forked from love.js:
- https://github.com/Davidobot/love.js
- https://github.com/TannerRogalsky/love.js

## Getting Started

Instructions for Windows users: install [Python 3.10.6 or higher](https://www.python.org/downloads/release/python-3106/). (When installing Python, make sure 'Add Python to PATH' is checked.)

## To Build Your Project:
Drag and drop the game folder or .love package onto the `build.bat` file.

Or run build.bat with arguments:
```
build.bat <input> <output>
```

Options:
```
<input>         the folder with your project or the `.love` file.
<output>        (optional) the folder to save the compiled project (default folder is 'game').
-h, --help      display usage information.
-n, --name      <string> game title.
-m, --memory    [bytes] the amount of memory your game will need (default is 16777216 bytes).
-t, --template  <string> html template name in the 'lovejs_source' folder.
```

Once the process is complete, it will display 'Done!'

## Running
1. In the <output> folder, start a web server using the command ```python -m http.server 8080```.
2. Open ```localhost:8080``` in any web browser.

## Notes
1. The Joystick module is completely disabled in the current version. Avoid using this module in your project, as it will lead to errors.
2. OpenGL ES 3 shaders are supported.
3. Also check out the notes here: https://github.com/Davidobot/love.js

## Building LÖVE from Source

If you want to make changes to the LÖVE source code, follow the instructions below:

### Windows

Make sure you have CMake and Make installed.
Clone and install [emsdk](https://github.com/emscripten-core/emsdk)
```
git clone https://github.com/emscripten-core/emsdk
cd emsdk

emsdk install 3.1.47
emsdk activate 3.1.47
```

Modify the paths to emsdk in the build_lovejs.bat file to the correct ones.

Clone the [megasource-web](https://github.com/rozenmad/megasource-web) and [love-web](https://github.com/rozenmad/love-web) source code:

```
git clone https://github.com/rozenmad/megasource-web
cd megasource-web
git clone https://github.com/rozenmad/love-web libs/love
```

Change the paths to emsdk and to the megasource directory in the `build_lovejs.bat` file to the correct ones.

When the process is complete, the `love.js` and `love.wasm` files in the `lovejs_source\compat` directory will be replaced.