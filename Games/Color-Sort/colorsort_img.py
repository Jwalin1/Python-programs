import numpy as np
import matplotlib.pyplot as plt

"""### read image as np array"""

def read_img(img_name):
  tubes_img = plt.imread(img_name)
  # original image is write protected so need to make a copy
  tubes_img = tubes_img.copy()
  # crop the top part of the image
  tubes_img = tubes_img[200:1200]
  tubes_img = tubes_img.astype("float") / 255
  return tubes_img

"""### get colors between the tubes"""

def get_tubes(tubes_img):
  height, width, channels = tubes_img.shape
  tubes = []
  tube_indx = 0
  n_tubes = 0

  for i in range(height):
    tube_start=False; tube_end=False
    tube_seq="outside"
    found = False
    for j in range(width):
      if (tube_seq=="outside") and (np.mean(tubes_img[i,j]) > .785):
        tube_seq="start"
      elif (tube_seq=="start") and (np.mean(tubes_img[i,j]) <= .785):
        tube_start = j
        tube_seq="inside"
      elif (tube_seq=="inside") and (np.mean(tubes_img[i,j]) > .785):
          tube_end = j-1
          tube_seq="end"
      elif (tube_seq=="end") and (np.mean(tubes_img[i,j]) <= .785):
          tube_seq="outside"

      if (tube_seq=="outside") and tube_end:
        tube_width = tube_end - tube_start
        if (tube_width < 100) and (tube_width > 50):
          mid = (tube_start + tube_end)//2
          mid_colr = tubes_img[i,mid]
          found = True
          colr = list(mid_colr) if np.mean(mid_colr)>0.2 else [1,1,1]
          if tube_indx < len(tubes):
            tubes[tube_indx].append(colr)
          else:
            tubes.append([colr])
          tube_indx += 1

        tube_start=False; tube_end=False
    # end width loop
    if found:
      tube_indx = n_tubes
    else:
      n_tubes = len(tubes)
      tube_indx = n_tubes

  return tubes

"""### only keep the colors with most frequency"""

def rem_extraColrs(tubes):
  for i,tube in enumerate(tubes):
    colrs, count = np.unique(tube, axis=0, return_counts=True)
    # only keep colrs whose count is greater than threshold (30)
    colrs = colrs[np.where(count>30)]
    colrs = [list(colr) for colr in colrs]
    new_tube = []
    for colr in tube:
      if colr in colrs:
        new_tube.append(colr)

    tubes[i] = new_tube

def get_patchColrs(tubes):
  for i,tube in enumerate(tubes):
    center_pts = np.linspace(0,len(tube),6)[1:-1].astype(int)
    new_tube = []
    for pt in center_pts:
      new_tube.append(tube[pt])
    tubes[i] = new_tube

def process_img(img_name):
  tubes_img = read_img(img_name)
  tubes = get_tubes(tubes_img)
  # inplace methods
  rem_extraColrs(tubes)
  get_patchColrs(tubes)
  return tubes

# tubes_img = read_img("tubes.jpeg")
# plt.imshow(tubes_img)
# tubes = process_img("tubes.jpeg")
