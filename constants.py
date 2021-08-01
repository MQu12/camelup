# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 08:34:22 2021

@author: Dr. P
"""

# 0 = show, 1 = save
PLOT_METHOD = 0

USE_CPP_CLASSES = True

from svgpath2mpl import parse_path

racingCamelMarker = parse_path("""M1047 1740 c-97 -25 -153 -75 -257 -231 -104 -156 -143 -189 -227
-189 -67 0 -102 25 -162 114 -66 97 -107 128 -174 134 -129 10 -186 -104 -217
-434 -14 -142 -2 -270 36 -402 34 -115 43 -131 125 -204 70 -61 74 -68 164
-253 101 -206 140 -258 194 -258 54 0 103 44 191 173 110 164 133 188 215 227
64 31 77 33 170 33 90 0 106 -3 162 -29 82 -39 126 -86 200 -213 97 -166 151
-217 217 -204 63 13 109 74 166 216 58 147 76 174 178 267 119 109 146 151
172 271 12 54 29 114 38 135 20 49 67 90 126 111 25 9 67 23 94 33 53 18 186
142 217 203 26 50 23 109 -7 161 -45 76 -103 109 -254 145 -157 37 -197 56
-247 123 -80 104 -125 76 -241 -148 -79 -154 -110 -193 -171 -217 -89 -34
-162 1 -232 113 -131 207 -197 275 -293 308 -59 20 -136 26 -183 15z""")
racingCamelMarker.vertices -= racingCamelMarker.vertices.mean(axis=0)

crazyCamelMarker = parse_path("""M1500 1735 c-105 -30 -181 -95 -265 -230 -111 -176 -131 -196 -208
-210 -50 -10 -117 16 -156 60 -16 18 -60 93 -97 166 -116 224 -161 252 -241
148 -50 -67 -90 -86 -247 -123 -151 -36 -209 -69 -254 -145 -30 -52 -33 -111
-7 -161 31 -61 164 -185 218 -203 26 -10 68 -24 93 -33 59 -21 106 -62 126
-111 9 -21 26 -81 38 -135 26 -120 53 -162 172 -271 102 -93 120 -120 178
-267 57 -142 103 -203 166 -216 66 -13 120 38 217 204 74 127 118 174 200 213
56 26 72 29 162 29 93 0 106 -2 170 -33 82 -39 105 -63 215 -227 88 -129 137
-173 191 -173 54 0 93 52 194 258 90 185 94 192 164 253 82 73 91 89 125 204
38 132 50 260 36 402 -31 330 -88 444 -217 434 -67 -6 -108 -37 -174 -134 -60
-89 -95 -114 -162 -114 -84 0 -123 33 -228 190 -34 52 -82 116 -106 141 -76
81 -194 114 -303 84z""")
crazyCamelMarker.vertices -= crazyCamelMarker.vertices.mean(axis=0)

RANDOM_SEED = 1

RACING_COLOURS = ['red',
                  'green',
                  'orange',
                  'blue',
                  'purple',
                  'brown',
                  'pink',
                  'olive',
                  'cyan',
                  'maroon',
                  'darkblue',
                  'lawngreen',
                  'dodgerblue',
                  'crimson',
                  'turquoise',
                  'yellow',
                  'beige',
                  'sandybrown',
                  'lime',
                  'darkgreen'
                  ]
CRAZY_COLOURS = ['black','white','gray','darkgray','lightgray','silver','grey','whitesmoke']

def printcols():
    import matplotlib.pyplot as plt
    for col in RACING_COLOURS:
        plt.bar(0,1,color=col)
        plt.text(0,0.5,col)
        plt.show()