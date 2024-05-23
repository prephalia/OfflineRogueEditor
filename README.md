# OfflineRogueEditor

**OfflineRogueEditor** is a solution for editing save files in the offline version for pokerogue written in Python.

## Preface

Due to the high number of players playing the offline version of pokerogue, this set of tools has been crafted. This tool covers two offline pokerogue versions:
- [Official pokerogue's version](https://github.com/pagefaultgames/pokerogue)
- [Admiral-Billy's version](https://github.com/Admiral-Billy/Pokerogue-App)

## Requirements

- Python 3.10.x
- Requests library

## Using the tool for the Official Pokerogue's version 

- Go into `compiled/` and copy the `patch/` folder into the root directory of the official pokerogue's build;
- Enter the patch folder that you just copied in the pokerogue directory and run as administrator `patcher.exe`;
- Run pokerogue as instructed in their github repo. Press M and press Manage Data, you'll get two export options:
    - Export Data will dump you `data_Guest.json` which is the equivalent of `trainer.json`, so it has all the informations and properties of your account;
    - Export Session will dump you `dataSession_Guest.json` which will contain the data of the gamesave slot you have choosen;
- Copy and paste these json files(or just the one file you want to edit) into `compiled/editor/` folder.
- After they've been copied in the same place where there is `offlineEditor.exe`. Run it as administrator, and choose the command you want to apply to the file;
- After you have finished, go back in the game, press M and then select:
    - For the trainer data `Import Data`: make sure to choose the right json file(the one in the `compiled/editor` folder);
    - For the gamesave slot data choose `Import session`;

## Using the tool for the Admiral-Billy's version
- Open the game and press M, and then Manage Data:
    - Export Data will dump you `data_Guest.prsv` which is the equivalent of `trainer.json`, so it has all the informations and properties of your account;
    - Export Session will dump you `dataSession_Guest.prsv` which will contain the data of the gamesave slot you have choosen;
- Go into `encrypt&decryptTool` and click on `index.html`. It should open a web page;
- Press `Choose File` and select the .prsv file you want to decrypt and press `Decrypt and Download`;
- After you decrypt it, take the downloaded .json file and move it to the `compiled/editor/` and run `offlineEditor.exe` as administrator;
- Make all the modifications you need to, open the index.html on `encrypt&decryptTool` again, press the `Choose File` button, load the .json file and choose `Encrypt and Download`;
- After you have finished, go back in the game, press M and then select:
    - For the trainer data `Import Data`: make sure to choose the updated .prsv file(the one in the `compiled/editor` folder);
    - For the gamesave slot data choose `Import session`(make sure to select the updated .prsv file);

## Warning

The AntiVirus might label it as a virus. All the source code is available into the `src/` folder, and you can even decompile the exe files; they've been compiled with pyinstaller.

## Commands list
(Refresh your pokerogue.net page after any modifications!)

Hatch all eggs
- This will make all your eggs hatch after you defeat 1 Pokemon.

Unlock/modify a starter Pokémon (name/id)
- This allows you to unlock and/or modify a Pokemon by its name or id (IVs, Candies, Shiny tiers, etc)

Modify the number of egg gacha tickets you have
- This allows you to set the amount of egg gacha tickets you have of every tier

Unlock all starters
- This will unlock every single Pokemon in the Pokedex with Perfect IVs, All natures, abilities, genders and optional shiny tiers.

Display all Pokémon with their names and id
- This simply shows you all the available Pokemon in the game with their names and id (Useful when you want to modify specific Pokemon)

Unlock all game modes
- Unlocks: classic, endless, spliced endless

Unlock all achievements
- Unlocks every achievement

Unlock all vouchers
- Unlocks every voucher

Edit a pokemon in your party
- Let's you edit moves, species and level of a Pokemon in your team. It let's you set it shiny and its variant and makes it 6 IVs

Show all biomes IDs
- Displays all the biomes's IDs

Show all moves IDs
- Displays all the moves's IDs
  
## Other Projects

If you're interested in the online solution for this editor, make sure to checkout [this repo](https://github.com/fire6945/RogueEditor) i'm working on with other people.

<!-- Metadata: keywords -->
<meta name="description" content="is a solution for editing save files in the offline version for pokerogue written in Python.">
<meta name="keywords" content="pokerogue, pokerogue save editor, pokerogue hacks, pokerogue hack, pokerogue cheats, pokerogue cheat, pokerogue trainer, pokerogue cheat table, rogueEditor, free, gacha, ticket, tickets, egg, eggs, shiny, save, edit, pokemon, unlimited, hack, hacks, cheat, cheats, trainer, table, pokedex, dex, wave, money, level, levels, iv, ivs, stat, stats, item, items, api, mod, mods, tool, tools">