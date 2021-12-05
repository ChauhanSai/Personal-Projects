from PIL import Image
import shutil
import os

packName = input('Zip Name: ')
if os.path.exists('temp/'):
    shutil.rmtree('temp/')

os.makedirs('temp/textures/block/')
os.makedirs('temp/textures/colormap/')
os.makedirs('temp/textures/entity/')
os.makedirs('temp/textures/environment/')
os.makedirs('temp/textures/item/')
os.makedirs('temp/textures/map/')
os.makedirs('temp/textures/misc/')
os.makedirs('temp/textures/models/armor/')
os.makedirs('temp/textures/painting/')
os.makedirs('temp/textures/mob_effect/')
os.makedirs('temp/textures/particle/')
print("The new directory is created!\n")

# blocks
bedrock = ['door_acacia_lower', 'amethyst_block']
java    = ['acacia_door_bottom', 'amethyst_block']
for i in range(len(bedrock)):
  textureB=bedrock[i]
  textureJ=java[i]
  src= r'textures/blocks/'
  src+=textureB
  src+='.png'
  dst= r'temp/textures/block/'
  dst+=textureB
  dst+='.png'
  rnm= r'temp/textures/block/'
  rnm+=textureJ
  rnm+='.png'
  shutil.copyfile(src, dst)
  os.rename(dst, rnm)
  print(textureB,' → ',textureJ)
print('Completed /block/\n')

# colormap
bedrock = ['foliage', 'grass']
java    = ['foliage', 'grass']
for i in range(len(bedrock)):
  textureB=bedrock[i]
  textureJ=java[i]
  src= r'textures/colormap/'
  src+=textureB
  src+='.png'
  dst= r'temp/textures/colormap/'
  dst+=textureB
  dst+='.png'
  rnm= r'temp/textures/colormap/'
  rnm+=textureJ
  rnm+='.png'
  shutil.copyfile(src, dst)
  os.rename(dst, rnm)
  print(textureB,' → ',textureJ)
print('Completed /colormap/\n')

# environment
bedrock = ['clouds', 'end_sky', 'moon_phases', 'sun']
java    = ['clouds', 'end_sky', 'moon_phases', 'sun']
for i in range(len(bedrock)):
  textureB=bedrock[i]
  textureJ=java[i]
  src= r'textures/environment/'
  src+=textureB
  src+='.png'
  dst= r'temp/textures/environment/'
  dst+=textureB
  dst+='.png'
  rnm= r'temp/textures/environment/'
  rnm+=textureJ
  rnm+='.png'
  shutil.copyfile(src, dst)
  os.rename(dst, rnm)
  print(textureB,' → ',textureJ)
print('Completed /environment/\n')

# items
bedrock = []
java    = []
for i in range(len(bedrock)):
  textureB=bedrock[i]
  textureJ=java[i]
  src= r'textures/items/'
  src+=textureB
  src+='.png'
  dst= r'temp/textures/item/'
  dst+=textureB
  dst+='.png'
  rnm= r'temp/textures/item/'
  rnm+=textureJ
  rnm+='.png'
  shutil.copyfile(src, dst)
  os.rename(dst, rnm)
  print(textureB,' → ',textureJ)
print('Completed /item/\n')

# map
bedrock = ['map_background']
java    = ['map_background']
for i in range(len(bedrock)):
  textureB=bedrock[i]
  textureJ=java[i]
  src= r'textures/map/'
  src+=textureB
  src+='.png'
  dst= r'temp/textures/map/'
  dst+=textureB
  dst+='.png'
  rnm= r'temp/textures/map/'
  rnm+=textureJ
  rnm+='.png'
  shutil.copyfile(src, dst)
  os.rename(dst, rnm)
  print(textureB,' → ',textureJ)
print('Completed /map/\n')

