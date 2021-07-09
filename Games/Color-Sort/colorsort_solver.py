# exmaple 1
original_tubes = [
          ['p','b','r','p'],
          ['y','g','g','r'],
          ['p','y','y','r'],
          ['b','g','r','p'],
          ['b','b','y','g'],
          [[1,1,1]]*4,  [[1,1,1]]*4
]

# exmaple 2
original_tubes = [
          ['y','g','g','r'],
          ['p','b','r','p'],
          [[1,1,1]]*4,  [[1,1,1]]*4,
          ['p','y','y','r'],
          ['b','g','r','p'],
          ['b','b','y','g'],
]

# exmaple 3
original_tubes = [
          ['lb','y','o','lg'],
          ['lb','g','y','dg'],
          ['p','lg','r','db'],
          ['y','lb','r','dp'],
          ['dg','lp','db','y'],
          ['b','dg','b','g'],
          ['b','db','p','r'], # one row
          ['p','lp','db','b'],
          ['dp','lp','lg','dp'],
          ['dg','dp','p','r'],
          ['o','lg','g','lb'],
          ['lp','o','g','o'],
          [[1,1,1]]*4, [[1,1,1]]*4
]

# exmaple 4
original_tubes = [
          [[0.6901960784313725, 0.2901960784313726, 0.0], [0.9490196078431372, 0.0, 0.7058823529411765], [0.9921568627450981, 0.5450980392156862, 0.16470588235294117], [0.6901960784313725, 0.2901960784313726, 0.0]] ,
          [[1.0, 0.4235294117647059, 0.5372549019607843], [0.4549019607843137, 0.4549019607843137, 0.4549019607843137], [0.12156862745098039, 0.996078431372549, 0.9215686274509803], [0.5372549019607843, 0.12156862745098039, 0.9921568627450981]] ,
          [[0.9490196078431372, 0.0, 0.7058823529411765], [0.4549019607843137, 0.4549019607843137, 0.4549019607843137], [0.9921568627450981, 0.5450980392156862, 0.16470588235294117], [1.0, 0.050980392156862744, 0.00392156862745098]] ,
          [[0.25098039215686274, 0.5686274509803921, 0.9921568627450981], [1.0, 0.050980392156862744, 0.00392156862745098], [0.6901960784313725, 0.2901960784313726, 0.0], [1.0, 0.4235294117647059, 0.5372549019607843]] ,
          [[0.9921568627450981, 0.5450980392156862, 0.16470588235294117], [0.996078431372549, 0.8784313725490196, 0.20392156862745098], [0.25098039215686274, 0.5686274509803921, 0.9921568627450981], [0.0, 0.7137254901960784, 0.4235294117647059]] ,
          [[0.996078431372549, 0.8784313725490196, 0.20392156862745098], [0.00784313725490196, 0.996078431372549, 0.07450980392156863], [0.9921568627450981, 0.5450980392156862, 0.16470588235294117], [0.25098039215686274, 0.5686274509803921, 0.9921568627450981]] ,
          [[0.25098039215686274, 0.5686274509803921, 0.9921568627450981], [0.00784313725490196, 0.996078431372549, 0.07450980392156863], [0.00784313725490196, 0.996078431372549, 0.07450980392156863], [0.12156862745098039, 0.996078431372549, 0.9215686274509803]] ,
          [[1.0, 0.4235294117647059, 0.5372549019607843], [0.5372549019607843, 0.12156862745098039, 0.9921568627450981], [0.0, 0.7137254901960784, 0.4235294117647059], [0.4549019607843137, 0.4549019607843137, 0.4549019607843137]] ,
          [[0.4549019607843137, 0.4549019607843137, 0.4549019607843137], [0.00784313725490196, 0.996078431372549, 0.07450980392156863], [0.0, 0.7137254901960784, 0.4235294117647059], [0.996078431372549, 0.8784313725490196, 0.20392156862745098]] ,
          [[0.5372549019607843, 0.12156862745098039, 0.9921568627450981], [0.9490196078431372, 0.0, 0.7058823529411765], [0.6901960784313725, 0.2901960784313726, 0.0], [0.12156862745098039, 0.996078431372549, 0.9215686274509803]] ,
          [[0.0, 0.7137254901960784, 0.4235294117647059], [0.5372549019607843, 0.12156862745098039, 0.9921568627450981], [0.9490196078431372, 0.0, 0.7058823529411765], [0.12156862745098039, 0.996078431372549, 0.9215686274509803]] ,
          [[0.996078431372549, 0.8784313725490196, 0.20392156862745098], [1.0, 0.050980392156862744, 0.00392156862745098], [1.0, 0.050980392156862744, 0.00392156862745098], [1.0, 0.4235294117647059, 0.5372549019607843]] ,
          [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]] ,
          [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
]

