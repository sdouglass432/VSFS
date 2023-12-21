# VSFS


## Description

1 This is a simulation of the Very Simple File System described in Chapter 40 of Operating Systems: Three Easy Pieces by Remzi & Andrea Arpaci-Dusseau
When this program is run it creates 24 blocks,marks the first one to store the system itself, then sets up bitmaps in the second and third blocks.
Pressing S once sets up an inode block that stores metadata and points to the blocks containing a file's actual data. A sample file is then saved to a data block and its metadata is saved and printed on the screen.
Pressing S again looks at the inode to see where that file's data is stored then reads that data and prints it on screen alongside the file's name.
Pressing S a third time will mark the data and inode spaces as empty so they are available to be written over by another file.
 

## Components and data structures
Blocks: each block is an object that is put into a list for easy identification. Each block contains its number, X and Y coordinates, and an empty list to store data. 
Data region: blocks 4-23 are the data region.
Inodes: block 3 is the inode with 10 slots for metadata. 
Metadata: object stored in inode that consists of file name, type, date created, size, owner, and direct pointers.
Inode bitmap: block 1, bitmap is contained in a list with 10 slots.
data bitmap: block 2, bitmap is contained in a list with 24 slots.
Superblock: block 0, theoretically contains my python code.
 
