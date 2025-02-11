import shutil
import os
import re
import json
import argparse
from uuid import uuid4
from pathlib import Path

import tempfile
# Create a temporary directory
temp_dir = tempfile.mkdtemp()

max_memory = 16777216
source_dir = 'lovejs_source/'
lovejs_dir_compat = source_dir + 'compat/'

lovejs_template = 'template.html'

love_game_name = 'game.data'

parser = argparse.ArgumentParser()

parser.add_argument('input', help = 'input game folder or .love package')
parser.add_argument('output', nargs='?', default='game', help = 'output folder')

parser.add_argument('-n', '--name', default="Title", help = 'specify game name')
parser.add_argument('-m', '--memory', type=int, default=max_memory, help = 'how much memory your game will require [16777216]')
parser.add_argument('-t', '--template', type=str, default=lovejs_template, help = 'html page template')

args = parser.parse_args()

def remove_file(filename):
      try:
            os.remove(filename)
      except OSError:
            pass

def meta_replace(input_filename, output_filename, meta):
      with open(output_filename, 'w') as output_gamejsfile:
            with open(input_filename, 'r') as input_gamejsfile:
                  filestring = input_gamejsfile.read()
                  for k, v in meta.items():
                        filestring = re.sub(k, v, filestring)
                  output_gamejsfile.write(filestring)


def build_webgl_game(gamedir, output_dir):
      if source_dir.rstrip('/') in os.path.basename(output_dir):
            print("The output directory cannot be 'lovejs_source'");
            return False

      output_dir += '/'
      if not os.path.exists(output_dir):
            os.makedirs(output_dir)
      else:
            remove_file(output_dir + love_game_name)
            remove_file(output_dir + 'index.html')
            remove_file(output_dir + 'game.js')
            remove_file(output_dir + 'love.js')
            remove_file(output_dir + 'love.wasm')
            themedir = output_dir + 'theme'
            if os.path.exists(themedir):
                  shutil.rmtree(themedir)
      
      if os.path.isfile(gamedir):
            shutil.copyfile(gamedir, output_dir + love_game_name)
      else:
            # Original: shutil.make_archive(output_dir + love_game_name, 'zip', gamedir)
            # Revised: make_archive should skip hidden files and directories, like .git, etc. 
            try:
                  # Copy all non-hidden files and directories from gamedir to temp_dir
                  temp_game_dir = os.path.join(temp_dir, 'game')
                  shutil.copytree(gamedir, temp_game_dir, ignore=shutil.ignore_patterns('.*'))

            # Create the archive from the temporary directory
                  shutil.make_archive(os.path.join(output_dir, love_game_name), 'zip', temp_game_dir)
            finally:
            # Clean up the temporary directory
                  shutil.rmtree(temp_dir)

            p = Path(output_dir + love_game_name + '.zip')
            p.rename(output_dir + love_game_name)

      shutil.copyfile(lovejs_dir_compat + 'love.js', output_dir + 'love.js')
      shutil.copyfile(lovejs_dir_compat + 'love.wasm', output_dir + 'love.wasm')

      shutil.copytree(source_dir + 'theme', output_dir + 'theme')

      package_size = os.path.getsize(output_dir + love_game_name)
      if args.memory < package_size:
            print('Warning: The memory (-m, --memory [bytes]) allocated for your game should at least be as big as your assets. '
                  + "The total size of your assets is %d bytes." % (package_size));

      files = [{
            'filename': '/game.love',
            'start': 0,
            'end': package_size
      }]

      package_info = {
            "files": files,
            "remote_package_size": package_size,
            "package_uuid": str(uuid4()),
      }

      meta_replace(source_dir + 'game.js', output_dir + 'game.js', { 
            '{{{ PACKAGE }}}' : json.dumps(package_info), '{{{ FILES }}}' : json.dumps(['/game.love']),
      })

      meta_replace(source_dir + args.template, output_dir + 'index.html', { 
            '{{{ TITLE }}}' : args.name,
      })

      return True


print("Build:", args.input)

if build_webgl_game(args.input, args.output):
      print('Done!')