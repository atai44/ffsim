#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 02:48:30 2020

@author: alex
"""
import numpy
import random
#import statistics

#define current conditions 
#outcomes: 0=miss playoffs, 1=wild card, 2=top 4
players = [
    {'Name': "Alex", 'scores':[103.84, 85.36, 81.72, 124.78, 72.44, 116.92, 99.14, 99.32, 75.96, 101.88, 100.7, 111.06], 'sched':[1,9,2,3,7,11,4,10,5,6,8,1,9], 'wins':0, 'tot':0, 'rank':[0,0,0,0,0,0,0,0,0,0,0,0], 'outcome':[0,0,0]},
    {'Name': "Aneesh", 'scores':[125.54, 103.1, 74.48, 81.2, 109.52, 97.96, 91.48, 87.16, 100.6, 90.22, 104.4,85.58], 'sched':[0,2,9,7,3,4,11,5,10,8,6,0,2], 'wins':0,'tot':0, 'rank':[0,0,0,0,0,0,0,0,0,0,0,0], 'outcome':[0,0,0] },
    {'Name': "Fawaz", 'scores':[65, 83.36, 92.22, 117.42, 66.54, 123.16, 122.82, 44.64, 123, 104.74, 87, 98.48], 'sched':[9,1,0,5,10,8,6,4,11,7,3,9,1], 'wins':0,'tot':0, 'rank':[0,0,0,0,0,0,0,0,0,0,0,0], 'outcome':[0,0,0] },
    {'Name': "Jeff", 'scores':[82.2, 99.36, 123.96, 52.1, 114.16, 135.28, 74.42, 126.4, 83.6, 101.48, 106.84,121.76], 'sched':[7,11,4,0,1,10,5,6,8,9,2,7,11], 'wins':0,'tot':0, 'rank':[0,0,0,0,0,0,0,0,0,0,0,0], 'outcome':[0,0,0] },
    {'Name': "Josh", 'scores':[97.5, 104.22, 123.06, 129.6, 85.92, 84.62, 80.54, 85.54, 114.36, 70.82, 112.54, 106.52], 'sched':[11,7,3,8,6,1,0,2,9,5,10,11,7], 'wins':0,'tot':0, 'rank':[0,0,0,0,0,0,0,0,0,0,0,0], 'outcome':[0,0,0] },
    {'Name': "Mihir", 'scores':[103.48, 141.54, 137.2, 97.62, 126.28, 73.42, 59.78, 124.44, 105.64, 78.28, 108.18,91.02], 'sched':[10,8,6,2,9,7,3,1,0,4,11,10,8], 'wins':0,'tot':0, 'rank':[0,0,0,0,0,0,0,0,0,0,0,0], 'outcome':[0,0,0] },
    {'Name': "Nick", 'scores':[99.6, 88.82, 89.16, 87.44, 114.86, 102.62, 110.26, 85.54, 95.46, 74.94, 91.52,71.14], 'sched':[8,10,5,11,4,9,2,3,7,0,1,8,10], 'wins':0,'tot':0, 'rank':[0,0,0,0,0,0,0,0,0,0,0,0], 'outcome':[0,0,0] },
    {'Name': "Nihal", 'scores':[111.16, 86.22, 129.58, 89.4, 70.3, 66.64, 159.02, 80.12, 50.04, 144.98, 55.86,62.16], 'sched':[3,4,11,1,0,5,10,8,6,2,9,3,4], 'wins':0,'tot':0, 'rank':[0,0,0,0,0,0,0,0,0,0,0,0], 'outcome':[0,0,0] },
    {'Name': "Pranav", 'scores':[76.66, 123.1, 80.78, 97.92, 96.28, 79.06, 108.94, 71.08, 91.72, 70.8, 80.88, 74.32], 'sched':[6,5,10,4,11,2,9,7,3,1,0,6,5], 'wins':0,'tot':0, 'rank':[0,0,0,0,0,0,0,0,0,0,0,0], 'outcome':[0,0,0] },
    {'Name': "Rahul", 'scores':[111.12, 76.1, 85.34, 148.24, 84.94, 76.38, 115.54, 78.62, 114.08, 81.1, 99.26,109.16], 'sched':[2,0,1,10,5,6,8,11,4,3,7,2,0], 'wins':0,'tot':0, 'rank':[0,0,0,0,0,0,0,0,0,0,0,0], 'outcome':[0,0,0] },
    {'Name': "Rohit", 'scores':[127, 132.96, 119.38, 130.02, 106.52, 76.48, 111.14, 72.94, 74.94, 65.2, 77.64,62.48], 'sched':[5,6,8,9,2,3,7,0,1,11,4,5,6], 'wins':0,'tot':0, 'rank':[0,0,0,0,0,0,0,0,0,0,0,0], 'outcome':[0,0,0] },
    {'Name': "Saud", 'scores':[101.7, 140.02, 117.62, 86.9, 105.5, 72.34, 91.66, 69.56, 85.78, 80.34, 107.86,111.74], 'sched':[4,3,7,6,8,0,1,9,2,10,5,4,3], 'wins':0,'tot':0, 'rank':[0,0,0,0,0,0,0,0,0,0,0,0], 'outcome':[0,0,0] },
]

#the number of weeks that have actually been completed 
actual_wk=12

# def get_name(plyr):
#     return plyr.get('Name')

# def get_wins(plyr):
#     return plyr.get('wins')

# def get_total(plyr):
#     return plyr.get('tot')

#helper function for reset_all 
def reset_player(plyr):
    plyr['scores'] = plyr['scores'][:actual_wk]
    plyr['wins'] = 0
    plyr['tot'] = 0
    
def reset_all(plylist):
    for playr in plylist:
        reset_player(playr)

#helper fn for sim_all        
def sim_scores(pyr):
    mlen = 13-actual_wk
    if (random.random()<-2): sims = numpy.random.normal(100,20,mlen)
    else:
        # mylist = pyr['scores']
        mylist = pyr['scores'][5:]
        mean = sum(mylist) / len(mylist) 
        variance = sum([((x - mean) ** 2) for x in mylist]) / len(mylist) 
        res = variance ** 0.5
        sims = numpy.random.normal(mean,res,mlen)
        
        
        
    pyr['scores'].extend(sims)
    pyr['tot'] = sum(pyr['scores'])
    
def sim_all(plist):
    for p in plist:
        sim_scores(p)
        
#only do this after scores are fully simulated 
def set_wins(playlst):
    for plyer in playlst:
        wk=0
        for opp in plyer['sched']:
            if plyer['scores'][wk] > playlst[opp]['scores'][wk]:
                plyer['wins']+=1
            wk+=1
        
        
#test for sim_scores
# players[1]['scores']=[10,20,30]
# sim_scores(players[1])
# print(players[1]['scores'])
                
#test for sim_all
# players[1]['scores']=[80]
# sim_all(players)
# for player in players:
#     print(player['scores'])

# #test for get_total
# players[1]['scores']=[10,20,30]
# print(get_total(players[1]))
        
# #test for reset_all() 
# players[1]['scores']=[10,20,30,40,60]
# players[3]['wins']=6
# print(players[1])
# print(players[3])
# reset_all(players)
# print(players[1])
# print(players[3])
                
#test set_wins
# sim_all(players)
# set_wins(players)
# for p in players:
#     print(p['Name'],p['wins'])
    
N=100000
for n in range(N):
    
    #reset
    reset_all(players)
    players = sorted(players, key=lambda x:x['Name'])
    
    #simulate 
    sim_all(players)
    set_wins(players)
    
    #rankings
    players = sorted(players, key = lambda x:(x['wins'],x['tot']), reverse=True)
    place=0
    for p in players:
        #print(p['Name'],p['wins'],p['tot'])
        p['rank'][place]+=1
        place+=1
    #print()
    
    #outcomes
    
    #for top 4 teams
    for i in range(4):
        players[i]['outcome'][2]+=1
        
    #for the wild cards
    most = 0
    mosti = 100
    secnd = 0
    secndi= 100
    for i in range(4,12):
        if(players[i]['tot']>most):
            #move previous number1 to second place
            secnd=most
            secndi=mosti
            #set new number1
            most = players[i]['tot']
            mosti = i
            #print(players[i]['Name'], 'is most')
        elif(players[i]['tot']>secnd):
            secnd = players[i]['tot']
            secndi = i
            #print(players[i]['Name'], 'is second')
    #print("wild cards: ",players[mosti]['Name'], players[secndi]['Name'])
    for i in range(4,12):
        if(i==mosti or i==secndi): players[i]['outcome'][1]+=1
        else: players[i]['outcome'][0]+=1
            
        
        
players = sorted(players, key=lambda x:x['Name'])
print()
        
for p in players:
    #print (p['Name'], end=": ")
    for r in p['rank']:
        print(r/N, end=" ")
    print()
    #print (p['Name'],p['rank'],p['outcome'])
    
print()

for p in players:
    #print (p['Name'], end=": ")
    for r in range(2):
        if (r==0): print(1-p['outcome'][r]/N, end=" ")
        else: print(p['outcome'][r]/N, end=" ")
    print()
    #print (p['Name'],p['rank'],p['outcome'])