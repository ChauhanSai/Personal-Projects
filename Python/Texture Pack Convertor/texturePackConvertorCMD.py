import os
import shutil

from PIL import Image

packName = input('Zip Name: ')
if os.path.exists('temp/'):
    shutil.rmtree('temp/')

os.makedirs('temp/assets/minecraft/textures/block/')
os.makedirs('temp/assets/minecraft/textures/colormap/')
os.makedirs('temp/assets/minecraft/textures/entity/')
os.makedirs('temp/assets/minecraft/textures/environment/')
os.makedirs('temp/assets/minecraft/textures/item/')
os.makedirs('temp/assets/minecraft/textures/map/')
os.makedirs('temp/assets/minecraft/textures/misc/')
os.makedirs('temp/assets/minecraft/textures/models/armor/')
os.makedirs('temp/assets/minecraft/textures/painting/')
os.makedirs('temp/assets/minecraft/textures/mob_effect/')
os.makedirs('temp/assets/minecraft/textures/particle/')
print("The new directory is created!\n")

src = r'pack_icon.png'
dst = r'temp/pack_icon.png'
rnm = r'temp/pack.png'
shutil.copyfile(src, dst)
os.rename(dst, rnm)

mcmeta = open('temp/pack.mcmeta', 'w')
mcmeta.write('{\n\t"pack": {\n\t\t"pack_format": 8,\n\t\t"description": "')
mcmeta.write(packName)
mcmeta.write('"\n\t}\n}')
mcmeta.close()

