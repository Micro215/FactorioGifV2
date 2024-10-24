# FactorioGifV2
This script creates factorio blueprints from gif or any video

Allows [ANY] x 216 resolution

***Currently works without SpaceAge***

## What do you need
Recomended python version: 3.12.3 (not tested with other)

You need to install the required packages from the "requirements.txt" file:

* for windows:
***pip -r requirements.txt***
* for linux:
***python3 -m pip -r requirements.txt***

## How to generate
1. Run main.py:
```python main.py```
2. Paste path to file:
```Enter file path: C:/.../MyGif.gif```
3. If the video has a high resolution or you want to change it, then select resize:
```Need resize? [Y/N]: y```
4. Then print new height of blueprint (in pixels): ```Enter new height (MAX=216): 144```
5. If the video has a high fps, then you can reduce it, which will reduce the size of the blueprint:
```Need change fps? [Y/N]: y```
6. Select Fps: ```Enter new fps: 10```
7. Wait until the program finishes its work
8. The finished blueprint will be located in the folder with "main.py" and called "blueprint.txt"

> [!CAUTION]
> If you have less than 8 gigabytes of RAM, then be careful and do not generate blueprints with high resolution or many frames

## Approximate RAM values
* 300MB for 64x64 36 frames
* 300MB for 144x144 8 frames
* 1GB for 128x128 36 frames
* 5GB for 200x200 120 frames
* 16GB for 96x72 2200 frames (Bad apple 10fps)
* 32GB for 96x72 5200 frames (Bad apple 24fps)

