@echo off
mkdir build
mkdir build\compat

:: Replace the path to emsdk\emsdk_env, e.g. "C:\emsdk\emsdk_env"
call F:\lovejs\emsdk\emsdk_env

(
echo Building compatibility version...
cd build\compat

:: Replace the path to megasource-web
emcmake cmake F:\lovejs\megasource-web -G "Unix Makefiles" -DLOVE_JIT=0 -DCMAKE_BUILD_TYPE=Release
emmake make -j 6
copy "love\love.js*" ..\..\lovejs_source\compat
copy "love\love.wasm" ..\..\lovejs_source\compat
PAUSE
)