# blocks
bedrock = ['door_acacia_lower', 'door_acacia_upper', 'leaves_acacia_opaque', 'log_acacia', 'log_acacia_top',
           'planks_acacia', 'sapling_acacia', 'acacia_trapdoor', 'rail_activator', 'rail_activator_powered',
           'flower_allium', 'amethyst_block', 'amethyst_cluster', 'ancient_debris_side', 'ancient_debris_top',
           'stone_andesite', 'anvil_base', 'anvil_top_damaged_0', 'melon_stem_connected', 'pumpkin_stem_connected',
           'azalea_leaves_opaque', 'azalea_plant', 'azalea_side', 'azalea_top', 'flower_houstonia', 'bamboo_leaf',
           'bamboo_singleleaf', 'bamboo_small_leaf', 'bamboo_sapling', 'bamboo_stem', 'barrel_bottom', 'barrel_side',
           'barrel_top', 'barrel_top_open', 'basalt_side', 'basalt_top', 'beacon', 'bedrock', 'bee_nest_bottom',
           'bee_nest_front', 'bee_nest_front_honey', 'bee_nest_side', 'bee_nest_top', 'beehive_top', 'beehive_front',
           'beehive_front_honey', 'beehive_side', 'beetroots_stage_0', 'beetroots_stage_1', 'beetroots_stage_2',
           'beetroots_stage_3', 'bell_bottom', 'bell_side', 'bell_top', 'big_dripleaf_side1', 'big_dripleaf_stem',
           'big_dripleaf_side2', 'big_dripleaf_top', 'door_birch_lower', 'door_birch_upper', 'leaves_birch_opaque',
           'log_birch', 'log_birch_top', 'planks_birch', 'sapling_birch', 'birch_trapdoor', 'concrete_black',
           'concrete_powder_black', 'glazed_terracotta_black', 'shulker_top_black', 'glass_black',
           'glass_pane_top_black', 'hardened_clay_stained_black', 'wool_colored_black', 'blackstone', 'blackstone_top',
           'blast_furnace_front_off', 'blast_furnace_front_on', 'blast_furnace_side', 'blast_furnace_top',
           'concrete_blue', 'concrete_powder_blue', 'glazed_terracotta_blue', 'blue_ice', 'flower_blue_orchid',
           'shulker_top_blue', 'glass_blue', 'glass_pane_top_blue', 'hardened_clay_stained_blue', 'wool_colored_blue',
           'bone_block_side', 'bone_block_top', 'bookshelf', 'coral_plant_pink', 'coral_pink', 'coral_fan_pink',
           'brewing_stand', 'brewing_stand_base', 'brick', 'concrete_brown', 'concrete_powder_brown',
           'glazed_terracotta_brown', 'mushroom_brown', 'mushroom_block_skin_brown', 'shulker_top_brown', 'glass_brown',
           'glass_pane_top_brown', 'hardened_clay_stained_brown', 'wool_colored_brown', 'coral_plant_purple',
           'coral_purple', 'coral_fan_purple', 'budding_amethyst', 'cake_bottom', 'cake_inner', 'cake_side', 'cake_top',
           'calcite', 'campfire', 'campfire_log', 'campfire_log_lit', 'carrots_stage_0', 'carrots_stage_1',
           'carrots_stage_2', 'carrots_stage_3', 'cartography_table_side1', 'cartography_table_side2',
           'cartography_table_side3', 'cartography_table_top', 'pumpkin_face_off', 'cauldron_bottom', 'cauldron_inner',
           'cauldron_side', 'cauldron_top', 'cave_vines_head', 'cave_vines_head_berries', 'cave_vines_body',
           'cave_vines_body_berries', 'chain_command_block_back', 'chain_command_block_conditional',
           'chain_command_block_front', 'chain_command_block_side', 'anvil_top_damaged_1', 'chiseled_nether_bricks',
           'chiseled_polished_blackstone', 'quartz_block_chiseled', 'quartz_block_chiseled_top', 'red_sandstone_carved',
           'sandstone_carved', 'stonebrick_carved', 'chorus_flower', 'chorus_flower_dead', 'chorus_plant', 'clay',
           'coal_block', 'coal_ore', 'coarse_dirt', 'cobblestone', 'web', 'cocoa_stage_0', 'cocoa_stage_1',
           'cocoa_stage_2', 'command_block_back', 'command_block_conditional', 'command_block_front',
           'command_block_side', 'comparator_off', 'comparator_on', 'composter_bottom', 'compost', 'compost_ready',
           'composter_side', 'composter_top', 'copper_block', 'copper_ore', 'flower_cornflower',
           'cracked_nether_bricks', 'cracked_polished_blackstone_bricks', 'stonebrick_cracked', 'crafting_table_front',
           'crafting_table_side', 'crafting_table_top', 'crimson_fungus', 'crimson_nylium_top', 'crimson_nylium_side',
           'crimson_roots', 'crimson_roots_pot', 'crying_obsidian', 'cut_copper', 'red_sandstone_smooth',
           'sandstone_smooth', 'concrete_cyan', 'concrete_powder_cyan', 'glazed_terracotta_cyan', 'shulker_top_cyan',
           'glass_cyan', 'glass_pane_top_cyan', 'hardened_clay_stained_cyan', 'wool_colored_cyan',
           'anvil_top_damaged_2', 'flower_dandelion', 'door_dark_oak_lower', 'door_dark_oak_upper',
           'leaves_big_oak_opaque', 'log_big_oak', 'log_big_oak_top', 'planks_big_oak', 'sapling_roofed_oak',
           'dark_oak_trapdoor', 'prismarine_dark', 'daylight_detector_inverted_top', 'daylight_detector_side',
           'daylight_detector_top', 'coral_plant_pink_dead', 'coral_pink_dead', 'coral_fan_pink_dead',
           'coral_plant_purple_dead', 'coral_purple_dead', 'coral_fan_purple_dead', 'deadbush', 'coral_plant_red_dead',
           'coral_red_dead', 'coral_fan_red_dead', 'coral_plant_yellow_dead', 'coral_yellow_dead',
           'coral_fan_yellow_dead', 'coral_plant_blue_dead', 'coral_blue_dead', 'coral_fan_blue_dead', 'rail_detector',
           'rail_detector_powered', 'diamond_block', 'diamond_ore', 'stone_diorite', 'dirt', 'grass_path_side',
           'grass_path_top', 'dispenser_front_horizontal', 'dispenser_front_vertical', 'dragon_egg', 'dried_kelp_top',
           'dried_kelp_side_a', 'dried_kelp_top', 'dripstone_block', 'dropper_front_horizontal',
           'dropper_front_vertical', 'emerald_block', 'emerald_ore', 'enchanting_table_bottom', 'enchanting_table_side',
           'enchanting_table_top', 'endframe_eye', 'endframe_side', 'endframe_top', 'end_rod', 'end_stone',
           'end_bricks', 'exposed_copper', 'exposed_cut_copper', 'farmland_dry', 'farmland_wet', 'fire_0', 'fire_1',
           'coral_plant_red', 'coral_red', 'coral_fan_red', 'fletcher_table_side2', 'fletcher_table_side1',
           'fletcher_table_top', 'flower_pot', 'azalea_leaves_flowers_opaque', 'flowering_azalea_side',
           'flowering_azalea_top', 'frosted_ice_0', 'frosted_ice_1', 'frosted_ice_2', 'frosted_ice_3',
           'furnace_front_off', 'furnace_front_on', 'furnace_side', 'furnace_top', 'gilded_blackstone', 'glass',
           'glass_pane_top', 'glow_item_frame', 'glow_lichen', 'glowstone', 'gold_block', 'gold_ore', 'stone_granite',
           'tallgrass', 'grass_side_carried', 'grass_block_snow', 'grass_top', 'gravel', 'concrete_gray',
           'concrete_powder_gray', 'glazed_terracotta_gray', 'shulker_top_gray', 'glass_gray', 'glass_pane_top_gray',
           'hardened_clay_stained_gray', 'wool_colored_gray', 'concrete_green', 'concrete_powder_green',
           'glazed_terracotta_green', 'shulker_top_green', 'glass_green', 'glass_pane_top_green',
           'hardened_clay_stained_green', 'wool_colored_green', 'hanging_roots', 'hay_block_side', 'hay_block_top',
           'honey_bottom', 'honey_side', 'honey_top', 'honeycomb', 'hopper_inside', 'hopper_outside', 'hopper_top',
           'coral_plant_yellow', 'coral_yellow', 'coral_fan_yellow', 'ice', 'iron_bars', 'iron_block',
           'door_iron_lower', 'door_iron_upper', 'iron_ore', 'iron_trapdoor', 'itemframe_background', 'pumpkin_face_on',
           'jigsaw_back', 'jigsaw_lock', 'jigsaw_side', 'jigsaw_front', 'jukebox_side', 'jukebox_top',
           'door_jungle_lower', 'door_jungle_upper', 'leaves_jungle_opaque', 'log_jungle', 'log_jungle_top',
           'planks_jungle', 'sapling_jungle', 'jungle_trapdoor', 'ladder', 'lantern', 'lapis_block', 'lapis_ore',
           'large_amethyst_bud', 'lava_flow', 'lava_still', 'lectern_base', 'lectern_front', 'lectern_sides',
           'lectern_top', 'lever', 'concrete_light_blue', 'concrete_powder_light_blue', 'glazed_terracotta_light_blue',
           'shulker_top_light_blue', 'glass_light_blue', 'glass_pane_top_light_blue',
           'hardened_clay_stained_light_blue', 'wool_colored_light_blue', 'concrete_silver', 'concrete_powder_silver',
           'glazed_terracotta_silver', 'shulker_top_silver', 'glass_silver', 'glass_pane_top_silver',
           'hardened_clay_stained_silver', 'wool_colored_silver', 'lightning_rod', 'flower_lily_of_the_valley',
           'waterlily', 'concrete_lime', 'concrete_powder_lime', 'glazed_terracotta_lime', 'shulker_top_lime',
           'glass_lime', 'glass_pane_top_lime', 'hardened_clay_stained_lime', 'wool_colored_lime', 'lodestone_side',
           'lodestone_top', 'loom_bottom', 'loom_front', 'loom_side', 'loom_top', 'concrete_magenta',
           'concrete_powder_magenta', 'glazed_terracotta_magenta', 'shulker_top_magenta', 'glass_magenta',
           'glass_pane_top_magenta', 'hardened_clay_stained_magenta', 'wool_colored_magenta', 'magma',
           'medium_amethyst_bud', 'melon_side', 'melon_stem_disconnected', 'melon_top', 'moss_block',
           'cobblestone_mossy', 'stonebrick_mossy', 'mushroom_block_inside', 'mushroom_block_skin_stem',
           'mycelium_side', 'mycelium_top', 'nether_brick', 'nether_gold_ore', 'portal', 'quartz_ore', 'nether_sprouts',
           'nether_wart_block', 'nether_wart_stage_0', 'nether_wart_stage_1', 'nether_wart_stage_2', 'netherite_block',
           'netherrack', 'noteblock', 'door_wood_lower', 'door_wood_upper', 'leaves_oak_opaque', 'log_oak',
           'log_oak_top', 'planks_oak', 'sapling_oak', 'trapdoor', 'observer_back', 'observer_back_lit',
           'observer_front', 'observer_side', 'observer_top', 'obsidian', 'concrete_orange', 'concrete_powder_orange',
           'glazed_terracotta_orange', 'shulker_top_orange', 'glass_orange', 'glass_pane_top_orange',
           'hardened_clay_stained_orange', 'flower_tulip_orange', 'wool_colored_orange', 'flower_oxeye_daisy',
           'oxidized_copper', 'oxidized_cut_copper', 'ice_packed', 'double_plant_paeonia_bottom',
           'double_plant_paeonia_top', 'concrete_pink', 'concrete_powder_pink', 'glazed_terracotta_pink',
           'shulker_top_pink', 'glass_pink', 'glass_pane_top_pink', 'hardened_clay_stained_pink', 'flower_tulip_pink',
           'wool_colored_pink', 'piston_bottom', 'piston_inner', 'piston_side', 'piston_top_normal',
           'piston_top_sticky', 'dirt_podzol_side', 'dirt_podzol_top', 'pointed_dripstone_down_base',
           'pointed_dripstone_down_frustum', 'pointed_dripstone_down_middle', 'pointed_dripstone_down_tip',
           'pointed_dripstone_down_merge', 'pointed_dripstone_up_base', 'pointed_dripstone_up_frustum',
           'pointed_dripstone_up_middle', 'pointed_dripstone_up_tip', 'pointed_dripstone_up_merge',
           'stone_andesite_smooth', 'polished_basalt_side', 'polished_basalt_top', 'polished_blackstone',
           'polished_blackstone_bricks', 'stone_diorite_smooth', 'stone_granite_smooth', 'flower_rose',
           'potatoes_stage_0', 'potatoes_stage_1', 'potatoes_stage_2', 'potatoes_stage_3', 'potted_azalea_bush_plant',
           'potted_azalea_bush_side', 'potted_azalea_bush_top', 'potted_flowering_azalea_bush_plant',
           'potted_flowering_azalea_bush_side', 'potted_flowering_azalea_bush_top', 'powder_snow', 'rail_golden',
           'rail_golden_powered', 'prismarine_rough', 'prismarine_bricks', 'pumpkin_side', 'pumpkin_stem_disconnected',
           'pumpkin_top', 'concrete_purple', 'concrete_powder_purple', 'glazed_terracotta_purple', 'shulker_top_purple',
           'glass_purple', 'glass_pane_top_purple', 'hardened_clay_stained_purple', 'wool_colored_purple',
           'purpur_block', 'purpur_pillar', 'purpur_pillar_top', 'quartz_block_bottom', 'quartz_block_side',
           'quartz_block_top', 'quartz_bricks', 'quartz_block_lines', 'quartz_block_lines_top', 'rail_normal',
           'rail_normal_turned', 'raw_copper_block', 'raw_gold_block', 'raw_iron_block', 'concrete_red',
           'concrete_powder_red', 'glazed_terracotta_red', 'mushroom_red', 'mushroom_block_skin_red',
           'red_nether_brick', 'red_sand', 'red_sandstone_normal', 'red_sandstone_bottom', 'red_sandstone_top',
           'shulker_top_red', 'glass_red', 'glass_pane_top_red', 'hardened_clay_stained_red', 'flower_tulip_red',
           'wool_colored_red', 'redstone_block', 'redstone_dust_cross', 'redstone_dust_line', 'redstone_dust_line',
           'redstone_lamp_off', 'redstone_lamp_on', 'redstone_ore', 'redstone_torch_on', 'redstone_torch_off',
           'repeater_off', 'repeater_on', 'repeating_command_block_back', 'repeating_command_block_conditional',
           'repeating_command_block_front', 'repeating_command_block_side', 'respawn_anchor_bottom',
           'respawn_anchor_side0', 'respawn_anchor_side1', 'respawn_anchor_side2', 'respawn_anchor_side3',
           'respawn_anchor_side4', 'respawn_anchor_top', 'respawn_anchor_top_off', 'dirt_with_roots',
           'double_plant_rose_bottom', 'double_plant_rose_top', 'sand', 'sandstone_normal', 'sandstone_bottom',
           'sandstone_top', 'sea_lantern', 'sea_pickle', 'seagrass', 'shroomlight', 'shulker_top_undyed', 'slime',
           'small_amethyst_bud', 'small_dripleaf_side', 'small_dripleaf_stem_bottom', 'small_dripleaf_stem_top',
           'small_dripleaf_top', 'smithing_table_bottom', 'smithing_table_front', 'smithing_table_side',
           'smithing_table_top', 'smoker_bottom', 'smoker_front_off', 'smoker_front_on', 'smoker_side', 'smoker_top',
           'smooth_basalt', 'stone_slab_top', 'stone_slab_side', 'snow', 'soul_campfire', 'soul_campfire_log_lit',
           'soul_fire_0', 'soul_fire_1', 'soul_lantern', 'soul_sand', 'soul_soil', 'soul_torch', 'mob_spawner',
           'sponge', 'spore_blossom', 'spore_blossom_base', 'door_spruce_lower', 'door_spruce_upper',
           'leaves_spruce_opaque', 'log_spruce', 'log_spruce_top', 'planks_spruce', 'sapling_spruce', 'spruce_trapdoor',
           'stone', 'stonebrick', 'stonecutter_bottom', 'stonecutter_side', 'stonecutter_top', 'stripped_acacia_log',
           'stripped_acacia_log_top', 'stripped_birch_log', 'stripped_birch_log_top', 'stripped_dark_oak_log',
           'stripped_dark_oak_log_top', 'stripped_jungle_log', 'stripped_jungle_log_top', 'stripped_oak_log',
           'stripped_oak_log_top', 'stripped_spruce_log', 'stripped_spruce_log_top', 'structure_block',
           'structure_block_corner', 'structure_block_data', 'structure_block_load', 'structure_block_save',
           'double_plant_sunflower_back', 'double_plant_sunflower_bottom', 'double_plant_sunflower_front',
           'double_plant_sunflower_top', 'sweet_berry_bush_stage0', 'sweet_berry_bush_stage1',
           'sweet_berry_bush_stage2', 'sweet_berry_bush_stage3', 'seagrass', 'target_side', 'target_top',
           'hardened_clay', 'tinted_glass', 'tnt_bottom', 'tnt_side', 'tnt_top', 'torch_on', 'trip_wire',
           'trip_wire_source', 'coral_plant_blue', 'coral_blue', 'coral_fan_blue', 'tuff', 'turtle_egg_not_cracked',
           'turtle_egg_slightly_cracked', 'turtle_egg_very_cracked', 'twisting_vines_bottom', 'twisting_vines_base',
           'vine', 'warped_fungus', 'warped_nylium_top', 'warped_nylium_side', 'warped_roots', 'warped_roots_pot',
           'warped_wart_block', 'water_flow', 'water_still', 'weathered_copper', 'weathered_cut_copper',
           'weeping_vines', 'weeping_vines_plant', 'sponge_wet', 'wheat_stage_0', 'wheat_stage_1', 'wheat_stage_2',
           'wheat_stage_3', 'wheat_stage_4', 'wheat_stage_5', 'wheat_stage_6', 'wheat_stage_7', 'concrete_white',
           'concrete_powder_white', 'glazed_terracotta_white', 'shulker_top_white', 'glass_white',
           'glass_pane_top_white', 'hardened_clay_stained_white', 'flower_tulip_white', 'wool_colored_white',
           'flower_wither_rose', 'concrete_yellow', 'concrete_powder_yellow', 'glazed_terracotta_yellow',
           'shulker_top_yellow', 'glass_yellow', 'glass_pane_top_yellow', 'hardened_clay_stained_yellow',
           'wool_colored_yellow']
