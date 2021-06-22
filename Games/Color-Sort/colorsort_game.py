import matplotlib.pyplot as plt

# exmaple 1
original_tubes = [
          ['p','b','r','p'],
          ['y','g','g','r'],
          ['0']*4,  ['0']*4,
          ['p','y','y','r'],
          ['b','g','r','p'],
          ['b','b','y','g'],
]

def copytubes(tubes):
  new_tubes = [list(tube) for tube in tubes]
  return new_tubes

def replaceColors(tubes, colrs):
  for tube in tubes:
    for i,colr in enumerate(tube):
      if colr != '0':
        tube[i] = colrs[colr]
  return tubes

colrs = {'p':"pink", 'b':"blue", 'r':"red", 'y':"yellow", 'g':"green"}
original_tubes = replaceColors(original_tubes, colrs)

def plot_tubes(tubes):
  n_plots = len(tubes)//5 + 1
  fig, axs = plt.subplots(1,n_plots, figsize=(10,3))

  for ax in axs:
    ax.set_xlim([-0.5,4.5])

  for i,tube in enumerate(tubes):
    for j,colr in enumerate(reversed(tube)):
      if colr != '0':
        axs[i//5].bar(str(i+1), 1, bottom=j, color=colr, width=0.5, edgecolor='k')
      else:
        axs[i//5].bar(str(i+1), 1, bottom=j, fc=[1,1,1,0], width=0.5, edgecolor='k')
  plt.show()

# plot_tubes(original_tubes)

def nonEmptyIndex(tube):
  i=0
  while i in range(len(tube)):
    if tube[i] != [1,1,1]:
      break
    i+=1
  return i

def check_transfer(tube1,tube2):

  # check if colr matches
  t1_indx = nonEmptyIndex(tube1)
  t2_indx = nonEmptyIndex(tube2)

  if t1_indx == len(tube1):  # tube1 should not be empty
    return False
  elif t2_indx == 0:  # tube2 should not be full
    return False

  t1_colr = tube1[t1_indx]
  if t2_indx < len(tube2):  # if tube not empty
    t2_colr = tube2[t2_indx]
    if t1_colr != t2_colr:  # check if color matches
      return False
  else:   # if tube empty
    if allSame([tube1]):  # if all same
      return False

  return True

def transfer(tube1,tube2):

  # check if colr matches
  t1_indx = nonEmptyIndex(tube1)
  t2_indx = nonEmptyIndex(tube2)
  t1_colr = tube1[t1_indx]


  if t2_indx < len(tube2):  # if tube not empty
    t2_colr = tube2[t2_indx]
    # calc chunk size
    chunk_size = 1
    i = t2_indx + 1
    while i < len(tube2) and tube2[i] == t2_colr:
      chunk_size += 1
      i += 1
  else:
    chunk_size = 0

  i = t1_indx
  while i in range(len(tube1)):
    j = (t2_indx-1) - (i-t1_indx)
    if (tube1[i] != t1_colr) or (j == -1):
      break
    tube2[j] = tube1[i]
    tube1[i] = [1,1,1]
    i+=1
    chunk_size += 1

  return tube1,tube2, chunk_size

def allSame(tubes):
  same = True
  colrs = []
  for tube in tubes:
    t_indx = nonEmptyIndex(tube)
    if t_indx == len(tube):  # all same if tube empty
      continue

    colr = tube[t_indx]
    colrs.append(colr)
    t_indx += 1
    while t_indx in range(len(tube)):
      if tube[t_indx] != colr:
        return False
      t_indx += 1

  seen = []
  unique_list = [x for x in colrs if x not in seen and not seen.append(x)]
  if len(colrs) != len(unique_list):
    return False

  return same

def playGame(original_tubes, moves=None):
  tubes = copytubes(original_tubes)

  move_indx = 0
  while True:
    plot_tubes(tubes)
    if allSame(tubes):
      break

    if moves is None:
      i = int(input("enter tube to transfer from: ")) - 1
      j = int(input("enter tube to transfer to: ")) - 1
    else:
      i = moves[move_indx][0]
      j = moves[move_indx][1]
      print("move:%d -> transfer tube%d to tube%d"%(move_indx+1,i+1,j+1))
    tube1, tube2 = tubes[i], tubes[j]

    if check_transfer(tube1,tube2):
      transfer(tube1,tube2)
      move_indx += 1
    else:
      print("invalid move")

# playGame(original_tubes)
