# Rename 

#### What does it do?
Allows you to rename TV shows in two different ways aimed at making sure file names are inline with Plex's metadata db's.
There are two ways to rename a set of files. 
1. Renaming the show, but keeping season and episode information intact. (ie renaming a file in the format "tvshow S01E01.mkv" will still retain the "S01E01.mkv" 
2. Or renaming the show and chaning the season and episode information. This is due to the format for some dvd or blueray rips being labeled cotinously with the episode number, but no information on the season. 

The script takes two arguments: 

Argument one is the name to be renamed to. 
The second is an optional argument specified by using "--s" and will add the season number based on the following digits

Using the "--s" will override the episode number, and sort them assuming they are labeled from from first to last episode. 

A circumstance where this would be used is a tv show having no season labeling and being labeled episode 1 - episode 100, where the show needs to be broken up in seasons
for plex to properly tag. 