java = ['acacia_door_bottom', 'acacia_door_top', 'acacia_leaves', 'acacia_log', 'acacia_log_top', 'acacia_planks',
        'acacia_sapling', 'acacia_trapdoor', 'activator_rail', 'activator_rail_on', 'allium', 'amethyst_block',
        'amethyst_cluster', 'ancient_debris_side', 'ancient_debris_top', 'andesite', 'anvil', 'anvil_top',
        'attached_melon_stem', 'attached_pumpkin_stem', 'azalea_leaves', 'azalea_plant', 'azalea_side', 'azalea_top',
        'azure_bluet', 'bamboo_large_leaves', 'bamboo_singleleaf', 'bamboo_small_leaves', 'bamboo_stage0',
        'bamboo_stalk', 'barrel_bottom', 'barrel_side', 'barrel_top', 'barrel_top_open', 'basalt_side', 'basalt_top',
        'beacon', 'bedrock', 'bee_nest_bottom', 'bee_nest_front', 'bee_nest_front_honey', 'bee_nest_side',
        'bee_nest_top', 'beehive_end', 'beehive_front', 'beehive_front_honey', 'beehive_side', 'beetroots_stage0',
        'beetroots_stage1', 'beetroots_stage2', 'beetroots_stage3', 'bell_bottom', 'bell_side', 'bell_top',
        'big_dripleaf_side', 'big_dripleaf_stem', 'big_dripleaf_tip', 'big_dripleaf_top', 'birch_door_bottom',
        'birch_door_top', 'birch_leaves', 'birch_log', 'birch_log_top', 'birch_planks', 'birch_sapling',
        'birch_trapdoor', 'black_concrete', 'black_concrete_powder', 'black_glazed_terracotta', 'black_shulker_box',
        'black_stained_glass', 'black_stained_glass_pane_top', 'black_terracotta', 'black_wool', 'blackstone',
        'blackstone_top', 'blast_furnace_front', 'blast_furnace_front_on', 'blast_furnace_side', 'blast_furnace_top',
        'blue_concrete', 'blue_concrete_powder', 'blue_glazed_terracotta', 'blue_ice', 'blue_orchid',
        'blue_shulker_box', 'blue_stained_glass', 'blue_stained_glass_pane_top', 'blue_terracotta', 'blue_wool',
        'bone_block_side', 'bone_block_top', 'bookshelf', 'brain_coral', 'brain_coral_block', 'brain_coral_fan',
        'brewing_stand', 'brewing_stand_base', 'bricks', 'brown_concrete', 'brown_concrete_powder',
        'brown_glazed_terracotta', 'brown_mushroom', 'brown_mushroom_block', 'brown_shulker_box', 'brown_stained_glass',
        'brown_stained_glass_pane_top', 'brown_terracotta', 'brown_wool', 'bubble_coral', 'bubble_coral_block',
        'bubble_coral_fan', 'budding_amethyst', 'cake_bottom', 'cake_inner', 'cake_side', 'cake_top', 'calcite',
        'campfire_fire', 'campfire_log', 'campfire_log_lit', 'carrots_stage0', 'carrots_stage1', 'carrots_stage2',
        'carrots_stage3', 'cartography_table_side1', 'cartography_table_side2', 'cartography_table_side3',
        'cartography_table_top', 'carved_pumpkin', 'cauldron_bottom', 'cauldron_inner', 'cauldron_side', 'cauldron_top',
        'cave_vines', 'cave_vines_lit', 'cave_vines_plant', 'cave_vines_plant_lit', 'chain_command_block_back',
        'chain_command_block_conditional', 'chain_command_block_front', 'chain_command_block_side', 'chipped_anvil_top',
        'chiseled_nether_bricks', 'chiseled_polished_blackstone', 'chiseled_quartz_block', 'chiseled_quartz_block_top',
        'chiseled_red_sandstone', 'chiseled_sandstone', 'chiseled_stone_bricks', 'chorus_flower', 'chorus_flower_dead',
        'chorus_plant', 'clay', 'coal_block', 'coal_ore', 'coarse_dirt', 'cobblestone', 'cobweb', 'cocoa_stage0',
        'cocoa_stage1', 'cocoa_stage2', 'command_block_back', 'command_block_conditional', 'command_block_front',
        'command_block_side', 'comparator', 'comparator_on', 'composter_bottom', 'composter_compost', 'composter_ready',
        'composter_side', 'composter_top', 'copper_block', 'copper_ore', 'cornflower', 'cracked_nether_bricks',
        'cracked_polished_blackstone_bricks', 'cracked_stone_bricks', 'crafting_table_front', 'crafting_table_side',
        'crafting_table_top', 'crimson_fungus', 'crimson_nylium', 'crimson_nylium_side', 'crimson_roots',
        'crimson_roots_pot', 'crying_obsidian', 'cut_copper', 'cut_red_sandstone', 'cut_sandstone', 'cyan_concrete',
        'cyan_concrete_powder', 'cyan_glazed_terracotta', 'cyan_shulker_box', 'cyan_stained_glass',
        'cyan_stained_glass_pane_top', 'cyan_terracotta', 'cyan_wool', 'damaged_anvil_top', 'dandelion',
        'dark_oak_door_bottom', 'dark_oak_door_top', 'dark_oak_leaves', 'dark_oak_log', 'dark_oak_log_top',
        'dark_oak_planks', 'dark_oak_sapling', 'dark_oak_trapdoor', 'dark_prismarine', 'daylight_detector_inverted_top',
        'daylight_detector_side', 'daylight_detector_top', 'dead_brain_coral', 'dead_brain_coral_block',
        'dead_brain_coral_fan', 'dead_bubble_coral', 'dead_bubble_coral_block', 'dead_bubble_coral_fan', 'dead_bush',
        'dead_fire_coral', 'dead_fire_coral_block', 'dead_fire_coral_fan', 'dead_horn_coral', 'dead_horn_coral_block',
        'dead_horn_coral_fan', 'dead_tube_coral', 'dead_tube_coral_block', 'dead_tube_coral_fan', 'detector_rail',
        'detector_rail_on', 'diamond_block', 'diamond_ore', 'diorite', 'dirt', 'dirt_path_side', 'dirt_path_top',
        'dispenser_front', 'dispenser_front_vertical', 'dragon_egg', 'dried_kelp_bottom', 'dried_kelp_side',
        'dried_kelp_top', 'dripstone_block', 'dropper_front', 'dropper_front_vertical', 'emerald_block', 'emerald_ore',
        'enchanting_table_bottom', 'enchanting_table_side', 'enchanting_table_top', 'end_portal_frame_eye',
        'end_portal_frame_side', 'end_portal_frame_top', 'end_rod', 'end_stone', 'end_stone_bricks', 'exposed_copper',
        'exposed_cut_copper', 'farmland', 'farmland_moist', 'fire_0', 'fire_1', 'fire_coral', 'fire_coral_block',
        'fire_coral_fan', 'fletching_table_front', 'fletching_table_side', 'fletching_table_top', 'flower_pot',
        'flowering_azalea_leaves', 'flowering_azalea_side', 'flowering_azalea_top', 'frosted_ice_0', 'frosted_ice_1',
        'frosted_ice_2', 'frosted_ice_3', 'furnace_front', 'furnace_front_on', 'furnace_side', 'furnace_top',
        'gilded_blackstone', 'glass', 'glass_pane_top', 'glow_item_frame', 'glow_lichen', 'glowstone', 'gold_block',
        'gold_ore', 'granite', 'grass', 'grass_block_side', 'grass_block_snow', 'grass_block_top', 'gravel',
        'gray_concrete', 'gray_concrete_powder', 'gray_glazed_terracotta', 'gray_shulker_box', 'gray_stained_glass',
        'gray_stained_glass_pane_top', 'gray_terracotta', 'gray_wool', 'green_concrete', 'green_concrete_powder',
        'green_glazed_terracotta', 'green_shulker_box', 'green_stained_glass', 'green_stained_glass_pane_top',
        'green_terracotta', 'green_wool', 'hanging_roots', 'hay_block_side', 'hay_block_top', 'honey_block_bottom',
        'honey_block_side', 'honey_block_top', 'honeycomb_block', 'hopper_inside', 'hopper_outside', 'hopper_top',
        'horn_coral', 'horn_coral_block', 'horn_coral_fan', 'ice', 'iron_bars', 'iron_block', 'iron_door_bottom',
        'iron_door_top', 'iron_ore', 'iron_trapdoor', 'item_frame', 'jack_o_lantern', 'jigsaw_bottom', 'jigsaw_lock',
        'jigsaw_side', 'jigsaw_top', 'jukebox_side', 'jukebox_top', 'jungle_door_bottom', 'jungle_door_top',
        'jungle_leaves', 'jungle_log', 'jungle_log_top', 'jungle_planks', 'jungle_sapling', 'jungle_trapdoor', 'ladder',
        'lantern', 'lapis_block', 'lapis_ore', 'large_amethyst_bud', 'lava_flow', 'lava_still', 'lectern_base',
        'lectern_front', 'lectern_sides', 'lectern_top', 'lever', 'light_blue_concrete', 'light_blue_concrete_powder',
        'light_blue_glazed_terracotta', 'light_blue_shulker_box', 'light_blue_stained_glass',
        'light_blue_stained_glass_pane_top', 'light_blue_terracotta', 'light_blue_wool', 'light_gray_concrete',
        'light_gray_concrete_powder', 'light_gray_glazed_terracotta', 'light_gray_shulker_box',
        'light_gray_stained_glass', 'light_gray_stained_glass_pane_top', 'light_gray_terracotta', 'light_gray_wool',
        'lightning_rod', 'lily_of_the_valley', 'lily_pad', 'lime_concrete', 'lime_concrete_powder',
        'lime_glazed_terracotta', 'lime_shulker_box', 'lime_stained_glass', 'lime_stained_glass_pane_top',
        'lime_terracotta', 'lime_wool', 'lodestone_side', 'lodestone_top', 'loom_bottom', 'loom_front', 'loom_side',
        'loom_top', 'magenta_concrete', 'magenta_concrete_powder', 'magenta_glazed_terracotta', 'magenta_shulker_box',
        'magenta_stained_glass', 'magenta_stained_glass_pane_top', 'magenta_terracotta', 'magenta_wool', 'magma',
        'medium_amethyst_bud', 'melon_side', 'melon_stem', 'melon_top', 'moss_block', 'mossy_cobblestone',
        'mossy_stone_bricks', 'mushroom_block_inside', 'mushroom_stem', 'mycelium_side', 'mycelium_top',
        'nether_bricks', 'nether_gold_ore', 'nether_portal', 'nether_quartz_ore', 'nether_sprouts', 'nether_wart_block',
        'nether_wart_stage0', 'nether_wart_stage1', 'nether_wart_stage2', 'netherite_block', 'netherrack', 'note_block',
        'oak_door_bottom', 'oak_door_top', 'oak_leaves', 'oak_log', 'oak_log_top', 'oak_planks', 'oak_sapling',
        'oak_trapdoor', 'observer_back', 'observer_back_on', 'observer_front', 'observer_side', 'observer_top',
        'obsidian', 'orange_concrete', 'orange_concrete_powder', 'orange_glazed_terracotta', 'orange_shulker_box',
        'orange_stained_glass', 'orange_stained_glass_pane_top', 'orange_terracotta', 'orange_tulip', 'orange_wool',
        'oxeye_daisy', 'oxidized_copper', 'oxidized_cut_copper', 'packed_ice', 'peony_bottom', 'peony_top',
        'pink_concrete', 'pink_concrete_powder', 'pink_glazed_terracotta', 'pink_shulker_box', 'pink_stained_glass',
        'pink_stained_glass_pane_top', 'pink_terracotta', 'pink_tulip', 'pink_wool', 'piston_bottom', 'piston_inner',
        'piston_side', 'piston_top', 'piston_top_sticky', 'podzol_side', 'podzol_top', 'pointed_dripstone_down_base',
        'pointed_dripstone_down_frustum', 'pointed_dripstone_down_middle', 'pointed_dripstone_down_tip',
        'pointed_dripstone_down_tip_merge', 'pointed_dripstone_up_base', 'pointed_dripstone_up_frustum',
        'pointed_dripstone_up_middle', 'pointed_dripstone_up_tip', 'pointed_dripstone_up_tip_merge',
        'polished_andesite', 'polished_basalt_side', 'polished_basalt_top', 'polished_blackstone',
        'polished_blackstone_bricks', 'polished_diorite', 'polished_granite', 'poppy', 'potatoes_stage0',
        'potatoes_stage1', 'potatoes_stage2', 'potatoes_stage3', 'potted_azalea_bush_plant', 'potted_azalea_bush_side',
        'potted_azalea_bush_top', 'potted_flowering_azalea_bush_plant', 'potted_flowering_azalea_bush_side',
        'potted_flowering_azalea_bush_top', 'powder_snow', 'powered_rail', 'powered_rail_on', 'prismarine',
        'prismarine_bricks', 'pumpkin_side', 'pumpkin_stem', 'pumpkin_top', 'purple_concrete', 'purple_concrete_powder',
        'purple_glazed_terracotta', 'purple_shulker_box', 'purple_stained_glass', 'purple_stained_glass_pane_top',
        'purple_terracotta', 'purple_wool', 'purpur_block', 'purpur_pillar', 'purpur_pillar_top', 'quartz_block_bottom',
        'quartz_block_side', 'quartz_block_top', 'quartz_bricks', 'quartz_pillar', 'quartz_pillar_top', 'rail',
        'rail_corner', 'raw_copper_block', 'raw_gold_block', 'raw_iron_block', 'red_concrete', 'red_concrete_powder',
        'red_glazed_terracotta', 'red_mushroom', 'red_mushroom_block', 'red_nether_bricks', 'red_sand', 'red_sandstone',
        'red_sandstone_bottom', 'red_sandstone_top', 'red_shulker_box', 'red_stained_glass',
        'red_stained_glass_pane_top', 'red_terracotta', 'red_tulip', 'red_wool', 'redstone_block', 'redstone_dust_dot',
        'redstone_dust_line0', 'redstone_dust_line1', 'redstone_lamp', 'redstone_lamp_on', 'redstone_ore',
        'redstone_torch', 'redstone_torch_off', 'repeater', 'repeater_on', 'repeating_command_block_back',
        'repeating_command_block_conditional', 'repeating_command_block_front', 'repeating_command_block_side',
        'respawn_anchor_bottom', 'respawn_anchor_side0', 'respawn_anchor_side1', 'respawn_anchor_side2',
        'respawn_anchor_side3', 'respawn_anchor_side4', 'respawn_anchor_top', 'respawn_anchor_top_off', 'rooted_dirt',
        'rose_bush_bottom', 'rose_bush_top', 'sand', 'sandstone', 'sandstone_bottom', 'sandstone_top', 'sea_lantern',
        'sea_pickle', 'seagrass', 'shroomlight', 'shulker_box', 'slime_block', 'small_amethyst_bud',
        'small_dripleaf_side', 'small_dripleaf_stem_bottom', 'small_dripleaf_stem_top', 'small_dripleaf_top',
        'smithing_table_bottom', 'smithing_table_front', 'smithing_table_side', 'smithing_table_top', 'smoker_bottom',
        'smoker_front', 'smoker_front_on', 'smoker_side', 'smoker_top', 'smooth_basalt', 'smooth_stone',
        'smooth_stone_slab_side', 'snow', 'soul_campfire_fire', 'soul_campfire_log_lit', 'soul_fire_0', 'soul_fire_1',
        'soul_lantern', 'soul_sand', 'soul_soil', 'soul_torch', 'spawner', 'sponge', 'spore_blossom',
        'spore_blossom_base', 'spruce_door_bottom', 'spruce_door_top', 'spruce_leaves', 'spruce_log', 'spruce_log_top',
        'spruce_planks', 'spruce_sapling', 'spruce_trapdoor', 'stone', 'stone_bricks', 'stonecutter_bottom',
        'stonecutter_side', 'stonecutter_top', 'stripped_acacia_log', 'stripped_acacia_log_top', 'stripped_birch_log',
        'stripped_birch_log_top', 'stripped_dark_oak_log', 'stripped_dark_oak_log_top', 'stripped_jungle_log',
        'stripped_jungle_log_top', 'stripped_oak_log', 'stripped_oak_log_top', 'stripped_spruce_log',
        'stripped_spruce_log_top', 'structure_block', 'structure_block_corner', 'structure_block_data',
        'structure_block_load', 'structure_block_save', 'sunflower_back', 'sunflower_bottom', 'sunflower_front',
        'sunflower_top', 'sweet_berry_bush_stage0', 'sweet_berry_bush_stage1', 'sweet_berry_bush_stage2',
        'sweet_berry_bush_stage3', 'tall_seagrass_bottom', 'target_side', 'target_top', 'terracotta', 'tinted_glass',
        'tnt_bottom', 'tnt_side', 'tnt_top', 'torch', 'tripwire', 'tripwire_hook', 'tube_coral', 'tube_coral_block',
        'tube_coral_fan', 'tuff', 'turtle_egg', 'turtle_egg_slightly_cracked', 'turtle_egg_very_cracked',
        'twisting_vines', 'twisting_vines_plant', 'vine', 'warped_fungus', 'warped_nylium', 'warped_nylium_side',
        'warped_roots', 'warped_roots_pot', 'warped_wart_block', 'water_flow', 'water_still', 'weathered_copper',
        'weathered_cut_copper', 'weeping_vines', 'weeping_vines_plant', 'wet_sponge', 'wheat_stage0', 'wheat_stage1',
        'wheat_stage2', 'wheat_stage3', 'wheat_stage4', 'wheat_stage5', 'wheat_stage6', 'wheat_stage7',
        'white_concrete', 'white_concrete_powder', 'white_glazed_terracotta', 'white_shulker_box',
        'white_stained_glass', 'white_stained_glass_pane_top', 'white_terracotta', 'white_tulip', 'white_wool',
        'wither_rose', 'yellow_concrete', 'yellow_concrete_powder', 'yellow_glazed_terracotta', 'yellow_shulker_box',
        'yellow_stained_glass', 'yellow_stained_glass_pane_top', 'yellow_terracotta', 'yellow_wool']
