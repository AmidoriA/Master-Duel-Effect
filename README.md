# Master-Duel-Effect

## Required Tools for build
* [Python 3](https://www.python.org/downloads/)
* [AssetStudio](https://github.com/Perfare/AssetStudio/releases) - Tool for read a list of asset in Unity
* [UABEA](https://github.com/nesrak1/UABEA/releases) - Tool for pack a mod file back into the game

## Extracting language files from the game
1. Following this [Yu-Gi-Oh modding guide](https://www.nexusmods.com/yugiohmasterduel/articles/3) to use AssetStudio. However, the file we want to load is `Yu-Gi-Oh!  Master Duel\masterduel_Data\data.unity3d`
2. Extract `CARD_Desc`, `CARD_Indx` and `CARD_Name` from the game using AssetStudio
3. In the directory with 3 files above. Run `python "_CARD_decrypt_Desc+Indx+Name.py"` to decrypt the file
4. Run `python "_CARD_Name+Desc_split.py"` to convert those files into JSON


## Build and replacing to the game file
1. Once you update the `CARD_Desc.dec.json` and `CARD_Desc.dec.json`. Then run the command `python "_CARD_merge+calc_index.py"`. This will give you 3 files `CARD_Desc`, `CARD_Indx` and `CARD_Name`
2. Rename 3 files above to be `.txt`. We doing this because UABEA only allow us to import `.txt` file.
3. We need to identify `path_id` of the file. Run AssetStudio and open the `data.unity3d` file from `Yu-Gi-Oh!  Master Duel\masterduel_Data`

![image](https://user-images.githubusercontent.com/4957582/181438129-98fa50ce-c50a-47e6-99b3-9df92f0ee1bd.png)

4. Remember the `PathId` of the language that you want to replace. Do this for every files (`CARD_Desc`, `CARD_Indx` and `CARD_Name`). Then close the AssetStudio.

![image](https://user-images.githubusercontent.com/4957582/181438417-b9b2ce1a-f26c-4a0f-bf58-280cbc47444f.png)

5. Open UABEA. Open `data.unity3d` and then click Info.
6. Try to locate the all 3 CARD_ files with the same PathId. Click `Plugins > Import .txt`. And then importing `.txt` files from step 2.

![image](https://user-images.githubusercontent.com/4957582/181439832-73631410-bd14-43b5-8c5f-189f36c0615b.png)

7. In the Assets Info window. `File > Save` and then `File > Close`.
8. Then Save again on UABEA window. UABEA won't allow us to override opened file. So we need to save it as another name.
9. Replace the old `data.unity3d` file with the new one. (Make sure you made a copy of it)

## Contribution
* You can create a pull request to update `CARD_Desc.dec.json` and `CARD_Desc.dec.json`. 

## Special Thanks
* [Yu-Gi-Oh modding guide](https://www.nexusmods.com/yugiohmasterduel/articles/3) from Nexus mod 