def copytubes(tubes):
  new_tubes = [list(tube) for tube in tubes]
  return new_tubes

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
  colrs = []
  for tube in tubes:
    t_indx = nonEmptyIndex(tube)
    if t_indx != len(tube):  # all same if tube empty    
      colr = tube[t_indx]
      for i in range(t_indx+1,len(tube)):
        if tube[i] != colr:
          return False
      if colr not in colrs:
        colrs.append(colr)
      else:
        return False  
  return True

def printMoves(original_tubes,moves):
  tubes = copytubes(original_tubes)
  if moves is not None:
    print("score: %d"%(tubes_score(tubes)))
    for k,(i,j) in enumerate(moves):
      transfer(tubes[i],tubes[j])
      print("move:%d -> transfer tube%d to tube%d, score: %d"%(k+1,i+1,j+1,tubes_score(tubes)))
  else:
    print("failed")

"""### sequential incremental"""

def seq_increment(original_tubes):  
  tubes = copytubes(original_tubes)
  solved = False
  move_indx = 0
  moves = []

  for k in range(1000):
    if allSame(tubes):
      solved = True
      break
    transferred = False

    # transfer from tube1 to tube2
    for i in range(len(tubes)):
      for j in range(i+1,len(tubes)):
        tube1, tube2 = tubes[i], tubes[j]
        if check_transfer(tube1, tube2):
            transfer(tube1,tube2)
            moves.append((i,j))
            transferred = True
            break
        elif check_transfer(tube2, tube1):
            transfer(tube2,tube1)
            moves.append((j,i))
            transferred = True
            break
      if transferred:
        break
    if not transferred:
      break
      
  if solved:
    return moves
  else:
    return None

def tubes_score(tubes):
  total_score = 0
  for tube in tubes:
    t_indx = nonEmptyIndex(tube)
    if t_indx != len(tube):
      score=1; colr=tube[t_indx]
      for i in range(t_indx+1, len(tube)):
        # for n consecutive colors in a tube
        # score is given as 4^n
        if tube[i] == colr:
          score *= 4
        else:
          if score > 1:
            total_score += score
          colr = tube[i]
          score = 1
      if score > 1:
        total_score += score
    # subtract 1 for every empty tube
    # so that initial moves would have higher score than tubes being empty
    else:
      total_score -= 1    
  return total_score

import numpy as np

"""### sequential backtracking"""