for i in range(len(bedrock)):
    textureB = bedrock[i]
    textureJ = java[i]
    src = r'textures/blocks/'
    src += textureB
    src += '.png'
    dst = r'temp/assets/minecraft/textures/block/'
    dst += textureB
    dst += '.png'
    rnm = r'temp/assets/minecraft/textures/block/'
    rnm += textureJ
    rnm += '.png'
    try:
        shutil.copyfile(src, dst)
        os.rename(dst, rnm)
    except Exception:
        pass
    print(textureB, ' → ', textureJ)
print('Completed /block/ pass #1\n')

# blocks candles/
bedrock = ['black_candle', 'black_candle_lit', 'blue_candle', 'blue_candle_lit', 'brown_candle', 'brown_candle_lit',
           'candle', 'candle_lit', 'cyan_candle', 'cyan_candle_lit', 'gray_candle', 'gray_candle_lit', 'green_candle',
           'green_candle_lit', 'light_blue_candle', 'light_blue_candle_lit', 'lime_candle', 'lime_candle_lit',
           'magenta_candle', 'magenta_candle_lit', 'orange_candle', 'orange_candle_lit', 'pink_candle',
           'pink_candle_lit', 'purple_candle', 'purple_candle_lit', 'red_candle', 'red_candle_lit', 'white_candle',
           'white_candle_lit', 'yellow_candle', 'yellow_candle_lit', 'light_gray_candle', 'light_gray_candle_lit']