# misc
bedrock = ['pumpkinblur']
java    = ['pumpkinblur']
for i in range(len(bedrock)):
  textureB=bedrock[i]
  textureJ=java[i]
  src= r'textures/misc/'
  src+=textureB
  src+='.png'
  dst= r'temp/textures/misc/'
  dst+=textureB
  dst+='.png'
  rnm= r'temp/textures/misc/'
  rnm+=textureJ
  rnm+='.png'
  shutil.copyfile(src, dst)
  os.rename(dst, rnm)
  print(textureB,' → ',textureJ)
print('Completed /misc/ pass #1\n')

# models
bedrock = ['chain_1', 'chain_2', 'cloth_1', 'cloth_2', 'diamond_1', 'diamond_2', 'gold_1', 'gold_2', 'iron_1', 'iron_2', 'netherite_1', 'netherite_2', 'turtle_1']
java    = ['chain_layer_1', 'chain_layer_2', 'leather_layer_1', 'leather_layer_2', 'diamond_layer_1', 'diamond_layer_2', 'gold_layer_1', 'gold_layer_2', 'iron_layer_1', 'iron_layer_2', 'netherite_layer_1', 'netherite_layer_2', 'turtle_layer_1']
for i in range(len(bedrock)):
  textureB=bedrock[i]
  textureJ=java[i]
  src= r'textures/models/armor/'
  src+=textureB
  src+='.png'
  dst= r'temp/textures/models/armor/'
  dst+=textureB
  dst+='.png'
  rnm= r'temp/textures/models/armor/'
  rnm+=textureJ
  rnm+='.png'
  shutil.copyfile(src, dst)
  os.rename(dst, rnm)
  print(textureB,' → ',textureJ)
print('Completed /models/\n')

# mob_effect bedrockUI
bedrock = ['absorption_effect', 'bad_omen_effect', 'blindness_effect', 'conduit_power_effect', 'fire_resistance_effect', 'haste_effect', 'health_boost_effect', 'village_hero_effect', 'hunger_effect', 'invisibility_effect', 'jump_boost_effect', 'levitation_effect', 'mining_fatigue_effect', 'nausea_effect', 'night_vision_effect', 'poison_effect', 'regeneration_effect', 'resistance_effect', 'slow_falling_effect', 'slowness_effect', 'speed_effect', 'strength_effect', 'water_breathing_effect', 'weakness_effect', 'wither_effect']
java    = ['absorption', 'bad_omen', 'blindness', 'conduit_power', 'fire_resistance', 'haste', 'health_boost', 'hero_of_the_village', 'hunger', 'invisibility', 'jump_boost', 'levitation', 'mining_fatigue', 'nausea', 'night_vision', 'poison', 'regeneration', 'resistance', 'slow_falling', 'slowness', 'speed', 'strength', 'water_breathing', 'weakness', 'wither']
for i in range(len(bedrock)):
  textureB=bedrock[i]
  textureJ=java[i]
  src= r'textures/ui/'
  src+=textureB
  src+='.png'
  dst= r'temp/textures/mob_effect/'
  dst+=textureB
  dst+='.png'
  rnm= r'temp/textures/mob_effect/'
  rnm+=textureJ
  rnm+='.png'
  shutil.copyfile(src, dst)
  os.rename(dst, rnm)
  print(textureB,' → ',textureJ)
print('Completed /mob_effect/\n')

# misc bedrockUI
bedrock = ['frozen_effect', 'spyglass_scope']
java    = ['powder_snow_outline', 'spyglass_scope']
for i in range(len(bedrock)):
  textureB=bedrock[i]
  textureJ=java[i]
  src= r'textures/ui/'
  src+=textureB
  src+='.png'
  dst= r'temp/textures/misc/'
  dst+=textureB
  dst+='.png'
  rnm= r'temp/textures/misc/'
  rnm+=textureJ
  rnm+='.png'
  shutil.copyfile(src, dst)
  os.rename(dst, rnm)
  print(textureB,' → ',textureJ)
print('Completed /misc/ pass #2\n')

shutil.make_archive(packName, 'zip', 'temp')
shutil.rmtree('temp/')
print('Successfully compressed', packName,'. zip')
