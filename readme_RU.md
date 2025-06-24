LÖVE HTML5/WebAssembly
============

[(English README)](README.md)

Emscripten порт фреймворка LÖVE версии 12.0 для запуска игр и приложений в браузере.

Текущая сборка выполнена на основе [коммита `cdf68b3`](https://github.com/love2d/love/tree/cdf68b3228f3092cdb5425cb6d7555e3ea52ee8e) (ветка [`main`](https://github.com/love2d/love/tree/main)),
используется **экспериментальный порт SDL3 для Emscripten**.

Если вам нужна предыдущая стабильная сборка, используйте ветку [`stable`](https://github.com/rozenmad/love-web-builder/tree/stable).

Ответвление от love.js:
- https://github.com/Davidobot/love.js
- https://github.com/TannerRogalsky/love.js


## С чего начать?

Инструкция для пользователей Windows: установить [Python 3.10.6 или выше](https://www.python.org/downloads/release/python-3106/). (При установке Python убедитесь, что напротив 'Add Python to PATH' стоит галочка.)

## Чтобы собрать свой проект:
Перетащите папку с вашим проектом, либо файл .love на файл build.bat.

Или запустите build.bat из командной строки с агрументами:
```
build.bat <input> <output>
```

Опции:
```
<input>         папка с проектом, либо файл `.love`.
<output>        (необязательный параметр) папка, в которую требуется сохранить собранный проект (по умолчанию 'game').
-h, --help      вывод информации об использовании.
-n, --name      <string> название игры.
-m, --memory    [bytes] сколько памяти потребуется вашей игре (по умолчанию 16777216 байт)
-t, --template  <string> имя html шаблона в папке 'lovejs_source'.
```

По завершению процесса будет выведено 'Done!'

## Запуск
1. В папке `<output>` запустите веб-сервер командой `python -m http.server 8080`.
2. Откройте `localhost:8080` в любом браузере.

## Заметки
1. Поддерживаются шейдеры OpenGL ES 3.
2. Ознакомтесь также с заметками: https://github.com/Davidobot/love.js
3. Используется **экспериментальный порт SDL3 для Emscripten**.

## Сборка из исходников LÖVE

Если вы хотите внести изменения в исходные коды LÖVE, то следуйте инструкциям ниже:

### Windows

Убедитесь, что у вас установлены CMake и Make.
Склонируйте и установите [emsdk](https://github.com/emscripten-core/emsdk):
```
git clone https://github.com/emscripten-core/emsdk
cd emsdk

emsdk install 4.0.10
emsdk activate 4.0.10
```

Склонируйте исходники [megasource-web](https://github.com/rozenmad/megasource-web) и [love-web](https://github.com/rozenmad/love-web):

```
git clone https://github.com/rozenmad/megasource-web
cd megasource-web
git clone https://github.com/rozenmad/love-web libs/love
```

Измените пути в файле `build_lovejs.bat` к emsdk и к директории megasource на корректные. Запустите файл `build_lovejs.bat`.

После завершения процесса файлы `love.js` и `love.wasm` в директории `lovejs_source\compat` будут заменены.