java = ['black_candle', 'black_candle_lit', 'blue_candle', 'blue_candle_lit', 'brown_candle', 'brown_candle_lit',
        'candle', 'candle_lit', 'cyan_candle', 'cyan_candle_lit', 'gray_candle', 'gray_candle_lit', 'green_candle',
        'green_candle_lit', 'light_blue_candle', 'light_blue_candle_lit', 'lime_candle', 'lime_candle_lit',
        'magenta_candle', 'magenta_candle_lit', 'orange_candle', 'orange_candle_lit', 'pink_candle', 'pink_candle_lit',
        'purple_candle', 'purple_candle_lit', 'red_candle', 'red_candle_lit', 'white_candle', 'white_candle_lit',
        'yellow_candle', 'yellow_candle_lit', 'light_gray_candle', 'light_gray_candle_lit']
for i in range(len(bedrock)):
    textureB = bedrock[i]
    textureJ = java[i]
    src = r'textures/blocks/candles/'
    src += textureB
    src += '.png'
    dst = r'temp/assets/minecraft/textures/block/'
    dst += textureB
    dst += '.png'
    rnm = r'temp/assets/minecraft/textures/block/'
    rnm += textureJ
    rnm += '.png'
    try:
        shutil.copyfile(src, dst)
        os.rename(dst, rnm)
    except Exception:
        pass
    print(textureB, ' → ', textureJ)
print('Completed /block/ pass #2\n')

# blocks deepslate/
bedrock = ['chiseled_deepslate', 'cobbled_deepslate', 'cracked_deepslate_bricks', 'cracked_deepslate_tiles',
           'deepslate', 'deepslate_bricks', 'deepslate_coal_ore', 'deepslate_copper_ore', 'deepslate_diamond_ore',
           'deepslate_emerald_ore', 'deepslate_gold_ore', 'deepslate_iron_ore', 'deepslate_lapis_ore',
           'deepslate_redstone_ore', 'deepslate_tiles', 'deepslate_top', 'polished_deepslate']
java = ['chiseled_deepslate', 'cobbled_deepslate', 'cracked_deepslate_bricks', 'cracked_deepslate_tiles', 'deepslate',
        'deepslate_bricks', 'deepslate_coal_ore', 'deepslate_copper_ore', 'deepslate_diamond_ore',
        'deepslate_emerald_ore', 'deepslate_gold_ore', 'deepslate_iron_ore', 'deepslate_lapis_ore',
        'deepslate_redstone_ore', 'deepslate_tiles', 'deepslate_top', 'polished_deepslate']
for i in range(len(bedrock)):
    textureB = bedrock[i]
    textureJ = java[i]
    src = r'textures/blocks/deepslate/'
    src += textureB
    src += '.png'
    dst = r'temp/assets/minecraft/textures/block/'
    dst += textureB
    dst += '.png'
    rnm = r'temp/assets/minecraft/textures/block/'
    rnm += textureJ
    rnm += '.png'
    try:
        shutil.copyfile(src, dst)
        os.rename(dst, rnm)
    except Exception:
        pass
    print(textureB, ' → ', textureJ)
print('Completed /block/ pass #3\n')

# blocks huge_fungus/
bedrock = ['crimson_door_lower', 'crimson_door_top', 'crimson_planks', 'crimson_log_side', 'crimson_log_top',
           'crimson_trapdoor', 'stripped_crimson_stem_side', 'stripped_crimson_stem_top', 'stripped_warped_stem_side',
           'stripped_warped_stem_top', 'warped_door_lower', 'warped_door_top', 'warped_planks', 'warped_stem_side',
           'warped_stem_top', 'warped_trapdoor']
java = ['crimson_door_bottom', 'crimson_door_top', 'crimson_planks', 'crimson_stem', 'crimson_stem_top',
        'crimson_trapdoor', 'stripped_crimson_stem', 'stripped_crimson_stem_top', 'stripped_warped_stem',
        'stripped_warped_stem_top', 'warped_door_bottom', 'warped_door_top', 'warped_planks', 'warped_stem',
        'warped_stem_top', 'warped_trapdoor']
for i in range(len(bedrock)):
    textureB = bedrock[i]
    textureJ = java[i]
    src = r'textures/blocks/huge_fungus/'
    src += textureB
    src += '.png'
    dst = r'temp/assets/minecraft/textures/block/'
    dst += textureB
    dst += '.png'
    rnm = r'temp/assets/minecraft/textures/block/'
    rnm += textureJ
    rnm += '.png'
    try:
        shutil.copyfile(src, dst)
        os.rename(dst, rnm)
    except Exception:
        pass
    print(textureB, ' → ', textureJ)
print('Completed /block/ pass #4\n')