def seq_backtrack(original_tubes, shuffle=False, seed=None):
  tubes = copytubes(original_tubes)
  if shuffle:
    indxs = list(range(len(tubes)))
    if seed is not None:
      rng = np.random.default_rng(seed)
    np.random.shuffle(indxs)
    shuffled_tubes = [tubes[indx] for indx in indxs]
    tubes = shuffled_tubes
  solved = False
  tubes_state = []

  run=0; max_moves=0; prev_score=-100
  while True:
    if allSame(tubes):
      solved = True
      break
    possible_moves = []

    visited_tubes = [tube_state[0] for tube_state in tubes_state]
    # transfer from tube1 to tube2
    for i in range(len(tubes)):
      for j in range(i+1,len(tubes)):
        tube1, tube2 = tubes[i], tubes[j]
        if check_transfer(tube1, tube2):
          new_tubes = copytubes(tubes)
          # pass a copy of the list so that the original is not changed after the transfer
          _, _, chunk_size = transfer(new_tubes[i], new_tubes[j])
          score = tubes_score(new_tubes)
          if (new_tubes not in visited_tubes) and (score > prev_score):
            #print("move:%d -> transfer tube%d to tube%d"%(move_indx,i+1,j+1))
            move = (i,j)
            possible_moves.append((move, score))
        # check transfer in reverse order
        if check_transfer(tube2, tube1):
          new_tubes = copytubes(tubes)
          _, _, chunk_size = transfer(new_tubes[j], new_tubes[i])
          score = tubes_score(new_tubes)
          if (new_tubes not in visited_tubes) and (score > prev_score):
            #print("move:%d -> transfer tube%d to tube%d"%(move_indx,j+1,i+1))
            move = (j,i)
            possible_moves.append((move, score))
      # end loop for tube to be transferred to
    # end loop for tube to be transferred from

    if len(possible_moves) == 0:   # stuck having checked all possibilities
      while True:
        tubes, possible_moves, move_choice = tubes_state[-1]    # get the last state and its moves
        tubes = copytubes(tubes)    # so that tubes_states doesnt get modified
        move_choice += 1
        if move_choice == len(possible_moves):  # exhausted all possible moves
          del tubes_state[-1]
          if len(tubes_state) == 0: break   # checked all
        else:
          move, _ = possible_moves[move_choice]
          tubes_state[-1][2] = move_choice   # update the move choice
          i, j = move
          tube1, tube2 = tubes[i], tubes[j]
          transfer(tube1,tube2)
          break
    else:
      # pick the move which results in the highest score
      possible_moves.sort(key=lambda x:x[1], reverse=True)
      move, _ = possible_moves[0]
      tubes_state.append([copytubes(tubes), possible_moves, 0])
      i, j = move
      tube1, tube2 = tubes[i], tubes[j]
      # sending original tubes instead of copy to transfer function
      transfer(tube1,tube2)
    prev_score = tubes_score(tubes)

    if len(tubes_state) == 0: break

    if len(tubes_state) > max_moves:
      max_moves = len(tubes_state)
    if run%1000==0:
      print("run %d, max_moves = %d"%(run,max_moves))
    run += 1
      
  if solved:
    print("found solution in run %d"%(run-1))
    moves = []
    for _, possible_moves, move_choice in tubes_state:
      move = possible_moves[move_choice][0]
      if shuffle:
        i,j = move
        move = indxs[i], indxs[j]
      moves.append(move)
    return moves
  else:
    return None

moves = seq_backtrack(original_tubes, shuffle=True)
printMoves(original_tubes,moves)

from tqdm.auto import tqdm

"""### random search"""

def random_search(original_tubes, n_runs=1000, check_all=False):
  run_moves = []
  n_possibleMoves = np.math.factorial(len(tubes))/(2*np.math.factorial(len(tubes)-2))

  for run in tqdm(range(n_runs)):
    tubes = copytubes(original_tubes)
    moves_tested = []
    moves = []
    visited_states = [tubes]
    solved = False
    
    move_indx = 1
    
    while True:
      if allSame(tubes):
        #print("run %d : done"%(run))
        solved = True
        break
        
      # transfer from tube1 to tube2
      if len(moves_tested) == n_possibleMoves:
        break
      while True:
        i,j = np.random.choice(range(len(tubes)),2,replace=False)
        if (i,j) not in moves_tested and (j,i) not in moves_tested:
          moves_tested.append((i,j))
          break

      transferred = False
      tube1, tube2 = tubes[i], tubes[j]
      if check_transfer(tube1,tube2):
        new_tubes = copytubes(tubes)
        transfer(new_tubes[i], new_tubes[j])
        if new_tubes not in visited_states:
          moves.append((i,j))
          transferred = True
      if (not transferred) and (check_transfer(tube2,tube1)):
        new_tubes = copytubes(tubes)
        transfer(new_tubes[j], new_tubes[i])
        if new_tubes not in visited_states:
          moves.append((j,i))
          transferred = True
      if transferred:
        move_indx += 1
        moves_tested = []
        tubes = new_tubes
        visited_states.append(tubes)
    if not solved:
      #print("run %d : failed"%(run))
      continue
    run_moves.append(moves)
    if not check_all:
      print("found a solution in run %d"%(run));
      break
  if check_all:
    print("all runs completed\n")  

  if len(run_moves) > 0:
    move_lens = [len(moves) for moves in run_moves]
    min_run = move_lens.index(min(move_lens))
    best_moves = run_moves[min_run]
    return best_moves
  else:
    return None

# from colorsort_game import playGame, replaceColors

# colrs = {'p':"pink", 'b':"blue", 'r':"red", 'y':"yellow", 'g':"green"}
# tubes = replaceColors(original_tubes, colrs)
# playGame(original_tubes, moves)