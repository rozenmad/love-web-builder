LÖVE HTML5/Web Assembly
============

[(English README)](README.md)

Emscripten порт фреймворка LÖVE версии 12.0 для запуска приложений в браузере.
- https://github.com/love2d/love/tree/12.0-development

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
1. В текущей версии полностью отключен модуль Joystick. Поэтому избегайте вызова этого модуля в проекте, так как это приведет к ошибкам.
2. Поддерживаются шейдеры OpenGL ES 3.
3. Ознакомтесь также с заметками: https://github.com/Davidobot/love.js

## Сборка из исходников LÖVE

Если вы хотите внести изменения в исходные коды LÖVE, то следуйте инструкциям ниже:

### Windows

Убедитесь, что у вас установлены CMake и Make.
Склонируйте и установите [emsdk](https://github.com/emscripten-core/emsdk):
```
git clone https://github.com/emscripten-core/emsdk

emsdk install 3.1.47
emsdk activate 3.1.47
```

Измените пути в файле `build_lovejs.bat` к emsdk на корректные.

Склонируйте исходники LÖVE HTML5/Web Assembly.

```
Скоро будет доступно.
```