# items
bedrock = ['boat_acacia', 'door_acacia', 'sign_acacia', 'amethyst_shard', 'apple', 'armor_stand', 'arrow',
           'bucket_axolotl', 'potato_baked', 'bamboo', 'beef_raw', 'beetroot', 'seeds_beetroot', 'beetroot_soup',
           'boat_birch', 'door_birch', 'sign_birch', 'dye_powder_black_new', 'blaze_powder', 'blaze_rod',
           'dye_powder_blue', 'bone', 'dye_powder_white', 'book_normal', 'bow_standby', 'bow_pulling_0',
           'bow_pulling_1', 'bow_pulling_2', 'bowl', 'bread', 'brewing_stand', 'brick', 'broken_elytra',
           'dye_powder_brown_new', 'bucket_empty', 'cake', 'campfire', 'carrot', 'carrot_on_a_stick', 'cauldron',
           'chain', 'chainmail_boots', 'chainmail_chestplate', 'chainmail_helmet', 'chainmail_leggings', 'charcoal',
           'minecart_chest', 'chicken_raw', 'chorus_fruit', 'clay_ball', 'coal', 'dye_powder_brown', 'fish_raw',
           'bucket_cod', 'minecart_command_block', 'comparator', 'beef_cooked', 'chicken_cooked', 'fish_cooked',
           'mutton_cooked', 'porkchop_cooked', 'rabbit_cooked', 'fish_salmon_cooked', 'cookie', 'copper_ingot',
           'banner_pattern', 'crimson_door', 'sign_crimson', 'crossbow_arrow', 'crossbow_firework',
           'crossbow_pulling_0', 'crossbow_pulling_1', 'crossbow_pulling_2', 'crossbow_standby', 'dye_powder_cyan',
           'boat_darkoak', 'door_dark_oak', 'sign_darkoak', 'diamond', 'diamond_axe', 'diamond_boots',
           'diamond_chestplate', 'diamond_helmet', 'diamond_hoe', 'diamond_horse_armor', 'diamond_leggings',
           'diamond_pickaxe', 'diamond_shovel', 'diamond_sword', 'dragons_breath', 'dried_kelp', 'egg', 'elytra',
           'emerald', 'empty_armor_slot_boots', 'empty_armor_slot_chestplate', 'empty_armor_slot_helmet',
           'empty_armor_slot_leggings', 'empty_armor_slot_shield', 'book_enchanted', 'end_crystal', 'ender_eye',
           'ender_pearl', 'experience_bottle', 'feather', 'spider_eye_fermented', 'map_filled', 'map_filled',
           'fireball', 'fireworks', 'fishing_rod_uncast', 'fishing_rod_cast', 'flint', 'flint_and_steel',
           'banner_pattern', 'flower_pot', 'minecart_furnace', 'ghast_tear', 'potion_bottle_empty', 'melon_speckled',
           'banner_pattern', 'glow_berries', 'dye_powder_glow', 'glow_item_frame', 'glowstone_dust', 'gold_ingot',
           'gold_nugget', 'apple_golden', 'gold_axe', 'gold_boots', 'carrot_golden', 'gold_chestplate', 'gold_helmet',
           'gold_hoe', 'gold_horse_armor', 'gold_leggings', 'gold_pickaxe', 'gold_shovel', 'gold_sword',
           'dye_powder_gray', 'dye_powder_green', 'gunpowder', 'heartofthesea_closed', 'honey_bottle', 'honeycomb',
           'hopper', 'minecart_hopper', 'dye_powder_black', 'iron_axe', 'iron_boots', 'iron_chestplate', 'door_iron',
           'iron_helmet', 'iron_hoe', 'iron_horse_armor', 'iron_ingot', 'iron_leggings', 'iron_nugget', 'iron_pickaxe',
           'iron_shovel', 'iron_sword', 'item_frame', 'boat_jungle', 'door_jungle', 'sign_jungle', 'kelp', 'lantern',
           'dye_powder_blue', 'bucket_lava', 'lead', 'leather', 'light_block_0', 'light_block_1', 'light_block_2',
           'light_block_3', 'light_block_4', 'light_block_5', 'light_block_6', 'light_block_7', 'light_block_8',
           'light_block_9', 'light_block_10', 'light_block_11', 'light_block_12', 'light_block_13', 'light_block_14',
           'light_block_15', 'dye_powder_light_blue', 'dye_powder_silver', 'dye_powder_lime',
           'potion_bottle_lingering_empty', 'dye_powder_magenta', 'magma_cream', 'map_empty', 'seeds_melon', 'melon',
           'bucket_milk', 'minecart_normal', 'banner_pattern', 'mushroom_stew', 'record_11', 'record_13',
           'record_blocks', 'record_cat', 'record_chirp', 'record_far', 'record_mall', 'record_mellohi',
           'record_otherside', 'record_pigstep', 'record_stal', 'record_strad', 'record_wait', 'record_ward',
           'mutton_raw', 'name_tag', 'nautilus', 'netherbrick', 'nether_sprouts', 'nether_star', 'nether_wart',
           'netherite_axe', 'netherite_boots', 'netherite_chestplate', 'netherite_helmet', 'netherite_hoe',
           'netherite_ingot', 'netherite_leggings', 'netherite_pickaxe', 'netherite_scrap', 'netherite_shovel',
           'netherite_sword', 'boat_oak', 'door_wood', 'sign', 'dye_powder_orange', 'painting', 'paper',
           'phantom_membrane', 'banner_pattern', 'dye_powder_pink', 'potato_poisonous', 'chorus_fruit_popped',
           'porkchop_raw', 'potato', 'potion_bottle_empty', 'potion_overlay', 'bucket_powder_snow',
           'prismarine_crystals', 'prismarine_shard', 'fish_pufferfish_raw', 'bucket_pufferfish', 'pumpkin_pie',
           'seeds_pumpkin', 'dye_powder_purple', 'quartz', 'rabbit_raw', 'rabbit_foot', 'rabbit_hide', 'rabbit_stew',
           'raw_copper', 'raw_gold', 'raw_iron', 'dye_powder_red', 'redstone_dust', 'repeater', 'rotten_flesh',
           'saddle', 'fish_salmon_raw', 'bucket_salmon', 'turtle_shell_piece', 'sea_pickle', 'shears', 'shulker_shell',
           'banner_pattern', 'slimeball', 'snowball', 'soul_campfire', 'soul_lantern', 'spawn_egg', 'spawn_egg_overlay',
           'spider_eye', 'boat_spruce', 'door_spruce', 'sign_spruce', 'spyglass', 'spyglass', 'stick', 'stone_axe',
           'stone_hoe', 'stone_pickaxe', 'stone_shovel', 'stone_sword', 'string', 'sugar', 'reeds', 'suspicious_stew',
           'sweet_berries', 'tipped_arrow_base', 'tipped_arrow_head', 'minecart_tnt', 'totem', 'trident',
           'fish_clownfish_raw', 'bucket_tropical', 'turtle_egg', 'turtle_helmet', 'warped_door',
           'warped_fungus_on_a_stick', 'sign_warped', 'bucket_water', 'wheat', 'seeds_wheat', 'dye_powder_white_new',
           'wood_axe', 'wood_hoe', 'wood_pickaxe', 'wood_shovel', 'wood_sword', 'book_writable', 'book_written',
           'dye_powder_yellow', 'leather_chestplate', 'leather_chestplate']
