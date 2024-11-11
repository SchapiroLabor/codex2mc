# Staging module for Miltenyi - MACSIMA to MCMICRO

The macsima2mc.py script stages MACSima data sets for being registerd with ASHLAR in MCMICRO.

The script takes as main input the path to the cycle folder that cointains the raw tiles generated by the Miltenyi-MACSima platform.  macsima2mc.py reads these tiles and distributes them into acquisition groups. i.e tiles with common rack, well, ROI and exposure levels will be written into an ome.tiff file with the necessary metadata for registration.  To be more precise two such ome.tiff files will be generated per cycle, one corresponds to the background signal and the other to the markers signal.
 
## CLI
### Required arguments
| Argument| Type| Description | Default value |
|----|----|----|---|
|-i|string/path|Absolute path to the the parent folder of the raw tiles, i.e. the cycle folder whose name follows the pattern X_Cycle_N, where N represents the cycle number.|NA|

|-o|string/path|Absolute path to the directory in which the outputs will be saved. If the output directory doesn't exist it will be created. |NA| 

### Optional arguments
| Argument| Type| Description | Default value |
|----|----|----|---|
|-rm|string|Name of the reference marker for registration|'DAPI'|
|-od|string|String specifying the name of the subfolder in which the staged images will be saved.|'raw'|
|-ic|boolean flag |Give this flag to apply illumination correction to all tiles, the illumination profiles are calculated with basicpy | FALSE |
|-he|boolean flag|Give this flag to extract only the set of images with the highest exposure time|FALSE|

## Container usage
# download container:
- Docker
```
singularity pull docker://ghcr.io/schapirolabor/multiplex_macsima:v1.1.0 

```
- Singularity
```
docker pull ghcr.io/schapirolabor/multiplex_macsima:v1.1.0
```