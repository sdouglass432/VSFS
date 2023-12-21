# Cairn University CIS 321, 9/24/2023, Professor Petcaugh
# Student Name: Sam Douglass

# to do: add feature to look through names in inode to find right file
# add logic to delete/store larger, fragmented files to data blocks
# divide size by 4kb and store to that many blocks
# turn each case into functions
# change inode data from list to dict to avoid placement changes on deletion

import pygame

blocks = []
counter = 0
class block:
    def __init__(self, n, x, y, d):
        # name, X coord, Y coord, data list
        self.n = n
        self.x = x
        self.y = y
        self.data = d

class file:
    def __init__(self, n, t, d, s, o, p):
        # name, type, date, size, owner, pointers
        self.n = n
        self.t = t
        self.d = d
        self.s = s
        self.o = o
        self.p = p


# Helper functions
def addtext(mytext,t_dest, f_color, f_size):
    font = pygame.font.SysFont(None, f_size)
    font_final = font.render(mytext, True, f_color)
    screen.blit(font_final, t_dest)
    # addtext("START", (220, 20), (0,0,0), 50)

# makes block outlines and creates block list & objects
def drawblocks():
    # rectangle x & y values
    recx = 5
    recy = 5
    count = 0
    for i in range(3):
        for j in range(4):
            pygame.draw.rect(screen, (0, 0, 0), (recx, recy, 20, 20), 1)
            blocks.append(block("block "+str(count), recx, recy, []))
            count += 1
            recx += 19
        recx += 8
    recx = 5
    recy += 37
    for i in range(3):
        for j in range(4):
            pygame.draw.rect(screen, (0, 0, 0), (recx, recy, 20, 20), 1)
            blocks.append(block("block " + str(count), recx, recy, []))
            count += 1
            recx += 19
        recx += 8
    print(count)
    print(blocks[1].n)


# Colors & sets up bitmaps & inodes
def setup():
    pygame.draw.rect(screen, (0, 0, 0), (blocks[0].x, blocks[0].y, 20, 20))
    # inode bitmap. for this sim the inode can store 10 files worth of metadata
    for i in range(10):
        blocks[1].data.append(0)
    for j in range(24):
        blocks[2].data.append(0)
    dbitmap.data[0] = 1
    dbitmap.data[1] = 1
    dbitmap.data[2] = 1

    addtext("Data bitmap: "+str(dbitmap.data), (20, 200), (0, 0, 0), 30)
    addtext("Inode bitmap: "+str(ibitmap.data), (20, 220), (0, 0, 0), 30)

    pygame.draw.rect(screen, (200, 0, 0), (blocks[1].x, blocks[1].y, 20, 20))
    pygame.draw.rect(screen, (200, 0, 0), (blocks[2].x, blocks[2].y, 20, 20))
    addtext("Finished setting up bitmaps (Red)",(20,450),(0,0,0), 30)
    addtext("Press S to continue simulation", (20, 470), (0, 0, 0), 30)

def simulation(c):
    # block 0: superblock, 1: inode bitmap, 2: data bitmap (starts with superblock, not data blocks), 3: inode
    match c:
        # save file
        case 0:
            # update bitmap and color/write inode
            dbitmap.data[3] = 1
            dbitmap.data[4] = 1
            ibitmap.data[0] = 1
            pygame.draw.rect(screen, (255, 255, 0), (blocks[3].x, blocks[3].y, 20, 20))
            inode.data.append(file("Hello", ".txt", "9/19/2023", "4kb", "admin", 4))
            # save to data & write new text
            blocks[4].data.append("Hello world")
            pygame.draw.rect(screen, (0, 0, 255), (blocks[4].x, blocks[4].y, 20, 20))
            pygame.draw.rect(screen, (150, 150, 150), (20, 200, 800, 270))
            # reads & prints some metadata for the last file saved
            addtext("File "+inode.data[len(inode.data)-1].n+inode.data[len(inode.data)-1].t+" saved to block "+str(inode.data[len(inode.data)-1].p), (20, 430), (0, 0, 0), 30)
            addtext("Metadata saved to inode (block 3): "+inode.data[len(inode.data)-1].n+inode.data[len(inode.data)-1].t+" "+inode.data[len(inode.data)-1].s+" saved on "+inode.data[len(inode.data)-1].d+" owner: "+inode.data[len(inode.data)-1].o, (20, 450), (0, 0, 0), 30)
            addtext("Data bitmap: " + str(dbitmap.data), (20, 200), (0, 0, 0), 30)
            addtext("Inode bitmap: " + str(ibitmap.data), (20, 220), (0, 0, 0), 30)

        case 1:
            # reads file data & prints to screen
            pygame.draw.rect(screen, (150, 150, 150), (20, 200, 800, 270))
            addtext("Reading last saved file", (20, 430), (0, 0, 0), 30)
            addtext(""+str(blocks[inode.data[0].p].data)+" Read from "+inode.data[0].n+inode.data[0].t, (20, 450), (0, 0, 0), 30)
            addtext("Data bitmap: " + str(dbitmap.data), (20, 200), (0, 0, 0), 30)
            addtext("Inode bitmap: " + str(ibitmap.data), (20, 220), (0, 0, 0), 30)
        case 2:
            pygame.draw.rect(screen, (150, 150, 150), (20, 200, 800, 290))
            dbitmap.data[4] = 0
            ibitmap.data[0] = 0
            blocks[inode.data[0].p].data.clear()
            pygame.draw.rect(screen, (150, 150, 150), (blocks[inode.data[0].p].x, blocks[inode.data[0].p].y, 20, 20))
            pygame.draw.rect(screen, (0, 0, 0), (blocks[inode.data[0].p].x, blocks[inode.data[0].p].y, 20, 20), 1)
            addtext("File '"+inode.data[0].n+inode.data[0].t+"' deleted", (20, 450), (0, 0, 0), 30)
            inode.data.pop(0)
            addtext("Simulation completed", (20, 470), (0, 0, 0), 30)
            addtext("Data bitmap: " + str(dbitmap.data), (20, 200), (0, 0, 0), 30)
            addtext("Inode bitmap: " + str(ibitmap.data), (20, 220), (0, 0, 0), 30)



# Screen controls
pygame.init()

screen = pygame.display.set_mode([1000,500])
clock = pygame.time.Clock()
screen.fill((150,150,150))
drawblocks()
sblock = blocks[0]
ibitmap = blocks[1]
dbitmap = blocks[2]
inode = blocks[3]
setup()

# Running loop
running = True
while running:
    # looks for inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                simulation(counter)
                counter += 1

    # Update screen, go to next frame
    pygame.display.flip()
    clock.tick(30)

pygame.quit()