java = ['acacia_boat', 'acacia_door', 'acacia_sign', 'amethyst_shard', 'apple', 'armor_stand', 'arrow',
        'axolotl_bucket', 'baked_potato', 'bamboo', 'beef', 'beetroot', 'beetroot_seeds', 'beetroot_soup', 'birch_boat',
        'birch_door', 'birch_sign', 'black_dye', 'blaze_powder', 'blaze_rod', 'blue_dye', 'bone', 'bone_meal', 'book',
        'bow', 'bow_pulling_0', 'bow_pulling_1', 'bow_pulling_2', 'bowl', 'bread', 'brewing_stand', 'brick',
        'broken_elytra', 'brown_dye', 'bucket', 'cake', 'campfire', 'carrot', 'carrot_on_a_stick', 'cauldron', 'chain',
        'chainmail_boots', 'chainmail_chestplate', 'chainmail_helmet', 'chainmail_leggings', 'charcoal',
        'chest_minecart', 'chicken', 'chorus_fruit', 'clay_ball', 'coal', 'cocoa_beans', 'cod', 'cod_bucket',
        'command_block_minecart', 'comparator', 'cooked_beef', 'cooked_chicken', 'cooked_cod', 'cooked_mutton',
        'cooked_porkchop', 'cooked_rabbit', 'cooked_salmon', 'cookie', 'copper_ingot', 'creeper_banner_pattern',
        'crimson_door', 'crimson_sign', 'crossbow_arrow', 'crossbow_firework', 'crossbow_pulling_0',
        'crossbow_pulling_1', 'crossbow_pulling_2', 'crossbow_standby', 'cyan_dye', 'dark_oak_boat', 'dark_oak_door',
        'dark_oak_sign', 'diamond', 'diamond_axe', 'diamond_boots', 'diamond_chestplate', 'diamond_helmet',
        'diamond_hoe', 'diamond_horse_armor', 'diamond_leggings', 'diamond_pickaxe', 'diamond_shovel', 'diamond_sword',
        'dragon_breath', 'dried_kelp', 'egg', 'elytra', 'emerald', 'empty_armor_slot_boots',
        'empty_armor_slot_chestplate', 'empty_armor_slot_helmet', 'empty_armor_slot_leggings',
        'empty_armor_slot_shield', 'enchanted_book', 'end_crystal', 'ender_eye', 'ender_pearl', 'experience_bottle',
        'feather', 'fermented_spider_eye', 'filled_map', 'filled_map_markings', 'fire_charge', 'firework_rocket',
        'fishing_rod', 'fishing_rod_cast', 'flint', 'flint_and_steel', 'flower_banner_pattern', 'flower_pot',
        'furnace_minecart', 'ghast_tear', 'glass_bottle', 'glistering_melon_slice', 'globe_banner_pattern',
        'glow_berries', 'glow_ink_sac', 'glow_item_frame', 'glowstone_dust', 'gold_ingot', 'gold_nugget',
        'golden_apple', 'golden_axe', 'golden_boots', 'golden_carrot', 'golden_chestplate', 'golden_helmet',
        'golden_hoe', 'golden_horse_armor', 'golden_leggings', 'golden_pickaxe', 'golden_shovel', 'golden_sword',
        'gray_dye', 'green_dye', 'gunpowder', 'heart_of_the_sea', 'honey_bottle', 'honeycomb', 'hopper',
        'hopper_minecart', 'ink_sac', 'iron_axe', 'iron_boots', 'iron_chestplate', 'iron_door', 'iron_helmet',
        'iron_hoe', 'iron_horse_armor', 'iron_ingot', 'iron_leggings', 'iron_nugget', 'iron_pickaxe', 'iron_shovel',
        'iron_sword', 'item_frame', 'jungle_boat', 'jungle_door', 'jungle_sign', 'kelp', 'lantern', 'lapis_lazuli',
        'lava_bucket', 'lead', 'leather', 'light_00', 'light_01', 'light_02', 'light_03', 'light_04', 'light_05',
        'light_06', 'light_07', 'light_08', 'light_09', 'light_10', 'light_11', 'light_12', 'light_13', 'light_14',
        'light_15', 'light_blue_dye', 'light_gray_dye', 'lime_dye', 'lingering_potion', 'magenta_dye', 'magma_cream',
        'map', 'melon_seeds', 'melon_slice', 'milk_bucket', 'minecart', 'mojang_banner_pattern', 'mushroom_stew',
        'music_disc_11', 'music_disc_13', 'music_disc_blocks', 'music_disc_cat', 'music_disc_chirp', 'music_disc_far',
        'music_disc_mall', 'music_disc_mellohi', 'music_disc_otherside', 'music_disc_pigstep', 'music_disc_stal',
        'music_disc_strad', 'music_disc_wait', 'music_disc_ward', 'mutton', 'name_tag', 'nautilus_shell',
        'nether_brick', 'nether_sprouts', 'nether_star', 'nether_wart', 'netherite_axe', 'netherite_boots',
        'netherite_chestplate', 'netherite_helmet', 'netherite_hoe', 'netherite_ingot', 'netherite_leggings',
        'netherite_pickaxe', 'netherite_scrap', 'netherite_shovel', 'netherite_sword', 'oak_boat', 'oak_door',
        'oak_sign', 'orange_dye', 'painting', 'paper', 'phantom_membrane', 'piglin_banner_pattern', 'pink_dye',
        'poisonous_potato', 'popped_chorus_fruit', 'porkchop', 'potato', 'potion', 'potion_overlay',
        'powder_snow_bucket', 'prismarine_crystals', 'prismarine_shard', 'pufferfish', 'pufferfish_bucket',
        'pumpkin_pie', 'pumpkin_seeds', 'purple_dye', 'quartz', 'rabbit', 'rabbit_foot', 'rabbit_hide', 'rabbit_stew',
        'raw_copper', 'raw_gold', 'raw_iron', 'red_dye', 'redstone', 'repeater', 'rotten_flesh', 'saddle', 'salmon',
        'salmon_bucket', 'scute', 'sea_pickle', 'shears', 'shulker_shell', 'skull_banner_pattern', 'slime_ball',
        'snowball', 'soul_campfire', 'soul_lantern', 'spawn_egg', 'spawn_egg_overlay', 'spider_eye', 'spruce_boat',
        'spruce_door', 'spruce_sign', 'spyglass', 'spyglass_model', 'stick', 'stone_axe', 'stone_hoe', 'stone_pickaxe',
        'stone_shovel', 'stone_sword', 'string', 'sugar', 'sugar_cane', 'suspicious_stew', 'sweet_berries',
        'tipped_arrow_base', 'tipped_arrow_head', 'tnt_minecart', 'totem_of_undying', 'trident', 'tropical_fish',
        'tropical_fish_bucket', 'turtle_egg', 'turtle_helmet', 'warped_door', 'warped_fungus_on_a_stick', 'warped_sign',
        'water_bucket', 'wheat', 'wheat_seeds', 'white_dye', 'wooden_axe', 'wooden_hoe', 'wooden_pickaxe',
        'wooden_shovel', 'wooden_sword', 'writable_book', 'written_book', 'yellow_dye', 'leather_chestplate',
        'leather_chestplate_overlay']
for i in range(len(bedrock)):
    textureB = bedrock[i]
    textureJ = java[i]
    src = r'textures/items/'
    src += textureB
    src += '.png'
    dst = r'temp/assets/minecraft/textures/item/'
    dst += textureB
    dst += '.png'
    rnm = r'temp/assets/minecraft/textures/item/'
    rnm += textureJ
    rnm += '.png'
    try:
        shutil.copyfile(src, dst)
        os.rename(dst, rnm)
    except Exception:
        pass
    print(textureB, ' → ', textureJ)

try:
    src = r'textures/ui/recipe_book_icon.png'
    dst = r'temp/assets/minecraft/textures/item/recipe_book_icon.png'
    rnm = r'temp/assets/minecraft/textures/item/knowledge_book.png'
    shutil.copyfile(src, dst)
    os.rename(dst, rnm)
except Exception:
    pass
try:
    src = r'textures/blocks/pointed_dripstone_down_tip.png'
    dst = r'temp/assets/minecraft/textures/item/pointed_dripstone_down_tip.png'
    rnm = r'temp/assets/minecraft/textures/item/pointed_dripstone.png'
    shutil.copyfile(src, dst)
    os.rename(dst, rnm)
except Exception:
    pass
print('Completed /item/ pass #1\n')

# items candles/
bedrock = ['black_candle', 'blue_candle', 'brown_candle', 'candle', 'cyan_candle', 'gray_candle', 'green_candle',
           'light_blue_candle', 'lime_candle', 'magenta_candle', 'orange_candle', 'pink_candle', 'purple_candle',
           'red_candle', 'white_candle', 'yellow_candle', 'light_gray_candle']
java = ['black_candle', 'blue_candle', 'brown_candle', 'candle', 'cyan_candle', 'gray_candle', 'green_candle',
        'light_blue_candle', 'lime_candle', 'magenta_candle', 'orange_candle', 'pink_candle', 'purple_candle',
        'red_candle', 'white_candle', 'yellow_candle', 'light_gray_candle']
for i in range(len(bedrock)):
    textureB = bedrock[i]
    textureJ = java[i]
    src = r'textures/items/candles/'
    src += textureB
    src += '.png'
    dst = r'temp/assets/minecraft/textures/item/'
    dst += textureB
    dst += '.png'
    rnm = r'temp/assets/minecraft/textures/item/'
    rnm += textureJ
    rnm += '.png'
    try:
        shutil.copyfile(src, dst)
        os.rename(dst, rnm)
    except Exception:
        pass
    print(textureB, ' → ', textureJ)
print('Completed /item/ pass #2\n')

# colormap
bedrock = ['foliage', 'grass']
java = ['foliage', 'grass']
for i in range(len(bedrock)):
    textureB = bedrock[i]
    textureJ = java[i]
    src = r'textures/colormap/'
    src += textureB
    src += '.png'
    dst = r'temp/assets/minecraft/textures/colormap/'
    dst += textureB
    dst += '.png'
    rnm = r'temp/assets/minecraft/textures/colormap/'
    rnm += textureJ
    rnm += '.png'
    try:
        shutil.copyfile(src, dst)
        os.rename(dst, rnm)
    except Exception:
        pass
    print(textureB, ' → ', textureJ)
print('Completed /colormap/\n')

# environment
bedrock = ['clouds', 'end_sky', 'moon_phases', 'sun']
java = ['clouds', 'end_sky', 'moon_phases', 'sun']
for i in range(len(bedrock)):
    textureB = bedrock[i]
    textureJ = java[i]
    src = r'textures/environment/'
    src += textureB
    src += '.png'
    dst = r'temp/assets/minecraft/textures/environment/'
    dst += textureB
    dst += '.png'
    rnm = r'temp/assets/minecraft/textures/environment/'
    rnm += textureJ
    rnm += '.png'
    try:
        shutil.copyfile(src, dst)
        os.rename(dst, rnm)
    except Exception:
        pass
    print(textureB, ' → ', textureJ)
print('Completed /environment/\n')

# environment
bedrock = ['clouds', 'end_sky', 'moon_phases', 'sun']
java = ['clouds', 'end_sky', 'moon_phases', 'sun']
for i in range(len(bedrock)):
    textureB = bedrock[i]
    textureJ = java[i]
    src = r'textures/environment/'
    src += textureB
    src += '.png'
    dst = r'temp/assets/minecraft/textures/environment/'
    dst += textureB
    dst += '.png'
    rnm = r'temp/assets/minecraft/textures/environment/'
    rnm += textureJ
    rnm += '.png'
    try:
        shutil.copyfile(src, dst)
        os.rename(dst, rnm)
    except Exception:
        pass
    print(textureB, ' → ', textureJ)
print('Completed /environment/ pass #1\n')

# environment bedrockDestroy
bedrock = ['destroy_stage_0', 'destroy_stage_1', 'destroy_stage_2', 'destroy_stage_3', 'destroy_stage_4',
           'destroy_stage_5', 'destroy_stage_6', 'destroy_stage_7', 'destroy_stage_8', 'destroy_stage_9']
java = ['destroy_stage_0', 'destroy_stage_1', 'destroy_stage_2', 'destroy_stage_3', 'destroy_stage_4',
        'destroy_stage_5', 'destroy_stage_6', 'destroy_stage_7', 'destroy_stage_8', 'destroy_stage_9']
for i in range(len(bedrock)):
    textureB = bedrock[i]
    textureJ = java[i]
    src = r'textures/environment/'
    src += textureB
    src += '.png'
    dst = r'temp/assets/minecraft/textures/block/'
    dst += textureB
    dst += '.png'
    rnm = r'temp/assets/minecraft/textures/block/'
    rnm += textureJ
    rnm += '.png'
    try:
        shutil.copyfile(src, dst)
        os.rename(dst, rnm)
    except Exception:
        pass
    print(textureB, ' → ', textureJ)
print('Completed /environment/ pass #2\n')

# map
bedrock = ['map_background']
java = ['map_background']
for i in range(len(bedrock)):
    textureB = bedrock[i]
    textureJ = java[i]
    src = r'textures/map/'
    src += textureB
    src += '.png'
    dst = r'temp/assets/minecraft/textures/map/'
    dst += textureB
    dst += '.png'
    rnm = r'temp/assets/minecraft/textures/map/'
    rnm += textureJ
    rnm += '.png'
    try:
        shutil.copyfile(src, dst)
        os.rename(dst, rnm)
    except Exception:
        pass
    print(textureB, ' → ', textureJ)
print('Completed /map/\n')

# misc
bedrock = ['pumpkinblur']
java = ['pumpkinblur']
for i in range(len(bedrock)):
    textureB = bedrock[i]
    textureJ = java[i]
    src = r'textures/misc/'
    src += textureB
    src += '.png'
    dst = r'temp/assets/minecraft/textures/misc/'
    dst += textureB
    dst += '.png'
    rnm = r'temp/assets/minecraft/textures/misc/'
    rnm += textureJ
    rnm += '.png'
    try:
        shutil.copyfile(src, dst)
        os.rename(dst, rnm)
    except Exception:
        pass
    print(textureB, ' → ', textureJ)
print('Completed /misc/ pass #1\n')

# models
bedrock = ['chain_1', 'chain_2', 'cloth_1', 'cloth_2', 'diamond_1', 'diamond_2', 'gold_1', 'gold_2', 'iron_1', 'iron_2',
           'netherite_1', 'netherite_2', 'turtle_1']
java = ['chain_layer_1', 'chain_layer_2', 'leather_layer_1', 'leather_layer_2', 'diamond_layer_1', 'diamond_layer_2',
        'gold_layer_1', 'gold_layer_2', 'iron_layer_1', 'iron_layer_2', 'netherite_layer_1', 'netherite_layer_2',
        'turtle_layer_1']
for i in range(len(bedrock)):
    textureB = bedrock[i]
    textureJ = java[i]
    src = r'textures/models/armor/'
    src += textureB
    src += '.png'
    dst = r'temp/assets/minecraft/textures/models/armor/'
    dst += textureB
    dst += '.png'
    rnm = r'temp/assets/minecraft/textures/models/armor/'
    rnm += textureJ
    rnm += '.png'
    try:
        shutil.copyfile(src, dst)
        os.rename(dst, rnm)
    except Exception:
        pass
    print(textureB, ' → ', textureJ)
print('Completed /models/\n')

# mob_effect bedrockUI
bedrock = ['absorption_effect', 'bad_omen_effect', 'blindness_effect', 'conduit_power_effect', 'fire_resistance_effect',
           'haste_effect', 'health_boost_effect', 'village_hero_effect', 'hunger_effect', 'invisibility_effect',
           'jump_boost_effect', 'levitation_effect', 'mining_fatigue_effect', 'nausea_effect', 'night_vision_effect',
           'poison_effect', 'regeneration_effect', 'resistance_effect', 'slow_falling_effect', 'slowness_effect',
           'speed_effect', 'strength_effect', 'water_breathing_effect', 'weakness_effect', 'wither_effect']
java = ['absorption', 'bad_omen', 'blindness', 'conduit_power', 'fire_resistance', 'haste', 'health_boost',
        'hero_of_the_village', 'hunger', 'invisibility', 'jump_boost', 'levitation', 'mining_fatigue', 'nausea',
        'night_vision', 'poison', 'regeneration', 'resistance', 'slow_falling', 'slowness', 'speed', 'strength',
        'water_breathing', 'weakness', 'wither']
for i in range(len(bedrock)):
    textureB = bedrock[i]
    textureJ = java[i]
    src = r'textures/ui/'
    src += textureB
    src += '.png'
    dst = r'temp/assets/minecraft/textures/mob_effect/'
    dst += textureB
    dst += '.png'
    rnm = r'temp/assets/minecraft/textures/mob_effect/'
    rnm += textureJ
    rnm += '.png'
    try:
        shutil.copyfile(src, dst)
        os.rename(dst, rnm)
    except Exception:
        pass
    print(textureB, ' → ', textureJ)
print('Completed /mob_effect/\n')

# misc bedrockUI
bedrock = ['frozen_effect', 'spyglass_scope']
java = ['powder_snow_outline', 'spyglass_scope']
for i in range(len(bedrock)):
    textureB = bedrock[i]
    textureJ = java[i]
    src = r'textures/ui/'
    src += textureB
    src += '.png'
    dst = r'temp/assets/minecraft/textures/misc/'
    dst += textureB
    dst += '.png'
    rnm = r'temp/assets/minecraft/textures/misc/'
    rnm += textureJ
    rnm += '.png'
    try:
        shutil.copyfile(src, dst)
        os.rename(dst, rnm)
    except Exception:
        pass
    print(textureB, ' → ', textureJ)
print('Completed /misc/ pass #2\n')

# tga blocks
bedrock = ['grass_side', 'stonecutter2_saw', 'seagrass_doubletall_top_a', 'seagrass_doubletall_bottom_a',
           'scaffolding_top', 'scaffolding_side', 'scaffolding_bottom', 'reeds', 'kelp_top', 'kelp_a',
           'grindstone_side', 'grindstone_pivot', 'grindstone_round', 'fern', 'double_plant_syringa_top',
           'double_plant_syringa_bottom', 'double_plant_grass_top', 'double_plant_grass_bottom',
           'double_plant_fern_top', 'double_plant_fern_bottom', 'cactus_top', 'cactus_bottom', 'cactus_side']
java = ['grass_block_side_overlay', 'stonecutter_saw', 'tall_seagrass_top', 'tall_seagrass_bottom', 'scaffolding_top',
        'scaffolding_side', 'scaffolding_bottom', 'sugar_cane', 'kelp', 'kelp_plant', 'grindstone_side',
        'grindstone_pivot', 'grindstone_round', 'fern', 'lilac_top', 'lilac_bottom', 'tall_grass_top',
        'tall_grass_bottom', 'large_fern_top', 'large_fern_bottom', 'cactus_top', 'cactus_bottom', 'cactus_side']
for i in range(len(bedrock)):
    textureB = bedrock[i]
    textureJ = java[i]
    src = r'textures/blocks/'
    src += textureB
    src += '.tga'
    rnm = r'temp/assets/minecraft/textures/block/'
    rnm += textureJ
    rnm += '.png'
    try:
        Image.open(src).save(rnm)
    except Exception:
        pass
    print(textureB, ' → ', textureJ)
print('Completed /block/ targa pass\n')

# tga items
bedrock = ['leather_boots', 'leather_boots', 'leather_helmet', 'leather_helmet', 'leather_horse_armor',
           'leather_leggings', 'leather_leggings']
java = ['leather_boots', 'leather_boots_overlay', 'leather_helmet', 'leather_helmet_overlay', 'leather_horse_armor',
        'leather_leggings', 'leather_leggings_overlay']
for i in range(len(bedrock)):
    textureB = bedrock[i]
    textureJ = java[i]
    src = r'textures/items/'
    src += textureB
    src += '.tga'
    rnm = r'temp/assets/minecraft/textures/item/'
    rnm += textureJ
    rnm += '.png'
    try:
        Image.open(src).save(rnm)
    except Exception:
        pass
    print(textureB, ' → ', textureJ)
print('Completed /item/ targa pass\n')

shutil.make_archive(packName, 'zip', 'temp')
shutil.rmtree('temp/')
print('Successfully compressed', packName, '. zip')
